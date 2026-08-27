// LootLocker server API client, plus an in-memory mock with the same interface.
//
// The interface is the set of calls ULootLockerServerGranter actually makes:
//   getWalletId, listBalances, creditWallet, debitWallet, addAssets, changeProgression
//
// IMPORTANT: the request paths below are UNVERIFIED. We have no LootLocker access for
// game a86igukp yet (asked 2026-08-19, unanswered), so they are written from the shape
// of the calls the UE server SDK makes and must be confirmed against the LootLocker
// server API reference before the first real call. They are collected in ENDPOINTS
// precisely so that confirmation is a single edit. Everything else in this service,
// including every test, runs against the mock and does not depend on them.

export const ENDPOINTS = {
  playerInfo: (playerId) => `/players/${playerId}/info`,
  walletBalances: (walletId) => `/balances/wallet/${walletId}`,
  credit: () => '/balances/credit',
  debit: () => '/balances/debit',
  alterInventory: (playerId) => `/players/${playerId}/inventory`,
  progressionAdd: (playerId, key) => `/players/${playerId}/progressions/${key}/points/add`,
  progressionSubtract: (playerId, key) => `/players/${playerId}/progressions/${key}/points/subtract`,
};

export class LootLockerError extends Error {
  constructor(message, { status, body, retryable } = {}) {
    super(message);
    this.status = status ?? null;
    this.body = body ?? null;
    this.retryable = Boolean(retryable);
  }
}

export class LootLockerClient {
  constructor({ baseUrl, serverKey, timeoutMs, maxRetries, fetchImpl = fetch, sleep }) {
    this.baseUrl = baseUrl.replace(/\/$/, '');
    this.serverKey = serverKey;
    this.timeoutMs = timeoutMs;
    this.maxRetries = maxRetries;
    this.fetch = fetchImpl;
    this.sleep = sleep ?? ((ms) => new Promise((r) => setTimeout(r, ms)));
  }

  // Mirrors ULootLockerApiQueue::HandleServerApiResponseWithRetry: transient failures
  // are retried, a rejection is not. Backoff is exponential so a LootLocker outage
  // does not turn into a request storm from every host at once.
  async #request(method, path, body) {
    let lastError;
    for (let attempt = 0; attempt <= this.maxRetries; attempt += 1) {
      const controller = new AbortController();
      const timer = setTimeout(() => controller.abort(), this.timeoutMs);
      try {
        const res = await this.fetch(this.baseUrl + path, {
          method,
          headers: {
            'Content-Type': 'application/json',
            'x-server-key': this.serverKey,
          },
          body: body === undefined ? undefined : JSON.stringify(body),
          signal: controller.signal,
        });
        const text = await res.text();
        const parsed = text ? JSON.parse(text) : {};
        if (res.ok) return parsed;
        const retryable = res.status === 429 || res.status >= 500;
        lastError = new LootLockerError(`lootlocker_${res.status}`, {
          status: res.status, body: parsed, retryable,
        });
        if (!retryable) throw lastError;
      } catch (err) {
        lastError = err instanceof LootLockerError
          ? err
          : new LootLockerError(err.name === 'AbortError' ? 'lootlocker_timeout' : 'lootlocker_network', { retryable: true });
        if (!lastError.retryable) throw lastError;
      } finally {
        clearTimeout(timer);
      }
      if (attempt < this.maxRetries) await this.sleep(2 ** attempt * 250);
    }
    throw lastError;
  }

  async getWalletId(playerId) {
    const res = await this.#request('GET', ENDPOINTS.playerInfo(playerId));
    return res?.wallet_id ?? res?.player?.wallet_id ?? null;
  }

  async listBalances(walletId) {
    const res = await this.#request('GET', ENDPOINTS.walletBalances(walletId));
    const out = {};
    for (const b of res?.balances ?? []) {
      out[b.currency?.id ?? b.currency_id] = Number.parseInt(b.amount, 10) || 0;
    }
    return out;
  }

  creditWallet(walletId, currencyId, amount) {
    return this.#request('POST', ENDPOINTS.credit(), {
      wallet_id: walletId, currency_id: currencyId, amount: String(amount),
    });
  }

  debitWallet(walletId, currencyId, amount) {
    return this.#request('POST', ENDPOINTS.debit(), {
      wallet_id: walletId, currency_id: currencyId, amount: String(amount),
    });
  }

  async addAssets(playerId, assetIds) {
    const res = await this.#request('POST', ENDPOINTS.alterInventory(playerId), {
      add: assetIds.map((id) => ({ asset_id: id })),
      remove: [],
    });
    return (res?.added ?? []).map((item) => item.id ?? item.asset_id);
  }

  changeProgression(playerId, progressionKey, amount) {
    const path = amount > 0
      ? ENDPOINTS.progressionAdd(playerId, progressionKey)
      : ENDPOINTS.progressionSubtract(playerId, progressionKey);
    return this.#request('POST', path, { amount: Math.abs(amount) });
  }
}

// Mock with the same surface. Holds wallets, inventories and progression in memory so
// the whole service can be exercised end to end without LootLocker access.
export class MockLootLocker {
  constructor(seed = {}) {
    this.wallets = new Map(Object.entries(seed.wallets ?? {}));   // walletId -> {currencyId: amount}
    this.walletIds = new Map(Object.entries(seed.walletIds ?? {}));// playerId -> walletId
    this.inventories = new Map();                                  // playerId -> Set(assetId)
    this.progression = new Map();                                  // `${playerId}:${key}` -> points
    this.calls = [];
  }

  #log(name, args) {
    this.calls.push({ name, args });
  }

  async getWalletId(playerId) {
    this.#log('getWalletId', { playerId });
    const existing = this.walletIds.get(String(playerId));
    if (existing) return existing;
    const created = `wallet_${playerId}`;
    this.walletIds.set(String(playerId), created);
    if (!this.wallets.has(created)) this.wallets.set(created, {});
    return created;
  }

  async listBalances(walletId) {
    this.#log('listBalances', { walletId });
    return { ...(this.wallets.get(walletId) ?? {}) };
  }

  async creditWallet(walletId, currencyId, amount) {
    this.#log('creditWallet', { walletId, currencyId, amount });
    const wallet = this.wallets.get(walletId) ?? {};
    wallet[currencyId] = (wallet[currencyId] ?? 0) + amount;
    this.wallets.set(walletId, wallet);
    return { currency: { id: currencyId }, amount: String(amount) };
  }

  async debitWallet(walletId, currencyId, amount) {
    this.#log('debitWallet', { walletId, currencyId, amount });
    const wallet = this.wallets.get(walletId) ?? {};
    wallet[currencyId] = Math.max((wallet[currencyId] ?? 0) - amount, 0);
    this.wallets.set(walletId, wallet);
    return { currency: { id: currencyId }, amount: String(amount) };
  }

  async addAssets(playerId, assetIds) {
    this.#log('addAssets', { playerId, assetIds });
    const inv = this.inventories.get(playerId) ?? new Set();
    for (const id of assetIds) inv.add(id);
    this.inventories.set(playerId, inv);
    return [...assetIds];
  }

  async changeProgression(playerId, progressionKey, amount) {
    this.#log('changeProgression', { playerId, progressionKey, amount });
    const key = `${playerId}:${progressionKey}`;
    const points = Math.max((this.progression.get(key) ?? 0) + amount, 0);
    this.progression.set(key, points);
    return { progression_key: progressionKey, points, step: 1, awarded_tiers: [] };
  }
}

export function makeLootLocker(config) {
  if (!config.lootLocker.serverKey) return new MockLootLocker();
  return new LootLockerClient(config.lootLocker);
}
