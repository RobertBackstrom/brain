# Ticker Execution Spec — Saxo OpenAPI (Phase 2)

**Status:** design / not built. Broker chosen 2026-06-16: **Saxo Bank OpenAPI**.
**Build owner:** DevOps agent. **Do not place a live order until every guardrail below is implemented and Robert has flipped the live switch.**

## Goal

Let Ticker propose a trade, post it to a dedicated Death Board lane, and — only after Robert confirms
go/no-go + final size in that lane — place the exact order via Saxo. Start on the **SIM account**.

## Why Saxo (vs alternatives, researched 2026-06-16)

| Broker | US + SE coverage | API | Verdict |
|---|---|---|---|
| **Saxo Bank OpenAPI** | Yes | REST + OAuth, free SIM account, 24h test token | **Chosen** — cleanest OAuth, fits VPS durable-token model |
| Interactive Brokers | Yes | Client Portal Web API + TWS | Strong fallback; auth via a local Java gateway needing periodic 2FA re-login (awkward headless) |
| Nordnet | SE-native | nExt API | **Closed to new API customers** |
| Avanza | SE-native | None official | Only ToS-violating reverse-engineered wrappers — ruled out |

## Architecture

```
Ticker (idea) ──▶ Death Board "Trades" lane (dedicated card, separate from daily catch-ups)
                      │  card shows: thesis, entry, target, stop, recommended size, invalidation
                      ▼
              Robert replies in-lane: go/no-go + final size (overrides recommendation)
                      │
                      ▼
         assistant/saxo.js place-order  ──▶ Saxo OpenAPI  POST /trade/v2/orders
                      │                         (SIM gateway first; live gateway after enable)
                      ▼
              Fill written back to the card + logged to ticker/trades_log.csv
```

### Components to build
1. **`assistant/saxo.js`** — OAuth (refresh-token, stored in VPS `.env`: `saxo.client-id`,
   `saxo.client-secret`, `saxo.refresh-token` in [secrets_registry.md](../secrets_registry.md)),
   plus `quote`, `place-order`, `order-status`, `positions`, `cancel`. SIM and live base URLs behind
   a `SAXO_ENV=sim|live` flag (defaults to `sim`).
2. **Death Board "Trades" lane** — a dedicated column / notification channel so execution decisions
   are visually and notification-wise separate from daily catch-ups. Card type `trade-decision` with
   structured fields and an explicit confirm action. (DevOps + UIbot.)
3. **Confirmation handler** — only a Robert-authored go reply in that lane triggers `saxo.js
   place-order`. No other path places an order.
4. **`ticker/trades_log.csv`** — every proposed/confirmed/filled/rejected order, append-only.

## Guardrails (hard, non-negotiable)

1. **No auto-execution, ever.** An order is placed only after Robert's explicit in-lane confirmation.
2. **SIM first.** `SAXO_ENV=sim` until Robert performs a logged, deliberate enable step to go live.
3. **Limit orders only.** No naked market orders.
4. **Caps:** per-order max (e.g. ≤ 40% of account), daily notional cap, max open positions. Configurable
   in `ticker/risk_limits.json`. An order exceeding a cap is blocked and re-surfaced, never silently clipped.
5. **Ticker allowlist = the watchlist.** No orders in names outside [watchlist.json](watchlist.json)
   without Robert adding them first.
6. **Kill switch.** A single flag (`ticker/HALT`) that blocks all order placement.
7. **Idempotency.** Each confirmation maps to exactly one order; re-confirms or retries must not
   double-fire (client order ID dedup).
8. **Full audit trail.** Proposed → confirmed → placed → filled/rejected, all logged with timestamps.

## Build sequence

1. Robert opens a Saxo account (or confirms an existing one) with OpenAPI access; create a SIM app.
2. DevOps builds `assistant/saxo.js` against SIM; prove quote + place + status + cancel end to end.
3. DevOps + UIbot build the dedicated Death Board "Trades" lane + confirm handler.
4. Wire Ticker idea → card → confirm → SIM order → fill-writeback. Run a week of SIM trades.
5. Review SIM results with Robert. Only then implement + test the live enable step.
6. Fund live with the ~10K SEK, keep caps tight, watch the first live cycle together.
