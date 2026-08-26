---
name: feedback_html_pitch_living_doc
description: "Preferred way to pitch projects to new clients is a styled HTML living-doc page on pitch.aurorapunks.com, not a deck or PDF."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 4f38dc9a-1efe-480a-b81d-2df508a08be0
  modified: 2026-08-17T23:09:54.618Z
---

Robert's preferred format for pitching a project to a new client/partner is a **styled single-page HTML pitch**, served at `pitch.aurorapunks.com/<slug>` (scheme: `pitches/<slug>/index.html`, public, no-login). He values it because it is a **living document** (one durable link he keeps refining, no re-export/re-send) and it simply looks great. Note the live URL no longer updates instantly since the 2026-08-24 host split, see the sync step below. Established on the Tears of Adria → Light Up Games pitch (2026-06-10).

**Host (canonical as of 2026-06-18, apw migration):** `pitch.aurorapunks.com`. The old `pitch.runatyr.games` still works but permanently **301-redirects** to the aurorapunks host (`pitches-server.js` enforces `PITCHES_CANONICAL_HOST`). Always give out / verify the `pitch.aurorapunks.com/<slug>` URL. Note: extensionless `/<slug>` 301s to `/<slug>/` (Express directory redirect) before serving 200 - that's normal, follow redirects when verifying. Use `pitch.aurorapunks.com` for AP-side pitches.

**Why:** A deck/PDF is a frozen snapshot you re-attach every revision; an HTML page is one durable link you keep refining as the conversation evolves. Owners/partners always see the current version. It also looks more crafted than slides and reinforces the AP brand. This now beats "Publish to web" decks (see [[feedback_deck_format_publish_web]]) as the default for *project pitches to new clients*.

**How to apply:**
- Default a new-client/partner project pitch to an HTML page under `pitches/<slug>/`, not a Google Slides deck. Reuse the ToA page (`pitches/tears-of-adria/index.html`) as the house style: Cinzel/Cormorant + gold/panel dark-fantasy tokens, eyebrow + section pattern, key-art hero, stat band, roadmap timeline, recommendation callouts, AP footer. Adapt theme tokens per title.
- Lead with whatever the pitch is selling (e.g. put the 6-month roadmap on top for a publishing pitch). Pull real key art/screens from the Steam media into a local `steam-media/` folder.
- **Since the 2026-08-24 split, editing `pitches/` does NOT change the live site.** The Brain (Claude sessions, Death Board) runs on the **Nitro**; the public web (`pitches.service` + `cloudflared`) stayed on the **Hetzner VPS**, reachable as tailnet host `brain`. Author on the Nitro, then push:
  ```
  assistant/sync-pitches.sh                      # dry run, shows both directions
  assistant/sync-pitches.sh --apply <slug>       # push + verify byte-match on the VPS
  ```
  The script never deletes on the VPS and byte-compares the slug afterwards. Always run the dry run first if anyone might have edited on the VPS side. Forgetting this step means telling a client a page is updated when it is not, which happened once before the script existed.
- Verify before sharing: curl the live `pitch.aurorapunks.com/<slug>` URL with its Basic Auth creds to confirm 200 **and grep the new content out of the response**, not just the status code.
- **Rendering a visual check now has to happen on the VPS**, not the Nitro: neither Playwright nor the chromium cache exists on the Nitro (confirmed 2026-08-24). Run the render over `ssh brain`, where `~/.cache/ms-playwright/` and the `_npx` playwright copies live. Without that, a Nitro-side session can only verify structurally and should say so rather than implying it looked at the page.
- **Render with Playwright's chromium, not with the chrome binary directly** (corrected 2026-08-18, Irons 2). `chrome-linux64/chrome --headless=new --screenshot` may work once and then hang indefinitely on later calls (exit 124/143/144), and killing stale processes plus a fresh `--user-data-dir` does not reliably fix it. This matches [[reference_rankone_agent]], which already found direct chrome unusable in this sandbox. What works:
  ```js
  const { chromium } = require('/home/assistant/.npm/_npx/9833c18b2d85bc59/node_modules/playwright');
  const b = await chromium.launch({ headless:true, args:['--no-sandbox','--disable-dev-shm-usage'] });
  const p = await b.newPage({ viewport:{ width:1420, height:1400 } });
  await p.goto('file:///home/assistant/projects/pitches/<slug>/index.html', { waitUntil:'networkidle' });
  await (await p.$('.some-section')).screenshot({ path:'out.png' });  // element shot beats full-page
  ```
  Element-level screenshots (`element.screenshot()`) are the practical way to check one component; full-page shots of a long pitch get downscaled too far to judge. Note that an element with `overflow-x:auto` only captures its visible width, so a wide table that scrolls will look truncated in the shot. That is a real signal worth fixing, not a rendering artifact.
- Also verify structurally, not only visually: count opening vs closing tags per element type and grep for em-dashes before publishing. Catches a broken table faster than a screenshot does.
- Keep voice rules: no hype, no em-dashes ([[feedback_no_em_dashes]]), focused features+content ([[feedback_design_proposals_focused]]).
- Slug/host details in [[reference_runatyr_domains]].
