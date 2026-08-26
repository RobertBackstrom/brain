---
project: tkr
status: open
priority: high
updated: 2026-08-18
created: 2026-08-18
type: decision
owner: Robert
---

## EVO.ST: mandatory cash offer is live. Do not confirm `tkr-015` (expires 18:00Z 2026-08-18).

The 2026-08-18 daily scan found that trade card `tkr-015-evo-st-buy-entry`, posted 2026-08-17,
rests on a thesis that was already false when it was written. **Recommendation: reject it.**

### What the card says

`tkr-015`: Buy 6,013 EVO.ST @ 738 limit, target 786, stop 719, 40% of equity (~4.44m SEK).
Thesis line: *"Q2 printed 2026-07-17 so the binary event is behind us ... **no scheduled event
risk in the window**"*, supported by Evolution's 3-7 August buyback as "an active structural bid".

### What is actually happening

1. **Candle Lake Limited** (Cayman vehicle wholly owned by **Kenneth Dart**) announced a
   **mandatory public cash offer for all shares in Evolution at SEK 695/share on 13 August 2026**,
   valuing the company at ~**SEK 131.7bn**.
2. Trigger: Candle Lake crossed the 30% budplikt threshold on **24 July** and now holds **31.56%**.
3. **Acceptance period opened 17 August and runs to 15 September**, payment ~23 September. That is
   squarely inside a swing horizon.
4. Candle Lake states it does **not** intend to take control, and has signalled it would **delist**
   Evolution from Nasdaq Stockholm if the offer is accepted.
5. The offer is a **discount** to market: 5.7% below the 12 Aug close, equal to the 24 July close,
   and only 1.6% above the 20-day VWAP.

### Why the card is dead regardless of view

- EVO closed **787.6 on 2026-08-17, +4.65%** - roughly **13% above the 695 cash offer**. The market
  is pricing the bid as inadequate.
- Price **never traded down to the 738 entry** and has **already passed the 786 target**. The
  breakout-retest geometry no longer exists.
- Confirming it parks a bid **6.3% below market**. It rests unfilled unless EVO falls 6.3%, and the
  realistic path there is the takeover resolving badly. **Its only fill scenario is the adverse one.**
- It would fail closed at placement anyway while the Saxo SIM token is dead (see `tkr-010`).

### Decisions needed

1. **`tkr-015`** - reject with the tender offer as the stated reason (preferred, so the
   rejection-history gate blocks a re-pitch on the same broken thesis), or let it lapse at 18:00Z.
2. **EVO policy to ~15 September** - recommended: skip under playbook §1 (live corporate action)
   and §2.3 (binary event in-horizon). Accept the consequence in point 3.
3. **Consequence for the sprint** - per the 2026-08-13 liquidity screen, EVO was the *only*
   watchlist name genuinely tradeable at SIM scale (~370m SEK/day turnover; a 40% order is ~1.2%
   of ADV). Removing it for a month leaves very few valid candidates. Options: run the sprint thin,
   widen the watchlist to more liquid SE/US large caps, or treat the SIM sprint as paused.

### Related

- `tkr-010` - Saxo SIM re-mint, still open, **day 45**. `node assistant/saxo.js auth-url` then
  `exchange "<redirected-url>"`. Nothing can place until this clears.
- Learnings written 2026-08-18 in `agents/memory/ticker_learnings.md`: why the catalyst check
  surfaced the routine buyback and missed the bid, and why the vol-deviation heuristic that caught
  delisted EA and spun-off HEXA-B cannot catch a pending offer (EVO's vol is 30.18%, exactly its norm).

_Not financial advice._
