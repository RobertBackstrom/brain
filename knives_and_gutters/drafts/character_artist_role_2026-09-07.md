---
title: "3D Character Artist role description (public ad + shortlist version)"
project: knives_and_gutters
date: 2026-09-07
status: draft, awaiting Robert
author: Assistant (ArtDirector lane)
sources:
  - Fredrik Laurent, Discord scope 2026-08-27
  - "K&G - character customization" (Drive, 2026-09-01, notes from Gautham Satheesh)
  - Ark Island draft "3D Character Artist.txt"
  - knives_and_gutters/CLAUDE.md workstream 4 + kng-003
---

# 3D Character Artist, Knives & Gutters

Two versions below.

**A. Public ad.** Faction names scrubbed (Reikland and Middenheim are Games Workshop
property and kng-003 is still open), no game title, no AI framing. This is the one that
goes on artist Discords, LinkedIn and ArtStation boards.

**B. Shortlist version.** Sent or spoken to named candidates. Adds the AI-assisted base
mesh pipeline, the disclosure practice, and the real scope numbers.

**One open decision:** whose name is on the public ad, Ark Island or Aurora Punks. Written
below as the studio speaking. Say the word and I flip it.

---

## A. Public ad

### 3D Character Artist (freelance, first batch scoped)

We are looking for a 3D character artist for a top-down tactical RPG in Unity HDRP.

Environment art and visual direction are set and the game is in production. Character
concepts and references are provided.

The work starts as a scoped first batch. If it goes well, more follows: additional
warbands, creatures and hero variants.

#### The first batch

Two rival warbands, built to be mixed and matched:

* 2 base human body and clothing styles, one per warband
* Around 3 torso and clothing variants
* Legs and boots
* Around 2 armour types per warband
* Optional shoulder pieces and accessories
* 3 interchangeable heads
* 4 interchangeable hairstyles
* 4 interchangeable beards
* Colour and material variations

That is 48 head combinations on top of the body work, before colour variants.

Hair and beards are solid modelled geometry, not realistic strand or card hair.

A paper doll system is already in place. Heads, hair, beards, clothing and equipment must
be interchangeable and reusable for every humanoid character built after this batch.

Optional in the first batch, tell us if you have a view: different clothing and armour
implying different body shapes, and adjustable body size or muscle mass driven through the
mesh rather than through separate meshes.

#### Art direction

The camera is top down. Characters do not need cinematic or close-up detail. They need
strong silhouettes, believable proportions, clothing and armour that read at distance, and
consistency with the environment art already in engine.

#### Technical

* Engine: Unity HDRP
* Platform: PC
* Target around 30,000 triangles for a complete character
* Game ready, optimised topology
* Clean topology suitable for deformation and animation
* PBR materials
* Up to 2K textures for primary character sets, 1K or lower where appropriate
* Clean UV layouts
* Modular pieces that fit together cleanly
* Consistent attachment points and proportions across interchangeable parts
* LOD generation optional
* Characters delivered ready for rigging and animation

#### You

* A strong game ready 3D character portfolio
* Character modelling and texturing
* Clothing and armour modelling
* Heads and faces
* Solid modelled 3D hair and beards
* A real understanding of topology and deformation
* Comfortable working modularly, where every piece has to fit every other piece
* Comfortable working fast and iterating on feedback, this is a small team and the loop
  is short

#### Practical

Freelance, remote is fine. The first batch is scoped at roughly four to six weeks of
focused work. Send your portfolio (ArtStation, a reel or a PDF), your rate, and what you
would need to deliver the batch.

---

## B. Shortlist version (additions, not a separate ad)

Send the ad above, then add this in the mail or the call. Do not post it publicly.

**On the pipeline.** Base meshes come out of Tripo and similar AI tools. The artist does
the rest: retopology, UVs, texturing, the modular fit and everything that has to survive
rigging and deformation. Generated meshes are not the deliverable. You would be working
from a rough generated base instead of starting every asset from a sphere, and we want to
hear where you think that saves time and where it costs more time than it saves.

If that way of working is not for you, say so now and we part on good terms.

**On disclosure.** We disclose gen-AI use in festival and platform submissions.

**On the wider system.** The character work sits inside a customization system we are
designing in parallel: blend shapes across body size states rather than separate meshes,
custom normal maps per state, armour configs built for combination, a camo style system for
colour and pattern variation, and runtime combining of the customized character for
performance. If you have shipped something like that before, tell us.

**On scope.** Our internal estimate for the first batch is roughly two to four artist days
per new character body variant, one day per head, half a day per hair, half a day per
beard. Give us your own numbers, not a match to these.

---

## Notes for Robert (not part of either version)

1. **Gautham Satheesh is already inside this conversation.** The customization notes dated
   2026-09-01 came out of a talk with him, and his CV is in our Drive. Before this goes out
   publicly, worth deciding whether he is the hire, the second hire, or a consultant on the
   system while someone else does the volume.
2. **Faction names are scrubbed.** Fredrik's scope says Reikland / Imperial and Middenheimer
   / Northern Order. The public ad says "two rival warbands" and nothing more.
3. **Hair contradiction to settle.** Fredrik's spec says solid modelled geometry, the
   customization notes discuss hair cards, Fibershop and Unity Asset Store hair packs. The
   ad follows Fredrik. If the cards route is still open, the ad should not close it.
4. **The estimate the ad quotes is deliberately vague.** Four to six weeks reflects the
   21 to 36 artist day range without AI assistance, not the 15 to 27 with it. Asking the
   candidate to price it themselves keeps our number private and tells us how they think.
5. **The two versions leak against each other.** The public ad asks the candidate to price
   the batch themselves so our number stays private (note 4). Section B then hands them our
   internal day estimates. If both go out in the same mail, the number is not private. Pick
   one: either drop "On scope" from the shortlist version, or accept that shortlisted
   candidates negotiate against our figures. Flagged by The Author, 2026-09-07.
6. **No contact channel in the ad.** It says send your portfolio but never says where. Needs
   a mail address or a form before it is posted anywhere.
