# Pecha Kucha 2026 - Output Log

## 2026-05-23 - Deck v1 delivered (Robert + Claude)

20-slide Pecha Kucha for Behold Summit 2026-05-25 (Malmö).

Prompt 1 ("Founder and Journey") - selected because neither Robert nor AP attended last year. Lina (Behold.vc) already briefed on the choice.

### Narrative spine (Robert's interview answers, 2026-05-23)
1. **Drive:** Full control / punk DIY. No label, start one. No show, host one.
2. **2026 engines:** Comeback (proof it works) + love of making things.
3. **Self-portrait:** Likeable, unfocused, conflict-avoider, sometimes loose cannon. Never gives up.
4. **Visual aesthetic:** John Blanche distortion + Dalí fantastic-escapist + beautiful darkness.
5. **AP 2026:** "A loose band of mercenaries. Battle scarred. Less naive. Unbreakable."
6. **Edge:** "We don't sell hours. We fix things."
7. **Proof:** The Finals (cross-platform commerce + console port release mgmt) + Ready or Not (console port + KB-to-controller UI) + Raw Fury co-dev (title kept vague per NDA flow-downs).
8. **The hard thing:** "What are we?" + "How do you build value with no employees?" + "How to pick up from such a dramatic pivot?"
9. **Ask:** Businesses + network.
10. **Unfair experience:** Closed 3 studios through bankruptcy. Laid off 50 devs. Knows the playbook.
11. **One-line takeaway:** "Don't wait too long before killing the darling."

### Deliverables
- **Google Slides deck:** https://docs.google.com/presentation/d/1iCRnZUj3wn9SZdL9QOsPKQ0YHSiM72TOVqzRnFN3ku8/edit (Robert is owner, gmail account is writer)
- **Publish URL (auto-advance 20s):** https://docs.google.com/presentation/d/1iCRnZUj3wn9SZdL9QOsPKQ0YHSiM72TOVqzRnFN3ku8/pub?start=true&loop=false&delayms=20000 (requires File > Publish to web one-click activation in the UI)
- **Script:** [script.md](script.md)
- **Visual brief:** [visual_brief.md](visual_brief.md) - 13 paste-ready MJ v6 prompts + The Finals/Ready or Not source URLs + Raw Fury placeholder options
- **Build script:** [build_slides.py](build_slides.py) - reusable for future Pecha Kucha decks

### Open follow-ups for Robert (next 24h)
1. File > Publish to web on the deck (one-click in Slides UI) to activate the auto-advance URL.
2. Drag the 13 generated images from the Drive folder into their respective slides (5 min job - all images are already in the folder next to the deck).
3. Slide 9 only: source The Finals key art (Steam/Embark press), Ready or Not key art, Raw Fury logo from rawfury.com/press/ - see visual_brief.md for exact URLs. Robert confirmed these are public assets for closed-room fair use.
4. Slide 5 note: the fallback image (generated studio team scene) is naturalistic/photographic in style, which will read differently from the gothic illustration slides around it. This is intentional - it's meant to feel like a real archived moment. If Robert wants it stylized to match, quick reroll with the ink-wash gothic prompt will do it.
5. Rehearse twice to the 20-second clock. Pecha Kucha is brutal on under-rehearsed speakers.

### Open follow-ups for me (Claude)
1. Re-auth Gmail and search for the 2021 Jillian Mood AP press shot (slide 5) - currently has fallback generated, but the real archival image would be stronger.

## 2026-05-23 - All 13 visuals generated (ArtDirector)

Generated all 13 images via fal.ai Flux.dev in 54 seconds wall-clock. 0 failures. $0.325 total.

### Files
- **VPS visuals folder:** `/home/assistant/projects/clients/aurora_punks/pecha_kucha_2026/visuals/`
- **Drive folder (same images):** https://drive.google.com/drive/folders/1hkJe4NrfJ3VrGZfgTjuiJANoK_yJlSkE
- **Contact sheet:** `visuals/concepts_grid.png` (also in Drive folder)
- **Generation log:** `visuals/generation_log.json` (prompts, seeds, Drive IDs, cost per image)

### Anchor seed: 1931856528
Used on slides 11, 14, 17. Palette and atmosphere carry through reliably; subjects are distinct (cathedral, figure with match, kintsugi vessel). Good visual consistency across emotionally adjacent slides.

### QA notes per image
- **slide_01_hero.png** - Strong. Solitary figure, ember glow at chest, gothic arches. Good negative space upper right. Lock this as the cover.
- **slide_03_engines.png** - Winged figure on vessel prow, compass + hammer. Reads clearly. Amber wingspread works.
- **slide_04_leadership.png** - Captain with cracked compass. Both lighthouse and storm visible. Slightly busy but on-brief.
- **slide_05_ap_2021.png** - Naturalistic (photographic style, not gothic illustration). Intentional for this slide. Four people, warm lamp, whiteboard. May read as stylistically odd between gothic slides. Flag to Robert.
- **slide_07_no_employees.png** - Figures around bonfire, ruined building backdrop. Fire is large and dramatic (not the amber campfire ember the brief requested). Functional but could reroll for a more intimate campfire feel.
- **slide_10_fixer.png** - Hands at workbench with mechanical object. Strong. Quiet competence reads correctly.
- **slide_11_pivot.png** - Gothic cathedral ruin interior. Stunning architecture. Amber lanterns in deep blue stone. Best image in the set.
- **slide_14_third_attempt.png** - Hooded figure crouching, match striking, two spent matches visible. Exactly on-brief. The "third attempt" narrative reads immediately.
- **slide_15_studios_need_fixing.png** - Cables on floor, fire in center, map on wall. More literal than gothic but the composition works. The map reads as a roadmap with gaps.
- **slide_16_peers_fire.png** - Intimate circle of figures around fire. Fellowship reads correctly. Good.
- **slide_17_scars.png** - Kintsugi vessel with glowing gold cracks. Photorealistic feel (not ink-wash), but the image itself is striking. The glowing repair seams are arresting.
- **slide_18_playbook.png** - Hands writing in notebook by candlelight, chess piece on table. Strong. Quiet competence framing.
- **text_plate_dark.png** - Abstract ink wash, very low contrast. Works as text substrate. Upper right has a slight bone-white bleed that may need darkening in post if text contrast is insufficient.

### Reroll candidates
1. **slide_07** - Fire is too large/bonfire-scale; brief wanted campfire/ember intimacy. Easy reroll.
2. **slide_05** - If Robert wants gothic illustration style to match the rest of the deck (rather than naturalistic photo feel).
3. **text_plate_dark** - If the upper-right bone-white bleed causes text contrast issues.

### Source agents
- Slides build: general-purpose (sonnet) - 525s runtime
- Visual brief: ArtDirector role on general-purpose (sonnet) - 251s runtime
- Image generation: ArtDirector (sonnet) - 54s fal.ai wall-clock + ~15 min total pipeline

## 2026-05-25 - Final deck readthrough + diff vs draft (Claude)

Robert rebuilt the deck without using any of the 13 fal.ai images. Read through his final published deck via Playwright, captured all 20 slides to `robert_final_deck_screens/slide_NN.jpg`, diffed against the original draft.

### What stayed
- 20-slide structure and slide-by-slide ordering (with minor re-ordering of the takeaway line)
- The mercenary-band identity for AP 2026
- The K2C / Raw Fury vague-naming posture (he just dropped Raw Fury entirely; kept the 7 other co-dev titles named)
- The "kill the darling" takeaway line (moved from slide 19 to slide 16, then visually punchlined on slide 19)

### What got replaced
- **All 4 full-bleed text slides** I drafted (edge, hard questions, takeaway) became image + small title bar
- **Every AI-generated visual** was swapped for either a real artifact or a cultural icon
- **The Achievements slide** went from 2 named titles + Raw Fury placeholder to 8 named co-dev titles with engine + role + scope per title, plus an 8-capsule-art grid

### The new visual stack
1. **Slide 1 + 20** - Drakar och Demoner book covers (childhood RPG) - structural bookend
2. **Slide 2** - Real hardcore-scene photos from Robert's archive (ALQUATTA CD, live shot, HATE YOU! records, amps)
3. **Slide 3** - Karate Kid crane kick (comeback) + photo of his real Unity workstation (craft)
4. **Slide 4** - Tom Hanks (likeable) + Boris Johnson (loose cannon) - self-deprecating juxtaposition
5. **Slide 5** - Real GamesBeat (Dean Takahashi) 2021 AP press article screenshot
6. **Slide 6** - Actual John Blanche illustration (Warhammer mercenary trio) + AP neon logo
7. **Slide 7** - Dark-fantasy scribe at desk concept art ("We take the leap with you")
8. **Slide 8** - Adeptus Mechanicus 40K art ("A rowdy crew of fixers")
9. **Slide 9** - 8-title co-dev portfolio: Ready or Not, The Finals, Helldivers 2, GOALS, Darktide, Huntdown, Garden of the Sea, Budget Cuts Ultimate. Each with engine, role, platform notes. AP watermark behind.
10. **Slide 10** - REAL photo of a stone church mid-demolition. Dated "2022 - The painful pivot."
11. **Slide 11** - Empty 1980s/90s corporate office ("The New Deal" - visual joke that AP doesn't need this anymore)
12. **Slide 12** - The Last of Us post-apocalyptic concept art ("Exploring a brave new world")
13. **Slide 13** - Interstellar Endurance ship near wormhole ("How do you build when you are all alone")
14. **Slide 14** - Dark fantasy dungeon-with-green-core concept art ("Scaffolds upon scaffolds")
15. **Slide 15** - Tyrion Lannister, Hand of the King pin ("We have learnings (not always asked for)")
16. **Slide 16** - Frodo at Mount Doom holding the Ring on its chain ("Kill your darlings")
17. **Slide 17** - Mr. Wolf from Pulp Fiction with coffee cup ("We are looking for problems")
18. **Slide 18** - Fantasy court scene with queen on throne ("We are looking for community")
19. **Slide 19** - Isildur and Elrond at Mount Doom ("Or not?") - callback joke to slide 16
20. **Slide 20** - DoD adventuring party splash ("A new adventure begins") - bookend close

### Structural patterns to remember
1. Bookend (slide 1 + 20 from same source world)
2. Two-slide visual callback joke (slides 16 + 19, LOTR Mount Doom dialectic)
3. Section headers in big gothic blackletter (red/grey/green), 3-4 slides only
4. Black title bar + white sans-serif top-left on all non-header slides
5. NO full-bleed text slides
6. Specific dates on hard truths ("2022 - The painful pivot")
7. Self-deprecating humor woven through (Boris, Tyrion, "not always asked for")
8. Reframed asks from defensive to curious ("WHAT ARE WE?" → "Exploring a brave new world")

### Learnings captured
- New feedback memory: [feedback_visual_voice_cultural_icons.md](/home/assistant/.claude/projects/-home-assistant-projects/memory/feedback_visual_voice_cultural_icons.md) — AI-generated metaphor is the wrong tool for presentation character beats; real artifacts + cultural icons + published concept art are the right stack. AI is for atmospheric transitions only.
- ArtDirector learnings appended: client-preference (0 of 13 survived), brief-authoring (PK structural patterns), process (talk-to-client-about-artifacts-first as step 0 of presentation visual briefs).

### Screenshots
All 20 slides captured at `robert_final_deck_screens/slide_NN.jpg` for future reference. These ARE the deck Robert is presenting today.
