---
name: project_starbreeze_irons2
description: "Project Irons 2 (Heist Royale 2, PAYDAY x PUBG) — AP co-dev pitch to Starbreeze: team shape, commercials, audience findings, and the Krafton evidence problem"
metadata: 
  node_type: memory
  type: project
  originSessionId: 2e8cd21b-fca1-4951-94a4-ae2f6cee3530
  modified: 2026-08-17T23:10:25.829Z
---

# Project Irons 2 — Starbreeze co-dev

Krafton-funded PAYDAY x PUBG crossover mode, internally "Project Irons", publicly shipped as "New Mode: PAYDAY" / Heist Royale. Aurora Punks is pitching to co-develop the second installment. Contacts: **Tobias Remmers** (PAYDAY Franchise Director, tobias.remmers@starbreeze.com) and **Matt Dixon** (matt.dixon@starbreeze.com). Distinct from [[project_upvote_starbreeze]], where Daniel Mesonero has replaced Matt as primary contact.

**Status 2026-08-21:** Starbreeze want a meeting and it is close to booked. Thread `19ff6451882f7d46`, 7 messages: Robert sent the pitch 18 Aug 01:05; **Matt replied same day 16:40** flagging a **Krafton call on 19 Aug to lock final scope**; **Tobias replied 20 Aug 13:17** saying the project is progressing, that **adjustments are coming out of that Krafton call**, and asking to meet on scope, complexity and our proposal; **Robert answered 20 Aug 15:32** proposing the **first half of w/c 24 Aug**. Krafton's adjustments are unknown to us and may move the plan again before the meeting.

**Live discrepancy to handle in the room:** the 18 Aug mail told them the team "peaks at 14 (not counting QA)". Staffing was revised upward 20 Aug on Robert's instruction and the page now says **peak 23**, budget 38,6 MSEK against the 24,9 they were told, so the gap is 9 people and 13,7 MSEK. This is no longer a correction to mention in passing, it is a different offer. Robert should raise it himself rather than let them find a 36% headcount increase on a page he described as living. The lean framing is gone; the honest positioning is now 23 against Tobias's 30-40, still meaningfully leaner but no longer a headline. **Three assumptions in the current numbers are mine and unconfirmed:** the enemy programmer runs First Playable to Beta, the technical designer runs September to Beta, and the second tech artist runs First Playable to Beta with only one left in Gold. Level design was read as a floor of 3 from First Playable, keeping 4 at Alpha 1 where two heists overlap; the alternative readings moved the total by only 336 000.

**Rift Gaming:** Robert meets them 21 Aug (Gustav Wassberg; **Dmitry** as Tech Lead and **Jesper** as Level Design Lead, both able to join the Starbreeze meeting). Gustav asked for a pre-meeting to align on expectations. The revised plan needs a peak of four level designers, so Rift carries more of the plan than before and their rate must sit under 140k/dev/month. Robert forwarded Tobias's feature list to Gustav 20 Aug 14:51.

Engagement now tracked on **`sbz-001`**; `db-294` holds the build history of the pitch and stays closed.

**The pitch (living doc, update in place, never re-send):**
- `pitch.aurorapunks.com/project-irons-2/` — user `starbreeze`, pass `Ai8M9hj8JNyG`. Gated because the page carries Krafton/PUBG-confidential scope detail. Source `pitches/project-irons-2/index.html`, auth in `assistant/pitch-auth.json`.

**Scope Starbreeze asked for** (Tobias's 12 Aug feature list, two PDFs on the thread): four new heists adapted from PAYDAY 3 (Turbid Station, 99 Boxes or Touch The Sky, Syntax Error, Under The Surphaze), the four HR1 stages upgraded, progression rework (EXP to currency, free skill and weapon selection), five new weapons, stealth ingredient expansion, shield enemy, one more difficulty, restart plus partial escape, UI/UX overhaul, PUBG engine and 3C changes. His staffing outline: 31-43 roles, peak 30-40, roughly 12 months.

**AP's counter-position:**
- Ramp **7.5 → 18.5 → 21 → 22 → 23 → 19 → 9 → 6** over 13 months (Sep 2026 to Sep 2027), **peak 23 in Alpha 2** (revised again 2026-08-24: +1 gameplay programmer, new enemy programmer, UI programmer extended to the last day, level design floored at 3 from First Playable, new technical designer from September). Earlier shapes peaked at 14 (the figure actually sent to the client 18 Aug), 19 and 22. Role naming settled 24 Aug: character artist replaced by **hard surface artist**, tech art lead renamed **tech artist** and doubled, console lead renamed **console programmer**. Console lead runs 50% through Sep and First Playable. Disciplines sequenced rather than held in parallel.
- **Engine and 3C work sits with AP**, not the PUBG team. Krafton was hands-off on Irons 1, so framing it as needing their engineers read as weakness.
- QA outside the headcount as external contractor. Leads on-site at SBZ (Birger Jarlsgatan 61), rest hybrid. No named resources in the first offer.
- September is a standalone-contractable paid evaluation month producing a technical evaluation, costed scope recommendations and a locked First Playable plan.

**Commercials (canonical):**
- **140 000 SEK per developer per month, flat retainer**, same for a lead as a content role. Robert's call: a flat retainer removes the hourly comparison against a cheaper Czech studio that is also bidding. Do not revert to an hourly rate card here.
- 229.5 FTE-months = 32 130 000 delivery subtotal, **+10% contingency 3 213 000 = 35 343 000 SEK** ex VAT, ex QA (contingency cut 20% to 15% to 10% on 2026-08-24; rate held at 140k). September alone 1 050 000. (Earlier: 148 FTE-months / 24 864 000 as sent to the client, then 180.5 / 30 324 000.)
- QA quoted separately at **500 SEK/h** (80 000 per full QA month).
- The page states unused contingency is not invoiced. That was a deliberate sellability choice, not a given.

**Audience findings** (full memo `starbreeze_irons2/drafts/design_due_diligence.md`, RankOne panel of 3 109 PUBG profiles plus SteamCharts, 80.lv and community sweep):
- Crossover affinity runs through **PAYDAY 2** (20.4%, 4.06x), not PAYDAY 3 (2.25%, 1.25x). The living PAYDAY community is PD2's, ~30k CCU against PD3's ~900. Recognition arguments built on PD3 content do not land.
- PUBG base is **exactly neutral on stealth (1.00x)** and strong on loud co-op PvE (1.63x) and SWAT-style tactical play (2.53x). Read as a sequencing and positioning argument, never as "cut stealth".
- HR1 produced **no Steam CCU lift** for PUBG; the PAYDAY 3 halo was real but ~260 concurrents.
- Tobias is **supported** on his stealth avoid-list, the progression rework and partial escape; **contradicted** on "bigger and more complex" as a goal.
- The one first-hand HR1 stealth account complained about the **10% completion bonus**, not the mechanics count. Cheapest stealth fix is payout tuning through the new currency economy.

**Krafton evidence problem — never put in writing.** Tobias and Matt told Robert they believe Krafton merely ran an AI sweep over player sentiment for the first mode, and that real telemetry might change their own assumptions. This puts AP **on the same side as Tobias and Matt**, not against them: the ask for HR1 mode telemetry backs a position they already hold. On the page this is carried as "measured behaviour rather than inferred sentiment" and "whoever produced them". Never name the AI sweep in a document or mail, it is an internal Starbreeze view of their funder.

**Open threads:** HR1 mode telemetry from Krafton (adoption, stealth-vs-loud split, retention, pass attach) is the single highest-value ask. Starbreeze Q2 2026 interim report is the first public read on post-launch economics, check before any meeting. Console-side sentiment is unsampled, see [[reference_vps_web_collection_limits]]. Rift Gaming may supply senior roles but must be held to the 140k level; tracked separately.
