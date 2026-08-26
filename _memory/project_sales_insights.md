---
name: SalesInsights (SIGH)
description: Automated console sales report parsing and Google Sheets updating system for game clients
type: project
---

Automated pipeline for processing console storefront royalty reports and updating client Google Sheets.

**First client:** Atomic Elbow (Sir Whoopass). System designed for multi-game/multi-client use.
**DB prefix:** `sigh` (tooling-level tasks only)
**Project path:** `C:\Users\johan\projects\sales-insights\`

**Stores:** Sony SIEE/SIEA/SIE Asia/SIEJ (XLSX via email), Xbox (manual portal download), Nintendo (manual portal download), IndieArk (PDF via email, future)

**Key contacts:**
- Niklas Karlsson (niklas@atomicelbow.com) — requests report updates
- Ellen Berglund (ellen.berglund@carler.se) — financial compilation/accounting
- Per Berggren — owner at Atomic Elbow

**Revenue split (Sir Whoopass):** AE 45% / AP 55%
**Sheet:** `1bwbbgWoAfml-AKvKjVi0IxPxQ62cYAQ-iYLnOrOHPnE`

**Why:** Robert manually copies revenue figures from store reports into Google Sheets. This is time-consuming and error-prone. Automating the parse→FX→sheet pipeline saves hours per month per game.

**How to apply:** When console report tasks come up, use the SIGH pipeline. When new games are onboarded, add config to `games.json`.
