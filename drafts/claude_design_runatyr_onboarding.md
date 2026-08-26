# Claude Design — Runatyr/Hive Onboarding Bundle

One-time setup. Run this during the first Claude Design session so every future project inherits the brand automatically.

Target URL: https://claude.ai/design (research preview, Pro/Max included)
Org to create: **Runatyr Games**
Expected time: ~20 min

---

## Step 1 — Upload the ground-truth docs

In the org onboarding flow, upload these two files. They are the canonical source for both Runatyr surfaces:

- [skills/runatyr_styleguide.md](/home/assistant/projects/skills/runatyr_styleguide.md) — full cross-surface styleguide (Board Gothic + Hive Bauhaus tokens, fonts, components, motion, gotchas)
- [skills/hive_visual_language.md](/home/assistant/projects/skills/hive_visual_language.md) — Hive-only deep dive (hex composition, density framework, component catalogue)

These contain the palette hex values, font stack, component vocabulary, and "do/don't" rules. Claude Design will extract tokens from them automatically.

---

## Step 2 — Link the codebase

Point Claude Design at the cc-hive Next.js app — this is the production reference for the Hive Bauhaus theme.

- **Repo path:** `/home/assistant/projects/cc-hive`
- **Token source file:** [cc-hive/src/app/globals.css](/home/assistant/projects/cc-hive/src/app/globals.css) — contains every CSS variable (--bg, --text, --epic, --chore, --rnd, --outreach, --accent, --danger, --active)
- **Font loader:** [cc-hive/src/app/layout.tsx](/home/assistant/projects/cc-hive/src/app/layout.tsx) — Fraunces + Geist + Geist Mono wiring
- **Representative components:**
  - [cc-hive/src/components/HexCell.tsx](/home/assistant/projects/cc-hive/src/components/HexCell.tsx) — project hex
  - [cc-hive/src/components/TicketHex.tsx](/home/assistant/projects/cc-hive/src/components/TicketHex.tsx) — ticket hex
  - [cc-hive/src/components/TicketDetail.tsx](/home/assistant/projects/cc-hive/src/components/TicketDetail.tsx) — detail panel
  - [cc-hive/src/components/HiveFilters.tsx](/home/assistant/projects/cc-hive/src/components/HiveFilters.tsx) — filter pill row

If Claude Design asks for a URL instead of a local path: the public Hive is at https://hive.runatyr.games (live production, same code).

For the Board Gothic theme, there's no single repo — it's static HTML in `assistant/*.html`. If Claude Design needs a Board reference, upload [assistant/kanban.html](/home/assistant/projects/assistant/kanban.html) as a text file (the `<style>` block at the top has the full Board palette + fonts).

---

## Step 3 — Upload brand assets

Drop these in during the "logos / brand assets" step:

**Runatyr / Hive marks**
- [assistant/runatyr-logo.png](/home/assistant/projects/assistant/runatyr-logo.png) — primary wordmark
- [assistant/icon.svg](/home/assistant/projects/assistant/icon.svg) — app icon (vector source, self-contained, uses currentColor)
- [assistant/icon-512-v2.png](/home/assistant/projects/assistant/icon-512-v2.png) — latest rasterized icon
- [assistant/icon-192-v2.png](/home/assistant/projects/assistant/icon-192-v2.png) — smaller raster

**Board Gothic texture**
- [assistant/bg.png](/home/assistant/projects/assistant/bg.png) — canvas background for Board pages (used at 85% dark overlay)

---

## Step 4 — Reference screenshots (the "show-don't-tell" layer)

Claude Design's own docs recommend 3-5 reference screenshots. Upload these from the project root so Claude Design sees the two surfaces in their real, shipped state:

**Hive surface (Bauhaus, paper canvas)**
- [hive-chat-zoom.png](/home/assistant/projects/hive-chat-zoom.png)
- [hive-chat-linkified.png](/home/assistant/projects/hive-chat-linkified.png)
- [hive-topright-crop.png](/home/assistant/projects/hive-topright-crop.png)
- [hive-after-search-move.png](/home/assistant/projects/hive-after-search-move.png)

**Board surface (Gothic, dark canvas)**
- [kanban-top.png](/home/assistant/projects/kanban-top.png)
- [kanban-header-wide.png](/home/assistant/projects/kanban-header-wide.png)
- [agents-top.png](/home/assistant/projects/agents-top.png)
- [time-top-v2.png](/home/assistant/projects/time-top-v2.png)

If Claude Design caps the upload count, prioritize **hive-chat-zoom.png** + **kanban-top.png** — they carry the most tokens between them.

---

## Step 5 — Paste these tokens verbatim (fallback if extraction is off)

After Claude Design auto-extracts tokens, spot-check them against this list. If anything is off, paste this block into the design-system editor:

### Hive Bauhaus (paper canvas)
```
--bg:             #f4f2ec
--bg-elev:        #ffffff
--text:           #0a0a0f
--text-dim:       #55555f
--text-faint:     #9c9ca4
--hex-fill:       #0a0a0f
--hex-content:    #ffffff

Signal tones (RGB for alpha mixing):
--epic:           140 190 255  (sky blue, parent work)
--chore:          255 130 130  (rose red, ops)
--rnd:            120 235 170  (mint green, research)
--outreach:       255 215 90   (golden yellow, external)

--accent:         #ffcc40      (needs_input)
--danger:         #ff5555      (due-today)
--active:         #63e28c      (active agent pulse)

Fonts:
Display  — Fraunces (variable, opsz 144, SOFT 50)
Sans     — Geist
Mono     — Geist Mono
```

### Board Gothic (dark canvas)
```
--black:         #0a0a0a
--black-card:    #0f0f0f
--bone:          #d4cfc0   (primary text, warm cream)
--bone-dim:      #7a766a
--white:         #ece8df
--gold:          #c8a84e   (accent, active)
--gold-bright:   #e8c85e
--pink:          #c43c5e   (critical)
--border:        #222

Fonts:
Body      — Libre Baskerville (400, 700, italic)
Headings  — UnifrakturMaguntia (sparingly, titles only)
Mono      — Share Tech Mono
```

---

## Step 6 — Verify onboarding worked

Run this prompt in a fresh Claude Design project after setup:

> Generate a one-page "Sprint review" pitch deck cover for the Hive surface. Include the Hive app icon, the Fraunces title "Sprint 47 Review", a Geist Mono date pill, and a dark hex badge in the top-right. Use the Hive Bauhaus palette.

**Checklist — expect to see:**
- [ ] Paper canvas (`#f4f2ec`), not white
- [ ] Title set in Fraunces (display), not Inter/Roboto
- [ ] Hex shape rendered as pointy-top polygon with solid `#0a0a0f` fill
- [ ] Mono pill uses Geist Mono, uppercase, letter-spacing visible
- [ ] No gradients, no decorative motion cues in a static render
- [ ] No Libre Baskerville or UnifrakturMaguntia anywhere (those are Board-only)

If any of the above fails, the design-system extraction is incomplete — re-upload the styleguide .md and ask Claude Design to re-read it.

Then run the same kind of test for Board Gothic:

> Generate a Board "Agents" page header with a gold nav underline, bone-cream text on the `#0a0a0a` canvas, and an UnifrakturMaguntia title "The Hive". Include a Share Tech Mono timestamp pill and a critical-state pink border accent.

**Checklist:**
- [ ] `#0a0a0a` canvas, not `#000`
- [ ] Bone cream (`#d4cfc0`) text, not pure white
- [ ] Gold accent is `#c8a84e`, not yellow or amber
- [ ] UnifrakturMaguntia renders the title (blackletter), not a generic serif
- [ ] Mono pill is Share Tech Mono (technical, square), not Geist Mono

---

## Step 7 — Publish

Once both checklists pass, toggle the org design system to **Published**. Every future Claude Design project will inherit Runatyr/Hive tokens by default.

---

## After onboarding — hand back to me

When you're done, drop a note in this session (or create a DB ticket) with:
1. Any extracted tokens Claude Design got wrong (so we can patch the styleguide)
2. The first real deck/mock you want to generate — I'll write the design brief

Then I'll do **(a)** — draft the `design_brief` skill + update [agents/ui.md](/home/assistant/projects/agents/ui.md) with the handoff-bundle consumer workflow.

---

## Next brands to onboard (not today)

Each of these will want its own Claude Design organization or project once the Runatyr pattern is proven:

- **Aurora Punks / Tears of Adria** — post-release GTM, capsule art pipeline
- **BADASS Studios** — XR platform, P&L decks
- **Elias (audio middleware)** — biz-dev decks, Fredrik's slide template
- **K2C / Sands of Duat** — Raw Fury co-dev, milestone decks
- **CZP** — finance reviews, contract cover pages

Don't seed these yet. Validate the flow on Runatyr first, then I'll build per-client bundles from their own GDrive Deliverables folders.

---

## Sources

- [Introducing Claude Design by Anthropic Labs](https://www.anthropic.com/news/claude-design-anthropic-labs)
- [Set up your design system in Claude Design](https://support.claude.com/en/articles/14604397-set-up-your-design-system-in-claude-design)
- [Get started with Claude Design](https://support.claude.com/en/articles/14604416-get-started-with-claude-design)
