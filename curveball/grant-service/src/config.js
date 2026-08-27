// Configuration for the Curveball grant service.
// Everything is overridable through the environment so the same build runs against
// the LootLocker mock (no access needed) and against the real API (once we have keys).

const bool = (v, dflt) => (v === undefined ? dflt : /^(1|true|yes|on)$/i.test(String(v)));
const int = (v, dflt) => (v === undefined || v === '' ? dflt : Number.parseInt(v, 10));

export const config = {
  port: int(process.env.GRANT_PORT, 8091),
  host: process.env.GRANT_HOST ?? '127.0.0.1',

  // Identity of the caller. "hmac" is a shared secret and is DEVELOPMENT ONLY:
  // the secret ships inside the game client, so any player can extract it.
  // "steam" additionally verifies the caller's Steam session ticket and is what
  // Early Access must run. See README section "Why the shared secret is not enough".
  authMode: process.env.GRANT_AUTH_MODE ?? 'hmac',
  hmacSecret: process.env.GRANT_HMAC_SECRET ?? 'dev-secret-not-for-production',
  clockSkewSeconds: int(process.env.GRANT_CLOCK_SKEW, 60),
  nonceTtlSeconds: int(process.env.GRANT_NONCE_TTL, 300),

  // LootLocker. Absent credentials means the mock backend is used.
  lootLocker: {
    baseUrl: process.env.LOOTLOCKER_SERVER_URL ?? 'https://api.lootlocker.io/server/v1',
    serverKey: process.env.LOOTLOCKER_SERVER_KEY ?? null,
    gameId: process.env.LOOTLOCKER_GAME_ID ?? 'a86igukp',
    timeoutMs: int(process.env.LOOTLOCKER_TIMEOUT_MS, 10000),
    maxRetries: int(process.env.LOOTLOCKER_MAX_RETRIES, 3),
  },

  dbPath: process.env.GRANT_DB ?? new URL('../data/grants.sqlite', import.meta.url).pathname,

  // Plausibility limits. These are the P2P replacement for "only a dedicated server
  // may call this". Ported from ULootLockerServerGranter + tightened per match.
  limits: {
    // ULootLockerServerGranter::SOFT_CURRENCY_CAP
    softCurrencyId: process.env.GRANT_SOFT_CURRENCY_ID ?? '01HSX2NNRWJWXBP89K9Z78VJKC',
    softCurrencyCap: int(process.env.GRANT_SOFT_CURRENCY_CAP, 6000),

    // Per match, per player.
    maxCurrencyPerMatch: int(process.env.GRANT_MAX_CURRENCY_PER_MATCH, 500),
    maxAssetsPerMatch: int(process.env.GRANT_MAX_ASSETS_PER_MATCH, 4),
    maxProgressionPerMatch: int(process.env.GRANT_MAX_PROGRESSION_PER_MATCH, 1000),

    // Rolling window, per player, across matches. Catches a host that opens
    // match after match to farm a single account.
    windowSeconds: int(process.env.GRANT_WINDOW_SECONDS, 3600),
    maxCurrencyPerWindow: int(process.env.GRANT_MAX_CURRENCY_PER_WINDOW, 3000),
    maxAssetsPerWindow: int(process.env.GRANT_MAX_ASSETS_PER_WINDOW, 20),
    maxProgressionPerWindow: int(process.env.GRANT_MAX_PROGRESSION_PER_WINDOW, 6000),

    // A match shorter than this cannot have produced real rewards.
    minMatchSeconds: int(process.env.GRANT_MIN_MATCH_SECONDS, 30),
    maxMatchSeconds: int(process.env.GRANT_MAX_MATCH_SECONDS, 3600),
    maxPlayersPerMatch: int(process.env.GRANT_MAX_PLAYERS_PER_MATCH, 16),

    // Empty list means "any", which is where we start until WP0.3 reads the
    // Blueprints and tells us the real key set. Configure to lock it down.
    allowedCurrencyIds: (process.env.GRANT_ALLOWED_CURRENCY_IDS ?? '').split(',').filter(Boolean),
    allowedProgressionKeys: (process.env.GRANT_ALLOWED_PROGRESSION_KEYS ?? '').split(',').filter(Boolean),
    allowedAssetIds: (process.env.GRANT_ALLOWED_ASSET_IDS ?? '')
      .split(',').filter(Boolean).map((s) => Number.parseInt(s, 10)),
  },

  logRequests: bool(process.env.GRANT_LOG_REQUESTS, true),
};

export default config;
