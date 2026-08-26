# Teef - Feature-Set Review + Questions for Fredrik (tech lead)

*Prepared 2026-07-09 for Robert, off TXG's updated brief (29 Jun 2026, GDoc 1HKPJ...D1Z1A). For the final-round prep + the tech scoping call with Fredrik Laurent (Ark Island), who takes Tech Lead. Not client-facing.*

## 1. Scope as it now stands
Four missions, all Soho, ~60 min (down from six / ~90 / Soho+Mayfair). No navigable Mayfair map. System values re-balanced for the shorter arc.

| # | Mission | Time | What it introduces (systems, not just content) |
|---|---|---|---|
| 1 | Fresh Dogs | 5 min | Steal loop (Phase 1 + Phase 2), fencing (Harry the Hand), target-marking (Eddie Eyes), shop + speed upgrade (Danny's Dogs shoes, +60% move) |
| 2 | Sticky Fingers | 10 min | Friction/difficulty step, Strength stat (The Gym), Wanted state, chase-redirect (Razzle), second shop (gloves, speeds Phase 1) |
| 3 | The Spot | 20 min | Base-building (Bed/Safe/Phone ordering, loot-stash protection), open Soho stealing, target-isolation (Laura Lure), reverse-steal Targeting system |
| 4 | The Big Score | 25 min | Notoriety system, crew recruitment + housing economy (Mitts), coordinated multi-agent heist, one-shot rare loot + payout multipliers |

**The headline for the call:** the cut is content + map area. The systems list is essentially unchanged, and M3/M4 (the heavy ones) survived intact.

## 2. Full system + asset inventory (what we're actually building)
**Core gameplay**
1. Steal loop - Phase 1 (approach) + Phase 2 (resolution). The unproven second-to-second core.
2. Wanted / chase - go Wanted on a failed steal; police chase on the Soho map; Razzle redirects a chaser.
3. Eddie Eyes (mark high-value target) and Laura Lure (isolate a target).
4. Targeting (reverse-steal) - player passively targeted ~1-in-5 steals, loses 20% assets, 1-in-3 counter-steal to grab the bot's resources.

**Economy + progression**
5. Cash / fencing / item values / payout multipliers (3x chains, one-shot watch = £2,500, £1,200 haul).
6. Upgrades - move speed (shoes), Phase-1 speed (gloves), Strength (Gym).
7. Shops - Danny's Dogs, GLOVES R US.

**Meta systems**
8. Notoriety - per-steal increase, bigger on capture, exponential chain multiplier, win-rate penalty at high notoriety, slow decay, instant pay-to-clear via Corrupt Copper on the phone. The most interacting system in the game.
9. Base-building - Phone-ordered Bed + Safe, loot protection.
10. Crew - recruit Mitts (own Bed/Phone/Safe, daily wage, net-positive income); Razzle/Laura/Mitts act as watchable agents on the map.
11. Phone - hub for base orders + contacting Corrupt Copper.

**Map + art**
12. Geo-to-3D Soho - recognisable street layout + landmarks, simplified buildings, camera-relative transparency, clear interactable locations.
13. Characters - 10 civilian targets x 2 expressions = 20 portraits; named cast (Harry, Eddie, Razzle, Laura, Mitts, Corrupt Copper, Police, Player). Mixed: some static pop-up 2D, some animated map agents. Plus simplified 3D map characters that must match the 2D designs.
14. UI - explicitly "one of the highest production priorities": objective, risk, rewards, actions, upgrade progress, heavily animated and polished, carries the game's personality.

**Live + instrumentation**
15. Remote config - system values re-balanced via the Sheet-to-Firebase pipeline.
16. Soft-launch - Magnetic SDK (CPI/D3 events), Crashlytics, offline play + local save (carried from the original brief - confirm).

## 3. Review - what it means for a 5-week light-team build
1. **Systems density is the real cost, and it didn't drop.** Our price cut passed through content/map savings; the engineering surface (notoriety, targeting, chase AI, base/crew economy, remote config) is close to the full game. This is exactly why a senior-only team is the right shape, and it's the honest answer to "why cheaper/faster" on the call.
2. **Critical-path items (where the 5 weeks is won or lost):** (a) steal-loop feel, (b) notoriety balancing, (c) chase AI + crew agents pathing on the baked geo map, (d) UI. Everything else is comparatively routine.
3. **UI is a scope-risk flag.** The brief elevates UI to a near-top priority (animated, polished, personality-carrying) covering HUD + shops + phone + base + progression + notoriety readout. Our current plan carries a part-time UI/systems programmer. Worth pressure-testing whether that allocation holds, or whether we need more UI muscle / a dedicated UI artist. Possible re-scope.
4. **Balancing is Phil Black's territory.** Notoriety + economy + targeting probabilities are a big tunable surface. The strong answer is "all Sheet-driven via remote config, tuned live across the runway to end-Q4" - but only if that's actually true, which is a Fredrik question.
5. **Ambiguities to close before we firm the number** (section 5).

## 4. Questions for Fredrik (tech lead) - prioritised
**Top 3 (these decide the 5-week answer):**
1. **Steal loop (Phase 1/2):** what's the real mechanic (input, timing, skill vs RNG), how far does the prototype get us, and how many iteration loops does the core feel realistically need before it's "right"? Can we prove it on device in week 1-2? This is the risk the client named.
2. **Notoriety system:** the exponential chain multiplier + decay + win-rate penalty + pay-to-clear is the most interacting system. Build effort, and is the whole curve remote-config tunable (so balancing happens live, not in the build window)?
3. **UI load:** given the brief makes UI a top-2 priority, is our UI allocation enough, or do we add a dedicated UI programmer/artist? What's your honest UI estimate across HUD + shops + phone + base + notoriety + progression?

**Next tier:**
4. **Reverse-steal Targeting bot:** autonomous map agent or scripted event? Effort for the 1-in-5 trigger / 20% loss / 1-in-3 counter-steal loop.
5. **Chase AI + crew agents on the baked map:** navmesh/pathfinding on geo-derived Soho geometry - any risk? Complexity of police chase + Razzle redirect + watchable Laura/Mitts agents.
6. **Base + crew economy:** scope of base UI/ordering plus the crew-housing + daily-wage + net-income simulation (M4). Bespoke or reusable off the economy layer?
7. **Geo-to-3D pipeline:** confirm bake to stylise to navmesh path, collision, and interactable-location tagging; your week-1 spike plan.
8. **Remote-config surface:** which tunables must be Sheet-driven (economy, notoriety curve, drop/targeting probabilities, upgrade costs)? Config schema + validation effort.
9. **Character/animation count:** 20 portraits + crew, plus simplified 3D matching the 2D, with anim sets (idle/walk/run/steal/panic/chase). Does the AI-assisted pipeline carry this in the window, and what's the 2D-to-3D consistency workflow?
10. **Your read as TL:** does the 5-week plan hold with you leading, and what do you need from Oskar / the bench to make it safe?

## 5. Scope clarifications to send TXG (separate from the Fredrik call)
1. **"Fortis"** - the brief says "Fortis provides one consolidated round of feedback." Confirm who Fortis is (Makosch's studio brand / the reviewer) and that it's genuinely one consolidated round per art pass (good for us - limits revision churn).
2. **Audio** - the updated brief is silent on the 4 licensed tracks + SFX that were in the original. Confirm audio scope and who sources tracks.
3. **Device matrix / min-spec** - not restated in the update. Confirm the Android min-spec for the QA matrix.
4. **Offline + local save** - assumed carried from the original brief; confirm still required.
5. **Kickoff date** - still the open lever that sets when the 5-week clock starts against the fixed end-Q4 launch.

## Note - team change to reflect
Fredrik Laurent (Ark Island co-founder) moves to **Tech Lead** on this project (our sent proposal named Oskar Hansen as TL, Fredrik as gameplay programmer). Update the proposal team section + estimate before anything else goes to TXG. Confirm where Oskar sits now (bench / second programmer / off).
