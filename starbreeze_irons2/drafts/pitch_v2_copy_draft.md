# Project Irons 2 — Pitch v2 copy draft, round 2 (pre-voice-pass)

Draft for The Author. Channel: gated web proposal page (document register). Recipients:
Tobias Remmers (PAYDAY Franchise Director) and Matt Dixon (CGO), Starbreeze. English.
Positioning: Aurora Punks × Rift Gaming as ONE co-development team, not two vendors.

Built to Robert's slide structure (PDF, 2026-09-01). Sources: the staffing sheet is the source of
truth for team size, months and money. The level-design content comes from Rift's "PUBG x Payday
Level design thoughts" doc (Elias and Jesper). Credits and evidence come from Robert's structure doc.

Numbers are locked, do not alter:
27 roles · peak 24,3 concurrent · 256,1 FTE-months · 12 months to Gold plus support ·
29 649 100 SEK ex VAT · blended 115 772 SEK per FTE-month · 140k flat equivalent 35 854 000 ·
internal AP 10 904 000 / Rift 10 885 000 / External 1 018 000.

---

## SLIDE 1 — Front

Aurora Punks × Rift Gaming

**PAYDAY × PUBG: Co-dev proposal**

Hook line:
An accessible, fast-paced PAYDAY built for PUBG players. That is the brief, and it is the
part we would hold on to hardest.

Executive summary:
Aurora Punks × Rift Gaming. 27 roles, peaking at 24 people. Stockholm. 12 months to Gold,
with support after.

Positioning line (verbatim, Robert's, do not touch):
An experienced co-development team built to take the project from concept to shipped experience.

Stat strip: 27 roles / peak 24 / Stockholm / 12 months + support / 29 649 100 SEK ex VAT

---

## SLIDE 2 — The Mission

Intent: show we understand the assignment before talking about ourselves.

Opening:
The audience is the constraint everything else follows from. The players will mostly be active
PUBG players who do not know PAYDAY, so anything that needs prior PAYDAY knowledge to enjoy is a
cost, not a feature. Irons 1 also showed that recreating levels in the PUBG engine takes a lot of
manual scripting and implementation, and we have staffed for that rather than hoped around it.

Three things we would hold on to (from Elias and Jesper, and the Irons 1 learnings):

1. **Accessible PAYDAY for the PUBG audience.** Simplify heist structures, objectives and stealth
   mechanics while preserving the core PAYDAY identity. Intuitive systems, clear progression, and
   gameplay that works equally well for players unfamiliar with PAYDAY.
2. **Fast-paced, varied and re-playable heists.** Shorter, action-packed experiences with strong
   visual and gameplay variation across environments, weapons, combat, stealth, enemies and
   objectives. Re-playability through progression, loadouts, weapon tuning and meaningful power growth.
3. **Evolve the whole experience, not just the new heists.** New stealth mechanics, progression,
   weapon balancing, difficulty and the Shield enemy should work cohesively across both the new and
   the existing heists. One consistent experience rather than separate pieces of content.

The delivery challenge:
27 roles from a standing start to peak inside four months, two IP holders in the approval chain,
and 12 months to Gold.

### Expandable detail — how we read the level design

**Variation.** The heists were chosen because they offer visual variation, multiple vistas and
environments. We keep that when we port them. Where we cut gameplay or size, we keep at least part
of each distinct environment intact.

**Simplify.** More linear structure and heist objectives. Remove complex optional objectives where
needed and adjust levels accordingly, including degrading loot and loot bag scanning. Reduce map
size where needed. Add new stealth mechanics but keep them simple, and keep the levels enjoyable
for players who do not want to play stealth.

**Fast pace.** We have been asked to investigate 3Cs. Significant changes to movement and camera
systems are hard, so we would also support a faster pace by other means: keep the heists short and
action packed, cut or simplify the slower segments, keep the gameplay loop tight so the tempo
between heists and progression rewards stays satisfying and long loss states are avoided, and tune
new and existing weapons closer to the PAYDAY experience with solid power spikes on unlock.

**Stealth mechanics.** Krafton has asked for additional stealth. The direction we would take is
simple stand-alone features rather than complex general systems: lockpicking and safe cracking in
the PD3 style, hacking to temporarily disable individual cameras, motion and floor sensors used
sparingly, QR codes simplified so no randomly spawned phones are needed, security lasers with fuse
boxes or wall terminals, silencer mods (default on side arms, unlocked on primaries), and stealth
skills and tools such as throwing knives and stealth variables on armour and skills.

**Enemy design.** One new enemy type, the Shield enemy. The work is less the enemy itself and more
implementing it well across both new and existing levels, and updating existing enemy behaviour to
use the shield as mobile cover in combat.

**The existing four levels.** Revisited and updated with the new enemy and AI behaviour, the new
stealth mechanics, the new difficulty, rebalancing against the new progression and weapon tuning,
and tutorial and HUD elements as needed.

**The new heists.**
- **99 Boxes (or Touch the Sky).** A large map blending outdoor and indoor environments around
  shipping containers and warehouse storage, patrolling guards and cameras with civilians spread
  out. We keep the smooth indoor/outdoor transition, rebalance for PUBG players, focus on avoiding
  cameras and guards, and remove civilians.
- **Syntax Error.** Large, with multiple visual styles and vistas: busy streets, parks, server
  rooms, futuristic interiors. We maintain that variation while shortening the heist and reducing
  the overall size.
- **Under the Surphaze.** Compact, stacked on itself across multiple floors with several entry
  options, heavy on stealth and on gathering information to locate objectives while bypassing
  motion detectors and lasers. We keep the stealth but make the flow more linear and clearer,
  simplify the security puzzles, group the information so there is less back and forth, and replace
  civilians with cameras, patrolling guards and level mechanics. Mechanics: QR code scans, motion
  scanners, laser traps.
- **Turbid Station.** [PLACEHOLDER - Rift flag this as a stretch goal and are not sure it belongs
  in the pitch. Robert to decide: in as a stretch goal, or out.]

---

## SLIDE 3 — Why Aurora Punks × Rift

Intent: complementary strengths, one delivery team, evidence over adjectives.

Five things we bring:
- **Senior leadership.** The people named here are the people who do the work.
- **AAA to indie experience.** Rift carries the AAA technical depth, Aurora Punks the indie and AA
  cost discipline.
- **On-site presence.** Both studios are in Stockholm.
- **Test driven game development.**
- **Trusted by studios.**

Evidence:

**Previous PUBG × PAYDAY experience — Dmitry Garkavenko.** Dmitry helped bring a PAYDAY-style heist
and stealth experience into PUBG's live-service codebase, with contributions across Heist and
Stealth Experience Integration, Interaction System Hardening, AI and Contextual VO, Combat
Readability and Feel, Unreal Animation, and PS5 Rendering, keeping features stable and network-safe.

**Krafton relationship and previous collaboration — Jimmy Chuong.** The first developer in place to
lead and build the core gameplay, systems and UI foundation for a story-driven Unreal Engine / C++
action game, delivering modular systems across Inventory, Navigation, Missions, Maps, Combat,
Multiplayer, Animation and development tools. Regular communication and recurring meetings with
Krafton throughout.

**Mojang Dungeons 2 team delivery and release — Per Kjellström and Jesper Staafjord.** The team
supported Mojang across Production, Product Advisory, Design Management, Game Engineering and Level
Design, working across multiple teams. The delivery covered roadmaps and priorities, team
leadership, production and design, gameplay development, performance and stability, and supporting
teams through key production and release milestones.

**Full responsibility for releasing games from idea to launch based on existing IP.**

**Ready or Not — porting from Unreal 4 to 5 for a live game.**

Studios our people come from: Ubisoft, Embark, Mojang, DICE, Neon Giant, Avalanche, Starbreeze,
King, Toca Boca, 10 Chambers, MAG Interactive, Arrowhead.
[PLACEHOLDER - studio logos instead of a text list]

Games released: The Ascent 2 (demo), Arc Raiders, Dungeons 2, Ready or Not, Kingdom Two Crowns,
PUBG × PAYDAY 1, The Finals, Crozzle.

One delivery team:
The work splits almost exactly down the middle between the two studios: not a prime and a
subcontractor. One producer, one backlog, one set of milestones. You talk to one team.

---

## SLIDE 4 — The Team

Intent: make the team feel real and ready.

- **Dmitry Garkavenko** - Tech (Rift). Mojang, Starbreeze (PAYDAY × PUBG), Fast Travel Games,
  Embark, Arrowhead, Battlestate Games
- **Jimmy Chuong** - Tech (Rift). Neon Giant, Embark, Liquid Swords, Creative Assembly
- **Robert Bäckström** - Production (Aurora Punks). Aurora Punks, Bright Gambit, Raw Fury, Fatshark
- **Per Kjellström** - Production (Rift). Mojang, Liquid Swords, Noid, DICE
- **Tim Browne** - Design (Aurora Punks). Avalanche, King, Ubisoft, Codemasters
- **Jesper Staafjord** - Design (Rift). Mojang, The Gang, Star Stable, Ringtail Interactive, Solve, King

The full team, 27 roles:
- Production and direction: 3
- Engineering: 8
- Design: 6
- Art and audio: 6
- QA: 4

12 roles Aurora Punks, 11 Rift, 4 external specialists.

---

## SLIDE 5 — Project and delivery plan

Intent: months, milestones, staffing, tangible deliverables.

We have kept the start month open. Krafton indicated a later start is workable as long as the
12-month development window and the support period after it hold, so month 1 is whenever we sign.

**Prototype, month 2.** 22 people.
- Player progression rework defined and prototyped
- All design documentation done
- Infrastructure in place and proven

**First Playable, month 3.** 24 people.
- Three new grey box levels playable end to end

**Pre-Alpha, month 5.** 24 people.
- Restart / Return system implemented
- New stealth mechanics defined and prototyped
- UI/UX wireframes approved and first iteration of the new HUD fleshed out in build
- Shield enemy functional

**Alpha 1, month 7. Feature complete.** 24 people.
- Player progression and loadout systems functional
- Restart / Return system functional
- Onboarding and tutorials functional
- All three new levels functional and visually representative
- New difficulty level implemented
- Five new weapons functional
- Polish and balancing across the game

**Alpha 2, month 9.** 23 people.
- HR1 levels updated and adjusted to the new mechanics and improvements
- Loadout customisation functional
- New stealth mechanics functional
- All AI enemies polished and improved
- Polish and balancing across the game

**Cert Candidate, month 10. Pre-cert candidate ready for Krafton.** 22 people.
- Gameplay, mechanics and game loops polished, balanced and optimised
- All levels, HUD, art and customisation in a shippable state
- Onboarding and tutorials shippable
- All weapons and gunplay balanced and improved
- New difficulty level balanced and proven
- Required marketing key art approved

**Beta, month 11. Content complete.** 18 people.
- Final polish and balancing across the game
- Builds for all platforms ready for CERT

**Gold, month 12.** 16 people.
- Certification and release candidate stabilisation

**Support.** After Gold, scoped separately.

Staffing curve, FTE by month: 11,8 / 21,8 / 23,8 / 24,3 / 24,3 / 24,3 / 23,8 / 23,8 / 22,8 / 21,8 / 17,8 / 15,8. Total 256,1 FTE-months.

---

## SLIDE 6 — Commercials

Intent: transparent and simple. Final cost clear and understandable.

**29 649 100 SEK ex VAT.** 27 roles, 256,1 FTE-months, 12 months to Gold.

This is priced from what the team actually costs, not from a fixed rate card. It works out at
115 772 SEK per FTE-month blended across every role, lead or content. For comparison, the flat
140 000 per developer per month we discussed earlier would put the same team at 35 854 000.

Payment schedule:
- On signature: [PLACEHOLDER - percentage to confirm, shown at 10% = 2 964 910]
- Prototype, months 1-2: 4 050 800
- First Playable, months 3-4: 5 532 800
- Pre-Alpha, months 5-6: 5 582 200
- Alpha 1, months 7-8: 5 452 200
- Alpha 2, month 9: 2 568 800
- Cert Candidate, month 10: 2 451 800
- Beta, month 11: 2 087 800
- Gold, month 12: 1 922 700
- Total: 29 649 100

What is included:
- All 27 roles, both studios plus the external specialists, for the months shown
- Production, engineering, design, art, audio and DevOps
- QA lead and three QA testers
- External art support for characters, VFX and weapons
- Tooling and infrastructure on our side

What is not included:
- VAT
- Platform certification fees
- Third-party licences owned by you or Krafton
- Support after Gold, scoped once the shape of it is known

Key assumptions:
- Source access, build access and a PUBG-side technical contact from day one
- Approvals inside five working days at each milestone
- Scope as per the 12 August feature list and three new heists. Material additions move the plan
  and the number
- This is a time-and-team price, not a fixed fee. A fixed-fee version carries a risk premium

---

## SLIDE 7 — Ways of Working

Intent: embedded with the client, but ownership of delivery.

**Stockholm-based partner.** We are in Stockholm, so we work on site, integrate with your studio
and build relationships face to face.

**One accountable team.** A senior core accountable for the whole delivery, not a set of
individually placed contractors. Single point of contact, single point of escalation and risk
management.

**Full ownership.** We understand the creative and technical goals of the project and take
end-to-end ownership of the work required to deliver against them.

### Expandable detail — risk and mitigation

1. **Ramp to 24 people inside four months.** Both studios are naming people now rather than
   recruiting later. The month 1-2 ramp is shallow so the seniors set the foundations before the
   wider team lands.
2. **Manual scripting load from the port.** Irons 1 showed that recreating levels in the PUBG engine
   is scripting-heavy. That is why the level design and tech design roles are staffed from early
   and held through Beta, rather than added when it hurts.
3. **Two IP holders in the approval chain.** Milestone gates are set against Krafton's cert
   candidate date at month 10, and we work back from it.
4. **Scope growth.** Every gate carries a named deliverable list. Additions are re-planned in the
   open, with a number attached.

---

## SLIDE 8 — Ready to build

Heading: Ready to deliver

**The mission is clear.**
Create an accessible, fast-paced and replayable PAYDAY experience for the PUBG audience, while
preserving what makes PAYDAY great.

**Aurora Punks × Rift brings the team to make it happen.**
A senior, Stockholm-based co-development team with the PAYDAY knowledge, shooter experience, Unreal
expertise and end-to-end delivery capability to take the project from concept to launch.

We are ready to take ownership, integrate closely with Starbreeze and Krafton, and deliver as one
accountable team.

**Proposed next step**
Align on scope, team and commercials, finalise the agreement, kick off.

Stat strip: 27 roles / peak 24 / Stockholm / 12 months + support / 29 649 100 SEK ex VAT
