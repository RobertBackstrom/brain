---
title: Disposable Corps - rated backlog from the design and UX evaluation
project: dsc
status: internal source of truth for the Jira board
created: 2026-09-15
author: Assistant (GameDev agent), for Robert Bäckström
source: drafts/jesper_rift_design_ux_evaluation_2026-09-15.md (Jesper Staafjord, Rift, Sept 2026) plus build_feedback.md (Robert's own sessions)
---

# Rated backlog

Jesper's evaluation contains roughly 120 recommendations in flat bullet form, with no severity, no
sizing and no order. **AP does the rating, he does not get sent back to write more** (Robert,
2026-09-15). This file is the rating. The Jira board is generated from it.

## The scale

**Severity**
- `blocks` - a player cannot learn or play the game, or the systems reward the wrong behaviour.
- `degrades` - the player can get through it, but the round is worse or slower than it should be.
- `polish` - visible quality, no functional cost.

**Effort** is deliberately crude, since we have the public demo and no repository: `hours`, `days`,
`weeks`, `weeks+`. Every number is a range until the review month opens the repo.

**Gate** maps to the twelve month plan already sold to LUG.
- `P0` - review and fix build, months 1 to 2.
- `P1` - into the loop work, must be in the build before **public playtest 1, month 4**.
- `P2` - content and polish window, before **Early Access, month 10**.
- `P3` - after EA, or a decision at the month 8 playtest. Not budgeted in the 1 860 000.

## Revised 2026-09-15, after Jesper's feedback and Robert's decision

The first version of this backlog opened with eleven small fixes, six of them inside the tutorial.
**Jesper's response: he would not patch the onboarding at all, he would scrap it and build a new
one.** He is right, and it makes the original P0 partly wrong: six of those eleven were properties of
the tutorial as it is built, so they disappear when it is replaced. Proposing that the team polish
them is proposing that they pay twice, which is exactly what a technical founder notices.

**Robert went further (Slack, 2026-09-15): rebuild the onboarding, take the public demo down while
that happens, and drop the small fixes.** Taking the demo down answers the objection that a rebuild
leaves the only public face of the game broken for weeks. Three quiet months cost less than three
months of bad first impressions, and the month 4 playtest is a better reintroduction than a broken
demo is a placeholder. The demo belongs to Armoured Dudes, so it is a recommendation, not a decision
we make.

**Cost of the demo coming down:** it stops the wishlist inflow, and wishlists at launch are the number
the whole recoup model rests on (40 000 is where the deferral is recovered at 2,5x, against 2 741
followers today). The counter-argument is stronger: a player who meets the current tutorial is a
wishlist lost rather than gained, so the inflow being stopped is worth less than it looks.

## P0, the first two months

Four items. Two decisions, one work package and one fix.

| Jira | Item | Sev | Effort |
|---|---|---|---|
| DSC-9 | **Decision: pick the game direction.** Recommendation: the sandbox direction, on commercial grounds. The game already looks and moves that way so it is cheaper to finish, wonkiness becomes a feature rather than a defect to polish out, and the simulation shelf is crowded with titles that have had years of polish. Settles player health, time to kill, vehicle visibility and the tone of the onboarding, so it comes before the rebuild starts | blocks | days |
| DSC-74 | **Decision: take the public demo down** for the duration of the rebuild, publish it again when the new onboarding is in. Reversible. Theirs to take, ours to recommend | blocks | hours |
| DSC-73 | **Rebuild the onboarding from scratch.** Absorbs twenty of the original items, six from the old P0 and fourteen from P1, which are relabelled `absorbed-by-onboarding-rebuild` and now serve as acceptance criteria for the new tutorial | blocks | weeks |
| DSC-32 | **The economy rewards dying near the enemy point.** The one finding that is neither small nor absorbed by the rebuild. Rebalance around time spent and enemies killed rather than proximity to the flag | blocks | days |

**Demoted to `hygiene`, not scheduled:** selling the hammer (DSC-12), respawn versus Deploy wording
(DSC-15), the Purchase button's enabled state (DSC-54), placeholder data in the lobby (DSC-65). Real,
small, outside the tutorial, and not worth a work package. Closed when someone is in that system for
another reason.

## The empty-game caveat, added 2026-09-15

There are not enough players to fill a 5v5 match today (Robert). The evaluation was therefore made
against bots, and so was every other source we have: the publisher's fault list and Robert's own
sessions. **Nobody has seen this game populated, the developers included.**

That does not weaken the onboarding, economy, menu, vehicle or HUD findings, which are all visible
with one player. It does suspend a specific set: **map too large, too much walking, the map reads as
empty, rounds are repetitive, NPC behaviour is static.** Those are exactly what a solo bot session
produces whether or not they are true of a populated match, and a map built for ten reads as empty
with one.

Those items carry the label `needs-populated-playtest` on the board. **Do not commit map work on
them.** The first evidence arrives at playtest 1, which means playtest 1 has a second job beyond
testing the new onboarding: it is the first populated match this project has ever had. It has to be
scheduled for concurrency, a booked window with enough people in the same match at the same time, not
a week-long open test where the participants never meet.

## P1, before public playtest 1 (month 4)

Eighteen items after the fourteen onboarding items moved into the rebuild. Playtest 1 is the first
outside evidence the UX work landed, so anything that decides whether a new player understands the
game belongs here.

| # | Item | Sev | Effort | Area |
|---|---|---|---|---|
| 12 | HUD objective element showing only the current objective, taught as part of the tutorial | blocks | days | HUD |
| 13 | Bespoke small tutorial map, instead of running onboarding on the full size map | blocks | weeks | Onboarding |
| 14 | Gate tutorial movement, or add a reset that returns the player who wanders off | degrades | days | Onboarding |
| 15 | Split basic and advanced tutorials (economy, construction strategy, squad control, phases) | degrades | weeks | Onboarding |
| 16 | Re-sequence the tutorial: buy the weapon, then shooting, then shovel, then hammer, then building | degrades | days | Onboarding |
| 17 | Remove interactions irrelevant to the current step (buying, building, squad) | degrades | days | Onboarding |
| 18 | Menu highlights, arrows and guiding prompts the first time each menu opens | degrades | days | Onboarding |
| 19 | Reduce the three scripted deaths, give the remaining ones context and feedback | degrades | days | Onboarding |
| 20 | Rebuild the defense phase step: small zone, build defences, man the gun, small enemy wave | degrades | weeks | Onboarding |
| 21 | Flag capture becomes its own step, with an actual capture performed | degrades | days | Onboarding |
| 22 | Teach squad control properly: move and form up, plus why you would use it | degrades | days | Squad and AI |
| 23 | Split the dense multi-objective steps (equipment, artillery use) into single-objective steps | degrades | days | Onboarding |
| 24 | Player health, avoid one shot kills so there is time to react **(gated on the identity decision)** | blocks | days | Combat |
| 25 | Build placement snapping to valid positions and world geometry | degrades | days | Build and buy |
| 26 | Stay in build mode until the player exits, instead of resetting after every purchase | degrades | hours | Build and buy |
| 27 | Build camera: stop forcing the player to aim at the ground, or move the object pivot | degrades | days | Build and buy |
| 28 | Digging: ground indicator showing where the dig will happen | degrades | hours | Build and buy |
| 29 | "Construct" and "Operate" prompts compete for the same space, and Operate has no disabled state | degrades | days | Build and buy |
| 30 | Building menu: colour cost by affordability, fade what cannot be bought | degrades | hours | Build and buy |
| 31 | Building menu: group into categories and sort by cost | degrades | hours | Build and buy |
| 32 | Building menu: one line of description per building, saying what it is for | degrades | hours | Build and buy |
| 33 | Unify the two purchase grammars (buildings click-then-place, equipment slot-item-confirm) | degrades | days | Build and buy |
| 34 | Store: make weapon slots and utility slots visually distinct, in shop and on the player | degrades | hours | Build and buy |
| 35 | Map icons: the player is marked with the same red as enemy spawns, and squad, spawn and vehicle circles look identical | degrades | days | HUD |
| 36 | Control points: explain how they are captured and what holding one gives you | degrades | days | Round |
| 37 | Tanks: enter with windows open by default, or fix the closed-window camera | degrades | days | Vehicles |
| 38 | Tank aiming: crosshair does not match the shell trajectory | degrades | days | Vehicles |
| 39 | Towing: two fixed interaction options (operate and tow) instead of an aim-dependent point | degrades | days | Vehicles |
| 40 | Repair: show which part of the vehicle is damaged | degrades | days | Vehicles |
| 41 | Sandbag step teaches placement but not purpose, explain what defences are for | degrades | hours | Onboarding |

## P2, before Early Access (month 10)

The round itself. Bigger, and this is where the budget gets spent.

| # | Item | Sev | Effort | Area |
|---|---|---|---|---|
| 42 | Reduce map size, or concentrate the control points, so less of the round is walking | degrades | weeks | Round |
| 43 | Transport vehicles to move players and squads between points | degrades | weeks | Round |
| 44 | Landscape features that support different play: high ground, water, cover, forest, buildings | degrades | weeks | Round |
| 45 | Pre-placed military structures that player buildings can extend | degrades | weeks | Round |
| 46 | Battlefield props so areas are visually distinct and navigable | polish | weeks | Round |
| 47 | Phase transition back to prepare is clunky, add redeploy or shorten the distances | degrades | days | Round |
| 48 | Squad pathing around complex terrain and buildings | degrades | weeks | Squad and AI |
| 49 | NPC engagement ranges make tactics hard to apply | degrades | days | Squad and AI |
| 50 | NPC movement and combat is static and predictable, rounds feel repetitive | degrades | weeks | Squad and AI |
| 51 | NPCs make poor use of buildings, vehicles and artillery | degrades | weeks | Squad and AI |
| 52 | No squad commands for operating vehicles | degrades | weeks | Squad and AI |
| 53 | Rebalance rewards: kills inside the enemy point, time held, equipment destroyed, friendly NPCs inside, building near it | degrades | weeks | Economy |
| 54 | Money arrives too slowly to change the round | degrades | days | Economy |
| 55 | NPC count never changes over a round | degrades | weeks | Round |
| 56 | Artillery handling is floaty, and collisions with world objects need polish | polish | days | Vehicles |
| 57 | Give a captured point weight beyond immediately defending it | degrades | days | Round |

## P3, after Early Access or decided at the month 8 playtest

**Not budgeted inside the 1 860 000, and not to be shown to LUG's financiers as part of the plan.**
Items 58 to 61 are one coherent proposal, and they are the largest idea in the evaluation.

| # | Item | Sev | Effort | Area |
|---|---|---|---|---|
| 58 | Round progression redesign: start small (few soldiers, little money, tight points) and scale the conflict outward as points are captured | n/a | weeks+ | Round |
| 59 | Grow the army during a round, automatically or through recruitment buildings | n/a | weeks+ | Round |
| 60 | Soldier upgrades and abilities (wire cutting, driving, new weapons, grenades) | n/a | weeks+ | Squad and AI |
| 61 | A counter mechanic for every building, vehicle and strategic system | n/a | weeks+ | Round |

## How to read the shape of this

1. **The first two months are two decisions and one rebuild**, not a list of small work. That is a
   better story than the original eleven items, because it says we will not spend their money
   polishing something that is going to be replaced.
2. **The rebuild is the whole first block.** It absorbs twenty separate findings, which is why the
   detailed observations are worth more as acceptance criteria than as tickets.
3. **P1 is where the seat earns**, eighteen items, mostly days, and it is the difference between
   playtest 1 producing usable retention numbers and producing another round of "players did not know
   what to do".
4. **P2 is where the money goes**, and several items there (map size, NPC behaviour, economy
   rebalance) have costs nobody can know without the repository.
5. **P3 is not in the plan.** If LUG's financiers see it without that label, the budget reads as
   understated.

## What is deliberately not in this list

1. Anything requiring the repository to even scope: netcode, hosting, dedicated servers,
   performance. Out of scope for a design evaluation made from the public demo, and still a written
   deliverable of the review month.
2. Comparables. Nobody has checked these recommendations against what neighbouring trench and squad
   shooters do, and for the combat and map items that check is cheap and worth doing before month 2.
3. Anything derived from telemetry, because we have none. The two developer playtests and the demo's
   own numbers are in the LUG ask and still unsent.
