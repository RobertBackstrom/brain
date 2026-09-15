---
title: Jesper Staafjord (Rift) design and UX evaluation, read and critique
project: dsc
status: internal
created: 2026-09-15
author: Assistant (GameDev agent), for Robert Bäckström
source: drafts/jesper_rift_design_ux_evaluation_2026-09-15.md (converted from the .docx, Drive file 16hAWVwjk6gzD6zuqlW0rudQxdwyENkDA)
audience: internal AP. Section 5 is the only part written to be reusable towards LUG, and nothing leaves AP without Robert.
---

# Jesper's evaluation: what it says, what it is worth, where it stops

**The document.** "Disposable Corps - Design & UX Evaluation", 4 155 words, authored in the file
2026-09-11, uploaded to Drive 2026-09-15. Four parts: player fantasy and USP, onboarding and
tutorial (including a step by step pass over roughly eighteen tutorial steps), core design elements,
and a list of specific UX interactions. Filed on Drive under **Projects / Disposable Corps**
(folder `1Fb0GN3piu7W8t4vrxfFfWVtKJwCIUAIZ`, created for this, `dsc` now registered in
`assistant/drive-folders.json`).

This is the first deliverable of the UX evaluation seat we sold to LUG on slide 06, and it arrived
without a mail in the thread, so it is worth noting that it came via Drive rather than as a reply to
`1a07e0b9149bc492`.

## 1. Three strengths of the game, as he found them

1. **The power fantasy lands.** His words: "players feel they can meaningfully affect the tide of
   battle", and the game is "fun and has real potential" once you get past the learning wall. That
   matters more than it reads, because it says the problem is access, not the core. Everything he
   then criticises is reachable by design work rather than by rebuilding what the game is.
2. **Three saleable fantasies sit on top of each other:** the officer commanding a unit, the soldier
   winning through individual skill, and the logistics engineer who turns a battle with well placed
   structures. He rates all three as strong and strategically fertile. That is the USP argument the
   store page has never made.
3. **The construction and vehicle layer is genuinely differentiated.** He treats sandbags, trenches,
   machine guns, factories, towed artillery and the armour simulation as the raw material worth
   building the round around, not as clutter, and his big design suggestion is built out of
   mechanics the game already has. Also worth logging: several late tutorial steps (heavy factory,
   entering the tank) he calls simple, clear and well written, so the team can do this when the step
   is scoped small.

## 2. Three weaknesses, ranked by how much they cost

1. **The game has not decided what it is.** Milsim (historical weapons, one shot kills, poor tank
   visibility) and goofy multiplayer sandbox (low fidelity, simple AI, a latrine as a spawn point)
   are both live in the same build. He says both can work but the identity has to be chosen, and
   that the choice then settles everything downstream. This is a positioning problem, not a UX
   problem, and it is the most strategic thing in the document.
2. **The onboarding is structurally wrong, not merely rough.** The load bearing finding: the
   tutorial and the normal game sequence run **in parallel, each with its own tutorial text and its
   own voice over**. On top of that, free roam across the full size map, the ability to sell the
   hammer and lose the building system entirely, buy and squad options exposed before they mean
   anything, and the player being killed three times in short order as a teaching device. His fix is
   a bespoke small tutorial map, gated movement, split basic and advanced tutorials, and a HUD
   objective element that shows only the current step.
3. **A round has no progression, and the economy pays for the wrong thing.** Rounds play out the
   same way (soldiers advancing in a line, funnelled into a barbed wire maze), NPC count never
   changes, money arrives too slowly to matter, the map is big and empty so a large share of
   playtime is walking, and phase transitions add more walking. The sharpest single line in the
   document: **the most effective way to earn money is to die repeatedly near the enemy point.** In
   a competitive multiplayer game that is a broken core incentive and an open griefing surface, and
   it is the kind of thing that writes the negative reviews at Early Access.

## 3. What it confirms, and the one question it answers for us

**It independently validates the publisher's own fault list.** Anthony's June 2026 symptoms (UI and
UX behind, map too large and poorly laid out, players do not know what to do, bots kill the player
too fast, squad pathing and commanding feel bad, not fun for long enough) are all six confirmed by a
paid outside designer who had not seen that list. For LUG that is the useful property of this
document, and it is the basis of section 5.

**It resolves, partly, the tutorial question we wrote down on 26 August.** `build_feedback.md` had
two hypotheses for the stacked instruction blocks and the doubled voice over: hypothesis A, every
localisation active at once, and hypothesis B, tutorial steps that never tear down. Jesper gives a
third answer neither of us had: **two separate systems running at the same time**, the tutorial layer
and the live game sequence, each with its own text and voice over. That is cheaper than B and it
explains the doubled voice. It does **not** explain the CJK glyphs Robert saw between the English
lines, so the localisation hypothesis is still open and still needs the ten second read test. Note
for the review month: check both, they are not exclusive.

## 4. Where his conclusions fall short

Ranked. This is the internal read, and it is the read of a deliverable from a seat priced at 55 000
a month.

1. **No evidence base is stated, and the game is 5v5.** The document never says which build, which
   platform, how many hours, or alone or with other people. This is a caveat on the findings rather
   than a fault of his: he had only the public Steam demo, no repository and no telemetry, so a
   populated ten player match may not have been available to him at all. It still has to be written
   down, because several of his biggest conclusions (map too large, map too empty, too much walking,
   rounds are repetitive, NPC behaviour is static) are exactly what a solo session against bots
   produces whether or not they are true of the populated game. **A map built for ten players reads
   as empty with one.** Until the player count is pinned down, treat those specific findings as
   hypotheses, the way our own UX assessment labelled its own. **Answered 2026-09-15, by Robert, not by Jesper: he almost certainly played against bots, because
   there are not enough players to fill a PvP match today.** That makes it worse rather than better.
   Nobody can currently validate those findings, the developers included, so every judgement about
   map scale, travel time, emptiness and round repetition in every source we have, his pass, the
   publisher's fault list and Robert's own sessions, was formed in an empty game. Treat them as
   unvalidated until the first populated playtest, and do not commit map work on them.**
2. **Roughly 120 recommendations, none of them prioritised or costed.** Flat bullets, no severity,
   no effort, no "these three first". The plan we sold has a fix build in month 2 and the first
   public playtest in month 4, so what it needs from the evaluation is a ranked top ten with rough
   sizing, not a complete list. The document ends without a summary, a priority list or a next step.
   That is a deliverable shape problem, and Robert's call (2026-09-15) is that **we close it ourselves**
   rather than sending him back to write more: AP does the ranking and the sizing, and asks him to
   sanity check the result.
3. **He parks the identity question and then answers it implicitly anyway.** He raises milsim versus
   goofy, says he will leave it out to stay neutral, and then writes a hundred recommendations that
   nearly all assume the accessible direction (more health, no one shot kills, snapping, smaller
   map, guided tutorial, forgiving tutorial). If the team chooses milsim, a meaningful share of the
   list argues against itself. The identity call is a gate that belongs in front of the fix list, not
   in a section that excuses itself from the analysis.
4. **The largest idea in the document is uncosted.** The new progression design (start with a small
   army, few soldiers, tight control points, then grow the army and scale the conflict outward as
   points are captured, with counter mechanics for each buildable) is the most interesting thing he
   wrote and it is a redesign of the round structure, spawning, economy and map layout. Presented
   without effort, risk or a note on what it displaces. Against a 1 860 000 budget, a two person
   team, and an EA date in month 10, that idea is a month 5 go or no go decision, not a bullet in
   section 3.
5. **No comparables.** The developer's two playtests, the demo's players and the 2 741 followers are
   not referenced, but he was never given that data, so that half is on us. The comparables are a
   real gap and a cheap one to close: trench and squad shooters are a well populated shelf, and
   "give the player more health" is asserted rather than argued. For a document that has to survive a
   financier reading it, one sentence of what neighbouring titles do carries more than ten bullets of
   preference.
6. **Not a gap: the technical layer.** Hosting, network layer, dedicated servers and performance are
   absent, and that is correct. Robert asked for design only, and the evaluation was made from the
   public Steam demo without repository access, so the technical direction could not have been
   answered here. Recorded only so nobody mistakes this for coverage: step 4 of the plan (answering
   Paul at the level of "A\* to JPS", "FishNet to Photon") still needs the repository, and the LUG ask
   for engine, repository, telemetry and wishlists is still the binding constraint on that, not on
   this document.

**What none of this changes:** it is a competent, specific, playtested design pass, delivered before
the engagement is signed, and its specificity is the argument that the seat is worth funding. The
gaps above are mostly gaps of framing, and four of the six are fixed by asking him two questions.

## 5. The LUG facing version (draft framing, not sent)

For Magnus and Anthony, the same content, without grading the partner. Never say "Jesper's analysis
falls short", say what the pass confirmed and what it deliberately leaves to the review month.

1. **An outside designer has independently confirmed the publisher's own fault list**, point for
   point, without having seen it. The problems LUG has been describing since June are real,
   specific and reproducible.
2. **The first pass already produced a finding that changes the game's economy:** the most rewarding
   play pattern today is dying near the enemy point. That is an exploit in a competitive title and it
   would have shipped.
3. **It also identified the mechanism behind the broken tutorial:** the tutorial and the live game
   run in parallel, each with its own text and voice over. That is a fixable bug, not a rewrite.
4. **The positioning question is now on the table with a name on it:** milsim or sandbox. We propose
   settling that in the review month, because it decides a large share of the fix list.
5. **What the review month still needs in order to rank and cost this work:** the build and
   repository, engine and version, playtest telemetry and current wishlist numbers. The design pass
   is deliberately silent on the technical direction because that answer needs the repository, and
   it is a written deliverable of month 1.

Do not put the 5v5 evidence question, the missing prioritisation or anything about seat pricing in
front of LUG. Those are ours to close with Rift first.

## 6. Actions

1. **Two questions back to Jesper** (Slack, Robert takes it himself, Author passed): how many of
   these sessions were populated multiplayer rather than solo against bots, and does he want his
   milsim versus goofy preference recorded as his recommendation. **We do the ranking and the sizing
   ourselves**, rather than sending him back to write more (Robert, 2026-09-15).
2. **We edit his text into the LUG facing version ourselves**, then ask him to approve it before
   anything goes to LUG. His approval is the gate, not his labour.
3. **Hold the new progression design as a month 5 decision**, and keep it out of anything shown to
   LUG's financiers until it has been costed, because it reads as scope.
4. **Check both tutorial hypotheses in the review month.** Parallel systems (his) and localisation
   stacking (ours, the CJK glyphs) can both be true.
5. **The LUG ask (`drafts/lug_ask_2026-09-07.md`) is still unsent** and is now more clearly the
   blocker: without the build, engine and telemetry, neither the ranking nor Paul's answer can be
   produced.
