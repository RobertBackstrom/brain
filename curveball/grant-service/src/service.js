// The grant service proper. HTTP-free so it can be tested directly.
//
// Every entry point follows the same shape:
//   idempotency -> match validity -> player is in the match -> rule check -> LootLocker -> ledger
//
// The ledger write happens after LootLocker confirms, and carries what was actually
// applied rather than what was asked for, because the soft-currency clamp can make
// those differ.

import {
  KIND, RuleError, clampSoftCurrency, validateAssetGrant, validateCurrencyGrant,
  validateProgressionGrant, validateMatchOpen, assertMatchGrantable, assertPlayerInMatch,
  assertWithinCaps,
} from './rules.js';

export class GrantService {
  constructor({ ledger, lootLocker, limits, now = () => Math.floor(Date.now() / 1000) }) {
    this.ledger = ledger;
    this.ll = lootLocker;
    this.limits = limits;
    this.now = now;
  }

  openMatch(body, caller) {
    const now = this.now();
    const match = validateMatchOpen(body, this.limits, now);
    if (this.ledger.getMatch(match.matchId)) throw new RuleError('match_already_open', match.matchId);
    this.ledger.openMatch({
      id: match.matchId,
      hostSteamId: caller?.steamId ?? null,
      mode: match.mode,
      players: match.players,
      now,
    });
    return { matchId: match.matchId, openedAt: now, playerCount: match.players.length };
  }

  closeMatch(matchId) {
    const row = this.ledger.getMatch(matchId);
    if (!row) throw new RuleError('unknown_match', matchId);
    const now = this.now();
    this.ledger.closeMatch(matchId, now);
    return { matchId, closedAt: now };
  }

  #preflight({ requestId, matchId, playerId }) {
    if (typeof requestId !== 'string' || requestId.length < 8) {
      throw new RuleError('bad_request_id', requestId);
    }
    if (!Number.isInteger(playerId)) throw new RuleError('bad_player_id', playerId);

    const replay = this.ledger.findGrant(requestId);
    if (replay) return { replay: replay.applied };

    const now = this.now();
    const match = this.ledger.getMatch(matchId);
    assertMatchGrantable(match, this.limits, now);
    assertPlayerInMatch(this.ledger.isPlayerInMatch(matchId, playerId), playerId);
    return {
      now,
      matchTotals: this.ledger.totalsForMatch(matchId, playerId),
      windowTotals: this.ledger.totalsInWindow(playerId, now - this.limits.windowSeconds),
    };
  }

  async grantAssets(body, caller) {
    const pre = this.#preflight(body);
    if (pre.replay) return { ...pre.replay, idempotent: true };

    const assetIds = validateAssetGrant(body.assetIds, this.limits);
    assertWithinCaps({
      kind: KIND.ASSETS,
      amount: assetIds.length,
      matchTotals: pre.matchTotals,
      windowTotals: pre.windowTotals,
      limits: this.limits,
    });

    const granted = await this.ll.addAssets(body.playerId, assetIds);
    const applied = { kind: KIND.ASSETS, playerId: body.playerId, assetIds: granted };

    this.ledger.recordGrant({
      requestId: body.requestId,
      matchId: body.matchId,
      playerId: body.playerId,
      kind: KIND.ASSETS,
      assetCount: granted.length,
      request: body,
      applied,
      identityProven: Boolean(caller?.identityProven),
      now: pre.now,
    });
    return applied;
  }

  async grantCurrency(body, caller) {
    const pre = this.#preflight(body);
    if (pre.replay) return { ...pre.replay, idempotent: true };

    const { credit, debit } = validateCurrencyGrant(body.currencies, this.limits);

    // Mirrors PlayerProfileChanged: an unset wallet is fetched rather than treated
    // as an error, since the client sends "NOT_SET" before its first wallet lookup.
    let walletId = body.walletId;
    if (!walletId || walletId === 'NOT_SET') walletId = await this.ll.getWalletId(body.playerId);
    if (!walletId) throw new RuleError('no_wallet_for_player', body.playerId);

    let creditsToApply = credit;
    const touchesSoftCurrency = credit.some((c) => c.currencyId === this.limits.softCurrencyId);
    if (touchesSoftCurrency) {
      const balances = await this.ll.listBalances(walletId);
      creditsToApply = clampSoftCurrency(credit, balances, this.limits);
    }

    const creditTotal = creditsToApply.reduce((sum, c) => sum + c.amount, 0);
    assertWithinCaps({
      kind: KIND.CURRENCY,
      amount: creditTotal,
      matchTotals: pre.matchTotals,
      windowTotals: pre.windowTotals,
      limits: this.limits,
    });

    // Debits first, same order as ULootLockerServerGranter::AddCurrencyToPlayer.
    const applied = { kind: KIND.CURRENCY, playerId: body.playerId, walletId, credited: [], debited: [] };
    for (const item of debit) {
      await this.ll.debitWallet(walletId, item.currencyId, item.amount);
      applied.debited.push(item);
    }
    for (const item of creditsToApply) {
      if (item.amount <= 0) {
        applied.credited.push({ ...item, skipped: 'at_cap' });
        continue;
      }
      await this.ll.creditWallet(walletId, item.currencyId, item.amount);
      applied.credited.push(item);
    }

    this.ledger.recordGrant({
      requestId: body.requestId,
      matchId: body.matchId,
      playerId: body.playerId,
      kind: KIND.CURRENCY,
      amount: creditTotal,
      currencyId: creditsToApply[0]?.currencyId ?? debit[0]?.currencyId ?? null,
      request: body,
      applied,
      identityProven: Boolean(caller?.identityProven),
      now: pre.now,
    });
    return applied;
  }

  async grantProgression(body, caller) {
    const pre = this.#preflight(body);
    if (pre.replay) return { ...pre.replay, idempotent: true };

    const { progressionKey, amount } = validateProgressionGrant(body, this.limits);
    assertWithinCaps({
      kind: KIND.PROGRESSION,
      amount: Math.max(amount, 0),
      matchTotals: pre.matchTotals,
      windowTotals: pre.windowTotals,
      limits: this.limits,
    });

    const res = await this.ll.changeProgression(body.playerId, progressionKey, amount);
    const applied = {
      kind: KIND.PROGRESSION,
      playerId: body.playerId,
      progressionKey,
      amount,
      points: res?.points ?? null,
      step: res?.step ?? null,
      // Tier rewards come back from LootLocker and the client mirrors them onto the
      // player controller, so they are passed through untouched.
      awardedTiers: res?.awarded_tiers ?? [],
    };

    this.ledger.recordGrant({
      requestId: body.requestId,
      matchId: body.matchId,
      playerId: body.playerId,
      kind: KIND.PROGRESSION,
      amount,
      progressionKey,
      request: body,
      applied,
      identityProven: Boolean(caller?.identityProven),
      now: pre.now,
    });
    return applied;
  }
}

export default GrantService;
