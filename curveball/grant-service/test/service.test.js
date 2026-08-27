import test from 'node:test';
import assert from 'node:assert/strict';
import { Ledger } from '../src/ledger.js';
import { MockLootLocker } from '../src/lootlocker.js';
import { GrantService } from '../src/service.js';

const limits = {
  softCurrencyId: 'SOFT',
  softCurrencyCap: 6000,
  maxCurrencyPerMatch: 500,
  maxAssetsPerMatch: 4,
  maxProgressionPerMatch: 1000,
  windowSeconds: 3600,
  maxCurrencyPerWindow: 3000,
  maxAssetsPerWindow: 20,
  maxProgressionPerWindow: 6000,
  minMatchSeconds: 30,
  maxMatchSeconds: 3600,
  maxPlayersPerMatch: 16,
  allowedCurrencyIds: [],
  allowedProgressionKeys: [],
  allowedAssetIds: [],
};

function harness({ startAt = 1_000_000 } = {}) {
  let clock = startAt;
  const ledger = new Ledger(':memory:');
  const ll = new MockLootLocker({ walletIds: { 7: 'wallet_7' }, wallets: { wallet_7: { SOFT: 0 } } });
  const service = new GrantService({ ledger, lootLocker: ll, limits, now: () => clock });
  return {
    ledger, ll, service,
    tick: (seconds) => { clock += seconds; },
    now: () => clock,
  };
}

async function openPlayedMatch(h, matchId = 'match-1') {
  h.service.openMatch({ matchId, players: [{ playerId: 7, ulid: 'ULID7', steamId: '76561198000000007' }] },
    { steamId: '76561198000000007' });
  h.tick(120); // long enough to have been played
  return matchId;
}

test('happy path: currency lands in the wallet and in the ledger', async () => {
  const h = harness();
  const matchId = await openPlayedMatch(h);
  const applied = await h.service.grantCurrency({
    requestId: 'req-currency-0001', matchId, playerId: 7,
    currencies: [{ currencyId: 'SOFT', amount: 250 }],
  }, { identityProven: false });

  assert.deepEqual(applied.credited, [{ currencyId: 'SOFT', amount: 250 }]);
  assert.equal((await h.ll.listBalances('wallet_7')).SOFT, 250);
  assert.equal(h.ledger.totalsForMatch(matchId, 7).currency, 250);
});

test('a retried grant is applied once, which is what LootLockerApiQueue will do to us', async () => {
  const h = harness();
  const matchId = await openPlayedMatch(h);
  const body = {
    requestId: 'req-retry-0001', matchId, playerId: 7,
    currencies: [{ currencyId: 'SOFT', amount: 100 }],
  };
  const first = await h.service.grantCurrency(body, {});
  const second = await h.service.grantCurrency(body, {});

  assert.equal(second.idempotent, true);
  assert.deepEqual(second.credited, first.credited);
  assert.equal((await h.ll.listBalances('wallet_7')).SOFT, 100, 'wallet credited once');
});

test('the soft cap is enforced against the live wallet balance', async () => {
  const h = harness();
  h.ll.wallets.set('wallet_7', { SOFT: 5900 });
  const matchId = await openPlayedMatch(h);

  const applied = await h.service.grantCurrency({
    requestId: 'req-cap-0001', matchId, playerId: 7,
    currencies: [{ currencyId: 'SOFT', amount: 400 }],
  }, {});

  assert.equal(applied.credited[0].amount, 100);
  assert.equal(applied.credited[0].clamped, true);
  assert.equal((await h.ll.listBalances('wallet_7')).SOFT, 6000);
});

test('a host cannot grant to somebody who was not in the match', async () => {
  const h = harness();
  const matchId = await openPlayedMatch(h);
  await assert.rejects(
    () => h.service.grantCurrency({
      requestId: 'req-outsider-01', matchId, playerId: 999,
      currencies: [{ currencyId: 'SOFT', amount: 10 }],
    }, {}),
    /player_not_in_match/,
  );
});

test('a host cannot harvest a match that was never played', async () => {
  const h = harness();
  h.service.openMatch({ matchId: 'instant', players: [{ playerId: 7 }] }, {});
  h.tick(2);
  await assert.rejects(
    () => h.service.grantProgression({
      requestId: 'req-instant-001', matchId: 'instant', playerId: 7, progressionKey: 'xp', amount: 100,
    }, {}),
    /match_too_young/,
  );
});

test('splitting a grant into pieces hits the same match cap', async () => {
  const h = harness();
  const matchId = await openPlayedMatch(h);
  for (let i = 0; i < 5; i += 1) {
    await h.service.grantCurrency({
      requestId: `req-split-000${i}`, matchId, playerId: 7,
      currencies: [{ currencyId: 'HARD', amount: 100 }],
    }, {});
  }
  await assert.rejects(
    () => h.service.grantCurrency({
      requestId: 'req-split-0099', matchId, playerId: 7,
      currencies: [{ currencyId: 'HARD', amount: 1 }],
    }, {}),
    /match_cap_exceeded/,
  );
});

test('opening fresh matches does not reset the rolling window', async () => {
  const h = harness();
  const grantInFreshMatch = (m) => {
    const matchId = `match-window-${m}`;
    h.service.openMatch({ matchId, players: [{ playerId: 7 }] }, {});
    h.tick(60);
    return h.service.grantCurrency({
      requestId: `req-window-00${m}`, matchId, playerId: 7,
      currencies: [{ currencyId: 'HARD', amount: 500 }],
    }, {});
  };

  // maxCurrencyPerWindow is 3000, so six matches of 500 fit exactly.
  for (let m = 0; m < 6; m += 1) await grantInFreshMatch(m);
  assert.equal(h.ledger.totalsInWindow(7, h.now() - 3600).currency, 3000);

  // The seventh match is a new match with an empty per-match total, and is still refused.
  await assert.rejects(() => grantInFreshMatch(6), /window_cap_exceeded/);
});

test('closed matches stop granting', async () => {
  const h = harness();
  const matchId = await openPlayedMatch(h);
  h.service.closeMatch(matchId);
  await assert.rejects(
    () => h.service.grantAssets({ requestId: 'req-closed-001', matchId, playerId: 7, assetIds: [651820] }, {}),
    /match_closed/,
  );
});

test('assets are granted and counted, and the per-match count holds', async () => {
  const h = harness();
  const matchId = await openPlayedMatch(h);
  await h.service.grantAssets({ requestId: 'req-assets-001', matchId, playerId: 7, assetIds: [1, 2, 3, 4] }, {});
  assert.deepEqual([...h.ll.inventories.get(7)], [1, 2, 3, 4]);
  await assert.rejects(
    () => h.service.grantAssets({ requestId: 'req-assets-002', matchId, playerId: 7, assetIds: [5] }, {}),
    /match_cap_exceeded/,
  );
});

test('an unset wallet is looked up rather than refused', async () => {
  const h = harness();
  const matchId = await openPlayedMatch(h);
  const applied = await h.service.grantCurrency({
    requestId: 'req-wallet-0001', matchId, playerId: 7, walletId: 'NOT_SET',
    currencies: [{ currencyId: 'HARD', amount: 10 }],
  }, {});
  assert.equal(applied.walletId, 'wallet_7');
  assert.ok(h.ll.calls.some((c) => c.name === 'getWalletId'));
});

test('progression passes tier rewards through untouched', async () => {
  const h = harness();
  const matchId = await openPlayedMatch(h);
  h.ll.changeProgression = async () => ({
    progression_key: 'xp', points: 120, step: 2,
    awarded_tiers: [{ rewards: { asset_rewards: [{ asset_id: 42 }], currency_rewards: [] } }],
  });
  const applied = await h.service.grantProgression({
    requestId: 'req-prog-00001', matchId, playerId: 7, progressionKey: 'xp', amount: 120,
  }, {});
  assert.equal(applied.points, 120);
  assert.equal(applied.awardedTiers[0].rewards.asset_rewards[0].asset_id, 42);
});
