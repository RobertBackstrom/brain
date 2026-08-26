---
project: knives_and_gutters
lane: A — fal-ai (Flux.dev primary, SDXL backup)
aspect: 1:1
seeds_per_prompt: 4
prompts: 3
total_images: 12
created: 2026-05-08
---

# Lane A — fal-ai prompts (3 angles × 4 seeds)

Flux handles natural language and typography reasonably well. Write descriptive sentences, not keyword salad.

## Angle 1 — Composition-led

Cribs layout language from Knivar och rännstenar key-art mockup; Gary Chalk crudeness on the ornament and weaponry.

```
A weathered tabletop game cover badge logo for a grimdark fantasy game titled "Knives & Gutters". Rectangular outer frame in chipped, ink-stained parchment. The two words split by a single curved blade running vertically through the center as a separator. Hand-painted illustrative weapons — knives, jagged spikes, hooks — flanking the type, drawn in thick real-ink outlines with painted gouache highlights in the style of Gary Chalk's Mordheim covers. Muted dirt-and-blood palette: bone-white, oxide red, charcoal. Type is hand-lettered, slightly off-register, with 80s tabletop-cover metallic highlight technique. Composition centered, isolated on flat dark background. Crude, weighty, hand-crafted, not digital-clean.
```

## Angle 2 — Detail-led (TOP PRIO)

Anchored on roc_logo02 detail density + John Blanche surrealism.

```
An ornate hand-painted wordmark logo reading "Knives & Gutters" for a grimdark gang skirmish RPG. Every letter is individually designed and hand-rendered with painterly detail — no two characters alike — in the style of John Blanche's Warhammer illustrations: baroque, grotesque, surreal flourishes growing out of the letterforms. Tiny figures, mutant gangers, blades, hooks, and ruined-city silhouettes embedded into the type itself. Real-ink outlines, painted highlights, oil-and-gouache texture. Rectangular outer frame in tarnished metal. Muted grimdark palette with blood-rust accents. Coin-stamp embossed feel on the type. Detail density rewards extended looking. Centered composition, 1:1 square, isolated on flat background.
```

## Angle 3 — Crudeness-led

Pure Gary Chalk / Mordheim-cover energy. Loosest, roughest of the three.

```
A crude hand-painted badge logo for a grimdark fantasy gang skirmish game titled "Knives & Gutters", in the unmistakable style of Gary Chalk's Mordheim and Warhammer Fantasy Roleplay covers from the late 1980s. Thick brush ink outlines bleeding slightly off-register. Painted gouache highlights with visible brush texture. Hand-lettered type with the 80s metallic-highlight technique — bone-white catch-light on chipped iron lettering. Single blade running vertically between "Knives" and "Gutters" as a separator. Rough rectangular ink-bordered frame. Two crude weapons — a notched knife and a hooked spike — flanking the type. Limited dirty palette: parchment, oxide red, charcoal black, bone. Govern by what was achievable with 1980s analog tabletop-cover tooling — no clean vector lines, no chrome 3D, no modern digital effects. Centered, isolated on flat dark background.
```

## Negatives (apply across all 3)

```
clean vector lines, chrome 3D, glossy plastic, AI-generic typography, mechanical sans-serif, Y2K aesthetic, glitch effects, generic dragon, generic skull, photorealism
```

## Notes

- Flux handles "Knives & Gutters" type passably; expect 1–2 of 4 seeds with garbled letters — that's fine, we read silhouette + style.
- Run with `flux-dev` model first. If detail too soft on Angle 2, escalate to `flux-pro`.
- 1:1 square. 1024×1024 default; bump to 1536 if detail-density is the deciding factor.
