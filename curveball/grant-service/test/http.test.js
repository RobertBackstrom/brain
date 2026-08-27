import test from 'node:test';
import assert from 'node:assert/strict';
import { createServer } from '../src/server.js';
import { HmacVerifier, NonceCache, sign } from '../src/auth.js';
import { Ledger } from '../src/ledger.js';
import { MockLootLocker } from '../src/lootlocker.js';
import { GrantService } from '../src/service.js';

const SECRET = 'http-test-secret';
const limits = {
  softCurrencyId: 'SOFT', softCurrencyCap: 6000,
  maxCurrencyPerMatch: 500, maxAssetsPerMatch: 4, maxProgressionPerMatch: 1000,
  windowSeconds: 3600, maxCurrencyPerWindow: 3000, maxAssetsPerWindow: 20, maxProgressionPerWindow: 6000,
  minMatchSeconds: 0, maxMatchSeconds: 3600, maxPlayersPerMatch: 16,
  allowedCurrencyIds: [], allowedProgressionKeys: [], allowedAssetIds: [],
};

function boot() {
  const ledger = new Ledger(':memory:');
  const ll = new MockLootLocker();
  const service = new GrantService({ ledger, lootLocker: ll, limits });
  const verifier = new HmacVerifier({ secret: SECRET, clockSkewSeconds: 60, nonceCache: new NonceCache(300) });
  const server = createServer({ service, verifier: { verify: (r) => verifier.verify(r) }, logRequests: false });
  return { server, ll };
}

async function call(base, path, body, { secret = SECRET, nonce } = {}) {
  const raw = JSON.stringify(body);
  const ts = Math.floor(Date.now() / 1000);
  const n = nonce ?? `n${Math.random()}`;
  const res = await fetch(base + path, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-MLC-Timestamp': String(ts),
      'X-MLC-Nonce': n,
      'X-MLC-Signature': sign(secret, 'POST', path, ts, n, raw),
      'X-MLC-Steam-Id': '76561198000000007',
    },
    body: raw,
  });
  return { status: res.status, json: await res.json() };
}

test('end to end over HTTP: open a match, grant, see it refused when unsigned', async (t) => {
  const { server, ll } = boot();
  await new Promise((r) => server.listen(0, '127.0.0.1', r));
  const base = `http://127.0.0.1:${server.address().port}`;
  t.after(() => server.close());

  const health = await (await fetch(`${base}/health`)).json();
  assert.equal(health.ok, true);
  assert.equal(health.lootLocker, 'MockLootLocker');

  const opened = await call(base, '/v1/matches', {
    matchId: 'http-match-1', players: [{ playerId: 7, ulid: 'ULID7' }],
  });
  assert.equal(opened.status, 200);
  assert.equal(opened.json.result.playerCount, 1);

  const granted = await call(base, '/v1/grant/currency', {
    requestId: 'http-req-00001', matchId: 'http-match-1', playerId: 7,
    currencies: [{ currencyId: 'SOFT', amount: 120 }],
  });
  assert.equal(granted.status, 200);
  assert.equal((await ll.listBalances('wallet_7')).SOFT, 120);

  const forged = await call(base, '/v1/grant/currency', {
    requestId: 'http-req-00002', matchId: 'http-match-1', playerId: 7,
    currencies: [{ currencyId: 'SOFT', amount: 5000 }],
  }, { secret: 'wrong-secret' });
  assert.equal(forged.status, 401);
  assert.equal(forged.json.error, 'bad_signature');
  assert.equal((await ll.listBalances('wallet_7')).SOFT, 120, 'nothing granted on a bad signature');

  const refused = await call(base, '/v1/grant/currency', {
    requestId: 'http-req-00003', matchId: 'http-match-1', playerId: 7,
    currencies: [{ currencyId: 'SOFT', amount: 5000 }],
  });
  assert.equal(refused.status, 422);
  assert.equal(refused.json.error, 'match_cap_exceeded');
});
