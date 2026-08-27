// Request authentication.
//
// Canonical string that gets signed:
//   <METHOD>\n<PATH>\n<TIMESTAMP>\n<NONCE>\n<sha256(body) as hex>
//
// Headers:
//   X-MLC-Timestamp   unix seconds
//   X-MLC-Nonce       random, unique within the TTL window
//   X-MLC-Signature   hex hmac-sha256 of the canonical string
//   X-MLC-Steam-Id    caller's SteamID64 (informational under hmac, verified under steam)
//   X-MLC-Steam-Ticket  session ticket, required when authMode is "steam"
//
// Replay protection is the nonce cache plus the timestamp window. Both are needed:
// the window bounds how long the cache has to remember, the cache stops replays
// inside the window.

import crypto from 'node:crypto';

export class NonceCache {
  #seen = new Map(); // nonce -> expiry epoch seconds

  constructor(ttlSeconds) {
    this.ttl = ttlSeconds;
  }

  // Returns false if the nonce was already used.
  claim(nonce, nowSeconds) {
    this.#sweep(nowSeconds);
    if (this.#seen.has(nonce)) return false;
    this.#seen.set(nonce, nowSeconds + this.ttl);
    return true;
  }

  #sweep(nowSeconds) {
    for (const [nonce, expiry] of this.#seen) {
      if (expiry <= nowSeconds) this.#seen.delete(nonce);
    }
  }

  get size() {
    return this.#seen.size;
  }
}

export function canonicalString(method, path, timestamp, nonce, rawBody) {
  const bodyHash = crypto.createHash('sha256').update(rawBody ?? '').digest('hex');
  return [method.toUpperCase(), path, String(timestamp), nonce, bodyHash].join('\n');
}

export function sign(secret, method, path, timestamp, nonce, rawBody) {
  return crypto
    .createHmac('sha256', secret)
    .update(canonicalString(method, path, timestamp, nonce, rawBody))
    .digest('hex');
}

function timingSafeEqualHex(a, b) {
  if (typeof a !== 'string' || typeof b !== 'string' || a.length !== b.length) return false;
  try {
    return crypto.timingSafeEqual(Buffer.from(a, 'hex'), Buffer.from(b, 'hex'));
  } catch {
    return false;
  }
}

// Verifier for authMode "hmac". Development only, see README.
export class HmacVerifier {
  constructor({ secret, clockSkewSeconds, nonceCache, now = () => Math.floor(Date.now() / 1000) }) {
    this.secret = secret;
    this.clockSkew = clockSkewSeconds;
    this.nonces = nonceCache;
    this.now = now;
  }

  // Returns { ok: true, caller } or { ok: false, status, error }.
  verify({ method, path, headers, rawBody }) {
    const timestamp = Number.parseInt(headers['x-mlc-timestamp'] ?? '', 10);
    const nonce = headers['x-mlc-nonce'];
    const signature = headers['x-mlc-signature'];

    if (!Number.isFinite(timestamp) || !nonce || !signature) {
      return { ok: false, status: 401, error: 'missing_auth_headers' };
    }

    const now = this.now();
    if (Math.abs(now - timestamp) > this.clockSkew) {
      return { ok: false, status: 401, error: 'timestamp_outside_window' };
    }

    const expected = sign(this.secret, method, path, timestamp, nonce, rawBody);
    if (!timingSafeEqualHex(expected, signature)) {
      return { ok: false, status: 401, error: 'bad_signature' };
    }

    if (!this.nonces.claim(nonce, now)) {
      return { ok: false, status: 401, error: 'nonce_replayed' };
    }

    return {
      ok: true,
      caller: {
        steamId: headers['x-mlc-steam-id'] ?? null,
        // Under hmac the identity is asserted, not proven. The ledger records
        // that so an audit can tell the two modes apart after the fact.
        identityProven: false,
      },
    };
  }
}

// Verifier for authMode "steam". Wraps the hmac check and additionally proves the
// caller owns the SteamID64 it claims, via ISteamUserAuth/AuthenticateUserTicket.
//
// This needs a Steam Web API publisher key for app 2805120, which Aurora Punks does
// not have for this title yet. Ticket verification is injected so the service can be
// wired, tested and reviewed before that access exists.
export class SteamVerifier {
  constructor({ hmacVerifier, verifyTicket }) {
    this.hmac = hmacVerifier;
    this.verifyTicket = verifyTicket;
  }

  async verify(request) {
    const base = this.hmac.verify(request);
    if (!base.ok) return base;

    const ticket = request.headers['x-mlc-steam-ticket'];
    const claimedSteamId = request.headers['x-mlc-steam-id'];
    if (!ticket || !claimedSteamId) {
      return { ok: false, status: 401, error: 'missing_steam_ticket' };
    }

    const result = await this.verifyTicket(ticket);
    if (!result?.ok) {
      return { ok: false, status: 401, error: result?.error ?? 'steam_ticket_rejected' };
    }
    if (result.steamId !== claimedSteamId) {
      return { ok: false, status: 401, error: 'steam_id_mismatch' };
    }

    return { ok: true, caller: { steamId: result.steamId, identityProven: true } };
  }
}
