---
title: Disposable Corps - initial UX assessment and work brief
project: dsc
status: draft
created: 2026-09-07
author: Assistant (game design + pm), for Robert Bäckström
audience: Jesper Staafjord (Rift Gaming) as prospective UX owner. Written to leave AP. Contains no assessment of people, no internal cost reasoning, no other AP client names.
---

# Disposable Corps: initial UX assessment and work brief

This is the UX side of the Disposable Corps production plan, written for the designer who would own it. It is reconstructed from the public demo, the developer's own playtest notes, the store page and Robert's play sessions. Nobody on our side has had repo, build pipeline or telemetry access yet. Treat every claim below as a hypothesis to be confirmed in the review month, not as a finding from an internal review. Section 7 lists what we do not know.

Short version: the game has more systems than it has readability. The onboarding that should carry a player across that gap is broken in the public build, not merely rough. The work is one real design pass (round-state HUD, squad orders, first-round guidance) plus a set of hygiene fixes the development team can close on their own once someone has written them down.

## Evidence base

What this document rests on, so you can weigh it.

1. **The developer's own control lists.** September 2025 playtest post: `B` buy weapons and items, `I` build fortifications, `M` open map and recruit AI soldiers at spawn icons, `T` open the command menu to issue orders to your AI squad. December 2025 "Refactoring Update" post: `1-9` weapons, `P` first/third person, `T` open squad command, `E` interaction, `B` open building panel, `M` open map, arrow keys to switch vehicle seats. Note the change: `I` is gone and there is no longer a separate buy key. Either buying was folded into the building panel or it moved somewhere the post does not list. Which of the two maps is live in the public demo is not confirmed.
2. **The December refactor notes.** Camera rebuilt on a physical camera system, player movement reworked, AI "reworked to handle more units and complex tasks", NPCs can now assist with building fortifications, pathfinding accounts for terrain changes. January 2026 added a host-region filter to the server list. Nothing public since 10 January 2026.
3. **The publisher's fault list (June 2026), symptoms only:** UI and UX are behind; the map is too large and poorly laid out; players do not know what to do; enemy bots kill the player too fast; squad pathing and squad commanding both feel bad; the whole is not fun for long enough.
4. **Robert's play sessions of the public build (June and August 2026),** four logged findings. Two of them block onboarding outright, see section 1.
5. **The eight Steam store screenshots.** Read below. They are the only view we have of the in-game HUD.

### What the screenshots actually show

Seven of the eight screenshots are taken with the gameplay HUD hidden or absent. They show combat, destruction and vehicles, and they show the map: a grass bowl walled in by cliffs, buildings, wire, craters, and a great deal of open ground between things. Friendlies and enemies wear dark grey-black and blue-grey uniforms with no outline, marker or nameplate distinguishing them in any shot. Every screenshot carries a ping readout top-left and an FPS counter top-right, and one carries the engine's "Development Build" watermark bottom-right, so these were captured from a debug build, not a presentation build.

One screenshot (ss_4) has the live HUD, and it is the most useful thing we have:

1. Top centre: a horizontal bar split blue and orange, roughly 55/45, unlabeled. Probably a team balance, ticket or capture readout. There is no way to tell from the image.
2. Under it: a hammer icon and the text "Enemy prepare phase". So the phase indicator exists, but it names the enemy's phase, and the player has to infer their own from it.
3. Top left: "$24,000". The economy is on screen at all times.
4. Mid screen: a "Progress" bar with "Repair" and "Operate" as context prompts on a tank.
5. Bottom left: "Cloud Player", a red health bar, and what looks like a portrait slot.
6. Bottom right: ammo "8 | 146" with a bullet icon.

What is not on that HUD: a phase clock, an objective marker, any indication of where the front or the active flag is, a compass or minimap, any squad status (how many soldiers you have, where they are, what they are doing), and any indication of what the player is supposed to do next.

What we cannot see at all, in any public material: the map screen, the recruit flow, the build panel, the buy flow, the `T` command menu, the lobby, the tutorial. Everything said about those below comes from text sources and Robert's sessions, not from images.

## 1. The UX problem in one paragraph

A new player launches the tutorial and meets at least five instruction blocks rendered on top of each other in the same text area, with two voice-over tracks playing at once. The one piece of the game whose job is to explain the rest cannot be read or heard. The player then enters a match where the HUD tells them the enemy's phase but not their own, shows a dollar figure but not what it buys, and shows no objective, no front line and no clock. Four separate key-driven systems (buy, build, map and recruit, squad command) sit behind single letters with no on-screen affordance, on a map large enough that the fight is usually somewhere else. Enemy AI then kills the player before they have worked any of this out. The bounce is not "the UI looks dated". It is that the game never manages to tell the player what a round is, and the first minute actively prevents them from finding out.

## 2. What the game asks a player to hold in their head today

This is the honest load, from the developer's own descriptions. None of it is hidden or optional in the current build.

1. **Two camera modes** (`P`), with different aiming feel, plus nine weapon slots.
2. **A money economy.** Earned from kills and presumably objectives, deducted for team kills, spent in three different sinks. The balance sits on the HUD permanently, which tells the player it matters, without saying for what.
3. **A buy flow** for weapons and items, on its own key in the September build, location unconfirmed in the December build.
4. **A build flow** for sandbags, gun nests, spawn points, digging, and since August 2025 a vehicle factory that produces tanks. NPCs can help build since December. This is an RTS-style base layer inside a shooter.
5. **A map screen** that is also the recruitment screen: AI soldiers are bought at spawn icons on the map. So the map is not just for orientation, it is a shop.
6. **A squad command menu** on `T` for the soldiers you recruited. Order set and menu layout unconfirmed. The publisher's list says both pathing and commanding feel bad, and the December notes say pathing was rebuilt, so the current state is unknown.
7. **Vehicles** with seats, repair and operate interactions, and a deep armour simulation (ammo racks, track damage, deformation).
8. **A three-phase round cycle**, Prepare, Defense, Attack, where the two teams are on opposite phases. Flags are capture points, each with a white ground circle that becomes a "defense zone" once captured; the tutorial tells the player to stay inside one during Prepare and Defense. Waypoints are coloured smoke.
9. **A map** big enough that the publisher's first complaint about the game is its size, with cliffs as the only strong landmark and open grass between objectives.

Nine things, most of them with their own key and their own screen, layered on a round structure the HUD does not explain, delivered by a tutorial that does not render. That is the diagnosis. The problem is not any one screen. It is that the game asks the player to be a shooter player, a squad commander, a base builder and a tank crew in the same minute, and gives them a single unlabeled bar and a dollar sign to do it with.

The production plan addresses the root of this at the scope level: the economy and factories are parked, one sector is live at a time, one objective, one clock, three squad orders. The UX work below serves that re-cut loop. It is not a repaint of the current one.

## 3. Prioritised work list

Ordered by what unblocks a player fastest. Sizes are design effort only, in working days for one designer, and assume implementation sits with the development team and the AP lead programmer against agreed deadlines. Ranges are wide because nobody has seen the build's UI code.

### 3.1 First session: the ten-second test, then the guidance path

**What.** Two things in sequence. First, the diagnostic: open the tutorial and read the overlapping lines. If they are the same sentence in several languages (English, Simplified and Traditional Chinese are all shipped with full audio), the root cause is that language selection is not applied to the tutorial layer and both text and VO are firing once per language. That is a settings-level fix. If the overlapping lines are different instructions from different tutorial steps, the step machinery is not tearing steps down before starting the next, and the two voices are two steps talking over each other. That is a broken sequencer. Listen to the two voices the same way. Second, once that answer is in, design the replacement: the plan cuts the tutorial as a separate level and replaces it with guidance inside the first round of a real match.

**Why.** It is the single confirmed blocker. And the answer to the test sets the scope of the second half: if the step sequencer is sound (case A), in-round guidance can be built on it. If it is not (case B), the guidance system needs its own trigger and teardown logic and the estimate for it roughly doubles.

**Size.** The test: an hour, including writing it up. The in-round guidance design: 8 to 10 days, spread across the phase because it only converges through playtests. This is the most iteration-heavy item on the list.

**Depends on.** Build access to run the test properly (the public demo will do for the test itself). The re-cut loop being locked, since guidance teaches the loop and the loop is changing.

### 3.2 Round-state readability: the HUD's four questions

**What.** A HUD that answers, at a glance, without a key press: which phase am I in, what is the objective, where is the front, how long is left. Concretely: the player's own phase named, not the enemy's; one objective marker for the active flag or trench line, world-space and on screen edge when off screen; a front-line or sector-boundary read so "where the fight is" does not depend on spotting smoke; a phase clock; and team identification on soldiers so friend and enemy are separable from behind. The blue-orange bar either gets a label and a meaning or goes.

**Why.** "Players do not know what to do" is the second item on the publisher's list and the HUD is where that is fixed. With the plan's one-sector-at-a-time loop, this becomes tractable: there is one objective and one clock to show.

**Size.** 6 to 8 days for the design and spec, plus two iteration rounds after playtests, 2 days each. This is the item the AP artist should be paired on for iconography.

**Depends on.** The sector-gating design being decided (what is a "front" in the re-cut loop). Engine and UI framework confirmed, since it decides whether the designer hands over mockups or working layouts.

### 3.3 Squad orders: three on a radial

**What.** The command menu currently on `T`, reduced to three orders on a radial: advance to marker, hold, dig here. Plus the read-back the current HUD lacks entirely: how many soldiers you have, whether they are following, holding or digging, and where they are relative to you. The radial should work with the same hand that is aiming; the current menu's input model is unknown.

**Why.** Squad recruitment and command are the game's differentiator and they already exist. They are on the fault list because they do not work well, not because they are missing. The plan's answer is fewer orders on a bounded navmesh. The interface has to make those three orders fast, legible and confirmable, otherwise the AI retuning underneath it will not be felt.

**Size.** 5 to 6 days for the radial and the squad readout, then iteration alongside the AI tuning, which will move the goalposts.

**Depends on.** The AI and pathfinding retuning on the development side; the order set is a design decision the two founders and Robert need to lock before the interface is drawn. Seeing the current `T` menu, which nobody on our side has.

### 3.4 Build and buy: one panel, phase-gated

**What.** Fold the buy and build flows into one panel that only opens during the phase where it makes sense (Prepare for the defender, the plan's 90-second window), shows what the money buys in that phase, and closes. The December control change may have already done part of this, since the separate buy key disappeared from the list. Confirm what exists before designing.

**Why.** With the economy and factories parked in the plan, the panel loses most of its content. What is left (dig points, barricades, gun nests) needs a fast, phase-bound placement flow, not a shop. The permanent dollar readout on the HUD should follow the same logic: visible when spendable, gone otherwise.

**Size.** 4 to 5 days if the December build already merged the two flows. 6 to 8 if the demo still has two separate systems and the merge is design work.

**Depends on.** The cut list being final. If the economy stays in any form, this item grows.

### 3.5 Map and recruit screen

**What.** The `M` screen doubles as orientation and as the place to buy AI soldiers at spawn icons. Under the plan it should do two things well: show the active sector, the front and the objective (the same read as 3.2, zoomed out), and offer recruitment in a form that does not need a map click at a spawn icon mid-firefight. Whether recruitment stays on the map, moves to the Prepare panel, or becomes automatic per round is a design question the plan does not settle.

**Why.** Recruitment is the on-ramp to the game's differentiator, and today it is behind a map screen on a key the tutorial fails to teach.

**Size.** 4 to 5 days if scoped as a fix (clearer map, recruit relocated). A full redesign is 8 plus and should be phase 2 unless playtests force it.

**Depends on.** 3.2 and 3.4, since it reuses their language. The recruit model decision.

### 3.6 Hygiene list

Items that need writing down, not designing: placeholder lobby name ("dsadasdasdasd") in the public build, player portraits rendering as white squares, debug overlays (ping, FPS, dev watermark) in store screenshots, unlocked mouse cursor visible during gameplay in one shot, hit-marker particles reading as debug squares. Size: half a day to catalogue in the review month, zero design time after that.

## 4. Fix versus redesign

This split is what decides whether a half-time seat is enough.

**Fixes: the development team can close these from a written spec, no designer ownership needed after the spec exists.**

1. The tutorial root cause, if the ten-second test lands on case A.
2. All of 3.6.
3. Phase text naming the player's own phase instead of the enemy's.
4. Labelling or removing the blue-orange bar.
5. Team identification on soldiers (outline or marker).
6. Hiding the money readout outside spendable phases.
7. Debug overlays and cursor lock in release builds.

**Redesigns: a designer owns the pass, iterates through playtests, and the outcome is not known in advance.**

1. In-round guidance replacing the tutorial (3.1, second half). Doubly so if the test lands on case B.
2. The round-state HUD (3.2): objective, front, clock.
3. The three-order radial and squad readout (3.3).
4. The phase-gated build panel (3.4), if the buy and build flows are still separate.
5. The map and recruit model (3.5), if a fix is not enough.

Rough weight: the fixes are perhaps a fifth of the effort and most of the visible improvement in the first month. The redesigns are the rest, and they are the ones that decide whether the closed playtest at the end of phase 1 measures retention or measures confusion.

## 5. Sizing against a 50% seat in phase 1

Phase 1 is months 2 to 5, four months. Half time is roughly 40 designer days.

Adding up section 3 at the low end of each range: test and guidance 9, HUD 10 with iteration, radial 7, build panel 4, map 4, plus playtest observation and write-ups across two closed playtests at 8, plus spec support for the hygiene list at 3. That is 45 days at the optimistic end and around 55 at the pessimistic. Against 40 available.

So the honest read: **50% flat across four months is thin, and it only works under three conditions.**

1. **The review month does the discovery.** The plan starts the UX seat in month 2, but the design teardown is in month 1. If the designer is not in the build during month 1, month 2 is spent finding out what the `T` menu looks like instead of redesigning it. Three to five days inside the review month is the cheapest correction available.
2. **Implementation and asset production sit elsewhere.** The seat is design and iteration, not UI implementation in engine and not icon production. If the designer is also building the prefabs, 50% is a quarter of what is needed.
3. **The map and recruit screen is scoped as a fix in phase 1.** The redesign version goes to phase 2 unless the first closed playtest forces it forward.

If those hold, 50% delivers the three redesigns that matter (guidance, HUD, radial) and the spec for the rest. A better shape than flat 50% is front-loaded: heavier in months 2 and 3 when the HUD and radial are being drawn and the first playtest is being prepared, lighter in month 5 when it is iteration on measured results. Same total, better fit to the curve. If the conditions do not hold, say so before month 2 rather than discovering it in month 4, because the closed playtest at the end of phase 1 is the investors' go or no-go and it will be read through whatever HUD exists on that day.

## 6. What Jesper would need to see before committing

Kept short and answerable.

1. **The current playtest build**, not just the public demo, with the December control map. The demo may be the August 2025 build.
2. **Fifteen minutes of screen capture** of the `T` command menu, the `M` map and recruit screen, the build panel and the lobby. This replaces most of the guesswork in section 3 at no cost.
3. **Engine and UI framework** confirmed, and whether UI lives in prefabs, data or code. This decides the handover format and half of the estimates.
4. **Any telemetry or playtest notes** from the two public playtests: session length, tutorial completion, where players quit. The publisher may have wishlist and playtest data the developer does not.
5. **The order set and recruit model decisions**, or a date for when they are decided, since 3.3 and 3.5 cannot be drawn without them.
6. **A named implementation counterpart** on the development side for UI, and the turnaround expectation on spec-to-build.
7. **Working language and hours.** The development team is China-based with limited English per the publisher, so the spec format (annotated images over prose, numbered items, one change per line) is part of the design.

## 7. Open unknowns

Stated as unknowns, not as caveats to be skipped.

1. **Engine and version are not confirmed.** The "Development Build" watermark in one store screenshot is a strong hint toward one engine, and nothing more than a hint.
2. **No repo, pipeline or internal build access.** Everything here is from the public demo, the developer's public posts, the store page and Robert's sessions.
3. **Which control map is live.** September and December 2025 lists differ; the demo Robert played may be either.
4. **The current state of squad AI and pathfinding.** The fault list predates the December refactor by six months in one direction and postdates it by six in the other; we do not know what the refactor changed in practice.
5. **The tutorial root cause.** Case A or case B, one hour to find out, not yet run on a build we control.
6. **What the blue-orange bar means.**
7. **Whether buy and build were merged in December** or the buy key simply moved.
8. **No telemetry of any kind** has been seen. Retention, session length and quit points are unknown.
9. **This is not an internal review.** It is a reconstruction from outside the studio plus a symptom list from the publisher. The review month exists to replace it.
