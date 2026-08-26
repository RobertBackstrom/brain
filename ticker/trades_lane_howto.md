# Trades Lane — How-To (tkr-001)

The dedicated Death Board "Trades" lane: where the Ticker agent posts a trade
idea and Robert clicks CONFIRM / REJECT to (SIM) execute via `assistant/saxo.js`.

**SIM only.** Live trading is hard-gated off in two places: `ticker/risk_limits.json`
(`environments.live.enabled=false`) and `ticker-trades.js` itself (refuses unless
`SAXO_ENV=sim`). saxo.js enforces every order guardrail.

## Where Robert sees it

- **URL:** https://hive.runatyr.games/trades
- Also reachable via the **TRADES** pill in the Hive top-right nav (green when
  there are trades awaiting confirm, with a count badge).

## How Ticker creates a trade-decision card

`POST` to the Death Board API (works from the VPS without auth — local-socket
bypass; through Cloudflare it's Robert-gated by CF Access):

```bash
curl -s -X POST http://localhost:3777/api/ticker/trades \
  -H 'Content-Type: application/json' \
  -d '{
    "ticker_symbol": "NVDA",
    "side": "Buy",
    "quantity": 18,
    "limitPrice": 190.50,
    "thesis": "Pullback to the 21 EMA after the earnings beat.",
    "entry_price": 190.5,
    "target_price": 215,
    "stop_price": 178,
    "recommended_size_sek": 3500,
    "recommended_pct": 35,
    "invalidation": "Close below 178 or negative analyst revisions.",
    "horizon": "position",
    "expires_at": "2026-06-17T20:00:00Z"
  }'
```

**Required:** `ticker_symbol`, `side` (Buy|Sell), `quantity`, `limitPrice`.
Everything else is optional context. The symbol MUST be on
`ticker/watchlist.json` or the watchlist guardrail blocks execution at confirm
time. `quantity` × `limitPrice` is the order notional — keep it under the
per-order cap (40% of account = 4000 SEK) and the daily cap (15000 SEK).

On creation: the card is written as a follow-up (`meta.type: trade-decision`,
project `tkr`, `trade_status: awaiting_confirm`) and a Discord ping fires
(TICKER_DISCORD_WEBHOOK, falling back to DISCORD_HEALTHZ_WEBHOOK).

## The confirm → execute → fill flow

1. **awaiting_confirm** — Ticker posted; Robert sees it on the Trades lane with a
   live countdown to `expires_at`.
2. **Robert clicks CONFIRM** → a modal lets him adjust final size in SEK (default
   = recommended). On submit, `POST /api/ticker/execute` runs `saxo.js
   place-order`. Status → **confirmed**, then **placed** with the Saxo OrderId.
   - The size override: `size_sek` is converted to shares at the limit price; or
     pass `quantity` directly.
   - If a guardrail blocks it (off-watchlist, oversized, kill-switch, etc.) the
     saxo.js error is shown verbatim and status stays at **confirmed** so Robert
     can adjust and retry. No order is placed.
   - Idempotent: re-confirming an already-placed card returns the existing order,
     never double-fires (saxo.js also dedups on a deterministic client order id).
3. **Robert clicks REJECT** → a small modal opens with a **"Reason (optional)"**
   textarea + Reject/Cancel. On submit, `POST /api/ticker/reject {id, reason}`.
   Status → **rejected**, logged, Discord ping (reason included), card moves to
   History (the reason shows on the rejected card). See "Rejection learning loop".
4. **Expiry** — the 15-min Routine sweeps: any `awaiting_confirm` card past
   `expires_at` → **expired** (no order).
5. **Fill** — the Routine polls `saxo.js order-status` for placed orders; when the
   order leaves the open-orders list it's marked **filled** (fill_price logged,
   Discord ping, card → done).

## Audit trail

Every lifecycle step appends to `ticker/trades_log.csv`
(`timestamp,action,symbol,side,quantity,limit_price,order_id,env`). saxo.js logs
the `placed`/`cancelled` rows; the lane logs `confirmed`/`rejected`/`expired`/`filled`.

## Backend pieces

- `assistant/ticker-trades.js` — all lane logic (create/execute/reject/sweep/poll/Discord).
- `assistant/server.js` — routes `GET|POST /api/ticker/trades`, `POST /api/ticker/execute`,
  `POST /api/ticker/reject`; expiry sweep + fill poll hooked into `runRoutine`.
- `assistant/saxo.js` — the broker wrapper (owns the live-gate + all guardrails).
- `cc-hive/src/app/trades/page.tsx` — the Trades view.
- `cc-hive/src/components/TradesPill.tsx` — the nav pill.
- `cc-hive/src/app/api/ticker/{trades,execute,reject}/route.ts` — Next proxies to the board.

## Rejection learning loop

When Robert rejects a card with a reason, the reason is captured in four places so
Ticker actually learns from it:

1. **Card frontmatter** — `reject_reason` + `reject_reason_at` (plus `trade_status: rejected`).
2. **Card Activity** — a "Rejected by Robert. Reason: …" line.
3. **`trades_log.csv`** — the `rejected` audit row (as before).
4. **Ticker agent learnings** — appended to a dedicated
   **"## Rejection feedback (Robert)"** section in
   [../agents/memory/ticker_learnings.md](../agents/memory/ticker_learnings.md),
   one append-only line per rejection (date · symbol · idea · reason). The agent
   reads this on every activation.

Both the card (source `followups`) and the learnings file (source `agents`) are
RAG-watched, so a `rag_search` for a symbol or "why rejected" surfaces Robert's
reasons after the next watcher tick (~30s debounce; no manual re-index needed —
`assistant/rag-indexer.js startWatcher`, booted by server.js). The card-generation
flow in [agents/ticker.md](../agents/ticker.md) requires Ticker to review this
section + rag_search prior rejections before pitching, so it won't re-pitch an idea
Robert already turned down for a stated reason.

A reason is optional — rejecting with an empty reason still works exactly as before
(no frontmatter field, no learnings line).

## Kill switch

`touch ticker/HALT` blocks ALL order placement (saxo.js guardrail). Remove the
file to re-enable.
