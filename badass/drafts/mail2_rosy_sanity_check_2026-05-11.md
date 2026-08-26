---
to: rosemary@lokhorst.com, rosemary@badass-studios.com
cc: dieter@badass-studios.com
subject: Re: Excel — sanity check + answers to your 7 Qs
in-reply-to: Rosy's 2026-05-09 "Excel" mail (thread 19e0cf3367b23b0a)
status: draft
---

Hi Rosy (cc Dieter),

Walked through the revenue sheet end to end. Numbers check internally and the discount/escalation taper is reasonable. One structural flag below, then proposed answers to your 7 questions in cell-level terms so we can land them straight into the file Monday.

## One flag — customer acquisition mechanism

The yellow row (B34) goes from 2 customers in Q3-2026 to 143 by Q2-2031. Dieter's comments on Early Adopters (I50/J50/K50/L50) name ~10 customers across 2025-2028 (E1, Kiro, Racing Unleashed, PWC Museum, CIS Lunar, Aurora, Nürburgring, PWC Saudi, PWC eSports, PWC Falcons Club). The jump from ~10 named to 143 over five years is the single biggest assumption in the curve — investors will go straight at it.

Worth us articulating the mechanism explicitly in Assumptions:
- How much is E1 spawning lookalike series (other electric/racing leagues)?
- How much is PWC tier expansion (Falcons Club model replicated)?
- How much is net-new categories (Entertainment, F1-adjacent)?

If we put a sentence per source against the customer ramp, the number defends itself. Right now it sits naked.

## Answers to your 7 questions (cell-level)

**Q1 — All sports same revshare → yes, simplify.**
No cell change needed; R45 (Percentage of Customer Revenue) is already a flat 30%. Add to Assumptions: *"Revenue share is uniform across sports (30% of gaming customer revenue). Per-sport variance is captured via the Customer Revenue size curve (B44), not via separate %."*

**Q2 — E1 sim module → drop post-early-adopters, bundle into Gaming License + Fan Engagement.**
Cell impact: zero in New Revenue (sim already isn't a line). Early Adopters sheet keeps sim line for E1 historical. Add to Assumptions: *"Post-2026 customers access sim experience via Gaming License (in-game) + Fan Engagement Module (onsite). Standalone Sim module is grandfathered for early adopters only."*

**Q3 — Entertainment template → fan-engagement-only, no gaming license.**
Two options:
- (a) Keep modeling simple — fold Entertainment count into B22 (Yearly Module Fan Engagement License) without a separate split. Note in Assumptions that ~X% of Fan Engagement customers are Entertainment-only.
- (b) Add a separate row group below R22 for "Entertainment customers" with its own count + own pricing if it differs.
My preference: (a) until we have a price-point for Entertainment that's clearly different from sports fan engagement (£24k/yr). Switch to (b) once we do.

**Q4 — Onsite services basis → switch to % of onsite modules, flat 30%.**
Cell change in New Revenue: replace R38 (Onsite Services Revenue) formula so it's `(R28 + R30) × 0.30` per quarter, not derived from R36 customization × R39. Then R39 collapses to a single flat 30% row.
Logic: 30% holds across broadcast (your read on the existing services) and sim (your niece's 25 GBP/hr → 250/day, ~30%). Consistent → defensible to investors. The current double-derivation (% of license × another %) is confusing without simplifying anything.

**Q5 — Gaming customizations covered by revshare → yes, agreed.**
No cell change. Add to Assumptions: *"Gaming customizations (in-game shop, package design, merchandising, branded ticketing/sponsorship integration) are bundled into the 30% revenue share with the customer. No separate customization line for gaming."*

**Q6 — Sanity-check the logic → done, above + below.**
Drivers + math + escalation/discount tapers look right. Question is the customer ramp (top flag) and the per-customer revenue assumption (B44 hitting £12M/customer/quarter by Q2-2031). If you have a Formula 1-equivalent reference for that number it's worth citing — F1 reportedly does $2-3B revenue across 23 races, so £12M/quarter per high-tier customer is in the right zip code for a top-tier league, but it shouldn't be the average.

**Q7 — Put decisions in Assumptions → I'll draft.**
I'll write the Assumptions paragraph for each of Q1-Q5 once we've sanity-checked on Monday and bring it to Tuesday's standup. Easier to land in one pass than piecemeal.

## Staff comments

You noted you left yesterday's staff comments untouched — those are still mine to close. Dieter and I synced Sat 17:00, I'll wrap and get back to you before Monday.

Talk Monday — let me know the time that works.

Best,
Robert
