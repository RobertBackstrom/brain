# Ticker Operating Playbook (rules Ticker follows)

Canonical rules the Ticker agent executes **mechanically** for the SIM sprint. Rationale + expectancy
math live in [sim_strategy_2026-06.md](sim_strategy_2026-06.md). Guardrails in
[risk_limits.json](risk_limits.json). **Robert's only deviation channel is industry insight** (the TTWO
veto model) - see section 7.

## 0. Automation contract (Robert's choices, 2026-06-18) — NOW WIRED
- **Entries:** Ticker proposes entry cards per these rules. Robert CONFIRMS (follows the plan) or
  REJECTS with insight (the override). Every capital deployment passes his gate.
  - **Automated:** a weekday ~08:00-Stockholm scheduled run (in `runRoutine`, after the digest)
    spawns the Ticker agent to execute sections 2-3 and POST entry cards (`awaiting_confirm`) into open
    slots. DRAFTING only - cards still await Robert's confirm. Skipped on weekends + under HALT.
- **Exits:** pre-set at entry and auto-managed. On a confirmed entry, the approved target + stop become
  the exit plan with NO separate confirm (he approved the levels at entry).
  - **Automated (Build 1, `ticker-trades.js`):** on FILL, a resting limit-sell target is placed and the
    stop is monitored every ~15 min against the `ticker-data.js` price; a breach auto-exits (cancel
    target, marketable sell, `stopped_out`); a target fill marks `target_hit`; ~5 trading days flat
    posts a rotation-suggestion card (no auto-close on time). HALT blocks new Buys but ALWAYS allows a
    protective exit Sell. All deterministic - no LLM in the exit loop.

## 1. Universe
The watchlist ([watchlist.json](watchlist.json)) only: SE gaming, SE tech, US gaming, US tech/space.
**SEK-preferred** (clean sizing); USD allowed (FX-converted by the guardrails). Skip any name showing a
corporate-action data anomaly (e.g. a large `previousClose` gap like Embracer's spin-off) until clean.

## 2. Daily scan (each weekday)
1. Pull quote + 1mo/3mo range + annualized vol for the watchlist (`ticker-data.js`).
2. For each name compute: position-in-range, recent trend, distance to a defined support, and a
   `WebSearch` catalyst check (earnings date, product, corporate actions) - flag event risk.
3. **Rank candidates** by a simple score (higher = better):
   - +Setup: clean uptrend continuation OR pullback to defined support with trend intact.
   - +R:R: a sane target gives >= **2.5:1** vs a sane stop.
   - +Catalyst tailwind (not into a binary event); -Catalyst/event risk inside the horizon.
   - -In rejection history for the same setup (section 7) -> skip unless a time-bound reason cleared.
   - -Dirty data / illiquid / anomaly -> skip.
4. Propose entry cards only while a slot is open (open positions + pending cards < **4**) and deployment
   is below ~100%. Target book shape: **2-3 concentrated positions** (~40% each), ~80-100% deployed.

## 3. Entry rules (per proposed card)
- **Order:** Buy **limit** at the entry zone (at/just below market for a pullback entry).
- **Size:** the larger-bounded-by-both of: <= **40%** of live equity (per-order cap) AND a quantity
  keeping `(entry - stop) x qty <= 4%` of equity (per-trade-risk). Whichever binds first wins.
  Compute size off live balance (`saxo.js suggest-size 40`).
- **Every card carries:** thesis (with the catalyst + the data), entry, target (>= 2.5R), stop
  (a real support/invalidation level), size (SEK + %), invalidation, horizon. No card without all of these.
- Never propose a name in rejection history for a still-valid reason; if re-proposing after a time-bound
  reason cleared, acknowledge the prior rejection in the thesis.

## 4. Exit rules (auto-managed once Robert confirms the entry)
- **Target:** rest a **limit-sell** of the full position at `target_price` immediately on fill.
- **Stop:** monitored every routine cycle (~15 min) against the latest `ticker-data.js` price; if price
  <= `stop_price`, **auto-exit** (marketable limit-sell) and Discord-ping + log. Protects while Robert is away.
- **Time stop:** if a position is flat (neither target nor stop) after **~5 trading days**, Ticker posts
  a *rotation* suggestion (close + the next candidate) for Robert to confirm - capital shouldn't sit dead.
- On any exit, the freed slot re-enters the next daily scan.

## 5. Sizing & deployment
- All sizing is **% of live equity** (balance-relative), so the same plan runs at SIM scale (~11M SEK)
  and divides straight down to live (~25K). Goal is a **return % (1.5x in 30d)**, never an absolute SEK number.

## 6. Cadence
- **Daily (weekday):** scan + propose (aligned with the 08:00 Stockholm digest).
- **Every ~15 min:** exit monitor (stops, target fills, drawdown brake, expiry).
- **Weekly:** review - realized hit rate, avg R:R, equity vs the glide path (wk1 +10.7% ... wk4 +50%),
  what's working; re-tune; Robert reviews.

## 7. Override protocol (the ONLY deviation)
Robert injects industry knowledge in three ways; nothing else deviates from the rules:
1. **Reject an entry card with a reason** (the TTWO model) -> stored on the card + appended to the
   "Rejection feedback" section of [ticker_learnings.md](../agents/memory/ticker_learnings.md); Ticker
   reads it before every future proposal and won't re-pitch it.
2. **A proactive instruction** ("avoid X into earnings", "add Y to the watchlist", "I think Z runs") ->
   Ticker records it as a standing note in learnings and applies it.
3. **Halt** (`touch ticker/HALT`) -> all order placement stops.

## 8. Hard stops on the whole experiment
- Equity < baseline x 0.8 (-20%) -> auto-HALT (drawdown brake), stop, review.
- 30-day window end -> stop, full review of hit rate / R:R / the cash-only-at-scale result.

_Not financial advice. SIM-first; live hard-disabled until a deliberate, separate enable step._
