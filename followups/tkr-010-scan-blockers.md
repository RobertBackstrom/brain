---
project: tkr
status: open
priority: high
updated: 2026-09-03
created: 2026-08-07
type: blocker
owner: Robert
---

## Ticker daily scan: data blocker FIXED 2026-08-13 (no EODHD needed). Saxo SIM re-mint is the last one.

The weekday SIM scan (`runRoutine` → Ticker agent, sections 2-3 of `ticker/playbook.md`) posted
**zero entry cards from 2026-06-19 to 2026-08-12** - 34 scheduled runs, every one a no-op. The
2026-08-13 scan ended the streak and posted `tkr-014-evo-st-buy-entry`.

**2026-08-13 - Blocker B is RESOLVED, and it never needed a subscription.** Yahoo was blocking on
**User-Agent fingerprint, not on IP**. Proven by a controlled, interleaved 4-way curl probe against
one URL: the full Chrome UA that `ticker-data.js` sent returned 429 in ~88ms, a bare `Mozilla/5.0`
returned 200 with real JSON, and no UA at all returned 429 `Edge: Too Many Requests`. Re-verified
clean across PDX.ST / EA / NVDA / EVO.ST. Fix applied: one line in `assistant/ticker-data.js`
(`const UA = 'Mozilla/5.0'`).

Both earlier diagnoses were wrong - the seven-week "the 08:00 digest burns the per-IP burst cap"
theory **and** its 2026-08-12 successor "the VPS IP is edge-blocked". The 08-12 probe that produced
the IP-block conclusion sent no UA, which is itself a blocked fingerprint, so it reproduced the
symptom and looked like confirmation.

Knock-on: **the 08:00 digest is fixed too.** It had logged 41 consecutive `spawnSync node ETIMEDOUT`
fatals; that was a downstream symptom, since each of 27 symbols burned 5 retries with exponential
backoff (~25s each) before failing. The full digest now completes in **3.0 seconds**.

**Do NOT buy the EODHD "All-World" key on account of this card.** It was listed here as the only
remaining fix; that was based on the wrong diagnosis. It remains a reasonable durability upgrade if
Yahoo tightens again, but it is not needed today and buys nothing the UA fix has not already bought.

**Blocker A — Saxo SIM refresh token is gone. THIS IS NOW THE ONLY BLOCKER.**
`assistant/.saxo_tokens_sim.json` has been a **0-byte file since Jul 4 23:06** (re-verified
2026-08-13, mtime unmoved for 40 days). `saxo.js positions` and `balance` both fail "No valid access
token and no refresh token". Two consequences:

1. The live open-position count cannot be verified. The 2026-08-13 scan worked around this by
   bounding the worst case (see below) rather than skipping, but that only stretches to one card.
2. **`tkr-014` cannot be confirmed until this is fixed** - placement will fail closed.

Fix:
```
node assistant/saxo.js auth-url        # → open in browser, approve
node assistant/saxo.js exchange "<redirected-url>"
```

**Blocker C — the 2026-08-11 scan died before it started (may be transient).**
`journalctl` showed `[ticker-scan] Daily scan agent completed (exit 1): Failed to authenticate. API
Error: 401 OAuth access token has expired.` The 08-12 and 08-13 runs both spawned fine, so this looks
like a one-off refresh gap. Worth watching in the `deathboard` journal; if it recurs the lane loses
days invisibly.

**Open question raised by the 2026-08-13 scan — what happened to the PDX.ST position?**
`ticker/trades_log.csv` records 35,500 PDX.ST bought @ 124.5 filled 2026-06-22 and a resting
limit-sell target @ 141 placed the same day, then **no exit line ever**. PDX traded through 141 on
2026-08-03 (high 144.3) and reached 147.6 on 2026-08-05, so that target almost certainly filled at
the broker around Aug 3 - a roughly +586k SEK win - but nothing wrote it back, because the exit
monitor had no Saxo auth and no prices. Card `tkr-009` was separately auto-closed on 2026-06-26 by a
`pending_close` housekeeping rule, which made the book *look* flat while the audit trail says
otherwise. The re-mint above is what settles this. Until then the true equity and the true slot count
are both unconfirmed.

**Activity:**
- [2026-09-03] **Ticker**: Daily scan, zero cards - **setup-limited, not budget-limited** (7th
  consecutive zero-card scan since 08-26). Budget was a genuine 1: 0 cards at
  `trade_status=awaiting_confirm`, worst case 1 open lot (35,500 PDX.ST, whose 141 GTC target is
  near-certainly filled with PDX at 142.7). Ran the 09-01 one-number test (max R = remaining upside
  / 1.5 x dailySigma) across all 25 names. **Exactly two passed against the raw 3mo high - AMZN
  3.12R and U 3.71R - and both collapsed against live supply: AMZN 1.22R to the 08-28 rejection at
  267.56, U 1.47R to the 43.80-44.00 congestion.** Both "highs" are single post-earnings spike bars
  (AMZN 07-31 +15.3%, U 08-06 +22.7%). Rest of the board died on the raw number alone: NVDA 0.67R,
  PDX 2.07R, RBLX 1.74R, HEXA-B 1.69R, MTG-B 1.58R, MSFT 1.07R, SF 0.70R, NIBE-B 0.46R, SINCH 2.40R.
  **The 08-31 carried trigger fired for the first time and it was a false positive:** AMZN closed
  254.98 against a recorded trigger of 260.44, but that trigger was derived off the period high
  287.2, which the 09-01 scan had already downgraded to the 267.6 shelf - off the correct shelf the
  trigger is 242.96. AMZN also broke its 257-259 shelf on 09-01, so the setup is gone, not cheap.
  Triggers re-derived against live supply and carried forward: **SINCH 43.89** (now 44.05, only 0.4%
  away and falling - closest name on the board), PDX 141.11 (142.7), HEXA-B 94.75 (97.14), NVDA
  209.42 (224.41), EMBRAC-B 70.00 (73.66), U 38.86 (40.76), AMZN 242.96 (254.98).
  EVO re-verified excluded on current facts - Candle Lake/Dart SEK 695 acceptance runs to **09-15**,
  today sits inside the window (§1). TTWO rejection still live (GTA VI 11-19). SINCH's Q3 date could
  not be established by search, so per the 08-31 rule that is a **failed check, not an all-clear** -
  re-run it if the 43.89 trigger fires.
  **Saxo SIM token still 0 bytes, mtime unmoved at Jul 4 23:06 - day 61.** Balance cache
  `fetched_at` 2026-06-30, now **65 days** past a 15-minute TTL. Nothing mis-sized (no card), but
  re-mint remains the only open blocker: `node assistant/saxo.js auth-url` -> approve in browser ->
  `node assistant/saxo.js exchange "<redirected-url>"`.
  **Raised for decision: the sprint is 47 days past its own terminal condition.** Playbook §8 ends
  the experiment at the 30-day window, which closed ~2026-07-18. It has since run with a dead broker
  token, an unreconciled PDX exit, and no confirmable equity. Recommend the weekly review either
  formally closes the sprint on the PDX result or restates the window.
- [2026-08-27] **Ticker**: Daily scan, zero cards - **setup-limited, not budget-limited**. Budget was a
  genuine 1 (0 cards at `trade_status=awaiting_confirm`; worst case 1 open lot, 35,500 PDX.ST, whose
  141 GTC target is now near-certainly filled with PDX at 144). Whole watchlist screened; the
  active-resistance correction killed the field again (EMBRAC-B 2.32 vs 7.73 needed against the real
  76 shelf rather than the single-bar 80.8 earnings spike; ERIC-B 3.3 vs 5.06 against the 99 shelf;
  META, RBLX, SPCX, TSLA, APP all failing once the pre-crash high is replaced by the recovery band).
  MTG-B, EG7, G5EN and SF fail the turnover screen at SIM scale (a 4.44m SEK order is 19% / 141% /
  497% / 36% of ADV). EVO remains excluded - the Candle Lake tender is live, board recommends
  REJECTING the 695 bid, acceptance runs to 09-15 and settlement from 09-23, with the stock at 832.6,
  i.e. ~20% above the offer. **NVDA is the one to watch tomorrow:** it reported a large Q2 FY27 beat
  after last night's close and is the only name whose geometry passes with no gap in the lookback, but
  the feed's last bar (`asOf 2026-08-26T20:00:00Z`) predates the announcement, so it cannot be priced
  today. It goes to the top of the 08-28 scan once a real post-earnings bar prints.
  **Saxo SIM token still 0 bytes, mtime unmoved at Jul 4 23:06 - day 54.** Sizing still works off the
  cached 11,095,039 SEK basis, so cards can be drafted, but nothing can place until:
  `node assistant/saxo.js auth-url` -> approve in browser -> `node assistant/saxo.js exchange "<redirected-url>"`.
- [2026-08-17] **Ticker**: Second clean-data scan; posted `tkr-015-evo-st-buy-entry` (EVO.ST, 6013
  @ 738, target 786, stop 719, R:R 2.53). `tkr-014` expired unconfirmed 08-14 18:03Z - price broke
  out rather than filling 730, so the entry is re-set on the breakout retest. **Saxo SIM token is
  still 0 bytes, mtime unmoved at Jul 4 23:06 - day 44.** This is now the only thing standing
  between a ranked scan and a placed order: `tkr-015` will fail closed at placement until you run
  `node assistant/saxo.js auth-url` → approve in browser → `node assistant/saxo.js exchange "<redirected-url>"`.
  The same re-mint is what confirms the PDX +585,750 SEK fill and closes the sprint's headline number.
- [2026-08-14] **Ticker**: Scan ran on clean data for the first time. Two findings. (1) **The PDX
  question is now all but settled: the target FILLED.** `placeExitSell()` defaults to
  **GoodTillCancel**, so the 35,500 @ 141 sell (Saxo 5038927319) has rested *at Saxo* since 06-22,
  unaffected by our dead auth. PDX then traded a complete session at or above 141 on **08-04 (low
  exactly 141, close 145.1)** and **08-05 (low 144.7)**, after high 144.3 on 08-03 - three sessions
  above a resting limit, with no cancel line in the audit trail. Implied **+585,750 SEK realized
  (~+13.3%)** around Aug 3. Treat the book as FLAT and the sprint as a win pending the re-mint.
  (2) Found and fixed a second data bug the UA fix had exposed - the digest's "Day %" column was a
  ~30-day change (MSFT printed **+27.08%** for a day the stock moved **+0.90%**; RBLX and PDX were
  sign-flipped). Yahoo has no `previousClose` field, so `chartPreviousClose` (which is relative to
  the whole fetched range) was being used as the daily baseline in **both** `digest` and `quote`.
  Fixed in `assistant/ticker-data.js` via a `prevCloseFromSeries()` helper; verified against a
  hand-computed value. **This was flowing into your 08:00 mail as fact.** No new card posted: full
  watchlist ranked, no setup cleared §2.3 (NVDA earnings 08-26 inside the horizon, EMBRAC-B a
  post-beat gap chase, RBLX/APP/PLTK downtrend knives, MTG-B fails turnover, TTWO in rejection
  history). `tkr-014` still unconfirmed and expires today 18:00Z.
- [2026-08-26] **Ticker**: Saxo SIM token file still **0 bytes, mtime Jul 4 23:06 - day 53**. Live
  position count remains unverifiable, so slot arithmetic is still a worst-case bound (1 possible open
  lot: 35,500 PDX.ST). Further evidence that lot's 141 GTC target filled: PDX closed **145.4** on 08-25,
  above the limit. `tkr-014` / `tkr-015` / `tkr-016` have all now expired unconfirmed, so pending = 0 and
  today's card budget was a genuine **1** - the first real open slot in over a week. No card posted
  anyway: the whole watchlist failed §2.3 on setup, not on budget. The two names that cleared geometry
  and trend (META, RBLX) both failed once remaining upside was measured to live resistance instead of a
  pre-earnings-gap high. NVDA reports today after the close; EVO is inside the Candle Lake/Dart mandatory
  offer (SEK 695, acceptance 08-17 to 09-15) and trades 21% above the bid.
- [2026-08-13] **Ticker**: Streak broken at 34. Root-caused the data blocker to a UA fingerprint and
  fixed it in one line; digest restored from 41 straight timeouts to a 3.0s full run; EODHD purchase
  recommendation withdrawn. Posted `tkr-014-evo-st-buy-entry` (EVO.ST, 6079 @ 730, target 775, stop
  713, R:R 2.65). Saxo re-mint is now the sole blocker and gates confirming that card. Flagged the
  unreconciled PDX.ST position above.
- [2026-08-12] **Ticker**: 34th consecutive no-op. Diagnosis "corrected" to an IP-level edge block
  and the free remedy withdrawn, leaving EODHD as the only listed fix. **Both of those conclusions
  were wrong** - see the 08-13 entry. Saxo token file still 0 bytes, mtime Jul 4 23:06.
- [2026-08-10] **Ticker**: 32nd consecutive no-op. Both blockers re-verified unchanged. First scan
  since the card was opened, so the card alone had not moved either fix.
- [2026-08-07] **Ticker**: Card opened after the 31st consecutive no-op scan. The blockers had been
  logged to `agents/memory/ticker_learnings.md` 31 times with no follow-up card in existence.

_Not financial advice._
