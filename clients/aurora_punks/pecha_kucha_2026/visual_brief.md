# Visual Brief - Pecha Kucha Behold Summit 2026-05-25
## Aurora Punks / Robert Backstrom

**Deck:** 20 slides x 20 seconds. Single dominant subject per slide, negative space for text overlay.
**Presentation context:** Closed room, Behold Summit, Malmo. Battle-scarred founder talking craft, scars, and what AP actually does.
**Generation deadline:** 2026-05-24 (day before).

---

## Reuse Index

| Image | Used on slides |
|---|---|
| Hero plate - Slide 1 figure | 1, 19, 20 (cover + close) |
| Text background plate | 6, 8, 12, 13 |
| Slide 11 ruin image | Can double as subtle bg for slide 14 if needed |

---

## Global Style Reference

Apply to ALL generated images unless a slide note overrides:

- **Palette:** Deep Prussian blue (#0d1b2a), oxblood red (#6b1a1a), bone white (#e8e0cc), aged gold (#c9a84c). No bright saturated hues. Use gold sparingly as accent only.
- **Texture:** Ink wash on rough paper, visible grain, gutter shadows. Feels hand-made, not rendered.
- **Lighting:** Candlelight / ember / lantern warmth against deep shadow. Never flat studio light.
- **Composition:** Single dominant subject. Generous negative space upper-left or upper-right for text overlay.
- **Mood anchor:** Beautiful darkness - shadow-heavy but alive, escapist not nihilist. Punk-DIY meets gothic-surreal.
- **Avoid:** Clean vector lines, saturated colors, modern UI/tech aesthetics, stock-photo compositions, lens flare, photorealism.

---

## Consistency Strategy

**Generation order recommendation:**

Generate Slide 1 first. It is the anchor image and gets reused as cover and slides 19-20. Once you have a seed you love from Slide 1, note the seed number. Use it (with `--seed <N>`) on Slides 11, 14, and 17 to pull through the same figure-distortion language and ink-wash grain. Slides 7, 10, 15, and 16 should share a second seed run from whichever of those you generate first that lands well. The text background plate can be generated any time - it is the most forgiving prompt.

Total distinct prompt runs: 13 (11 originals + 1 text plate + 1 seed anchor from Slide 1).

---

## Estimated Generation Time

| Phase | Task | Minutes |
|---|---|---|
| 1 | Paste + queue Slide 1 in MJ v6, wait for grid | 5 |
| 2 | Upscale 1-2 variants, pick seed | 3 |
| 3 | Paste remaining 10 originals (batched in MJ v6, 2-3 at a time) | 20 |
| 4 | Text background plate | 5 |
| 5 | Upscale selects, light crop in any editor | 15 |
| **Total** | | **~48 min active, ~90 min wall-clock** |

Robert's actual hands-on time: roughly 48 minutes of pasting and picking. Queue wait accounts for the rest.

---

## Prompts

---

### SLIDE 1 - "The Image of Me" (Hero Plate / Cover / Slides 19-20)

**Tool:** Midjourney v6 (primary) - use MJ v6 for its superior ink-wash grain and figure distortion.
**Aspect ratio:** 16:9 (`--ar 16:9`)
**Reuse:** Slides 1, 19, 20.

**Prompt:**

```
ink-wash gothic illustration, a solitary figure standing in deep shadow, distorted proportions, elongated limbs, tattered coat with worn patched details, face partially obscured by shadow and hair, a faint warm amber glow emanating from the figure's chest as if carrying an ember, dark surreal background of tangled architectural fragments and gothic arches dissolving into darkness, occult aesthetic, beautiful darkness, deep Prussian blue and oxblood palette, aged gold accent, bone white highlights on edges, rough paper texture, visible ink grain, negative space upper right, punk-DIY sensibility, masterwork illustration, 8k detail --ar 16:9 --style raw --v 6
```

**Style/seed notes:** This is your anchor. Run it first. Note the seed from the best upscale (visible in MJ job details). Apply that seed to Slides 11, 14, and 17 for visual continuity.

---

### SLIDE 3 - "Two Engines Drive Me"

**Tool:** Midjourney v6
**Aspect ratio:** 16:9 (`--ar 16:9`)

**Prompt:**

```
ink-wash gothic illustration, a lone figure standing at the prow of a vessel in stormy dark water, one hand on a worn compass, the other holding a hammer, wings half-unfurled behind the figure composed of smoke and embers rather than feathers, returning-hero energy, comeback-and-craft composition, deep Prussian blue storm sky, oxblood sea, amber ember glow from the wingspread, rough paper texture, visible ink grain, single dominant subject with negative space upper left, surreal dream-logic atmosphere, masterwork illustration --ar 16:9 --style raw --v 6
```

**Style/seed notes:** If Slide 1 seed is available, pass `--seed <N>` here to pull through consistent figure-distortion language.

---

### SLIDE 4 - "How I Lead"

**Tool:** Midjourney v6
**Aspect ratio:** 16:9 (`--ar 16:9`)

**Prompt:**

```
ink-wash gothic illustration, a ship captain figure holding a brass compass, the compass glass cracked with a hairline fracture, warm lantern light catching the crack and making it glow gold, behind the figure a lighthouse beam cuts through fog on one side while on the other side a storm churns, both things true simultaneously, the captain's expression calm and aware, tattered epaulettes, distorted surreal proportions, beautiful darkness composition, deep blue and oxblood palette, aged gold accent on the crack and light, bone white highlights, rough paper texture, visible ink grain, negative space upper left for text overlay --ar 16:9 --style raw --v 6
```

---

### SLIDE 7 - "No Employees"

**Tool:** Midjourney v6
**Aspect ratio:** 16:9 (`--ar 16:9`)

**Prompt:**

```
ink-wash gothic illustration, a mercenary campfire at dusk in a ruined courtyard, four or five shadowed figures loosely gathered around the fire, each figure slightly distinct in silhouette, some standing some crouching, the fire warm and amber, the surrounding ruins dark Prussian blue, no faces visible, implied presence not permanence, camp-without-walls energy, figures might leave any moment, smoke curling into gothic arches above, deep shadow with warm ember accents, rough paper texture, visible grain, negative space in upper portion for text, surreal atmosphere, masterwork ink illustration --ar 16:9 --style raw --v 6
```

---

### SLIDE 10 - "What It Feels Like to Work With Us"

**Tool:** Midjourney v6 (or DALL-E 3 as alternative for more literal still-life control)
**Aspect ratio:** 16:9 (`--ar 16:9`)

**MJ v6 Prompt:**

```
ink-wash gothic illustration, close-up of calm hands at a worn workbench, hands holding delicate repair tools over a partially disassembled mechanical object, the object complex and beautiful, gears and glass and wire, amber candlelight from one side, deep shadow on the other, the hands are skilled and unhurried, the opposite of urgency, quiet competence, the workbench surface scarred wood with scattered small tools, deep blue and oxblood palette, gold candlelight on the hands, rough paper texture, visible ink grain, surreal slightly dreamlike proportions, negative space upper right for text, masterwork illustration --ar 16:9 --style raw --v 6
```

**DALL-E 3 alternative (if you want more literal control over the bench objects):**

```
Dark atmospheric illustration in the style of gothic ink wash, candlelit workbench scene, close view of two calm skilled hands holding precision repair tools over a partially disassembled clockwork-like mechanism, the mechanism is beautiful and intricate, warm amber candlelight from left side, deep shadow on right, scattered tools on worn dark wood, color palette of deep Prussian blue and warm gold only, bone-white highlights on fingertips and tool edges, quiet competence and patience, no tech-bro aesthetic, dark surreal masterwork illustration, 16:9 composition with negative space in upper right corner
```

---

### SLIDE 11 - "The Dramatic Pivot"

**Tool:** Midjourney v6
**Aspect ratio:** 16:9 (`--ar 16:9`)

**Prompt:**

```
ink-wash gothic illustration, a ruined gothic cathedral interior, the shell of the old structure intact - arched windows open to dark sky, stone crumbling - but inside scaffolding rises and new construction begins within the ruin, warm amber lanterns hanging from the scaffolding casting light upward against the dark stone, the old bones visible, new life emerging inside them, beauty-from-ruin composition, surreal dreamlike scale with slightly distorted perspectives, deep Prussian blue stone and sky, oxblood accent on archways, aged gold from the lanterns, bone white on the scaffolding, rough paper texture, visible ink grain, negative space upper left --ar 16:9 --style raw --v 6 --seed <SLIDE_1_SEED>
```

**Style/seed notes:** Apply Slide 1 seed here. This image can double as a subtle background plate for Slide 14 if needed (darken in post).

---

### SLIDE 14 - "Starting Over"

**Tool:** Midjourney v6
**Aspect ratio:** 16:9 (`--ar 16:9`)

**Prompt:**

```
ink-wash gothic illustration, a solitary figure crouching in darkness striking a match, this is visibly the third attempt, two spent matchsticks on the stone floor beside the figure, the new match just catching, a small warm amber flame emerging in a field of deep blue-black shadow, the figure's face turned toward the tiny flame, third-attempt energy, quiet determination not despair, distorted slightly elongated figure proportions, surreal atmosphere, deep Prussian blue and bone-white palette with the single amber flame as the only warm accent, rough paper texture, visible ink grain, generous negative space in upper area for text overlay, masterwork illustration --ar 16:9 --style raw --v 6 --seed <SLIDE_1_SEED>
```

---

### SLIDE 15 - "Studios That Need Fixing"

**Tool:** Midjourney v6
**Aspect ratio:** 16:9 (`--ar 16:9`)

**Prompt:**

```
ink-wash gothic illustration, a tangle of thick old cables and broken connectors on a dark floor, among the cables a small fire being carefully tended by unseen hands barely visible at the frame edge, the fire warm amber, the cables Prussian blue-black, a torn and partially-visible roadmap or chart pinned to the wall behind showing routes with gaps and erasures, send-me-your-broken-things energy, the mess is present but not catastrophic - it is workable, deep shadow with warm focal light on the fire and map, rough paper texture, visible ink grain, negative space upper right for text overlay, surreal slightly dreamlike composition, masterwork illustration --ar 16:9 --style raw --v 6
```

---

### SLIDE 16 - "Peers Around a Fire"

**Tool:** Midjourney v6
**Aspect ratio:** 16:9 (`--ar 16:9`)

**Prompt:**

```
ink-wash gothic illustration, a small intimate circle of five or six figures seated and standing around a low campfire in deep darkness, the fire modest and warm amber, the figures in quiet conversation, no faces clearly visible, but body language reads as ease and trust not performance, the surrounding darkness is absolute and comfortable, warmth-as-network composition, no heroism just fellowship, distorted slightly surreal figure proportions, deep Prussian blue darkness, oxblood earth tones underfoot, aged gold firelight on edges and shoulders, rough paper texture, visible ink grain, negative space at top for text overlay, masterwork gothic illustration --ar 16:9 --style raw --v 6
```

---

### SLIDE 17 - "The Scars"

**Tool:** Midjourney v6 (primary) or DALL-E 3 for the ceramic vessel variant
**Aspect ratio:** 16:9 (`--ar 16:9`)

**MJ v6 Prompt (kintsugi vessel - recommended):**

```
ink-wash gothic illustration, a large dark ceramic vessel occupying most of the frame, the vessel has been broken and repaired with kintsugi gold joinery, the gold cracks glow faintly with warm inner light as if the vessel is alive in the repaired places, the unbroken ceramic is deep oxblood and Prussian blue, the kintsugi veins aged gold, the vessel sits on a worn stone surface in deep shadow, beauty-through-damage composition, surreal slightly dreamlike atmosphere, rough paper texture, visible ink grain, negative space in upper area for text overlay, masterwork gothic illustration --ar 16:9 --style raw --v 6 --seed <SLIDE_1_SEED>
```

**DALL-E 3 alternative (if you want more photo-real ceramic control):**

```
Dark atmospheric illustration in the style of gothic ink wash, a large handmade ceramic vessel with kintsugi gold repair, broken-and-healed cracks traced in glowing gold across the dark surface, the gold lines appear to emit soft warm light, vessel sits in deep shadow on worn stone, deep Prussian blue and oxblood ceramic body, aged gold kintsugi veins, bone-white highlights on rim, surrounding darkness is heavy and peaceful, 16:9 composition with generous negative space upper left, beauty-through-damage, masterwork gothic illustration
```

---

### SLIDE 18 - "The Playbook"

**Tool:** Midjourney v6
**Aspect ratio:** 16:9 (`--ar 16:9`)

**Prompt:**

```
ink-wash gothic illustration, hands writing in a worn leather notebook by candlelight, the notebook open to a densely annotated page, small dense text and diagrams visible but not legible, the handwriting deliberate and careful, a single amber candle casting warm light on the hands and page, deep shadow on all sides, the hands are experienced not young, the notebook is battle-worn, optional - a chess piece lying on its side on the table beside the notebook as if deliberately sacrificed, quiet competence under pressure, deep Prussian blue shadow, gold candlelight, bone-white page, rough paper texture, visible ink grain, negative space upper right for text overlay, masterwork gothic illustration --ar 16:9 --style raw --v 6
```

---

### TEXT SLIDE BACKGROUND PLATE (Slides 6, 8, 12, 13)

**Tool:** Midjourney v6 or DALL-E 3 (either works - this is a texture plate, not a hero)
**Aspect ratio:** 16:9 (`--ar 16:9`)
**Note:** Must be LOW CONTRAST. This is a substrate for big white text. Do not generate this with a visible figure or focal subject.

**MJ v6 Prompt:**

```
abstract ink wash texture, dark atmospheric background plate, heavy black ink dispersed into deep Prussian blue water on rough paper, faint suggestion of gothic architectural linework dissolving into shadow, no clear subject or figure, near-monotone, very low contrast, occasional faint gold speck like a distant ember, rough paper grain very visible, intended as a dark background for text overlays, masterwork abstract texture --ar 16:9 --style raw --v 6
```

**DALL-E 3 alternative:**

```
Abstract dark texture for presentation slide background, ink wash on rough paper, deep Prussian blue and near-black tones, faint ghostly gothic architectural suggestion dissolving into darkness, no focal subject, very low contrast, occasional tiny warm gold speck, heavy paper grain texture visible throughout, designed for white text overlay, near-monotone atmospheric plate
```

---

## Public Assets to Source

### Slide 9 - The Finals Key Art

**Asset:** The Finals official key art
**Studio:** Embark Studios / Nexon
**Where to find:**
- Steam page: https://store.steampowered.com/app/2073850/THE_FINALS/ (scroll to screenshots / banner)
- Official press kit: https://www.embark-studios.com/games/the-finals (check for Press Kit download)
- Alternative: SteamDB has hi-res capsule art at https://www.steamdb.info/app/2073850/info/

**Usage note:** Closed-room presentation, no public distribution. Standard fair use for press/commentary context applies.

---

### Slide 9 - Ready or Not Key Art

**Asset:** Ready or Not official key art
**Studio:** VOID Interactive / Team17
**Where to find:**
- Steam page: https://store.steampowered.com/app/1144200/Ready_or_Not/ (header image / capsule)
- Press kit: https://www.voidinteractive.net/ (check for press/media page)
- Alternative: SteamDB capsule at https://www.steamdb.info/app/1144200/info/

**Usage note:** Same closed-room fair use context as above.

---

### Slide 9 - Raw Fury Co-Dev Placeholder (NDA - DO NOT NAME TITLE)

**Do not use any specific title key art.**

Use one of the following instead:

**Option A - Raw Fury logo plate:**
- Raw Fury logo (press/media): https://rawfury.com/press/ - grab the logo PNG, place on a neutral dark background. Add text "Co-development project" below. No game name.

**Option B - Generic workbench image (generated):**
Generate a neutral game-dev workbench image using the Slide 10 prompt above, cropped differently. Use that as the placeholder visual with "Co-development" as the only label.

**Option C - Abstract placeholder (fastest):**
Use the text background plate generated above, add the Raw Fury logo as a small overlay in corner, and "Co-development project" as the slide text. Done.

**Recommendation:** Option A is cleanest and fastest. Grab the RF logo from their press page and composite on the dark background plate.

---

### Slide 5 Bonus - AP 2021 Press Shot (Jillian Mood)

**Gmail search attempted:** Token expired on this session - search could not run.

**Manual check for Robert:** Search your Gmail for `from:jillian@jillianmood.com` or `aurora punks press` or `press shot 2021`. Also check Google Drive for folders from 2021 with "press" or "Aurora Punks" in the name.

**If found:** Use that image directly. It is the most honest asset for this slide - a real photo from a real moment in the company's origin story.

**Fallback (if not found) - Generate:**

**Tool:** DALL-E 3 (better for naturalistic group/scene photography feel)

```
Dark atmospheric photographic illustration, a small creative collective gathered around a table in a dimly lit Stockholm studio space, late evening, warm practical lighting from a few desk lamps, three or four people in their early thirties, casual creative clothing, looking at laptop screens and printed materials spread on the table, the space has the feeling of a starting point - sparse furniture, exposed brick or concrete, a whiteboard with early sketches visible in the background, the mood is focused and alive not posed, analog-warmth aesthetic, slight grain, 2021 vintage photography feel, 16:9 composition
```

---

## AP Brand Color Reference

No canonical AP brand color file found in the project folder. From the deck brief and Robert's own description, working palette confirmed as:

- Deep Prussian blue: `#0d1b2a`
- Oxblood red: `#6b1a1a`
- Bone white: `#e8e0cc`
- Aged gold: `#c9a84c`
- Near-black background: `#070d13`

These are embedded in all prompts above. If Robert has a separate brand guide with hex codes, substitute on any generated image in post-processing (no need to re-run the prompts - color grading in post is faster).

---

## Quick Reference Checklist

- [ ] Slide 1 hero plate - GENERATE FIRST, note seed
- [ ] Slide 3 - Two engines
- [ ] Slide 4 - Lighthouse and loose cannon captain
- [ ] Slide 7 - Campfire / mercenary camp
- [ ] Slide 10 - Fixer at workbench
- [ ] Slide 11 - Ruined cathedral with scaffolding (use Slide 1 seed)
- [ ] Slide 14 - Third match being struck (use Slide 1 seed)
- [ ] Slide 15 - Tangled cables + small fire
- [ ] Slide 16 - Peers around a fire
- [ ] Slide 17 - Kintsugi vessel (use Slide 1 seed)
- [ ] Slide 18 - Hands writing in notebook
- [ ] Text background plate (run any time, lowest priority)
- [ ] Source: The Finals key art (Steam/Embark press)
- [ ] Source: Ready or Not key art (Steam/VOID press)
- [ ] Source: Raw Fury logo for co-dev placeholder
- [ ] Check Gmail/Drive for Jillian Mood 2021 AP press shot
