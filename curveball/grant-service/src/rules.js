// Plausibility rules.
//
// On a dedicated server, "can this grant happen" was answered by
// UHelperLibrary::IsWorldDedicatedServer: the machine asking was ours, so it was
// trusted. Under P2P the machine asking is a player's, so trust has to be replaced
// by arithmetic. These rules are that arithmetic.
//
// The rules do not try to detect cheating. They bound what a compromised host can
// take, and they make what it took visible in the ledger.

export const KIND = { CURRENCY: 'currency', ASSETS: 'assets', PROGRESSION: 'progression' };

export class RuleError extends Error {
  constructor(code, detail) {
    super(code);
    this.code = code;
    this.detail = detail ?? null;
  }
}

// Aggregate a currency list the way ULootLockerServerGranter::AddCurrencyToPlayer does:
// same currency id appearing twice is summed, and credits and debits are separated.
export function splitCurrencies(entries) {
  const credit = new Map();
  const debit = new Map();
  for (const item of entries) {
    const amount = Number(item.amount);
    if (!Number.isInteger(amount) || amount === 0) continue;
    const target = amount > 0 ? credit : debit;
    const key = item.currencyId;
    target.set(key, (target.get(key) ?? 0) + Math.abs(amount));
  }
  return {
    credit: [...credit].map(([currencyId, amount]) => ({ currencyId, amount })),
    debit: [...debit].map(([currencyId, amount]) => ({ currencyId, amount })),
  };
}

// ULootLockerServerGranter::CreditCurrencyToPlayerCapped, ported exactly:
// the soft currency is clamped so balance + credit never exceeds the cap, and a
// wallet already at or over the cap gets zero rather than a negative credit.
export function clampSoftCurrency(credits, walletBalances, limits) {
  return credits.map((entry) => {
    if (entry.currencyId !== limits.softCurrencyId) return entry;
    const balance = Number(walletBalances?.[entry.currencyId] ?? 0);
    if (balance + entry.amount <= limits.softCurrencyCap) return entry;
    return { ...entry, amount: Math.max(limits.softCurrencyCap - balance, 0), clamped: true };
  });
}

function checkAllowList(list, value, code) {
  if (list.length > 0 && !list.includes(value)) throw new RuleError(code, String(value));
}

export function validateMatchOpen(match, limits, now) {
  if (!match.matchId) throw new RuleError('missing_match_id');
  if (!Array.isArray(match.players) || match.players.length === 0) {
    throw new RuleError('match_needs_players');
  }
  if (match.players.length > limits.maxPlayersPerMatch) {
    throw new RuleError('too_many_players', match.players.length);
  }
  const seen = new Set();
  for (const p of match.players) {
    if (!Number.isInteger(p.playerId)) throw new RuleError('bad_player_id', p.playerId);
    if (seen.has(p.playerId)) throw new RuleError('duplicate_player', p.playerId);
    seen.add(p.playerId);
  }
  return { matchId: match.matchId, players: match.players, mode: match.mode ?? null, openedAt: now };
}

// A match that is not open, is already closed, or ran impossibly short or long
// cannot produce grants. minMatchSeconds is the one that matters: it stops a host
// opening and immediately harvesting a match that was never played.
export function assertMatchGrantable(matchRow, limits, now) {
  if (!matchRow) throw new RuleError('unknown_match');
  if (matchRow.closed_at) throw new RuleError('match_closed');
  const age = now - matchRow.opened_at;
  if (age < limits.minMatchSeconds) throw new RuleError('match_too_young', age);
  if (age > limits.maxMatchSeconds) throw new RuleError('match_too_old', age);
}

export function assertPlayerInMatch(inMatch, playerId) {
  if (!inMatch) throw new RuleError('player_not_in_match', playerId);
}

// Caps are checked against what the ledger already holds, so splitting a grant into
// several requests hits the same ceiling as asking for it all at once.
export function assertWithinCaps({ kind, amount, matchTotals, windowTotals, limits }) {
  const perMatch = {
    [KIND.CURRENCY]: limits.maxCurrencyPerMatch,
    [KIND.ASSETS]: limits.maxAssetsPerMatch,
    [KIND.PROGRESSION]: limits.maxProgressionPerMatch,
  }[kind];
  const perWindow = {
    [KIND.CURRENCY]: limits.maxCurrencyPerWindow,
    [KIND.ASSETS]: limits.maxAssetsPerWindow,
    [KIND.PROGRESSION]: limits.maxProgressionPerWindow,
  }[kind];

  const usedMatch = { currency: matchTotals.currency, assets: matchTotals.assets, progression: matchTotals.progression }[kind];
  const usedWindow = { currency: windowTotals.currency, assets: windowTotals.assets, progression: windowTotals.progression }[kind];

  if (usedMatch + amount > perMatch) {
    throw new RuleError('match_cap_exceeded', { kind, used: usedMatch, requested: amount, cap: perMatch });
  }
  if (usedWindow + amount > perWindow) {
    throw new RuleError('window_cap_exceeded', { kind, used: usedWindow, requested: amount, cap: perWindow });
  }
}

export function validateAssetGrant(assetIds, limits) {
  if (!Array.isArray(assetIds) || assetIds.length === 0) throw new RuleError('no_assets');
  for (const id of assetIds) {
    if (!Number.isInteger(id) || id <= 0) throw new RuleError('bad_asset_id', id);
    checkAllowList(limits.allowedAssetIds, id, 'asset_not_allowed');
  }
  if (assetIds.length !== new Set(assetIds).size) throw new RuleError('duplicate_assets');
  return assetIds;
}

export function validateCurrencyGrant(entries, limits) {
  if (!Array.isArray(entries) || entries.length === 0) throw new RuleError('no_currencies');
  for (const entry of entries) {
    if (typeof entry.currencyId !== 'string' || entry.currencyId === '') {
      throw new RuleError('bad_currency_id', entry.currencyId);
    }
    if (!Number.isInteger(entry.amount)) throw new RuleError('bad_amount', entry.amount);
    checkAllowList(limits.allowedCurrencyIds, entry.currencyId, 'currency_not_allowed');
  }
  return splitCurrencies(entries);
}

// AddProgressionForPlayer rejects zero outright, and so do we.
export function validateProgressionGrant({ progressionKey, amount }, limits) {
  if (typeof progressionKey !== 'string' || progressionKey === '') {
    throw new RuleError('bad_progression_key', progressionKey);
  }
  if (!Number.isInteger(amount) || amount === 0) throw new RuleError('bad_progression_amount', amount);
  checkAllowList(limits.allowedProgressionKeys, progressionKey, 'progression_not_allowed');
  return { progressionKey, amount };
}
