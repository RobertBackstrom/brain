# Ticker — Project Instructions

Personal market-trends agent + small managed trading account. Owned by the **Ticker agent**
([agents/ticker.md](../agents/ticker.md)). Not billable. Not a client engagement.

## What this is

A small, personal risk-capital account (~10K SEK to start) that Robert has delegated to the Ticker
agent. Robert sets goals; Ticker researches, forms trade ideas, sizes them, and posts execution
decisions for Robert to confirm. **Every order is gated on Robert's explicit confirmation.** This is
his own money and his own account — not third-party financial advice.

## Coverage

SE gaming · SE tech (broad) · US gaming · US big tech/space. Symbols in
[watchlist.json](watchlist.json). Horizon: swing / position / long-term. **No intraday.**

## Data source

`node assistant/ticker-data.js` — two providers, identical command surface + JSON output shape.

| Command | Use |
|---|---|
| `quote <sym> [...]` | last price, prev close, day move, 52w hi/lo |
| `history <sym> --range 3mo` | daily OHLC series |
| `vol <sym> --range 1mo` | annualized historical volatility + range + position-in-range |
| `digest [--watchlist <file>] [--json]` | formatted markdown digest of the whole watchlist |
| `--provider <yahoo\|eodhd>` | force a provider (default: auto by `EODHD_API_KEY`) |
| `_parse <file>` | offline: parse a saved Yahoo chart JSON (debug) |
| `_parse-eodhd <sym> --rt <f> [--eod <f>]` | offline: parse saved EODHD fixtures (hermetic test) |

Every output object carries a `provider` field for visibility.

**Provider selection:** `EODHD_API_KEY` set in `assistant/.env` → **EODHD** (keyed, no rate limit);
absent → **Yahoo** (free) fallback. `--provider` overrides per-run.

Stockholm symbols use the `.ST` suffix (EMBRAC-B.ST, PDX.ST, EVO.ST) — **identical** on both
providers. US names are bare on Yahoo (NVDA, TTWO); the EODHD path appends `.US` automatically.

### EODHD (paid, recommended — fixes the rate-limit gap)
- **Plan:** "EOD Historical Data — All World" ($19.99/mo). Includes the `/api/real-time/` delayed
  quote (15-20min — exactly what the 15-min auto-stop monitor needs) + EOD for US + Stockholm.
  All-In-One ($99.99) is only needed for WebSocket realtime + fundamentals; Ticker doesn't use those.
- `quote` → EODHD `/api/real-time/` (delayed); `history`/`vol` → `/api/eod/`. Quotes cached 60s
  (`assistant/.eodhd_quote_cache.json`).
- **Key drop:** subscribe → `EODHD_API_KEY=<token>` in `assistant/.env` + LastPass
  ([secrets_registry.md](../secrets_registry.md) `eodhd.api-key`). No code change, no restart.
  `monitorExits()`, the digest, and the daily scan all keep working unchanged — provider flips
  automatically. A missing price still returns `null` (stop monitor keeps its safe no-op).

### Known limitation (Yahoo free tier — why EODHD exists)
- Yahoo **fingerprint-blocks Node's `fetch`** → the script fetches via **curl**.
- Yahoo enforces a **low per-IP burst cap**; the full ~27-symbol digest can partially `429`, and the
  15-min auto-stop monitor can be starved of prices. The fetcher mitigates (curl, concurrency 2,
  exponential backoff, host rotation, one call/symbol) but the real fix is the EODHD key.

## Execution (Phase 2 — Saxo, pending build)

Broker chosen: **Saxo Bank OpenAPI**. Build + prove on the **SIM account first**; live only after an
explicit enable step. Architecture, guardrails, and the dedicated Death Board lane are specified in
[execution_spec_saxo.md](execution_spec_saxo.md). This is DevOps build work (Saxo OAuth service +
order endpoint + Death Board lane).

## Rules

- Verify live before any market claim. Never assert listing/price from memory (the SPCX lesson).
- Every trade idea: thesis + entry + target + stop + size + invalidation + horizon.
- Never execute without Robert's in-channel confirm. Limit orders only. Caps + kill switch.
- Numbered lists, no hype, no em-dashes, "not financial advice" footer.
- Log significant changes to [output_log.md](output_log.md).
