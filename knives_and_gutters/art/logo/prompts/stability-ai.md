---
project: knives_and_gutters
lane: B — stability-ai (SDXL / SD3)
aspect: 1:1
seeds_per_prompt: 4
prompts: 3
total_images: 12
created: 2026-05-08
---

# Lane B — stability-ai prompts (3 angles × 4 seeds)

SDXL responds to comma-separated keyword stacking + short descriptive scaffolds. Weighted syntax `(term:1.3)` works. Type fidelity is weaker than Flux — evaluate composition and style, not letter-shapes.

## Angle 1 — Composition-led

```
(badge logo:1.3), (rectangular frame:1.2), grimdark fantasy game cover, hand-painted, "Knives & Gutters" wordmark, single blade vertical separator between two words, flanking knives and hooks, Gary Chalk style, Mordheim cover, real ink outlines, painted gouache highlights, 80s tabletop cover technique, hand-lettered type, off-register coin-stamp metallic highlight, muted bone-white oxide-red charcoal palette, weighty crude hand-crafted, centered isolated on dark flat background, 1:1 square, illustrative, painterly
```

## Angle 2 — Detail-led (TOP PRIO)

```
(ornate wordmark logo:1.4), "Knives & Gutters", (every letter individually hand-painted:1.3), John Blanche style, Warhammer illustration, baroque grotesque surreal flourishes, tiny mutant figures and weapons embedded in the letterforms, ruined-city silhouettes inside the type, (real ink outlines:1.2), painted highlights, oil and gouache texture, tarnished metal rectangular frame, grimdark palette, blood-rust accents, (coin-stamp embossed type:1.2), detail density, rewards close inspection, 1:1 square, centered, isolated flat dark background
```

## Angle 3 — Crudeness-led

```
(crude hand-painted badge logo:1.3), "Knives & Gutters", Gary Chalk Mordheim cover style, Warhammer Fantasy Roleplay 1989, (thick brush ink outlines:1.2), bleeding off-register, painted gouache, visible brush texture, hand-lettered type, (80s metallic highlight technique:1.2), bone-white catch-light on chipped iron, single blade vertical separator, rough rectangular ink frame, notched knife and hooked spike flanking, limited dirty palette parchment oxide-red charcoal bone, (analog tabletop cover tooling:1.2), no vector lines, no chrome, no digital effects, centered, isolated dark background, 1:1
```

## Negatives (apply across all 3)

```
clean vector, chrome 3D, glossy plastic, AI typography, mechanical sans-serif, Y2K, glitch, dragon, skull, photoreal, modern digital effects, smooth gradient, neon, cyberpunk, pristine, polished, corporate
```

## Notes

- SDXL base is older; expect more "AI-ish" tells than Flux. We're using it as a cross-check, not a primary.
- Type WILL garble. Read silhouette, frame, ornament, palette — not letterforms.
- Default model: `sdxl-base-1.0`. If results feel too generic, try `sd3-medium` for better prompt adherence.
- 1024×1024 default.
