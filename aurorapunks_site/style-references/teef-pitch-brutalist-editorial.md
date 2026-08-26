---
title: Candidate UI style for the new Aurora Punks site — "Teef pitch" brutalist editorial
project: aurorapunks_website
owner: UIbot
status: candidate / not yet chosen
source: derived from the Teef co-dev pitch page (pitch.aurorapunks.com/teef), liked by Robert 2026-06-18
visual: ./teef-pitch-style.png
---

# Candidate style: "Teef pitch" brutalist editorial

Robert flagged the look of the Teef co-dev pitch page as a style he'd want to consider for the
new Aurora Punks website. Saved here as a **candidate direction** for UIbot to pull when the AP
site redesign UI work starts. Not a decision — one option on the table.

**Reference image:** [teef-pitch-style.png](./teef-pitch-style.png) (the rendered pitch hero + cards).
Live original: `pitch.aurorapunks.com/teef/` (gated — see pitch-auth for creds).

## What the look is
A high-contrast, print-inspired **brutalist editorial** style. Reads like a confident indie-zine /
record-sleeve layout rather than a soft SaaS site. Oversized condensed display type, hard rules,
halftone and diagonal-hatch textures, a single hot accent against warm paper.

## Design tokens (lifted from the pitch CSS)
- **Palette**
  - Ink / near-black: `#0d0d0f`
  - Paper (warm off-white background): `#f4f1ea`; pure white card: `#ffffff`
  - Accent magenta: `#e6186e`, bright magenta: `#ff2d83`
  - Deep maroon: `#2a191c`
  - Muted greys: `#5f5b56`, `#9a948c`
- **Type**
  - Display / hero: **Anton** (heavy condensed, all-caps wordmark)
  - Headings: **Archivo** (600–900)
  - Mono / labels / data: **Space Mono**
  - Body: **Inter**
- **Texture / motifs**
  - Halftone dot field (`radial-gradient` dots, ~9px grid)
  - Diagonal slash hatch (`repeating-linear-gradient`, 135deg)
  - Hard 1px ink borders on cards, no soft shadows; section numbering; flat blocks

## Why it could fit AP
AP is a collective of indie studios — the style signals craft, edge and confidence without looking
corporate. Translates well to a portfolio/studio grid and to bold section headers.

## Caveats for UIbot
- This palette (magenta-on-cream) was tuned for the Teef brief; for AP, treat the **structure +
  type + texture system** as the reusable part and re-pick the accent against AP brand colour.
- It is intentionally loud; verify it still works for long-form copy and a games portfolio grid.
- Accessibility: check magenta-on-paper and white-on-magenta contrast ratios before adopting.

See also: [[project_aurorapunks_website]], UIbot learnings.
