# Ironcrest x Paradox - Business Case Working Doc

**Purpose:** the reasoning and number logic behind a go/no-go on signing *Ironcrest*. This is a thinking document, not a deck. Every number has a "why". The friend presenting can lift the structure and dress it up; the value here is the logic chain.

**Date:** 2026-06-22 (v2 - revenue + cost models adversarially pressure-tested by Analytics + PM agents and reconciled)
**Sources:** work-test brief; our masterbrain benchmarks ([[game_gtm_plan_benchmarks]], [[game_publishing_deals]], [[paradox_publishing_model]]); GameDiscoverCo / Alinea Analytics / Chris Z DLC data in RAG; AP's own Rust Racers financing model (GDrive); Polish Gamedev Salary Report 2025; CK3 localisation + sales-timeline data; Paradox FY2025 year-end report + EU5 launch (web, June 2026).

**v2 changes (what the pressure-test moved):** base-case units pulled 600K -> 500K (only ~21% of EA titles get a bigger 1.0 beat); conversion logic restated as explicit lifetime tiers instead of a hidden multiplier; net-per-unit made scenario-specific; localisation re-scoped (8-10 languages is EUR 350-500K, not 150K - we recommend 4-5 launch languages); "EA pays for the back half" corrected to "advance + EA jointly fund through 1.0"; advance raised to EUR 1.0-1.5M with a post-EA top-up; timeline slip widened to 50-100%. Net effect: bear/base 2-year revenue down ~10-15%, costs up, and the go-recommendation is unchanged but rests more explicitly on the milestone-gated advance + the post-2-year DLC tail.

---

## 0. How to read this / the meta-point for the panel

The brief says it twice: *they care more about reasoning than numbers.* So the spine of the presentation is not "here is a revenue forecast", it is:

1. **What does Paradox specifically bring** that makes this deal worth more to them than to any other publisher? (If the answer is "nothing special", you self-publish and walk.)
2. **What is the honest risk**, named out loud, including the risk inside Paradox's own portfolio and strategy.
3. **A deal structure that prices those risks in** rather than hand-waving them.
4. **Success defined as a funnel, not a number** - because the Paradox model makes most of its money years after launch.

Lead with the strategic fit, be candid about the tension, then let the model support the call. A panel hiring a Business Owner wants to see commercial judgement under ambiguity, not a spreadsheet.

---

## 1. Stated assumptions (the brief invites these - state them clearly)

| # | Assumption | Why we assume it |
|---|-----------|------------------|
| A1 | Wishlists grow to ~250K by EA (base case) | 95K organic now + 6 months + Paradox cross-promo to the CK3/Vic3/EU5 base (a ~2.6x climb). Conservative vs Manor Lords' 3.2M. Caveat: conversion is NOT linear in bank size - bigger banks accrete old/low-intent wishlists and convert at a lower %. |
| A2 | Scenario-specific net revenue per base unit: bear EUR 13 / base EUR 15 / bull EUR 16 | Headline EUR 30-40, minus Steam 30%, minus blended discount/regional/refund realisation. A slow seller discounts harder and sooner, so the bear case nets less. Anchored to AP's Rust Racers attenuation model + [[game_gtm_plan_benchmarks]]. |
| A3 | Fully-loaded studio burn ~EUR 600-800K/year (15 people, Wroclaw) | Polish Gamedev Salary Report 2025: mid-tier studio blended fully-loaded ~EUR 35-45K/head. EUR 800K/yr (~EUR 53K/head) is the conservative-high end; used as our planning figure. Cross-checks against EUR 2.1M spent (~2.6 years burn, ~2023 production start). |
| A4 | "6mo to EA / 18mo to full" is optimistic; treat a 50% slip as the BASE case, up to 100% | First-time-with-publisher teams on systems-heavy genres routinely slip 50-100% (Manor Lords, Vic3, CK3 all elastic). Realistic: EA ~8-10mo, 1.0 ~24-30mo. The remaining 40% is the hard 40% (late-game, balance, AI, performance). Size the advance for the long case. |
| A5 | Paradox treats this as a base + DLC live title for 5-10 years | This is Paradox's actual operating model (CK3, EU, Stellaris). The 2-year window understates lifetime value; we flag it. |
| A6 | EU5 (launched Nov 2025, EUR 59.99) is live and ramping DLC through this whole window | Same wallet, same player time. Internal portfolio overlap is real and must be in the risk column. |

If any of these is wrong, say which and the call can move. That is the point of listing them.

---

## 2. Market read

### 2.1 The opportunity
- **Genre is in a proven, hungry niche.** Grand strategy is small but deep-pocketed and loyal. The comparables bracket the upside: Manor Lords (accessible end) did 3M+ units and EUR 60M+ by mid-2024 off 3.2M wishlists; CK3 (deep end) sustains a ~EUR 250 DLC library and a subscription, proof that the dedicated base pays for a decade.
- **Ironcrest sits in a real gap.** "Between Manor Lords and CK3" is not marketing fluff - it is a genuine open lane. Manor Lords is light on the political/dynasty layer; CK3 intimidates newcomers. A medieval dynasty game that is deeper than Manor Lords but more approachable than CK3 is a position Paradox does not currently own with a fresh IP.
- **Organic signals are healthy, not hyped.** 95K wishlists, 8,200 Discord, 340K reveal views, all organic. That is a real audience forming with zero paid push. The wishlist/Discord ratio (~11:1) and organic-only origin read as genuine demand, not bought hype.
- **Audience overlaps Paradox's existing base almost perfectly.** CK3 + Victoria 3 players, 25-40, PC-only. This is the single most important line in the brief, and it is covered in section 3.

### 2.2 The risks (named honestly)
1. **Execution risk on the hard 40%.** Grand strategy lives or dies on late-game depth, AI, balance and performance - exactly the three gaps the brief lists. "60% content complete" is the comfortable 60%. The remaining work is the part that historically slips and breaks games in this genre.
2. **Studio is unproven at this scope.** Ashfeld (480K units, 78%) shows competence, but a city-builder is a different systems-complexity class than a multi-generational grand strategy sim. No prior publishing partner means no track record of hitting external milestones.
3. **Timeline optimism.** 6mo/18mo from a team with limited QA and no publisher discipline is likely 30-50% short. Plan and price for slippage.
4. **Portfolio cannibalisation (internal risk).** EU5 just launched and will absorb the same strategy wallet and attention through Ironcrest's whole EA window. Paradox would be partly competing with itself for the CK3/EU audience's time.
5. **Strategic-fit tension at Paradox right now (the big one).** Paradox FY2025: revenue flat at SEK 2.19bn, operating profit down 80% to SEK 146M, a write-down on Vampire: The Masquerade - Bloodlines 2 for missing expectations. Their stated response was a refocus on *deep strategy and management games, mostly developed in-house*, bringing Cities: Skylines in-house and acquiring Haemimont. Ironcrest is dead-centre genre fit but cuts against the "in-house" half of that pivot: an external 15-person studio with founders protective of design. The deal has to answer "why does this external bet not become the next thing we write down?"
6. **Relationship/control friction.** Founders protective of design + Paradox's hands-on systems-design culture = friction risk. This is foreshadowed directly by Task 2.

**Net read:** genuine opportunity in Paradox's exact wheelhouse, with a credible audience, but the risk is concentrated in execution and in Paradox's own current risk appetite. The deal lives or dies on structure, not on whether the game is good.

---

## 3. Why Paradox specifically (the core of the case)

A publisher deal is only worth signing if the publisher adds more than the developer gives up. Paradox's added value here is unusually high for three reasons:

1. **Owned-audience funnel.** Paradox can put Ironcrest in front of the CK3, Victoria 3, EU5, Stellaris base through the launcher, mailing lists, forums and cross-promo. For almost any other publisher, the 95K wishlists are a starting point; for Paradox, that audience overlap de-risks the single hardest step in the funnel - turning wishlists into players - more than money could.
2. **DLC live-ops as a core competency.** Nobody runs a base + DLC strategy title for a decade better than Paradox. The late-game-content gap that is a *risk* at launch becomes a *post-launch DLC roadmap* in Paradox's hands. They are the one publisher that can turn Ironcrest's biggest weakness into its business model.
3. **Localisation + QA capacity.** The studio explicitly lacks both. These are exactly the gaps a publisher fills, and Paradox has the pipelines.

The flip side, stated plainly: this is also why the studio should not give away IP or accept punishing terms. Paradox needs titles for its refocused core slate. There is mutual leverage.

---

## 4. The cost side (PM lens: what does it take to finish and ship?)

### 4.1 Cost to complete
| Bucket | Estimate | Logic |
|--------|----------|-------|
| Core dev to full release | ~EUR 1.2-1.6M | 15 people x ~EUR 600-800K/yr (A3) x ~1.5-2.5 yr remaining (A4 slip). The remaining 40% is the *hard* 40%, so cost-per-unit is above a linear extrapolation of the EUR 2.1M sunk. |
| Localisation (scoping decision) | EUR 150-250K at launch | Grand strategy is the most text-heavy genre (CK3 ships ~1.05M words; a new mid-size GSG ~300-500K). Full 8-10 languages would be EUR 350-500K. **Recommend the Paradox pattern: 4-5 launch languages (~EUR 150-250K), rest added live/DLC-funded.** This must be stated, not assumed - "8-10 languages @ EUR 150K" is indefensible. |
| External QA (PC-only, no cert) | ~EUR 200K | Studio lacks QA. ~18-24 months of external PC QA. No console certification cost (PC-only), so this is a QA-only line. |
| Marketing (publisher's main spend) | EUR 750K-1.0M | For a EUR 30-40 title targeting six-figure units, ~5-7% of base-case gross / ~30% of new money. Owned-audience leverage keeps paid efficient, so do not over-spend - the launcher base is the point. |
| **New money to full release** | **~EUR 2.4-3.3M** | What Paradox actually risks. Lower end assumes 4-5 launch languages; upper end assumes full loc + the harder dev/timeline case. |

### 4.2 Total project budget
- Sunk by studio: EUR 2.1M.
- New money to 1.0: ~EUR 2.4-3.3M.
- **All-in to full release: ~EUR 4.5-5.4M** (or ~EUR 4.4-4.7M if loc is deliberately scoped to 4-5 launch languages). Still a reasonable mid-size strategy budget, well below a Paradox AAA like EU5.

### 4.3 Advance sizing (corrected)
- The studio has 9-12 months runway and needs ~18-30 months of dev (A4). 
- The honest version of the cash logic: **EA revenue alone does NOT fund the back half.** EA first-month revenue is roughly 50K units x EUR 15 net x ~50% dev share = ~EUR 375K one-off plus a declining tail - nowhere near the ~EUR 50-67K/month burn across a 12-20 month EA-to-1.0 window. So the advance and EA revenue have to fund through 1.0 *jointly*.
- **Recommended structure: recoupable advance EUR 1.0-1.5M, milestone-gated**, with (a) a pre-EA tranche bridging runway, (b) **EA as a hard go/no-go gate before the largest tranche**, and (c) a **post-EA top-up tranche tied to EA unit + review performance** to fund the EA-to-1.0 tail. This limits Paradox's at-risk capital before the EA gate proves the funnel, without relying on the false "EA pays for everything" story a sharp panellist will push on.

---

## 5. The revenue model (Analytics lens: scenarios, not a point forecast)

The brief wants logic, so this is built as bear / base / bull with the conversion chain visible. All figures are gross-to-the-deal (after Steam's 30%, before the dev/publisher split), over a **2-year window**. Remember A5: Paradox's real model runs 5-10 years, so even the bull case understates lifetime value.

### 5.1 Base-game units (stated lifetime-conversion logic, two cross-checks)

**Method 1 - wishlist funnel with explicit lifetime tiers.** Instead of a first-week ratio plus a hidden multiplier, use AP's own Rust Racers financing tiers (which already encode the industry conversion curve):
- Week 1: 10-30% of the EA wishlist bank. Month 1: 15-40%. **Year 1: 30-90%** (roughly month-1 x 2-3).
- At a 250K EA bank that is ~25-75K month-1 and ~75-225K year-1 *from the EA bank alone*, before the bank rebuilds for 1.0.

**The honest caveat (this is the model's real risk).** The optimistic part is assuming a big "1.0 second beat". GameDiscoverCo: **only ~21% of 2026 Steam EA graduates earned more at 1.0 than in their first 30 days of EA.** So the median title does NOT get a large 1.0 spike. We therefore keep the 1.0-rebuild beat small and separately justified.

**Method 2 - comparables anchor.** CK3 (deep end) reached ~1M in year 1 and only ~4M after ~5 years - the deep niche compounds slowly. Manor Lords (broad, exceptional) did 3M+ but that is an outlier with mass-market reach. Ashfeld did 480K. Ironcrest is a new-IP genre title between these, so the base case lands a touch under CK3's year-1 trajectory extended over 2 years.

| Scenario | Lifetime base units (2yr) | Reasoning |
|----------|---------------------------|-----------|
| Bear | ~250K | EA validates but stays niche; EU5 soaks attention; slippage hurts momentum. ~= Ashfeld floor. |
| Base | ~500K | Owned-audience funnel works, 80%+ reviews, a *modest* 1.0 beat (not a big one - the 21% rule). A solid, defensible outcome for a new-IP genre title with a publisher push. |
| Bull | ~1.1-1.2M | Breaks out the way Manor Lords did, strong word of mouth, Paradox push lands, a real 1.0 beat. |

### 5.2 Base-game revenue
At scenario-specific net/unit (A2):
- Bear: 250K x EUR 13 = **~EUR 3.25M**
- Base: 500K x EUR 15 = **~EUR 7.5M**
- Bull: 1.2M x EUR 16 = **~EUR 19.2M**

### 5.3 DLC (where the Paradox model actually lives)
The benchmarks for an engaged strategy base are strong: DLC wishlist conversion ~43% vs ~18% for base ([[game_gtm_plan_benchmarks]]); hard Alinea estimates of 21-55% expansion/supporter-pack attach in 2026 (StarRupture pack 55% early settling to ~24%; Monster Train 2 expansion 21%). Paradox's own model shows the dedicated base buying DLC for a decade (CK3's ~EUR 250 library + subscription).

DLC as a multiplier on base revenue, **window-constrained to 2 years** (a new IP needs the base installed before attach compounds):
- Bear: +30% of base = +EUR 1.0M
- Base: +50% of base = +EUR 3.75M
- Bull: +60% of base = +EUR 11.5M (capped at +60% over 2yr - the +70% only shows up once the install base matures)

The key point for the panel: in years 3-10 this multiplier compounds and usually overtakes base revenue entirely (CK3 is the proof). **The 2-year number is the floor of the DLC story, not the ceiling** - and the downside is well-protected (engaged strategy bases reliably attach DLC) while the upside is uncapped.

### 5.4 Combined 2-year gross-to-deal
| Scenario | Base | DLC | Total (2yr, post-Steam) |
|----------|------|-----|--------------------------|
| Bear | 3.25M | 1.0M | **~EUR 4.25M** |
| Base | 7.5M | 3.75M | **~EUR 11.25M** |
| Bull | 19.2M | 11.5M | **~EUR 30.7M** |

*(EU5 cannibalisation: bound it as a ~5-15% drag on Ironcrest base units in the EA window - same wallet, same player, same launcher real estate. The lever is timing: sequence the EA launch into a softer EU5-DLC quarter. Treat as a -10% mid sensitivity, not a separate line.)*

### 5.5 Does the deal pencil for Paradox? (the sharpened version)
- Paradox's at-risk new money is ~EUR 2.4-3.3M (section 4).
- In the **bear case**, Paradox's ~50% share of EUR 4.25M = ~EUR 2.1M, which only *roughly* covers the low end of outlay over 2 years **once the post-2-year DLC tail is counted**. The 2-year bear P&L on its own is thin.
- This is the important, honest point: **the deal's downside protection does NOT come from the 2-year P&L - it comes from (a) the milestone-gated advance that limits at-risk capital before the EA gate, and (b) the post-2-year DLC tail that the Paradox model reliably produces for an engaged strategy base.**
- That makes the "lean, EA-gated advance" condition *more* important, not less. The base case (Paradox's ~EUR 5.6M share of EUR 11.25M) and bull case are comfortably profitable, and every scenario improves sharply in years 3-10.
- **Conclusion: the downside is protected by structure + the DLC tail, and the upside is a genre franchise.** That asymmetry is the financial argument for go - it is a stronger, more defensible version of the v1 claim, not a weaker one.

### 5.6 Data points behind the numbers (for the panel, if pushed)
- **Only ~21% of 2026 Steam EA graduates earned more at 1.0 than in their first 30 days of EA** (median EA duration ~1y3m). - GameDiscoverCo, May 2026. *Pre-empts the "big 1.0 beat" assumption and supports the EA-is-the-real-gate framing.*
- **CK3 sales timeline: ~1M month 1 (2020) -> 2M (Mar 2022) -> 3M (Sep 2023) -> 4M (Apr 2025).** - Paradox press releases. *The deep end takes ~5 years to reach 4M; justifies a conservative 2-year base.*
- **Manor Lords: ~1M day-one off 3.2M wishlists (~31% day-1), ~26% lifetime conversion.** - gamedeveloper.com, 2024. *The accessible-end ceiling, and proof conversion % falls as the bank inflates.*
- **DLC attach hard estimates: StarRupture Supporter Pack 55% -> ~24%; Monster Train 2 expansion 21%; Steam baseline DLC attach low single digits.** - Alinea Analytics, 2026.
- **House wishlist-conversion tiers: Wk1 10-30%, Mo1 15-40%, Yr1 30-90%.** - AP's Rust Racers financing model (GDrive).

---

## 6. Pricing and strategy changes

The proposed EUR 29.99 EA / 34.99 1.0 is close but leaves value on the table and misreads where this model earns.

1. **Raise 1.0 to EUR 39.99.** The CK3/EU5 audience pays premium-indie/AA prices; EU5 itself is EUR 59.99, so EUR 39.99 reads as value, not greed. The brief's EUR 34.99 underprices the depth (40-80h campaigns) and the target buyer's willingness to pay.
2. **Keep EA at EUR 29.99 (or even EUR 27.99).** Counter-intuitive but deliberate: in the Paradox model the base price is not where you optimise. **Optimise EA for install-base growth, not ASP.** Every extra EA buyer is another DLC customer for a decade. A slightly lower EA price maximises wishlist conversion and review velocity, which feeds Steam's algorithm and the DLC funnel. This is a Paradox-native insight worth saying out loud in the room.
3. **Free content roadmap during EA; the paid DLC flywheel starts at 1.0.** Late-game content is the studio's biggest gap. Ship a polished core loop at EA, then fill the gap with *free* content updates across the EA period - this is the building-in-public model that strategy audiences expect and reward. Keep paid gameplay DLC out of EA entirely: charging for content on top of an unfinished base is the one move that reliably sours an EA community. The paired free-plus-paid expansion model (every paid expansion shipped alongside a free patch for everyone) is a *post-1.0* rhythm, not an EA tactic. The only acceptable paid item during EA is an optional, non-gameplay cosmetic/supporter pack (the StarRupture supporter-pack pattern). This protects the launch *and* seeds the live model without the EA-monetisation backlash.
4. **Hold the subscription lever for later.** Once the DLC library is deep enough (CK3 only added a sub years in), a subscription smooths the "EUR 250 pile is intimidating" problem. Not a launch move, but a stated part of the long arc.
5. **No live service, keep it that way.** The brief says no live service and that is right for the genre. Base + DLC is the proven Paradox shape; do not over-engineer.

---

## 7. What success looks like (a funnel, measured at three gates)

Success is not one number. It is whether each stage of the funnel validates before the next tranche of spend.

### 7.1 At 6 months (= EA launch window)
The question this gate answers: *did EA validate conversion and stickiness?*
| Metric | Target | Why it matters |
|--------|--------|----------------|
| Wishlists at EA launch | 250K+ | Proves the owned-audience funnel is working. |
| EA first-month units | 50-75K | Conversion of the funnel into cash. |
| Steam review rating | 80%+ ("Very Positive") | Below this, the algorithm and word of mouth stall. |
| Median playtime / D30 retention | High for genre | Strategy is retention-driven; this predicts DLC attach. |
| Refund rate | <8% | Sanity check on expectation vs delivery. |

### 7.2 At launch (1.0, ~18mo, realistically later per A4)
The question: *did it hold up and start the live model?*
| Metric | Target | Why |
|--------|--------|-----|
| Cumulative base units | 500K+ | On track to base case. |
| 1.0 review uplift | Rating up vs EA | EA did its job. |
| First DLC attach rate | 20%+ | The flywheel turns. |
| Recoup status | Advance near/fully recouped | De-risks the back catalogue decision. |
| Wishlist bank rebuilt for 1.0 | Strong 1.0 spike | Funnel still feeding. |

### 7.3 At 2 years
The question: *is this a franchise?*
| Metric | Target | Why |
|--------|--------|-----|
| Lifetime base units | 600K-1M+ | Base/bull territory. |
| DLC as % of total revenue | 30%+ and climbing | The Paradox flywheel is live. |
| Returning DAU around DLC drops | Clear spikes | The base is engaged, not churned. |
| Cohort LTV / DLC attach trend | Rising | Greenlight signal for a sequel or standalone expansions. |

The 2-year strategic decision is not "did it sell" but "do we commit to Ironcrest as a 5-10 year franchise". That is the real prize and the real measure.

---

## 8. Recommendation: CONDITIONAL GO

**Sign it - structured to price the risks in.**

The case for go: Ironcrest is dead-centre in Paradox's refocused core genre, the audience overlap de-risks the funnel more for Paradox than for any other publisher, DLC live-ops turns the biggest weakness into the business model, and the downside is protected even in the bear case while the upside is a decade-long franchise. That asymmetry is the call.

The conditions that make it a *responsible* go (and that answer the "next Bloodlines 2 write-down?" question):
1. **Milestone-gated advance (EUR 1.0-1.5M)** with a pre-EA tranche to bridge runway, **EA as the first hard go/no-go gate before the largest tranche**, and a post-EA top-up tied to EA unit + review performance to fund the EA-to-1.0 tail. This limits at-risk capital before the funnel is proven, without the false "EA pays for the back half" assumption.
2. **Dev share ~50-55%, concurrent recoupment, studio keeps IP**, Paradox takes a publishing licence plus DLC/sequel rights. The franchise potential is the prize; do not fight over ownership ([[game_publishing_deals]]: IP stays with dev in 96%+ of deals).
3. **Pricing per section 6** - premium 1.0, install-base-optimised EA.
4. **Localisation scoped to 4-5 launch languages** (the Paradox pattern), rest added live/DLC-funded - keeps loc at EUR 150-250K instead of EUR 350-500K and matches how CK3 shipped.
5. **Free content roadmap during EA, paid DLC from 1.0** - fills the late-game gap in public without charging on an unfinished base; the paid free-plus-paid flywheel starts at launch (an optional cosmetic supporter pack is the only acceptable paid item during EA).
6. **A defined design-authority split with the founders up front** - because Task 2 is coming, and the relationship is the asset that makes the 10-year flywheel possible.

If the studio refuses EA entirely (Task 2 taken to its extreme), the deal thesis weakens toward the exact pattern Paradox just wrote down: premium-priced, closed-dev, external, protective founders. At that point it becomes a leadership/greenlight question, not a deal you push through on optimism.

---

## TASK 2 - The hard conversation

*Six months in, the studio wants 12 more months of closed development before any player-facing release. No slides; this is the discussion.*

### My response to the studio
1. **Separate the two things they are conflating.** "More polish" is legitimate. "No EA at all for 12+ months" is a different thing - it is a change of commercial strategy, not a schedule slip. Name that distinction calmly and early.
2. **Lead with their fear, not my authority.** What sits under "we need more time" is usually "EA will tarnish the game, reviews will tank, we will ship half-baked". Address that head-on: the fix is **narrower EA, not later EA.** Ship fewer systems, fully polished core loop, rather than everything at half quality. Smaller scope protects the reviews they are worried about.
3. **Bring the cash curve.** Runway is 9-12 months; 12 more months of closed dev means they run out of money unless we re-open the advance - which means a bigger advance, more recoup, worse terms for them, and more risk for us. EA revenue plus the advance fund the back half *jointly*; remove EA and the whole burden shifts onto a much larger advance they will like far less. Show the curve. This reframes EA from "exposure risk" to "survival plus validation, on better terms".
4. **Use the genre truth, with data.** Grand strategy is the best-suited genre on the market for EA - CK-style audiences expect and reward building in public, and late-game balance is exactly what an EA community helps tune. And the data cuts against waiting: only ~21% of 2026 EA graduates earned more at 1.0 than in their first 30 EA days (GameDiscoverCo). The commercial peak for this kind of title is usually the EA launch itself, not a delayed 1.0 - so "wait for a perfect 1.0" is often leaving the biggest revenue moment on the table. Their protectiveness can be honoured *through* EA (community-driven balance, with them controlling what ships), not against it.
5. **Offer real compromise space.** Narrower-scope EA on roughly the original timeline; or a short, defined slip (3 months, not 12) to a polished vertical-slice EA; with any extension tied to milestone evidence, not vibes.

### Balancing business case vs relationship
- I do not "win" this by pulling rank. The founders being protective was a known, signed-in risk. The relationship is the asset that makes the 5-10 year DLC flywheel possible - torching it to hit a date is value-destructive.
- The goal is the **smallest change that protects the commercial logic** (EA happens, roughly on time) while giving them a **real concession** (scope control, the polish bar, design authority over what is *in* the EA build). Concede on the things that cost little and protect their pride; hold the line on the thing that protects the model.

### What I escalate vs what I own
**I own:**
- The EA-scope renegotiation and the "narrower not later" proposal.
- The cash-curve modelling and walking them through it.
- The relationship management and finding the compromise.
- The success criteria for any agreed slip.

**I escalate:**
- Any change to the advance / recoup structure or total committed capital. That is a P&L and greenlight-committee decision, not mine to grant.
- A fundamental timeline change that pushes ROI past the portfolio's hurdle.
- The strategic-fit question if they genuinely refuse EA. At that point the deal starts to resemble the risk pattern Paradox just wrote down, and leadership needs to know the thesis is bending before more money goes in.

The one-line version for the panel: *protect the EA gate, protect the relationship, and be honest about which decisions are mine and which belong to the people who own the capital.*
