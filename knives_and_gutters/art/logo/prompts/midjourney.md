---
project: knives_and_gutters
lane: C — Midjourney v6.1+ (manual via Discord)
aspect: 1:1
seeds_per_prompt: 4
prompts: 3
total_images: 12
created: 2026-05-08
---

# Lane C — Midjourney prompts (3 angles × 4 seeds)

**Manual lane.** Robert runs these in Discord himself; ArtDirector ingests the output PNGs back into `art/logo/concepts/midjourney/`. Robert: paste each block as `/imagine`, then re-roll seeds 3× per prompt to get the four-seed batch.

MJ favors descriptive natural language with style anchors. Parameters at the end. Type fidelity is weaker than Flux — read composition, mood, ornament; the artist redoes the type.

## Angle 1 — Composition-led

```
A weathered grimdark fantasy game cover badge logo, rectangular ink-bordered frame, hand-painted in the style of Gary Chalk's Mordheim covers. Wordmark reads "Knives & Gutters" with a single curved blade as vertical separator between the two words. Flanking the type: a notched knife and a hooked spike, drawn in thick real-ink outlines with painted gouache highlights. Bone-white, oxide-red, charcoal palette. Hand-lettered type with off-register 80s metallic catch-light technique. Centered, isolated on flat dark background. Crude, weighty, hand-crafted. --ar 1:1 --stylize 250 --v 6.1
```

## Angle 2 — Detail-led (TOP PRIO)

```
An ornate hand-painted wordmark logo for a grimdark gang skirmish RPG, "Knives & Gutters", in the style of John Blanche's Warhammer illustrations. Every letter individually designed and hand-rendered. Baroque grotesque surreal flourishes growing out of the letterforms — tiny mutant gangers, blades, hooks, ruined-city silhouettes embedded inside the type itself. Tarnished metal rectangular frame. Real-ink outlines, oil-and-gouache painted texture. Coin-stamp embossed feel on the type. Grimdark palette with blood-rust accents. Detail density rewards extended looking. Centered, isolated on flat dark background. --ar 1:1 --stylize 500 --weird 100 --v 6.1
```

## Angle 3 — Crudeness-led

```
A crude hand-painted badge logo in the unmistakable style of Gary Chalk and the late-1980s Warhammer Fantasy Roleplay covers. Title reads "Knives & Gutters". Thick brush ink outlines bleeding slightly off-register. Painted gouache highlights with visible brush strokes. Hand-lettered type with chipped-iron 80s metallic catch-light. Single blade vertical separator. Rough rectangular ink frame. Notched knife and hooked spike flanking. Limited dirty palette: parchment, oxide red, charcoal, bone. Governed by 1980s analog tabletop-cover tooling — no vector cleanliness, no chrome, no modern digital effects. Centered, isolated dark background. --ar 1:1 --stylize 150 --v 6.1
```

## Parameter notes

- `--stylize`: Angle 1 = 250 (balanced), Angle 2 = 500 (let MJ flourish), Angle 3 = 150 (rein in MJ's polish, push toward crude).
- `--weird 100` on Angle 2 to lean into Blanche surrealism.
- `--v 6.1` default. If `v7` is current at run-time, swap.
- For each `/imagine`, re-roll 3× to get 4 base images per prompt = 4 seeds.

## Ingestion

After Robert runs in Discord:
1. Save the four 4-up MJ grids as `mj_angle1.png`, `mj_angle2.png`, `mj_angle3.png`
2. Drop into `knives_and_gutters/art/logo/concepts/midjourney/inbox/`
3. ArtDirector splits each grid into 4 individual PNGs and adds to the contact sheet
