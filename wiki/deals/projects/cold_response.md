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
