---
to: rosemary@lokhorst.com, rosemary@badass-studios.com
cc: dieter@badass-studios.com
subject: Re: Excel — merged file + sanity check + scenarios + 7-Q answers
in-reply-to: Rosy's 2026-05-09 "Excel" mail (thread 19e0cf3367b23b0a)
status: draft (pending Robert review)
---

Hi Rosy (cc Dieter),

## TL;DR

- **Direction:** Heard you on Saturday — we ship your 90%-done shape with your revenue numbers. v3 modular spec parked as a "next step" exploration only.
- **Merged file (link below):** built on your May 9 file as the base. Yellow-marked every cell we touched.
- **Executed in file:** Direct Cost lump-it (Early Adopters, per your own pre-existing note); Onsite Services flat 30% (your Q4); Staff fixes from Apr 27 v2 that hadn't propagated (6 renames + 8 hire-date flips); 8 new Assumption rows covering all 7 of your discussion points; typo + reference fixes in your existing Assumptions text; new Scenarios tab with 70 / 120 % bands per Dieter.
- **Needs your decision (two items):**
  - (a) **Potential P&L bug** — Row 14 ("Customization & Onsite Services") pulls from `New Revenue!R40` which is `=R38` only. Customization Revenue R36 (~£18M over 5y) appears missing from the P&L. Bug or intentional? Don't want to treat £353M baseline as canonical until confirmed.
  - (b) **K column escalation** — labelled "Rev Increase /Quarter" but formulas apply it as 1% per *year*. Material to 5-year totals.
- **Open questions for you:** Dieter's "ramp of Ben?" comment at Staff A167; meaning of 5 year P&L B5 distribution multipliers (we have a reading, want to confirm).
- **Coming tonight:** v2-shape org chart in a follow-up mail.
- **For Monday:** what time works for the Peter + Ben walkthrough?

---

## Merged file

https://drive.google.com/file/d/18dqAg2zloBNjqAhbvTCx6bPDZPJ9cFhc/view

Started from your May 9 file as the base. Every cell we changed has a yellow fill so you can spot edits at a glance. Threaded comments, embedded images, drawings, charts all preserved.

## What changed (by sheet)

### Staff — 14 cells + 1 open question

Named-staff title alignment (6 cells):

1. **E7** — Marco location: US → UK
2. **A8** — Sezar: "Unreal Eng Developer" → "UE Developer (Intermediate)" (per your role doc, intermediate not senior)
3. **A23** — John Liou: full title + Jon → John
4. **A79** — Alex: "Creative Director from 2026" → "CCO Alex Sangwin-Skillen"
5. **A86** — Adam: "Partnership Manager" → "eSports Community & Partner Manager" (per your Apr 27 note that Adam is more sales)
6. **A99** — Michiel: "Business Developement/PAM" → "BusDev Manager" (spelling + title)

Hire-date flips for open Platform / Customisation UK roles (8 cells, Empl't % NEW columns):

7. **O15** — Tech Artist Platform UK — Q3-26 (Como wrap optimisation)
8. **R12** — Senior AI Engineer — Q4-26 (AP covers Q3-26 interim)
9. **R13** — Release Manager — Q4-26 (first 1st-party CERT push)
10. **R14** — DevOps Engineer — Q4-26
11. **R10** — Producer / Tech Lead — Q4-26 (AP coverage from now)
12. **O43** — Tech Producer AR/VR Broadcast — Q3-26 (E1 broadcast cycle)
13. **O44** — Technical Artist Customisation UK — Q3-26 (broadcast crunch)
14. **O45** — Developer Customisation UK — Q3-26 (urgent: Fortnite Monaco Verse/UEFN dev)

DISCUSS block at A1005:

15. Should we spell out row 45 as "Verse / UEFN Developer" so investors see the urgent hire clearly, or keep generic "Developer" so the slot flexes to other engine work later?

What we explicitly **did NOT** do:

16. We did not move Marco / Jake from Platform UK to Customisation UK. Your Saturday note — *"a lot of what we do currently should be going into components for the platform and not be seen as customer project"* — was clear; keeping them on Platform UK organisationally makes the investor story cleaner.

### Early Adopters — Direct Cost lump-it (executed)

17. Picked up your own Apr-vintage note on the Direct Cost block (E58-E60, yellow): *"I think we can just lump it all in one set of % as assumption."* Six 5% categories (Data, Licenses, Hardware, Broadcast, Travel, other) consolidated into a single 30% line at B58. Same math, single number for investor narrative.
18. Your original comment is preserved in E59-E60. Added E61 with execution note for traceability. Trivial to revert if you decide otherwise.

### New Revenue — Q4 onsite services + K4 flag (executed) + B70 pointer

19. **Q4 executed:** R38 formula changed from `(R25+R33)×R39` to `R33×R39`. Onsite Services now = % of Onsite Module Revenue only (rows 28 + 30), not % of total license revenue. R39 row collapsed from 35→10% taper to flat 30%. Logic: 30% holds for broadcast (your read) AND for sim (your B67 math: 25 GBP/hr × 250/day → 30%). One number, defensible. Cells D38:W38 + D39:W39 all yellow-marked.
20. **K4 flagged:** Column K (cells K5-K11) is labelled "Rev Increase /Quarter at 1%". The formulas use `(1+K)^row16_value`, where row 16 increments by year (1,1,1,1, 2,2,2,2, 3,3,3,3...). So the 1% is applied as *annual*, not quarterly. Over 5 years: ~5% total escalation, not the ~22% the label implies. Material to baseline revenue. Need your call: (a) fix label to match math, or (b) fix math to match label. Flagged in-file at B71-B72.
21. **B70 pointer:** added one-line note below your B60-B69 discussion block pointing to Assumptions tab rows 12-19 (where decisions are encoded) and this email (for reasoning).

### Assumptions tab — 8 new rows + 4 typo fixes + ref fixes

Typo fixes (existing cells, yellow fill + bold on corrected word — Excel xlsx doesn't support per-word background highlight, bold is the closest):

22. A8: *tickeeting* → **ticketing**, *perveiling* → **prevailing**
23. A9: *tehn* → **then**
24. A10: *duch* → **such**

Reference fixes:

25. C6: ref was "19-20" (Yearly Gaming rows) but the text is about Fan Engagement which lives at rows 21-22 → corrected.
26. B3:B10: TAB column changed from "Revenue" → "New Revenue" (leftover from a sheet rename).

New assumption rows (12-19) covering your 7 discussion points + 2 model decisions we executed:

27. Row 12 — Customer Acquisition Ramp
28. Row 13 — Sim Module Post-Early-Adopters
29. Row 14 — Uniform Revshare Across Sports
30. Row 15 — Entertainment Template
31. Row 16 — Onsite Services Flat 30%
32. Row 17 — Gaming Customisations Bundled in Revshare
33. Row 18 — Direct Cost Lump Assumption
34. Row 19 — Rev Escalation Column K (flagged for confirmation)

### Scenarios — new sheet

35. Per Dieter's Sunday note: Baseline / 70% / 120% sensitivity bands around your Total Revenues. Live formulas reference `'New Revenue'!Y52:AD52`, so the table stays in sync if you tweak any input. Pure what-if read — does NOT alter your New Revenue model.

35a. **Staff-side 70/120 NOT yet modelled.** Dieter's Sunday ask specifically mentioned staff calculations at 70/120, not just revenue. Building that requires defining (a) which hires flex with revenue (Customisation team scales? Platform team holds?) and (b) timing rule (delay vs add hire). Flagged in-file at Scenarios A21-A22. Worth 30 minutes in the Monday walkthrough — happy to build it Tuesday once the flex rules are aligned.

### 5 year P&L sheet — three things to flag

35b. **POTENTIAL BUG — needs your call.** Row 14 ("Customization & Onsite Services") pulls from `'New Revenue'!*40` (Total Customization Revenue). The row-40 formula in New Revenue is `=R38` only (Onsite Services Revenue). That means R36 — your AR/VR/Broadcast Customization Revenue line, ~£18M cumulative over 5 years per the current numbers — does NOT flow into the P&L. Either:
- (i) **Bug** — R40 should be `=R36+R38`. P&L is currently understating revenue by ~£18M cumulative.
- (ii) **Intentional** — R40 was meant to be just services, the row label "Total Customization Revenue" is misleading, and AR/VR customization is captured elsewhere.

We did not change R40 — this is a CEO-level financial decision. Need your confirmation before we treat the £353M 5-year baseline as canonical for investor numbers.

35c. **B5 distribution multipliers (your "I don't understand this" threaded comment).** Row 5 holds quarterly distribution multipliers used to spread the annual Early Adopters revenue across quarters: 10% / 20% / 30% / 40% across the 2026 quarters (a ramp-up year) then flat 25% per quarter every year after (sums to 1.0 per year). Multiplied against the annual Early Adopters figure from row 6. Annotated in-file at A1100 so the threaded comment can be retired. Confirm reading matches your intent.

35d. **Dieter's "ramp of Ben?" comment (Staff A167).** Ben Jeffreys is currently set at M9=1 (100% Junior AR Designer from Q3-2026, no future changes). Dieter's question reads as: should Ben have a progression ramp (Junior → Mid → Senior with corresponding salary bumps over the 5-year horizon), or stay flat in role + salary? Need your call. Worth treating as a template question — same applies to other junior hires we may bring on (UEFN dev, 2D Artist, etc.).

## Our take on your 7 discussion points (B60-B69)

These are recommendations, not decisions — mgmt group calls. For investor purposes we'd run with these positions:

36. **Q1 (uniform revshare):** Yes, simplify. Per-sport carve-outs explode the model with marginal accuracy gain. Per-sport variance is already captured via the B44 customer-revenue curve.
37. **Q2 (sim module post-early-adopters):** Drop standalone Sim module for new customers. Bundle into Gaming License (in-game) + Fan Engagement Module (yearly access, used at events and year-round). E1 keeps standalone Sim line for historical reasons.
38. **Q3 (Entertainment template):** Fold into Fan Engagement License count for now. Break out as separate row when there's a confirmed Entertainment-specific price point that differs from £24k/yr sports band.
39. **Q4a (onsite services basis):** Switch to flat 30% of onsite modules. Executed in file (see point 19).
40. **Q4b (sim onsite pricing rationality):** Implicit in Q4a — 30% now holds across broadcast AND sim. Your £25/hr × 250/day math is consistent.
41. **Q4c (gaming customisations in revshare):** Yes, agreed. Gaming customisations (in-game shop, packages, merch, branded ticketing / sponsorship, live racing component) are bundled into the 30% revshare. No separate customisation line for gaming.
42. **B68 ("fine with either, want someone to walk the logic"):** Done — this mail is that walk-through. Override anything you disagree with.

## One thing to pre-arm for investors — the customer-count number

43. **Important distinction:** The yellow row B34 ("INTERNAL total cumulative customers") in New Revenue is *not* a unique-customer count. It's the running sum of Platform license counts across quarters — a customer active for 4 quarters gets counted 4 times. End value 143 = 143 customer-quarter activations. Useful as a denominator for event-count derivation; misleading for an investor narrative.
44. **Unique customer count by Q2-2031:** row B18 = 20. That's the defensible number.
45. **Acquisition story for those 20:** ~10 named in Dieter's prospect comments today (E1, Kiro, Racing Unleashed, PWC Museum, CIS Lunar, Aurora, Nürburgring, PWC Saudi, PWC eSports, PWC Falcons Club). Remaining ~10 from (a) E1 spawning lookalike electric/racing series, (b) PWC tier expansion across regions and categories, (c) net-new Entertainment / non-racing customers.
46. **Recommendation for the deck / pitch:** lead with "by Year 5 we'll have ~20 platform-license customers paying recurring annual fees", not "143 customers". Investors will pressure-test the 20 number anyway — having the 3-source breakdown ready defuses the question.

## Org chart

47. v2-shape org chart in a separate mail tonight. Platform vs Customisation cost-center split, current named staff + open hires, all aligned with this file. v3 modular spec stays on my side as a personal exploration only.

## Monday

48. What time works for the Peter + Ben walkthrough? I can flex around your day.

Best,
Robert
