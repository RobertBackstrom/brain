# Content Editor — Learnings

Cross-project knowledge for the Content Editor agent. Append after each task with date + project tag + category.

Format:
```
## YYYY-MM-DD — <project> — <category>
<learning>
```

Categories: `tooling`, `deck-building`, `client-preference`, `process`, `voice`, `cost`.

---

## 2026-06-22 — paradox_ironcrest_case — tooling
**python-pptx is NOT pre-installed on the VPS, and pip itself was missing.** Bootstrap sequence that worked: (1) `sudo apt-get install -y python3-pip` (apt is available; the kernel-version warning it prints is harmless), then (2) `python3 -m pip install --break-system-packages python-pptx`. The `--break-system-packages` flag is required on this Python 3.12 (PEP 668 externally-managed). PIL/Pillow 10.2 IS pre-installed. There is NO LibreOffice/soffice on the VPS, so you cannot render a .pptx to PNG locally for visual QA — verify structurally instead (read shapes back via python-pptx) and then verify the converted Google Slides via the Slides API.

## 2026-06-22 — paradox_ironcrest_case — deck-building
**pptx -> native Google Slides pipeline (clean, works).** Build the .pptx with python-pptx, then `node assistant/gdrive-upload.js <file.pptx> --convert`. The CONVERT_MAP in that script maps the pptx mimetype to `application/vnd.google-apps.presentation`, so `--convert` alone gives a native editable Google Slides deck (no per-slide image insertion, no public-URL dance — that gotcha in artdirector_learnings only applies to inserting generated IMAGES via the Slides API, not to whole-deck conversion). No folder arg = uploads to Robert's My Drive root. Returns the docs.google.com/presentation edit link directly.

## 2026-06-22 — paradox_ironcrest_case — deck-building
**Verify the converted deck via the Slides API, not by re-reading the pptx.** GET `https://slides.googleapis.com/v1/presentations/<id>` with Robert's OAuth bearer (refresh from `~/.claude/.gdrive-server-credentials.json` + `gcp-oauth.keys.json`). Returns `.slides.length`, `.pageSize` (16:9 = 12191675 x 6858000 EMU), and per-slide `pageElements` (count `.table`, `.shape`, `.image`). This confirms tables actually converted to native Slides tables (they do — python-pptx `add_table` survives the conversion intact) and the theme rectangles carried over. Good final-QA step when no local renderer exists.

## 2026-06-22 — paradox_ironcrest_case — deck-building
**Reusable clean-business deck recipe (slate + bronze).** 16:9, warm off-white paper bg (#F6F4EF) for content slides, deep slate (#1C2530) for title/section/statement slides, single muted-bronze accent (#B0864A). Type hierarchy: Georgia serif for titles (the restrained "grand strategy"/premium nod), Calibri sans for body. Per-slide pattern: 0.18in bronze left-edge bar + small bronze ALL-CAPS kicker + serif title + hairline rule. Helpers that paid off: a `content_header()` for the standard header, a `table()` that manually colors header row (slate) + alternating rows (no python-pptx banding — it renders ugly), and a `bullets()` using a "▪  " bronze square run as the marker (python-pptx blank-bullet behavior is unreliable; drawing the marker as a colored run is cleaner). Script saved at `paradox_ironcrest_case/drafts/build_deck.py` — good template to copy for the next boardroom deck.

## 2026-06-22 — paradox_ironcrest_case — process
**No-overflow check before shipping a generated deck.** Since there's no local renderer, after building, iterate every shape and flag any whose `left+width > 13.4in` or `top+height > 7.55in` (off-canvas). Caught nothing this time because boxes were placed conservatively, but it's a cheap guard against text boxes running off the edge — the main risk with programmatic decks. Keep body text to short lines / 14-16pt and lean on multiple slides rather than cramming (per presentation_building density rules).

## 2026-06-22 — paradox_ironcrest_case — tooling
**In-place Google Slides update preserves the share link — do NOT re-upload + re-convert (that mints a new fileId/link).** To revise a deck already converted to native Slides: rebuild the .pptx, then Drive `files.update` (HTTP PATCH to `https://www.googleapis.com/upload/drive/v3/files/<fileId>?uploadType=multipart&supportsAllDrives=true`) with a multipart body where the metadata part is `{"mimeType":"application/vnd.google-apps.presentation"}` and the media part is the pptx (Content-Type `...presentationml.presentation`). Drive re-converts the uploaded pptx into the SAME presentation file — same id, same `docs.google.com/presentation/d/<id>` link, content fully replaced. `gdrive-upload.js` has no in-place mode (its uploadFile POSTs to `/files` = new file), so I wrote a tiny `update_slides.js` reusing the exact same OAuth flow (refresh from `~/.claude/.gdrive-server-credentials.json` + `gcp-oauth.keys.json`). Saved at `paradox_ironcrest_case/drafts/update_slides.js` — reusable for any "fix the deck, keep the link" task.

## 2026-06-22 — paradox_ironcrest_case — voice
**Speaker notes carry the "why" for a presenter who is NOT the author.** This deck is presented by Robert's friend, and the panel cares about reasoning over numbers. So each slide's notes (1-3 lines) state the point to MAKE and the reasoning behind landing there — not a script to read. Pattern: "lead with X because [panel motive], the key line is Y, this sets up slide Z." Voice rules still apply in notes too: no em-dashes (use " - "), no hype words.
