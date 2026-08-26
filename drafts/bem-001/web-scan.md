# BlockEm — Web Scan (bem-001)

Scanned 2026-05-02 for the `pitch.runatyr.games/blockem` one-pager.

## Title corrections

- Official title is **`Block'Em!`** (with apostrophe + exclamation), not `BlockEm`. Steam, Wavedash, and Aurora Punks copyright line all match. The `bem` ticket prefix and `block_em` folder name keep the underscore form for path safety, but **page copy must use `Block'Em!`** to match the brand.
- Confirmed on Steam DB legal notice: "© Copyright 2021-2023 Cat Shawl Games, Aurora Punks All Rights Reserved."

## Platforms — both, not Wavedash-only

The ticket flagged this. Confirmed:

| Platform | URL | Released | Status |
|---|---|---|---|
| Steam | https://store.steampowered.com/app/1529220/BlockEm/ | Sept 8, 2022 | Live, $6.99 |
| Wavedash | https://wavedash.com/games/block-em (store) / `/play/block-em` (in-browser) | March 2026 | Live, $6.99 |

Memory file `project_blovck_em.md` says "released on Wavedash (March 2026)" with no Steam mention — needs update.

The Wavedash launch is the fresh angle (instant-play, no install, browser-native). The Steam footprint gives it credibility (~4 years live, 13 languages, 122 reviews, 89% positive, "Very Positive").

## Steam — appdetails (app 1529220)

- **Title:** Block'Em!
- **Tagline:** "An action-filled block-building party game for 2 to 4 players! The controls are simple but the road to victory is complex."
- **Developer:** Cat Shawl Games
- **Publishers:** Aurora Punks, IndieArk
- **Genre:** Action / Casual / Indie (party platformer)
- **Players:** 2-4 (Online PvP + Shared/Split Screen + Remote Play Together)
- **Categories:** Multi-player, PvP, Online PvP, Shared/Split Screen PvP, Steam Achievements (10), Full controller support, Steam Trading Cards, Remote Play Together, Family Sharing
- **Languages (14):** English, Japanese, Simplified Chinese, Traditional Chinese, Korean, French, Italian, German, Spanish, Portuguese-Brazil, Russian, Turkish, Swedish + 1 more
- **Price:** $6.99
- **Demo:** appid 1776680
- **DLC:** appid 2132150
- **Support:** hektor@aurorapunks.com / blockemgame.com

## Steam — review summary

**Re-verified 2026-08-26** (supersedes the May scan below):

- **Score description:** "Very Positive" (Steam's own tier, returned by the API)
- **Total reviews:** 122 (108 positive / 14 negative = 89%)
- **Method matters.** Query the `appreviews` endpoint with `language=all`:
  `https://store.steampowered.com/appreviews/1529220?json=1&language=all&purchase_type=all&num_per_page=0`
  The store page HTML and the default API call return a *locale-filtered* subset. On 2026-08-26 that
  subset read 43-63 reviews at 86% while the true all-time total was 122 at 89%. Always pass
  `language=all`, and cross-check `review_score_desc` rather than computing the tier yourself.

### Superseded (May 2026 scan)

- ~~Score description: "Positive"~~
- ~~Total reviews: 40 (34 positive / 6 negative = 85%)~~
- ~~The ticket's "94% positive (34 reviews)" was pre-2026 data.~~ The May scan then read the
  locale-filtered subset and concluded "Mostly Positive", which understated the title on both counts.

## Pull quote candidates (from Steam reviews)

The English long-form review (xxadonisxx, Dec 2025, 8/10) is the strongest source. Quotable bits:

- "A compact, high-energy multiplayer game that focuses on immediacy, chaos, and social competition." — pull as Steam Reviewer / 8/10
- "Tense, laugh-out-loud moments during competitive play."
- "Trash talk, alliances, betrayals, and last-second reversals all naturally emerge from its design."
- "Emergent chaos is where Block'Em! finds its strongest identity."
- "A fast, accessible party platformer built around shared laughter and competitive chaos."

Press coverage is thin — no major outlet reviews surfaced. Recommendation: lean on Steam-reviewer + Aurora Punks framing. Don't fabricate critic quotes.

## Wavedash — store page

- **Schema.org JSON-LD on page** confirms publisher = Aurora Punks, datePublished = 2022-09-08 (Wavedash carries the original release date, not the Wavedash port date — odd, but consistent with their schema).
- Wavedash's own short description matches Steam's "Eat. Sleep. Block'Em. Repeat." marketing copy.
- 1 hero video (mp4, ~49 MB raw — too heavy to embed; using Steam webm clips instead).
- 4 supplementary thumb assets.

## Asset inventory pulled into `pitches/blockem/assets/`

| File | Source | Size | Use |
|---|---|---|---|
| `steam-capsule-616x353.jpg` | Steam | 60 KB | Hero key art |
| `steam-header.jpg` | Steam | 37 KB | Fallback / mobile |
| `ss-01..05.jpg` | Steam (5x) | ~225 KB ea | Screenshot grid |
| `clip-5b8e2734.webm` | Steam description | 290 KB | Gameplay clip 1 |
| `clip-c754164e.webm` | Steam description | 120 KB | Gameplay clip 2 |
| `clip-1751985b.webm` | Steam description | 280 KB | Gameplay clip 3 |
| `clip-ed61f857.webm` | Steam description | 210 KB | Gameplay clip 4 (extra / standby) |
| `clip-f1cef842.webm` | Steam description | 590 KB | Banner / wide clip |
| `wavedash-square-cover.webp` | Wavedash | 490 KB | Standby (square format, Wavedash branding) |
| `ap-logo.png` | reused from 1993 pitch | — | Footer |

Total folder ~3.2 MB — well within mobile budget.

## GDrive AP-side assets (catalogued, not pulled)

`block_em/Blockem Art/` Drive folder has player character renders (PinkPlayer, GreenPlayer, PurplePlayer, YellowPlayer) + Main_Capsule + Vertical_Capsule. Main_Capsule was 400x229 — lower-res than the Steam capsule, so didn't use it. The four character PNGs could be a fun decorative element if the page needs more visual personality on a v2 pass, but Steam capsule + screenshots are sufficient for v1.

Logo assets exist (`Blockem2_Logo_EN.png/.ai`, `BlockEmLogo.png`, animated logo mp4s) — not pulled for v1; the wordmark on the Steam capsule reads cleanly enough.

## Visual identity notes

- Bright, saturated palette: hot pinks, electric purples, yellow + cyan accents. Pixar-cute "Blockies" with expressive faces — opposite of 1993's dark retro-tech aesthetic.
- Page palette should be **light or warm**, not the 1993 deep-space dark theme. Going with a warm cream / off-white background + magenta-pink accent to match the Block'Em capsule.
- VT323 / Share Tech Mono fonts from the 1993 template are too retro-tech for a party platformer. Switching to a rounded display font (Fredoka or Baloo) for headers, Inter for body.

## Honest framing

- Older title (3.5 years on Steam), modest review count. Wavedash launch is the angle — instant-play in-browser, no installs, lowers the friction floor for a party game by a huge amount. Sit-down-on-someone's-laptop multiplayer use-case is where Wavedash clicks for a title like this.
- Don't oversell as "fresh release." Frame as "old AP IP, fresh life on Wavedash." Honest disqualifier opener works better than reach (per gen-189 learning).
