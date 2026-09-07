---
title: Disposable Corps, open items at end of 2026-09-07
project: dsc
status: live worklist
created: 2026-09-07
---

# Where things stand

Deck live and current at **pitch.aurorapunks.com/disposable-corps-rift** (`rift` / `qpFdQhXTL0I0`).
Gmail draft **`r3638134461610185643`**, Swedish, not sent, to Jesper + Victor + Gustav.
Commercial model v4 in `rift_split_2026-09-07.md`. LUG ask drafted in `lug_ask_2026-09-07.md`,
not sent.

## 1. Robert's correction to the team facts, 2026-09-07 (NOT YET APPLIED)

**Our material says the developer is two people. That is wrong or at least incomplete.** Robert:

> "We know that there are two founders still working with a few contractors. But a lot of delays and
> real concern from LUG."

So the hard facts are: **two founders plus a few contractors**, sustained delays, and **real concern
on the publisher's side**. Update everywhere it currently says the team is two people:
`disposable_corps/CLAUDE.md`, memory `project_disposable_corps`, the deck's slide 02 and its cover
stat "2 people on the developer side", and `commercial_analysis_2026-09-07.md`.

## 2. Slide 02 reads as speculation, rewrite to hard facts

The current copy chains public observations into an implied narrative ("the second playtest in a row
spent on foundation work", "said the team was going dark. Nothing since."). Robert flagged it as
speculation. Replace with what is actually known:

- Store page and free demo live since May 2025. Two public playtests. Six trade show appearances.
- Last public post 10 January 2026.
- Two founders plus a few contractors.
- Sustained delays.
- The publisher has real concern about delivery.

State them. Do not chain them into a diagnosis on the page.

## 3. Comparable set: DONE 2026-09-07, live

**Format:** bullet points per title, each giving **what is alike and what is different**. No selling
lingo, no fluff. **User manual mindset.** Comparable sets are highly subjective, so keep it safe and
factual and let the reader draw the conclusion.

**Missing titles to add:**
- **BattleBit Remastered** — resolved, Robert meant BattleBit. In the set: 146 375 reviews, 81 %,
  5 to 10M owners, 523 playing, 14,99 USD, three developers.
- **Minecraft WW1 trench mods.** Genuinely relevant and not yet in the set. Found: *War of Valor:
  WW1* and *PlumePack: WW1 (Modular Warfare)* mods, the *World War I: Trenches* modpack, and the
  server project *Trenches: The Dystopian Fronts*, where each faction holds six trenches and the
  goal is to push the enemy off each in turn. That is close to the plan's own sector loop, built by
  hobbyists, free. Reads both as evidence of appetite and as a free alternative.
- In the set alongside it: **Foxhole**, **Ravenfield**, **Operation: Harsh Doorstop**,
  **Battlefield 1** (positioning reference only), **Minecraft WW1 trench mods and servers**.
- Checked and left out on data: **Trench Simulator** (1366040) is still "Coming soon" with zero
  reviews, never shipped. **Low Poly Forces** (1268150) has 31 reviews and zero players.

**Excluded on purpose: `Dig In` (Steam app 2152500, Cold Pixel).** It is the closest comparable
found, a WW1 trench-building colony sim, but it is an AP-adjacent project
([[project_cold_pixel_dig_in]]), so naming it in Rift-facing material breaks the
never-name-another-client rule. Flag to Robert rather than quietly omit.

**Blocker:** the Steam store and review APIs began returning **403 from the VPS** during this
session, after working earlier the same day. `market-intel.js` and the appreviews/appdetails
endpoints all failed. Needs a retry later or a different route before the new comparables can carry
real numbers. Do not put a comparable on the page without live figures.

## 4. Still open from earlier

1. Ask LUG: wishlist count, playtest telemetry, current build, engine plus repo access.
   Draft ready in `lug_ask_2026-09-07.md`.
2. Robert can answer himself, having played the build: which key bindings the public demo ships
   with, and what the blue and orange HUD bar means.
3. First position in the waterfall is not written down. Highest-value clause in the model.
4. The 30 percent revenue share is double what LUG has seen. Decide AP's floor before the
   conversation.
5. The recoup shown to Rift is 975 000 combined against the 750 000 LUG has seen. Whoever raises
   that first sets the framing.
6. Reverse the bots-first cut.
7. No artist in the budget, so UI asset and icon production has no home.
8. AP x Rift NDA scope: company level or Starbreeze only, unconfirmed.
