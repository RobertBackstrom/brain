---
type: project_pipeline
project: cold_response
slug: cold_response
owner: BizDev
status: active
updated: 2026-09-16
---

# Cold Response - Pipeline

Defence and professional-training play built on the **Cold Response** FPV drone simulator (Steam app 3831420, Eternal Minds AB, Robin Hofstrom). A NewCo licenses the simulation technology, a co-development partner builds operator-grade UX and UI, and the product is sold into Swedish defence procurement. Part of the consideration to the developer is a co-production of the consumer game. Funding lead comes through Ralph Strandberg.

Project home `cold_response/`, background brief `cold_response/background_2026-09-15.md`, epic `cr-000`.

## Deals
| Deal | Status | Priority | Last activity |
|------|--------|----------|---------------|
| [[ralph-strandberg-network]] | Contacted | high | 2026-09-15 |

## Counterparties
- **Eternal Minds AB** (559527-5719) - licensor. Robin Hofstrom sole director and VD, Monowo AB (Bibbi Wikman) still majority owner on the record. Robert is deputy board member, which is a conflict to manage, not to ignore.
- **Ralph Strandberg / DuoBox Legal KB** - investor lead.
- Co-development partner for UX and UI, unnamed in outward-facing material.

## Commercial Shape (as of 2026-09-15, nothing agreed)
- Licence with a **field-of-use split**: defence, security and professional training to the NewCo, consumer game to Robin.
- **Exclusivity** on the defence field is the central term, and the hardest one, because Robin already has his own defence advisers.
- Consideration: cash plus **co-production of the consumer game**.
- Vehicle: **new company**, not Aurora Punks and not CZP, to keep defence exposure and an external cap table out of the games portfolio.

## Risks
1. Robin's parallel defence track (Abelian Group / Cloke, Fred Addy, Logal Torrence; Mandai Tech success-fee proposal Feb 2026) may already have committed the field.
2. Ownership of Eternal Minds is still 66,66 per cent Monowo on the record, so Robin may not be able to grant alone.
3. Export control is unresolved, see `cr-006`.
4. FMV timelines are long, and the investor case rests on which door we go through, see `cr-008`.

## Route to market (desk research 2026-09-16, `cr-008`)
Full map in `cold_response/fmv_route_map_2026-09-16.md`. Five routes, in the order they should
actually be run.

1. **Innovation procurement and test beds.** The correct first door. Vinnova *Acceleration av
   civil-militara innovationer 2027* is open and closes **2026-10-06 14:00**, up to 1 150 000 SEK,
   up to 100 per cent for a company under five years old, decision 2026-12-15. See `cr-009`.
   FMV **Battle Week** is the recurring demonstration route, first edition weeks 38 and 39 2026,
   round two is the target. FMV also runs **forkommersiell upphandling**, which sits outside
   procurement law and is built for immature suppliers.
2. **The unit route.** Forsvarsmakten trains FPV operators at the **UAS centre in Karlsborg**,
   Ukraine-informed, and has said publicly that simulators will be an important component. Below
   the LUFS direct award limit of 1 200 000 SEK a first order needs no advertising. Small money,
   real reference.
3. **Adjacent civil buyers.** Police, Kustbevakningen, MSB, rescue services, infrastructure.
   LOU direct award limit 700 000 SEK. Fastest revenue, no export control question, needs a build
   without the ballistics and threat modelling.
4. **Under a prime.** Saab Training and Simulation, Combitech, 4C Strategies. 4C is the most
   complementary, their Exonaut is the training management layer, ours is the simulation under it.
   Requires a licence that permits sublicensing or OEM supply, which belongs in `cr-001` now.
5. **Direct FMV procurement.** The destination, not the first door. 18 to 36 months and it needs a
   need owner who already wants it.

**Timeline for the investor case:** first non-dilutive money realistically Q1 2027, first paying
user Q4 2026 to Q2 2027 and probably civil, a real FMV order is a 2028 event.

## Competitive picture (2026-09-16)
Flight fidelity is no longer scarce. **F-Drones Simulator** went free to Ukrainian users on Steam
2026-08-24 and is reported as planned for US military training. **Simtech Solutions' UFDS** claims
over 7 000 operators trained. **RSI Europe** has trained Lithuanian, Belgian and German personnel
since June 2024. What is still scarce, and what these do not have, is the operator layer:
scenario authoring by a non-developer, after-action review, curriculum and measured competence,
multi-seat instructor control, offline deployment, DIS, and Swedish GIS terrain. That is `cr-003`.

## Added risk
5. **Security screening reaches the cap table.** FMV must put a sakerhetsskyddsavtal in place
   under 2 kap. 6 sakerhetsskyddslagen (2018:585) where a contract touches classified information
   or security-sensitive activity, and foreign ownership and ultimate control are what that
   screening examines. Subcontractors with source access are in scope too. Ask Ralph's contact
   where the capital ultimately comes from before a term sheet, not after. Feeds `cr-002`.

## Added risk (2026-09-17)
6. **Grant rules reach the cap table too, and from a second direction.** Vinnova's
   *Acceleration av civil-militara innovationer 2027* caps **konsult- och licenskostnader at 20
   per cent of the budget**, verbatim and without qualifier. Both the licence fee to Eternal Minds
   and the co-development partner sit in that category, so of a 1 000 000 SEK project no more than
   about 200 000 SEK can reach them combined. **The grant is a salary instrument, not a purchasing
   instrument**, and the applicant must have people on payroll from January 2027. Separately, the
   100 per cent startup rate (GBER art. 22) requires a company under five years old and Vinnova's
   own text adds that **the whole group must meet the conditions**. CZP dates from 2019, so a
   NewCo held as a CZP subsidiary loses the startup rate. Fallback is de minimis, also 100 per cent
   but capped at 300 000 EUR over three years and counted per "single undertaking", so the ceiling
   is shared with the parent. Detail and sources:
   `cold_response/vinnova_2027_bolagsval_och_budget_2026-09-17.md`. Feeds `cr-002` and `cr-009`.

## Grant competition, for the investor case
2026's round of the same call had **over 120 applicants and 30 grants**, roughly one in four.
**VCraft Aeronautics** (unmanned aerial systems) and **SCAILAB** (synthetic data for machine
learning) were both funded, which is close to Robin's own description of Eternal Minds as building
"simulation and synthetic data solutions for modern aerial security". The framing that gets through
is autonomous systems with AI supporting, not simulation and training, which is not one of NATO's
nine EDT areas.

## Ralph Strandberg, status 2026-09-17
Cover note with the gated pitch link sent 2026-09-15 16:51 CEST, thread `1a0a5554a33a00d7`.
**Still no reply after two days**, verified live in Gmail 2026-09-17. Ticket due date is
2026-09-22, so this is still inside the normal window. A sixth call question has been added in
`cr-005`: whether an investor would come in before year end at a level that covers two salaries
through 2027, because the Vinnova budget rules make NewCo staffing a first-call topic rather than a
post-term-sheet one.

## Grant landscape corrected and extended (2026-09-18)
Vinnova's **open funded-projects database** (`data.vinnova.se/api/projekt`, 4 869 records) was read
in full rather than the call texts alone. Source:
`cold_response/motpartslage_och_bidragsvagar_2026-09-18.md`.

1. **Correction to the section above.** The accelerator place is **not** a second selection. Step 1
   (round 2025-00980) has 30 companies and step 2, the 150 000 SEK accelerator (round 2025-04031),
   has **the same 30**. (The database does not name the host, so "10 to LEAD" may hold if the programme is split across several hosts; what is disproved is that the accelerator is a second filter.) The Forsvarshogskolan place comes with the grant, which makes the
   third-party-validation argument for `cr-008` stronger, not weaker.
2. **Correction to the framing claim.** Simulation does not disqualify. **Vimotek AB took
   1 000 000 SEK for "Simulering av forsvarscenarion"** in the same round. Lead with autonomous
   systems because that matches the EDT list, but the simulation precedent exists and has a
   diarienummer.
3. **Actual awards** run 829 200 to 1 000 000 SEK with 1 000 000 the modal outcome. Budget to the
   ceiling.
4. **No collision.** Eternal Minds, Monowo, Cold Pixel and Hofstrom appear in **no** funded Vinnova
   project. The database covers granted projects, not pending applications, so it cannot rule out
   an application to this same round, but the broader worry is dead.
5. **New route: a second instrument attached to FMV Battle Week.** Round **2026-00496**, *Stod till
   sma och medelstora foretag for test och evaluering*, **17 grants in 2026** at 220 000 to
   500 000 SEK, two of them naming FMV Battle Week outright. **De minimis, up to 100 per cent**,
   eligible cost is **only bought-in access to test infrastructure**, and the application requires
   **a quote from the chosen test facility**. Closed 2026-05-20; expect a spring 2027 edition.
   Because the basis is de minimis, neither the five-year nor the group condition applies, so a CZP
   subsidiary could use this one without penalty. **Action that needs no vehicle and no decision
   from Robert: establish contact with a test infrastructure this autumn**, since the quote is an
   application requirement in May.
6. **Neither instrument pays the licence fee to Eternal Minds.** The acceleration call caps external
   cost at 20 per cent; the test call funds only infrastructure access. The cash component of the
   licence has to come from the investor or a first order. Feeds `cr-001`.

## Counterparty verified against primary source (2026-09-18)
Eternal Minds AB 559527-5719, per allabolag today: turnover 2025 **1 258 tkr**, result **-37 tkr**,
share capital 25 000, **three employees** (our record said two), registered for VAT, F-skatt and
**employer contributions**, address moved from Bibbi's Bondegatan 31 in Stockholm to **c/o Hofstrom,
Roslagsgatan 20 b, Norrtalje**. **Robert is still on the public register as suppleant**, so the
ABL 8:23 point in `cr-002` is a current, publicly checkable fact. Monowo AB 559207-4933: turnover 0,
profit 989 tkr, i.e. a holding profile.

Two consequences for `cr-001`. The counterparty's thin finances make **source-code escrow a
reasonable mutual protection rather than an insult**, and it should be framed that way. And
**Eternal Minds holds a claim in the WLBS bankruptcy estate** (Robert to Bibbi 2026-07-31, thread
`19f22114e38fd395`) which says nothing about assets having moved but makes the source-tree question
in `cr-007` a concrete diligence item.

**Unresolved and not resolvable from the desk:** our own sources disagree on whether the majority
shareholder is **Bibbi personally** or **Monowo AB**. The share register is not public.

## Relationship note: the path to the majority shareholder is warm
Robert did a free investment assessment for Cold Pixel this summer (`cpx-001`) and is currently
running the bankruptcy-claim question for her companies, with a written "I'll come back when I hear"
from July that appears unfulfilled. **Open the ownership question with that reply, not with a request
for licence consent.** And do not run it through Robin alone: he holds signing authority and can bind
the company, but an exclusive licence over its only asset is not something the majority holder should
hear about afterwards.

## Ralph Strandberg, status 2026-09-18
Still **no reply**, verified live in Gmail the same turn: thread `1a0a5554a33a00d7`, a single message,
sent 2026-09-15 16:51 CEST. Three days. `cr-005` is due 2026-09-22.

## The route to market has a price tag (2026-09-19)
Primary sources read in full: the Vinnova call text for round 2026-00496 (PDF via the file API),
the full register of application rounds under the programme, and **FMV's own map of the Swedish
defence development landscape**. Detail in `cold_response/testinfrastruktur_och_dorrar_2026-09-19.md`.

**FMV Battle Week costs 500 000 to 1 000 000 SEK excl. VAT per submitted solution**, set by FMV
after they have assessed the proposals. The Vinnova grant covers "a subset of the registration fee",
capped at 500 000 SEK, and FMV themselves call it an infrastructure voucher. **The door is never
free, even with a full voucher.** Odds on the first challenge: 32 applicants, 11 selected. The
sequence is inverted: you get the place first, the fee is set then, and only then can the place be
evidenced in a grant application. Figures come from a search index rendering of fmv.se, which
returns 403 to machine fetch, and need a human with a browser before they go into a budget.

**Correction to `cr-010`.** The call gives two alternative formal requirements: a quote from a
technical infrastructure **or** notice of a place at Battle Week. And "technical infrastructure"
explicitly includes **support services** with a "broad approach" - two of the 17 grants bought no
range time at all (Scailab bought advisory from Knightec, Synclair Vision bought a security
evaluation of software). **A pure software evaluation has already been funded under this call**,
though 15 of 17 tested hardware and both software projects bought a bounded security or robustness
evaluation rather than functional assessment. Foreign infrastructure qualifies (two bought testing
at Millog in Finland).

**The simulator matches none of the six priority areas directly.** All six are capability areas and
training is not one of them. The two framings that carry: counter-UAS operator training under
"air and missile defence, including protection against drones", and sensor-operator training under
"improved and sustained situational awareness".

**Candidate infrastructures, from FMV's own map:** FOI is the strongest counterparty for the quote
(state agency, commissioned research, Battle Week co-organiser, holds the specific competence in
evaluating simulation-based training). Drone Center Sweden / Testbädd UAV Västervik (RISE, 2 400 km²
approved test area, commercial operation) is second, for comparative flight of the same manoeuvre
real and simulated, which ties to `cr-007`. FM UAS-centrum Karlsborg is the sharpest counterparty
for military relevance but is a need-owner and cannot issue the quote.

**FOI already described the gap, for the Armed Forces.** FOI-R--3957--SE surveyed 15 Swedish
simulator facilities: many have no stated pedagogical model, assessment is qualitative, the
quantitative measures the simulator logs "cannot be used" for resource reasons, and group behaviour
is not measured for lack of tools. That is the operator layer in `cr-003` almost verbatim. **The
report is from 2014** - use it as the origin of a question, never as a statement about today.

## ISP screens the investment, not only the product (2026-09-19)
Act (2023:560) on the screening of foreign direct investments, in force 1 December 2023 with ISP as
the screening authority: an investment in protected activity that gives the investor a certain
influence must be notified, and can be prohibited or made conditional. FMV lists "you receive
external financing or investment for your innovations" as an ISP matter. **If the capital behind
Ralph's contact is ultimately foreign, the investment in the NewCo may be notifiable regardless of
whether the simulator is classified as war materiel.** Another reason to ask where the capital
ultimately comes from before a term sheet. Logged on `cr-006`; layman's reading, needs a specialist.

FMV's own glossary also names **military software** as an example of war materiel, turning on
"designed or modified for military use" - which argues directly for the forked codebase in `cr-006`.

## Ralph Strandberg, status 2026-09-19
Still **no reply**, verified live in Gmail the same turn: thread `1a0a5554a33a00d7`, a single
message, sent 2026-09-15 16:51 CEST. Four days. `cr-005` is due 2026-09-22.
