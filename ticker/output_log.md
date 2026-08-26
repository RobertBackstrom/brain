# Ticker — Output Log

## 2026-08-13 — Daily scan unblocked: Yahoo was blocking on User-Agent, not IP (Ticker)

Ended a 34-scan no-op streak (2026-06-19 to 2026-08-12) and posted the first entry card since June.

1. **Root cause: UA fingerprint, not IP, not a burst cap.** `ticker-data.js` sent a full Chrome UA; that exact string returns **429 in ~88ms**, bare `Mozilla/5.0` returns **200 with real JSON**, and no UA returns 429 `Edge: Too Many Requests`. Proven by an interleaved 4-way curl probe on a single URL (time-drift excluded), re-verified across PDX.ST/EA/NVDA/EVO.ST with the Chrome UA re-tested afterwards and still failing. Fix: one line, `const UA = 'Mozilla/5.0'`.
2. **Both prior diagnoses were wrong.** The seven-week "the 08:00 digest burns the per-IP burst cap" theory and its 2026-08-12 successor "the VPS IP is edge-blocked" both pointed outward. The 08-12 probe that produced the IP-block verdict sent *no UA*, itself a blocked fingerprint, so it reproduced the symptom and read as confirmation.
3. **Digest fixed by the same line.** Its 41 consecutive `spawnSync node ETIMEDOUT` fatals were a symptom: 27 symbols x 5 retries x exponential backoff (~25s/symbol). Full digest now completes in **3.0s** (1.8s on the trimmed 25-symbol list).
4. **EODHD purchase withdrawn.** `followups/tkr-010` had been updated on 08-12 to name the $19.99/mo All-World key as the *only* remaining fix. That was based on the wrong diagnosis; the paid key would have masked a free one-line bug. Still a reasonable durability upgrade, not a need.
5. **Watchlist rot removed.** **EA** deleted: the $55bn PIF/Silver Lake take-private closed 2026-08-04 at $210/share and Nasdaq suspended the shares 08-05, so the feed returns a frozen 209.70 at **3.93%** annualized vol, which ranks like a pristine low-vol uptrend. **MAXENT.ST** deleted (no data, delisted). This file is also the guardrail allowlist, so leaving a dead name in it is a live risk. 27 symbols to 25.
6. **Card posted: `tkr-014-evo-st-buy-entry`.** EVO.ST Buy limit 6079 @ 730, target 775, stop 713, R:R **2.65:1**, 4,437,670 SEK = 40.00% of equity, per-trade risk 103,343 SEK = 0.93% (cap 4%). Q2 printed 07-17 so no binary event in the horizon; Galaxy Gaming merger terminated 07-21 clearing an overhang; two-week consolidation on a three-touch shelf at 721.2/722.4/723.0. Awaiting Robert's confirm.
7. **Unreconciled position flagged.** `trades_log.csv` shows 35,500 PDX.ST filled @124.5 on 06-22 and a resting target @141, then no exit line ever. PDX traded through 141 on 08-03 and hit 147.6 on 08-05, so that target very likely filled at the broker for a ~+586k SEK win that nothing recorded. Card `tkr-009` was separately auto-closed by a `pending_close` housekeeping rule, which made the book look flat. Settles on the Saxo re-mint.
8. **Saxo SIM re-mint is now the only blocker.** `.saxo_tokens_sim.json` still 0 bytes, mtime unmoved since Jul 4 23:06 (40 days). It gates confirming `tkr-014` and reconciling the PDX lot.

## 2026-06-19 — Pinned Trades hex on the main Hive board (UIbot)

Made the Trades lane reachable from the Hive home (honeycomb) itself, not just the top-bar TRADES pill.

1. **New `cc-hive/src/components/TradesHex.tsx`** — a pinned hex mirroring `OpsHex.tsx` (same shape, viewBox, positioning outside the camera transform, same poll cadence). Sits top-left immediately right of the Ops hex (`left: 24 + 110 + 14`, `top: 96`), projects view only. Links to `/trades`.
2. **Count source reused** — same `/api/ticker/trades` fetch + `trade_status === 'awaiting_confirm'` filter as `TradesPill.tsx`; 15s poll. No new endpoint, no backend/server.js/trade-logic changes.
3. **Badge behavior** — neutral state: white-ish border, "Trades / ALL CLEAR". Awaiting state: green (`#2e9e5b`/`#3fae6b`) border + green drop-shadow glow + green "Trades" title + "N AWAITING" sub-label. Same hex visual language as Ops; green accent distinguishes it from Ops' amber ember (Ops = amber, Trades = green).
4. **Additive** — existing TRADES nav pill kept; existing hexes/Ops/pill unaffected.
5. **Verify** — `npm run build` clean (bare run), cc-hive restarted (`systemctl --user restart cc-hive`), `/` and `/trades` both 200. Screenshotted both states at 1440px (live "all clear" + stubbed-fetch "2 awaiting"); green active state and the matching lit-up top-bar pill both confirmed.

## 2026-06-18 — EODHD data integration: pure key-drop, fixes Yahoo rate-limit (DevOps, tkr-002)

Built the EODHD fetch path into `assistant/ticker-data.js` so the rate-limited free Yahoo feed (which intermittently 429s the VPS IP and starves the 15-min auto-stop monitor of prices) becomes a pure key-drop swap. SIM-first, additive, zero changes to any consumer.

1. **Provider selection.** `EODHD_API_KEY` in `assistant/.env` → EODHD; absent → Yahoo fallback (existing behavior, byte-for-byte). `--provider yahoo|eodhd` overrides per-run. Every output object now carries a `provider` field. A custom `.env` loader (mirrors saxo.js, no dotenv) pulls only `EODHD_API_KEY`.
2. **Endpoints.** `quote` → EODHD `/api/real-time/` (15-20min delayed — exactly what the intraday stop monitor needs); `history`/`vol` → `/api/eod/`. Quotes cached 60s in `assistant/.eodhd_quote_cache.json` (mirrors fx.js cache + fail-soft). Same command surface + JSON output shape, so `monitorExits()`, the digest, and the daily scan need ZERO changes. A missing/halted price returns `null` (stop monitor keeps its safe no-op, never a false trip).
3. **Symbol mapping.** Stockholm `.ST` is identical to Yahoo (EODHD also uses `.ST`); bare US symbols (NVDA, TTWO) get `.US` appended automatically. Verified against eodhd.com docs + demo endpoint — not assumed.
4. **Plan to buy: "EOD Historical Data — All World" ($19.99/mo)**, NOT the $99.99 All-In-One. The $19.99 tier already includes the HTTP `/api/real-time/` delayed quote + EOD for US + Stockholm. All-In-One is only for WebSocket realtime + fundamentals, which Ticker doesn't use. (Corrected the old "~$80/All-World" note.)

- **Hermetic test:** `assistant/test/ticker-data-eodhd.test.js` + fixtures in `assistant/test/fixtures/eodhd/` (real EODHD response shapes). **5/5 pass** — US real-time→quote shape, bare→`.US` mapping, `.ST` identity, EOD→series+vol math intact, halted symbol→`price: null`, and the no-key Yahoo `_parse` path unchanged. No network.
- **No-key fallback confirmed:** with `EODHD_API_KEY` unset, provider resolves to `yahoo` and the existing path is untouched. No restart needed (ticker-data.js is a CLI; server.js shells it fresh each cycle).
- **Status:** code ready; flips automatically when Robert subscribes + drops the key into `.env` (see secrets_registry `eodhd.api-key` + tkr-002 for the steps).

## 2026-06-18 — Automation engine: auto-managed exits + scheduled daily scan (DevOps)

Built the engine that makes Ticker FOLLOW its playbook automatically. SIM-first; live stays hard-disabled. Additive to server.js — existing flows + tkr-009 untouched.

1. **Auto-managed exits (Build 1, `ticker-trades.js`).** When an entry Buy card FILLS (detected in the 15-min fill poll), exits are armed from the card's `target_price` + `stop_price` with NO separate confirm (Robert approved the levels at entry):
   - **Target:** a resting **limit-sell** of the filled qty at `target_price` is placed immediately; its order id is recorded on the card (`target_order_id` / `target_saxo_order_id`) and a `target_placed` row hits trades_log.
   - **Stop:** monitored every Routine cycle against the latest **`ticker-data.js`** price (NOT Saxo - SIM has no market data). Price <= `stop_price` -> auto-exit: cancel the resting target first, then a marketable limit-sell (2% through the stop) flattens the position; card -> `stopped_out`, `stopped_out` log row, Discord ping.
   - **Target fill:** the resting target poll (order gone from open orders) -> card `target_hit`, `target_hit` log row, ping.
   - **Time stop:** a filled position flat after ~5 trading days posts a **rotation-suggestion** card (`type: rotation-suggestion`, needs_input) for Robert to confirm - never auto-closes on time.
   - Exit state on the card: `exit_status` (none|armed|stopped_out|target_hit|exit_failed), `target_order_id`, `target_saxo_order_id`, `stop_armed`, `exit_qty`, `stop_trigger_price`, `stop_exit_saxo_order_id`, `time_stop_suggested`.
2. **HALT now allows protective exits (`saxo.js`).** The kill-switch blocks new ENTRIES (Buys) but a closing **Sell** with `intent:'exit'` is exempt - a stop-loss must fire even during a halt. Exits also bypass watchlist + per-trade-risk + the sizing caps + balance-unavailable (they reduce risk), but KEEP the live-gate (SIM-only), order-type (Limit), invalid-order, and idempotency. A Buy can never claim the exit bypass (`intent:'exit' && side==='Sell'` both required).
3. **Scheduled daily scan-and-propose (Build 2, `server.js`).** Weekdays ~08:00 Stockholm (DST-correct via `Intl` Europe/Stockholm; 06:00 UTC), after the digest, `runRoutine` spawns the **Ticker agent** (reusing the same `spawn(CLAUDE_CLI ...)` mechanism as the weekly reflection / 4am sweep, `cwd` = project root) to run playbook 2-3: scan the watchlist, rank candidates, and POST entry cards (`awaiting_confirm`) toward the 2-3 position book - respecting max 4 (open + pending), rejection history, and balance-relative sizing. **DRAFTING ONLY** - cards await Robert's confirm (autonomous-queue rule). Skipped on weekends, under HALT, and when the agent cap is hit.

- **Self-test:** `assistant/saxo-selftest.js` extended with 8 exit-semantics cases (HALT blocks Buy / allows exit; exit bypasses watchlist / per-trade-risk / per-order cap / balance-basis; exit still enforces order-type; Buy can't claim the bypass). **27/27 pass**, hermetic.
- **Live SIM end-to-end (verified, then cleaned to zero residue):** created a PDX.ST entry card -> executed a marketable buy that filled -> pollFills armed a real resting target sell (target_placed) -> monitorExits with price > stop did NOT trip -> stubbed price <= stop -> auto-exit fired: resting target cancelled, marketable stop sell placed, card `stopped_out`, stopped_out log row. **15/15 checks.** Then flattened (0 positions), cancelled orders, deleted the test card, restored trades_log.csv. HALT semantics confirmed live: Buy blocked at `kill-switch`, exit Sell passed all local guardrails (Saxo only replied `NotOwned`, proving it cleared HALT). **tkr-009 untouched throughout.**
- **Test hook:** `TICKER_PRICE_STUB='{"PDX.ST":118}'` injects a deterministic price into `getLatestPrice` (mirrors `FX_CACHE_FILE`/`SAXO_ENV_FILE`); never set in production. Needed because Yahoo rate-limits the VPS IP.
- **No new cron/timer:** both builds ride the existing 15-min `runRoutine` cadence (exit monitor every cycle; daily scan gated to one weekday 08:00-Stockholm fire). Restarted `deathboard.service`; /api/health 200, /api/ticker/trades 200.

## 2026-06-17 — Guardrails made BALANCE-RELATIVE (risk_limits v3, tkr-009, DevOps)

The execution caps now size off **live account equity**, so the SIM trades at its full ~1M EUR (~11M SEK) scale and going live (~25K SEK) auto-divides every cap down by the same ratio with NO rewrite. SIM-first; live stays hard-disabled.

1. **Account-value basis = live equity (cached).** Replaced the static `account_value_sek: 25000` with live Saxo equity. `saxo.js resolveAccountValueSek()`: if `account_value_sek` is a number → manual override; if null/absent → live balance (`getBalance()` → `/port/v1/balances/me` TotalValue, FX→SEK), cached in `assistant/.ticker_balance_<env>.json` (15-min TTL) so the order hot path doesn't refetch each order. **Fail-closed:** no basis (balance unreachable + no override) → order blocked (`guardrail: balance-unavailable`), same posture as `fx-rate-unavailable`. For the full-scale SIM test `account_value_sek` is null.
2. **Caps as % of that balance (v3).** `per_order.max_pct_of_account` 40 and `per_trade_risk.max_pct_of_account` 4 now compute off live equity. `daily_limits` migrated to a ratio `max_notional_pct_of_account: 160` (= the old 40K/25K). `position_limits.max_open_positions` stays an absolute count (4).
3. **Drawdown brake → % from a baseline.** `drawdown_brake.floor_sek` → `floor_pct: 20`. Baseline equity per env recorded in `assistant/.ticker_baseline_<env>.json` (auto-captured on first run; (re)set via `saxo.js set-baseline [sek]`). `checkDrawdownBrake()` trips when current equity < baseline × (1 − floor_pct/100). Fires identically in SIM (off ~11M baseline) and live (off ~25K). Verified live: equity 11,049,919 / baseline 11,049,919 / floor 8,839,935 → `halted: false`.
4. **Courtage caveat.** New `commission_note` block documents that SIM-at-scale understates Saxo's per-trade minimum-fee drag a small live account feels (live net % will trail SIM net %). No fee modelling in code.
5. **Sizing helper.** New `saxo.js suggest-size <pct> [price]` → SEK = pct% of live equity (+ share count at a price). How new full-scale SIM cards get sized. ticker.md updated with a one-line note.

- **Self-test:** [assistant/saxo-selftest.js](../assistant/saxo-selftest.js) rewritten to inject a mock 11,000,000 SEK balance — 19/19 pass: per-order blocks at 41% / passes at 39%, per-trade-risk scales, daily-cap ratio = 160% = 17.6M, balance-unavailable blocks, drawdown floor = baseline × 0.8 = 8.8M (fires −21%, holds −19%). Hermetic (no creds/network).
- **Live SIM verified:** `saxo.js balance` = 999,992 EUR (11,049,919 SEK); `suggest-size 40` = 4,419,967 SEK. At-scale place→cancel: PDX.ST Buy 36,833 @ 120 = ~4.42M SEK (40% of balance) **accepted** at scale (proves the % caps allow full SIM scale), then cancelled; 0 open orders left, test log rows scrubbed, pre-existing positions/cards untouched.
- **What changes going live:** nothing in code/config except flipping `environments.live.enabled: true` + `SAXO_ENV=live`. The same percentages apply to the smaller live balance, so every cap auto-divides down. Set a fresh live baseline (`SAXO_ENV=live saxo.js set-baseline`) so the brake anchors to live equity.

## 2026-06-17 — SIM-sprint guardrails wired into code (tkr-005, DevOps)

The four 25K-SIM-sprint guardrails that were POLICY ONLY in risk_limits.json v2 are now enforced in code (SIM-first; same code serves live later). Live stays hard-disabled.

1. **Per-trade-risk cap** — saxo.js `enforceGuardrails` now enforces `(entry - stop) x qty <= 4% of account` (1,000 SEK), FX-converted to SEK. `entry_price`/`stop_price` thread from the card through `/api/ticker/execute` → `ticker-trades.executeTrade` → `saxo.js place-order`. Skipped (not blocked) when either is absent. Verified live: PDX.ST entry 130/stop 110 x100 = 2,000 SEK risk → blocked.
2. **Drawdown brake** — new `checkDrawdownBrake()` in ticker-trades.js, hooked into the 15-min Routine after fill-poll. Fetches Saxo equity (new `saxo.js balance` → `/port/v1/balances/me` TotalValue, FX-converted to SEK); if equity < `drawdown_brake.floor_sek` (20,000), creates `ticker/HALT` (idempotent) + Discord ping + `drawdown_halt` log row. Never auto-clears HALT. Verified live (forced high floor → HALT created + idempotent re-run; restored).
3. **FX-correct sizing** — new [assistant/fx.js](../assistant/fx.js): Yahoo daily FX (`<CCY>SEK=X`, USD via `SEK=X`) via curl (Node fetch is Yahoo-blocked), cached in `assistant/.fx_cache.json` (daily TTL, fail-closed on the money path). saxo.js per-order cap, daily cap, per-trade-risk, and the brake all convert non-SEK notional to SEK first. Currency derived network-free from the symbol (.ST=SEK, else USD), overridable via `order.currency`. **Headline fix verified live:** TTWO Buy 10 @ $150 = $1,500 = 14,254 SEK is now BLOCKED by the 10,000 SEK per-order cap (it passed before the FX fix); no order placed.
4. **Cancel-a-placed-order** — new `cancelTrade()` + `POST /api/ticker/cancel` + Next proxy + **CANCEL ORDER** button on `placed` cards in cc-hive /trades. Calls `saxo.js cancel <saxoOrderId>`, flips card to `cancelled`, log row, Discord ping. Idempotent. Verified live: created → executed (placed SIM order 5038887014) → cancelled via the lane → SIM account left clean (0 open orders/positions), test card removed.

- **Self-test:** new checked-in [assistant/saxo-selftest.js](../assistant/saxo-selftest.js) — hermetic (no creds/network, seeded FX fixture), 12 cases incl. the new per-trade-risk + FX-sizing cases. All pass.
- **Verified:** `node -c` clean on fx.js/saxo.js/ticker-trades.js/server.js; self-test 12/12; cc-hive `npm run build` clean; deathboard + cc-hive restarted, `/api/health` 200, `/trades` 200, board intact (769 followups), the 2 awaiting cards (tkr-006/007) + tkr-003 untouched.

## 2026-06-17 — Death Board "Trades" lane built (tkr-001, DevOps + UIbot)

The confirmation channel is live. Ticker posts a trade idea, Robert clicks CONFIRM/REJECT to (SIM) execute via saxo.js.

- **Backend** ([assistant/ticker-trades.js](../assistant/ticker-trades.js) + 4 routes in [assistant/server.js](../assistant/server.js)):
  `trade-decision` card type (rides the followup store; project tkr; lifecycle awaiting_confirm → confirmed → placed → filled | cancelled | rejected | expired).
  `GET|POST /api/ticker/trades`, `POST /api/ticker/execute`, `POST /api/ticker/reject` — all behind the existing CF Access gate (Robert-only).
  Execute refuses unless `SAXO_ENV=sim` (defense in depth), calls `saxo.js place-order`, surfaces guardrail/Saxo errors verbatim, idempotent, logs to `trades_log.csv`.
  Expiry sweep + fill polling hooked into the 15-min Routine. Discord pings (TICKER_DISCORD_WEBHOOK → DISCORD_HEALTHZ_WEBHOOK) on new card / fill / reject.
- **UI** (cc-hive): dedicated [/trades](https://hive.runatyr.games/trades) page (big symbol, thesis, entry/target/stop, recommended SEK+%, horizon badge, live countdown, prominent CONFIRM/REJECT, confirm-modal size override, result states) + `TradesPill` in the Hive nav + 3 Next API proxies.
- **Verified on SIM:** create → execute placed real SIM order 5038886962 → cancelled (clean trades_log audit rows). Off-watchlist (AMD) and oversized (NVDA 10000 SEK > 4000 cap) both blocked with the saxo.js guardrail returned verbatim, no order. cc-hive build clean; Trades view + modal screenshot-verified. deathboard + cc-hive restarted, both healthy, existing board/kanban/Hive intact.
- **Howto:** [trades_lane_howto.md](trades_lane_howto.md).
- **Next (Robert):** run a week of SIM trades → review → then the separate live-enable step.

## 2026-06-16 — Agent scaffolded (Phase 1)

- Created the **Ticker agent**: [agents/ticker.md](../agents/ticker.md),
  [agents/memory/ticker_learnings.md](../agents/memory/ticker_learnings.md), registry row, and the
  `/ticker` command.
- Built the free-tier data layer [assistant/ticker-data.js](../assistant/ticker-data.js): `quote`,
  `history`, `vol`, `digest` over Yahoo Finance (no key). Covers US + Stockholm (`.ST`). Verified on
  real data — Paradox ~30% annualized vol, Evolution ~30%, computed correctly.
- Captured the data-source quirks (Yahoo fingerprint-blocks Node fetch → use curl; low per-IP burst
  cap → backoff + EODHD upgrade path) to the agent learnings.
- Defined coverage in [watchlist.json](watchlist.json) and the Phase 2 Saxo execution design +
  guardrails in [execution_spec_saxo.md](execution_spec_saxo.md).

**Decisions locked:** active trade ideas (personal account, ~10K SEK) · SE+US gaming & tech · swing /
position / long-term (no intraday) · free data first → EODHD later · Saxo for execution · execution
questions on a dedicated Death Board lane, Robert confirms go/no-go + size.

**Open / next:** (1) enable the scheduled digest cron once a delivery lane exists; (2) DevOps to build
the Saxo SIM integration + dedicated Death Board "Trades" lane per the execution spec; (3) decide
digest cadence + landing spot.

## 2026-06-16 (later) — Digest delivery wired + Saxo build handed off

- **Delivery decided:** Discord + mail. Built [assistant/ticker-digest.js](../assistant/ticker-digest.js)
  (runs `ticker-data.js digest`, saves to `digests/`, emails full via gmail-api `sendRawMessage`, posts
  chunked to Discord webhook). Falls back to `DISCORD_HEALTHZ_WEBHOOK` until a dedicated one exists.
- **Cron installed:** weekdays 06:00 UTC (08:00 Stockholm) → Discord + mail. Second US-premarket run
  staged (commented) for the EODHD phase. Goes live next weekday morning.
- **Saxo build green-lit** and handed to DevOps as [tkr-001](../assistant/followups/tkr-001-saxo-sim-execution-build.md)
  (blocked on Robert opening a Saxo account + SIM app). Epic [tkr-000](../assistant/followups/tkr-000-epic.md);
  config upgrades in [tkr-002](../assistant/followups/tkr-002-discord-webhook-eodhd-upgrade.md).
- **Secrets registered (planned):** `ticker.discord-webhook`, `eodhd.api-key`, `saxo.openapi`.

## 2026-06-17 — Saxo execution infrastructure built (Phase 2, SIM-first)

Built the full code + config layer for confirmation-gated trade execution via Saxo OpenAPI. **All guardrails implemented**. Still blocked on Robert creating the SIM developer app to get credentials (~5 min, no approval wait needed).

**Files created:**
- `assistant/saxo.js` — OAuth wrapper + commands (quote, place-order, order-status, positions, cancel). Env toggle for SIM/live. Full guardrail enforcement: limit-orders-only, per-order/daily caps, watchlist allowlist, kill switch, idempotent order IDs.
- `ticker/risk_limits.json` — caps config (per-order max 40%, daily notional 15k SEK, max 5 open positions, limit-orders-only). Live trading **gated** (`environments.live.enabled: false`) until Robert confirms after a week of SIM trades.
- `ticker/trades_log.csv` — append-only audit trail (timestamp, action, symbol, side, quantity, limit_price, order_id, env).
- `ticker/death_board_trades_lane_spec.md` — full spec for the dedicated "Trades" lane (card type `trade-decision`, UI presentation, confirmation flow, expiry handling, fill notification, access control). Handoff to DevOps + UIbot for Death Board integration.

**Files updated:**
- `secrets_registry.md` — `saxo.openapi` entry updated with build status, credential requirements, and current blocker.

**Next steps** (after Robert drops SIM credentials in .env):
1. Prove SIM flow end-to-end: quote → place-order → order-status → cancel
2. DevOps + UIbot build the Death Board "Trades" lane per spec
3. Wire Ticker idea → card → confirm → SIM order → fill-writeback
4. Run a week of SIM trades with Robert reviewing each
5. Review SIM results → only then flip live enable flag (explicit step)

Research: Saxo OpenAPI [developer docs](https://www.developer.saxo/openapi/referencedocs) + [order placement guide](https://developer.saxobank.com/openapi/learn/order-placement). All endpoints mapped.

See: [tkr-001](../assistant/followups/tkr-001-saxo-sim-execution-build.md).

## 2026-06-17 — Saxo saxo.js hardened + completed (DevOps pass, still SIM-only)

DevOps took over the overnight-autogenerated `assistant/saxo.js` (which had never run — it crashed on `require('dotenv')`) and made it correct, complete, and guardrail-enforcing. Verified everything testable without creds.

**Fixed / built:**
1. `.env` loading — removed `dotenv`, switched to the project custom loader reading `assistant/.env` (was wrongly pointed at `../.env`).
2. OAuth host topology corrected (token endpoint is NOT under the gateway): SIM token `https://sim.logonvalidation.net/token`, gateway `https://gateway.saxobank.com/sim/openapi`. Verified against developer.saxo.
3. First-token mint added: `auth-url` + `exchange <code|url>` (authorization-code grant), plus `SAXO_TOKEN` 24h fast-path for smoke tests.
4. All guardrails implemented and enforced BEFORE any network: HALT, Limit-only, live-gate, watchlist allowlist, per-order cap, daily notional cap, max-open-positions, idempotent client order id (`ExternalReference`).
5. Real implementations for instrument search, quote (infoprices), accounts/clients-me, positions; place-order auto-resolves AccountKey + Uic.
6. SIM-only `smoke` command (refuses live; `--order` does a tiny far-from-market place→status→cancel).

**Verified (no creds):** `node -c saxo.js` passes; all 5 guardrail reject paths (HALT, Market, off-watchlist, oversized notional, live-while-disabled) throw locally with zero network. `status` reports missing creds cleanly. No side effects (HALT/trades_log untouched, no stray token files).

**Docs:** `assistant/SAXO_SETUP.md` — exact developer.saxo steps + first-token mint + 24h fast path.

**Remaining (Robert, ~5 min):** create SIM app → drop `SAXO_CLIENT_ID`/`SAXO_CLIENT_SECRET` in `assistant/.env` → `node saxo.js auth-url` + `exchange`. Then `node saxo.js smoke`.

See: [tkr-001](../assistant/followups/tkr-001-saxo-sim-execution-build.md), [SAXO_SETUP.md](../assistant/SAXO_SETUP.md).

## 2026-06-17 — Saxo SIM execution PROVEN end-to-end (live SIM account)

Robert created the SIM app ("Runatyr Trader", AppKey `ddbc...`, Code grant, trading enabled) and
authorized. Creds in `assistant/.env`; durable refresh token minted + saved (`.saxo_tokens_sim.json`, 0600).

**Verified live on SIM:**
- `smoke` (read-only): auth ok, account resolved (Robert Bäckström), instrument search (AAPL→uic 211),
  positions 0. `ready: true`.
- Full loop: placed NVDA Buy 1 @ 193.91 (OrderId 5038886733) → order-status confirmed → cancelled →
  positions back to 0. Both rows in `trades_log.csv`. Idempotency ref `TKR-20260617-333FCAC532`.
- Guardrails confirmed firing on real calls (the $1 fallback order was correctly rejected by Saxo's
  own TooFarFromMarket check after passing all our guardrails).

**Operational note:** the free SIM app has NO market-data license — Saxo quotes return
`PriceTypeAsk/Bid: NoAccess`. By design we price limit orders off the free Yahoo feed (Saxo is execution
only). Orders must be near-market or Saxo rejects them (TooFarFromMarket).

**Next:** Death Board "Trades" lane (DevOps + UIbot) → wire idea→card→confirm→SIM order→fill-writeback →
run a week of SIM trades → review → only then the live enable step.

## 2026-06-17 — 25K SIM sprint strategy planned

Robert set a SIM sprint goal: **25,000 SEK → 37,500 (+50%) in 30 days**, profile = aggressive-but-
survivable, **cash equities only**, active rotation.

- Wrote `ticker/sim_strategy_2026-06.md`: honest expectation (cash-only base case ~+5-15%/mo, +50% is a
  stretch needing a ~50% hit rate at 2.5:1 R:R), the expectancy math, the core+satellite engine, entry/
  exit/rotation rules, weekly glide-path checkpoints, kill conditions.
- Re-based `risk_limits.json` to v2 for 25K: per-trade risk 4% (~1,000 SEK), per-order 40% (10,000),
  max 4 positions, daily 40,000, **drawdown brake at 20,000 (-20%)**, limit-only, SEK-preferred.
- Logged 3 enforcement dependencies as [tkr-005](../assistant/followups/tkr-005-sim-sprint-guardrail-enforcement.md)
  (drawdown brake, per-trade-risk, FX-correct sizing) - currently policy-only.

Note: the live PDX.ST card (tkr-003) was sized to the old 10K profile (3,542 SEK = 14% of 25K) - undersized
for the sprint; to re-issue at sprint size if Robert wants.

## 2026-06-18 — Trades lane: rejection-reason capture + learning loop (DevOps + UIbot)

Added a why-did-you-reject capture to the Trades lane so Ticker learns from Robert's no's.

- **UI** (`cc-hive/src/app/trades/page.tsx`): REJECT now opens a small modal with a
  "Reason (optional)" textarea + Reject/Cancel (replacing the bare confirm()). The reason
  posts to `/api/ticker/reject {id, reason}`. Rejected cards in History show the reason.
- **Backend** (`assistant/ticker-trades.js` `rejectTrade`): stores `reject_reason` +
  `reject_reason_at` on the card frontmatter, writes it to the card Activity + the `rejected`
  log row + the Discord ping (all as before), and appends a one-line entry to a new
  "## Rejection feedback (Robert)" section in `agents/memory/ticker_learnings.md`. Empty
  reason = old behaviour, no new fields. server.js route + Next proxy already passed `reason`.
- **Learning surface**: the agent reads "## Rejection feedback (Robert)" on every activation;
  `agents/ticker.md` now requires reviewing it + rag_search'ing prior rejections BEFORE pitching.
- **RAG**: card (followups) + learnings (agents) are both watcher-indexed (server.js
  startWatcher, ~30s debounce) — no manual re-index. Verified end-to-end: `rag_search` returned
  the rejected card (0.89) and the learnings line (0.88) with Robert's exact reason.
- Tested with a throwaway EVO.ST card (created → rejected with reason → all 4 surfaces verified →
  RAG-searchable → deleted, learnings + log reverted, zero residue). Live tkr-006/007/003 untouched.
  Restarted cc-hive + deathboard; /api/health 200, /trades 200.

## 2026-06-19 — Live "NOW" share price on Trades cards (UIbot, tkr-009 context)
Additive, SIM-only display feature. Shows where each stock trades vs entry/target/stop/limit.
- **Backend** (`assistant/ticker-trades.js`): new `quoteSymbol(sym)` helper (ticker-data.js
  `quote` CLI subprocess → `{price, currency, asOf, provider}` or null) with a 60s in-memory
  cache (`_quoteCache` Map) mirroring the EODHD quote-cache TTL; nulls are cached too so a
  throttled feed isn't re-hit every list load. New `listTradesWithPrices()` fetches one quote
  per UNIQUE symbol on ACTIVE cards only (awaiting_confirm + placed) — never the watchlist —
  and attaches `current_price`/`currency`/`price_asof`/`price_provider` to each card meta.
  Null-safe end to end. Reuses the `TICKER_PRICE_STUB` test hook. Both new fns exported.
- **server.js**: GET /api/ticker/trades now `await tickerTrades.listTradesWithPrices()`, with a
  try/catch fallback to bare `listTrades()` so the price path can never error the list. No change
  to trade/order/exit logic or risk_limits.
- **UI** (`cc-hive/src/app/trades/page.tsx`): new `NowCol` as the 5th stat (ENTRY/TARGET/STOP/
  LIMIT/NOW), active cards only. Price + currency in the card's display font; color by position —
  green at/through target, red at/through-or-near stop, amber approaching (within 15%), neutral
  between — plus a "% to target/stop" hint on the nearer level. Null price → "—" + "awaiting feed".
  Refreshes via the page's existing 15s poll.
- **Verify**: `npm run build` BARE → clean (/trades 4.48 kB, "Compiled successfully"). Restarted
  cc-hive + deathboard (user units). /trades 200, board intact. PDX.ST (tkr-009, placed) renders
  ENTRY 124.5 / TARGET 141 / STOP 119.5 / LIMIT 124.5 / NOW "—" "awaiting feed" — Yahoo is 429-ing
  the VPS (expected until EODHD key lands, tkr-002); null-handling covers it. Priced path verified
  via stub (PDX.ST 125.5 → current_price attached; 4.8% to stop, near → red). tkr-009 data untouched.
