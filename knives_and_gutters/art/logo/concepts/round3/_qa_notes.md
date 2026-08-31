# Round 3 — QA notes (2026-08-31, ArtDirector, unattended)

12/12 generated. Contact sheets: `contact_master.png` (all), `contact_gnarl.png`, `contact_clean.png`, `contact_fluxpro.png`. Cost ~$0.48 (8× SD3.5-large + 4× Flux Pro v1.1).

## The headline finding

**Flux Pro v1.1 spells "Knives & Gutters" correctly in 3 of 4 seeds. SD3.5-large got it fully right in 0 of 8.** SD3.5 keeps winning on 80s-tabletop *texture* (cracked stone, moss, off-register hand-paint) but garbles the wordmark (KNIIVES, GUTTTERS, KUTERS, doubled ampersands). Flux Pro's texture is cleaner/more modern-digital but the type is legible and correct. For a Fiverr hand-finish engagement this may not matter much — the artist redraws the type anyway — but it matters for which concept communicates the direction.

## Per-seed verdicts

**gnarl/ (SD3.5, seed-7777 direction pushed gnarlier)**
1. `seed7777` — best composition of the branch: dagger + skull top-right, mossy roots, stacked two-line type on cracked stone. Type reads "Kn'ves" (dropped i). 70% there.
2. `seed7781` — broken: doubled ampersand, right-edge crop.
3. `seed7793` — broken type (KNIIVE & &) but the thorned border + oxide-red field is the best *frame* treatment of the whole round. Worth stealing the frame.
4. `seed7807` — the sleeper. Near-monochrome woodcut look, dagger-through-skull under the type is a genuinely good badge motif. "KUTERS" misspelt. 75% there as a *direction*.

**clean/ (SD3.5, seed-9001 direction pushed cleaner)**
5. `seed9001` — strongest SD3.5 image overall: full badge lockup, skull left, vine-wrapped frame, Mordheim energy, type nearly correct and instantly readable. 85% there.
6. `seed9013` — cropped right edge, kills it. Skull + thorn detail is nice.
7. `seed9027` — best figure-ground contrast of the round (white-on-black), very readable, one stray t. Good "small-size test" proof.
8. `seed9041` — misspellings, but the red field + horizontal dagger-divider between the words is a strong layout idea.

**fluxpro/ (Flux Pro v1.1, merged prompt)**
9. `seed7777` — correct spelling, vertical dagger as separator with skull at the crossguard, bone/gold metallic. Most "finished-logo-looking" of the round; slightly more metal-album than 80s-tabletop.
10. `seed9001` — correct spelling, dense B&W thornwork eating the letterforms — closest to Blanche ink density of the Flux set.
11. `seed4242` — correct spelling, gold letterforms over black thorns + hidden skulls; most readable + most commercial. Arguably the round's best single image.
12. `seed5150` — garbled ("Kni & fers"), discard.

## Recommended curation shortlist (react to these 4)

1. **clean/seed9001** — best SD3.5 badge lockup (texture benchmark)
2. **fluxpro/seed4242** — best overall readability + correct type
3. **gnarl/seed7807** — dagger-through-skull woodcut direction
4. **fluxpro/seed7777** — dagger-as-separator, most finished-feeling

Open call for Robert: pick 2–3 → brief v1 + PDF. The Fiverr scout stays blocked on db-334 (needs a proxy/spend decision from you regardless).
