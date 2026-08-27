// HTTP front for the grant service. Zero dependencies, same shape as build-drop-server.js.

import http from 'node:http';
import config from './config.js';
import { HmacVerifier, NonceCache, SteamVerifier } from './auth.js';
import { Ledger } from './ledger.js';
import { makeLootLocker } from './lootlocker.js';
import { GrantService } from './service.js';
import { RuleError } from './rules.js';

const MAX_BODY_BYTES = 64 * 1024;

function readBody(req) {
  return new Promise((resolve, reject) => {
    const chunks = [];
    let size = 0;
    req.on('data', (chunk) => {
      size += chunk.length;
      if (size > MAX_BODY_BYTES) {
        reject(new RuleError('body_too_large'));
        req.destroy();
        return;
      }
      chunks.push(chunk);
    });
    req.on('end', () => resolve(Buffer.concat(chunks).toString('utf8')));
    req.on('error', reject);
  });
}

function send(res, status, payload) {
  const body = JSON.stringify(payload);
  res.writeHead(status, { 'Content-Type': 'application/json', 'Content-Length': Buffer.byteLength(body) });
  res.end(body);
}

export function createServer({ service, verifier, logRequests = true } = {}) {
  const routes = {
    'POST /v1/matches': (body, caller) => service.openMatch(body, caller),
    'POST /v1/matches/close': (body) => service.closeMatch(body.matchId),
    'POST /v1/grant/assets': (body, caller) => service.grantAssets(body, caller),
    'POST /v1/grant/currency': (body, caller) => service.grantCurrency(body, caller),
    'POST /v1/grant/progression': (body, caller) => service.grantProgression(body, caller),
  };

  return http.createServer(async (req, res) => {
    const url = new URL(req.url, 'http://localhost');
    const key = `${req.method} ${url.pathname}`;

    if (key === 'GET /health') {
      send(res, 200, { ok: true, mode: config.authMode, lootLocker: service.ll.constructor.name });
      return;
    }

    const handler = routes[key];
    if (!handler) {
      send(res, 404, { error: 'not_found' });
      return;
    }

    let rawBody;
    try {
      rawBody = await readBody(req);
    } catch (err) {
      send(res, 413, { error: err.code ?? 'bad_body' });
      return;
    }

    const auth = await verifier.verify({
      method: req.method,
      path: url.pathname,
      headers: req.headers,
      rawBody,
    });
    if (!auth.ok) {
      if (logRequests) console.warn(`[grant] auth rejected ${key}: ${auth.error}`);
      send(res, auth.status, { error: auth.error });
      return;
    }

    let body;
    try {
      body = rawBody ? JSON.parse(rawBody) : {};
    } catch {
      send(res, 400, { error: 'bad_json' });
      return;
    }

    try {
      const result = await handler(body, auth.caller);
      if (logRequests) {
        console.log(`[grant] ${key} ok player=${body.playerId ?? '-'} match=${body.matchId ?? '-'}`);
      }
      send(res, 200, { ok: true, result });
    } catch (err) {
      if (err instanceof RuleError) {
        if (logRequests) console.warn(`[grant] ${key} refused: ${err.code} ${JSON.stringify(err.detail)}`);
        send(res, 422, { error: err.code, detail: err.detail });
        return;
      }
      console.error(`[grant] ${key} failed:`, err);
      send(res, 502, { error: 'upstream_failed', detail: err.message });
    }
  });
}

export function buildDefaultServer() {
  const ledger = new Ledger(config.dbPath);
  const lootLocker = makeLootLocker(config);
  const service = new GrantService({ ledger, lootLocker, limits: config.limits });
  const hmac = new HmacVerifier({
    secret: config.hmacSecret,
    clockSkewSeconds: config.clockSkewSeconds,
    nonceCache: new NonceCache(config.nonceTtlSeconds),
  });
  const verifier = config.authMode === 'steam'
    ? new SteamVerifier({
      hmacVerifier: hmac,
      verifyTicket: async () => ({ ok: false, error: 'steam_verification_not_configured' }),
    })
    : { verify: (req) => hmac.verify(req) };
  return { server: createServer({ service, verifier, logRequests: config.logRequests }), ledger, service };
}

if (import.meta.url === `file://${process.argv[1]}`) {
  const { server } = buildDefaultServer();
  server.listen(config.port, config.host, () => {
    console.log(`[grant] listening on ${config.host}:${config.port} auth=${config.authMode}`);
    if (!config.lootLocker.serverKey) {
      console.log('[grant] no LOOTLOCKER_SERVER_KEY set, running against the in-memory mock');
    }
    if (config.authMode === 'hmac') {
      console.log('[grant] auth mode hmac is development only, see README');
    }
  });
}
