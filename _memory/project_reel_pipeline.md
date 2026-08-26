---
name: Reel/Shorts production pipeline
description: JSON-driven reel builder for Instagram Reels, TikTok, YT Shorts — tools, workflow, known issues, resume point
type: project
---

## Pipeline tools
- `tears_of_adria/content/build_reel.py` — Main reel builder. Takes a JSON config, outputs final reel.
- `tears_of_adria/content/build_carousels.py` — Carousel builder (Pillow, 1080x1350)
- `tears_of_adria/content/build_static_discord.py` — Static post builder (Pillow, 1080x1350)
- `assistant/clip-indexer.py` — Scene detection + AI labeling for finding footage
- `assistant/footage-watcher.py` — Auto-monitors GDrive for new uploads

## Reel builder workflow
1. Create a JSON config with segments (source, start, duration, crop_x, text_events)
2. Run `python build_reel.py --config <json>` — extracts, burns ASS subtitles, builds endcard, concats
3. Add music optionally (GDrive has music_ancient_rite.mp3, music_strength_of_titans.mp3)

## Key files per reel
- Config JSON: defines segments, crop positions, subtitle text+timing
- ASS files: auto-generated from config, brand fonts (Cinzel Decorative 110pt title, Montserrat 78pt body)
- Endcard: auto-generated with Pillow (logo, title, 94% reviews, Steam CTA)

## Brand specs
- Vertical: 1080x1920, 9:16, 29.97fps
- Carousel: 1080x1350, 4:5
- Fonts: `skills/fonts/` (CinzelDecorative-Bold, Montserrat, BebasNeue, Cinzel, MedievalSharp)
- Colors: Gold #FFD700, Red #CC0000, Background #0A0A0A
- Full guidelines: `tears_of_adria/brand_guidelines.md`
- Content calendar: `tears_of_adria/content_calendar_social.md`
- Captions: `tears_of_adria/content/captions.md`

## Known issues to fix next session
1. **Camera centering** — must verify party position at exact timestamps, not scene frames. See feedback_reel_camera.md
2. **Slower panning** — Robert wants more stable viewport, less jumping between segments
3. **Resolution softness** — inherent to 608px→1080px upscale from 16:9 source. Lanczos helps but limited.
4. **AI labeling not run yet** — 591 scenes detected but not labeled. Run clip-indexer with --game-context to find specific content (e.g. Imp/Ark Zahk scenes). Costs ~$0.60.
5. **No music on reels yet** — can add from GDrive or let Robert add trending audio in-app

## Draft status (as of 2026-03-31)
| Content | Path | Status |
|---------|------|--------|
| Fri 28 Imp reel | — | Needs dedicated recording |
| Sat 29 HoMM reel | `sat29_homm/reel_no_music.mp4` | Draft, camera needs work |
| Mon 31 Carousel | `carousel_homm_fans/` 6 slides | Draft, review pending |
| Tue 1 Review reel | `tue01_review/reel_no_music.mp4` | Draft, same camera fixes |
| Wed 2 Discord CTA | `wed02_discord_cta.jpg` | Draft, review pending |

**Why:** First project using the content pipeline. Learnings here become skills for all future projects.

**How to apply:** When resuming, read this file + the reel configs + output_log.md to get full context. The build scripts are reusable across projects — just swap the JSON config and game_context.txt.
