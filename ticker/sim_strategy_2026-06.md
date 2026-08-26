# Ticker SIM Sprint Strategy - June 2026

**Account:** Saxo SIM (22396987) | **Scale:** full SIM balance (~1,000,000 EUR / ~11M SEK) | **Window:** 30 days (~21 trading days)
**Goal:** +50% return (1.5x) | **Profile:** aggressive-but-survivable, cash equities only, active rotation

> **Sizing is percentage-based and balance-relative (risk_limits.json v3).** The SIM runs at its full
> ~1M EUR balance so the model is tested at scale. Every cap is a % of *live account equity*, so when we
> go live with real money (~25K SEK) the identical strategy **divides down automatically** - same
> percentages, smaller numbers, no rewrite. The **goal is a return % (1.5x), not an absolute SEK amount.**

## 1. Honest expectation

Cash-only with no leverage means returns come solely from being concentrated and right, repeatedly.
+50% in a month is a **stretch north-star, not a forecast**. Disciplined base case: roughly +5% to
+15% in a strong month; a real chance of a flat-to-down month; +50% requires a hot streak of
concentrated winners. The drawdown brake guarantees a bad run can't zero the account. This is a
learning sprint on SIM - the point is to find the real edge (and failure modes) at zero cost.

## 2. Capital & guardrails (see risk_limits.json v3 - all % of live equity)

All caps compute off **live account equity** (cached), so they hold at SIM scale (~11M SEK) and at live
scale (~25K SEK) without a rewrite. SEK amounts below are the live-equivalent at ~25K.

- **Per-trade risk:** (entry - stop) x qty <= **4%** of equity (~1,000 SEK live). The core lever.
- **Per-position cap:** **40%** of equity (~10,000 SEK live). Concentrated, no single name dominates.
- **Max open positions:** **4** (absolute count). Cash-only -> ~2-3 near cap = ~80-100% deployed.
- **Drawdown brake:** halt (HALT file) if equity falls **-20% from the sprint baseline**. Now fires in
  SIM too (off the ~11M baseline), so the SIM genuinely rehearses the live safety behaviour.
- **Daily turnover cap:** **160%** of equity (rotation headroom).
- **Limit orders only**, watchlist-only, idempotent, SIM-gated. Live hard-disabled.

### Courtage caveat (SIM-at-scale vs live)
At ~11M SEK, Saxo commissions are ~0.1% of a trade - negligible. At ~25K live, Saxo's *per-trade
minimum* fee dominates: a ~10K SEK position can cost ~0.3-0.7% per side, and with active rotation
(many trades) that compounds into a **few % a month of drag**. So **SIM net % will read rosier than
live net %.** When sizing down to live, subtract an estimated commission drag from the SIM result -
the strategy's gross % transfers, the net does not, one-for-one.

## 3. The expectancy math (why the levers are what they are)

Per-trade edge = (WinRate x AvgWin) - (LossRate x AvgLoss). Risking 4% at **2.5:1 R:R**:
- At 50% win rate: 0.5(10%) - 0.5(4%) = **+3%/trade** -> ~20 trades ≈ +80% (hits goal).
- At 40% win rate: 0.4(10%) - 0.6(4%) = **+1.6%/trade** -> ~20 trades ≈ +38%.
- At 33% win rate: 0.33(10%) - 0.67(4%) = **+0.6%/trade** -> ~20 trades ≈ +13%.

The target is reachable **only** with a sustained ~50% hit rate at 2.5:1 - which is hard. The binding
constraint is the **edge (hit rate x R:R)**, not the risk size. So the whole game is: asymmetric targets,
cut losers at the stop without exception, and let winners run.

## 4. The engine

**Universe (cash equities, watchlist only):**
- **Satellite (momentum/beta):** high-vol movers and catalyst plays - RKLB, SPCX, TSLA, NVDA, TTWO
  (GTA VI), RBLX. These provide the move size needed for big winners.
- **Core (cleaner trends):** Swedish names size cleanly in SEK - EVO, PDX, SF, EG7, HEXA, SINCH.
- **Currency caveat:** USD names are under-protected by the SEK caps until FX sizing is added (see #6).
  Until then, lean SEK for clean sizing; USD only when Ticker sizes in SEK terms and Robert confirms.

**Entry:** momentum continuation or pullback-to-support on a named catalyst/trend; every entry has a
defined stop and a target at >= 2.5x the risk. No setup without entry/target/stop/invalidation.

**Exits:**
- **Stop:** hard, at the predefined level - no widening, ever.
- **Target:** scale or exit at the 2.5R level; trail the remainder if momentum persists.
- **Time stop:** if a position hasn't worked in ~5 trading days, recycle the capital (active rotation).

## 5. Process

- **Daily:** Ticker reviews the watchlist (digest + intraday checks), posts trade-decision cards to the
  Trades lane with full thesis/entry/target/stop/size. Robert confirms/rejects. Cut losers same-day at stop.
- **Weekly:** review hit rate, R:R realized, what's working, equity vs the +50% glide path
  (~+10.7%/week compounded if on pace). Re-tune.
- **Glide path checkpoints:** wk1 ~27.7K, wk2 ~30.7K, wk3 ~34.0K, wk4 ~37.5K. Falling behind early is
  expected and not a reason to over-risk - the drawdown brake and per-trade risk stay fixed.

## 6. Open dependencies (DevOps, to make this fully sound)

1. **Drawdown-brake enforcement:** wire an equity check into the fill-poll routine that auto-creates
   HALT below 20,000 SEK. Today it's policy-only (manual monitoring).
2. **Per-trade-risk enforcement:** add the (entry-stop)x qty <= 4% check to saxo.js. Today Ticker sizes
   to it manually.
3. **FX-correct sizing:** convert USD notional to SEK before the cap checks, so USD names are bounded
   correctly. Until then, SEK-preferred.

## 7. Kill conditions

- Equity < 20,000 SEK -> HALT, stop, review.
- Any guardrail or data anomaly (e.g. corporate-action price gaps like Embracer) -> skip the name.
- End of 30 days -> stop, full review of hit rate / R:R / what the cash-only ceiling actually was.

_Not financial advice. SIM only. Robert's own risk capital plan for a learning experiment._
