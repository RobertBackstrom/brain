---
name: reference_rankone_agent
description: "RankOne AI agent (R1) — Playwright-driven game-intel/audience tool at r1-agent.fly.dev; returns RankOne Insights audience size, demographics, affinity overlaps, KPI benchmarks, comparables."
metadata: 
  node_type: memory
  type: reference
  originSessionId: f6c3dd76-d13b-481c-adc5-8b60f1388384
---

RankOne's own AI agent, "R1 — Game Recommendation / Game Intel", is reachable for audience and market research. Robert granted access 2026-06-29.

- **URL:** https://r1-agent.fly.dev/  (React SPA, password-gated)
- **Passphrase:** `FgikmfTq35eCK9` (input placeholder "Enter passphrase", then the "Enter" button)
- **No MCP / API** — drive it with Playwright (headless). The bundled Playwright lives at `/home/assistant/.npm/_npx/9833c18b2d85bc59/node_modules/playwright` (same one the Fortnox scripts use). Working driver pattern saved at `curveball/drafts/` session scratch; reusable recipe below.

**Driver recipe (what works):**
1. `chromium.launch({headless:true, args:['--no-sandbox','--disable-dev-shm-usage']})` — Playwright's chromium launches fine even though direct `chrome --headless --screenshot` core-dumps in this sandbox.
2. Login: `fill('input[type=password]', PASS)` then `click('button')`.
3. Click `button:has-text("New chat")` for a fresh thread.
4. Composer is `textarea[placeholder^="Ask about games"]`. Fill + `keyboard.press('Enter')`.
5. **Completion signal:** the composer textarea goes `disabled` while generating and re-enables when done. Poll every 3s; treat done when `!textarea.disabled` AND body-text length stable for ~2 polls AND elapsed > 12s. Responses take 60-180s (it searches web + RankOne + reasons).
6. Capture: `document.body.innerText` after the echoed query.

**What it returns:** RankOne Insights behavioral data — audience size (DAU/MAU/CCU), age + platform + region splits, psychographic over-index (attribute affinity), cross-game affinity/overlap, KPI benchmarks for a genre/price, named comparables with CCU/price/rating/owners, and reachable-profile counts. Cites profile counts as its source. Good for grounding pitch KPI + audience sections without manual GDCo paste.

RankOne is a CZP portfolio co Robert advises ([[project_rankone]]); this agent is the consumer face of its "AI data monetization" thesis ([[reference_company_structure]]). Used across two pitches so far: Curveball / Blade Ball ([[curveball-the-gang-studio]]) and Flightball / Formula Drone (audience-overlap intel folded into the FD commercial proposal). Candid production feedback on the tool (data quality, no-API friction, provenance, latency, prioritized fixes) written up at `rankone/drafts/r1_agent_feedback.md` (+ one-page PDF `r1_agent_feedback_onepager.pdf`); emailed to Johan Tjäder 2026-07-03. Credential handling per [[feedback_secrets_registry]].

**Feedback channel + outcome (WhatsApp group "Rankone Insights Feedback", id `120363411382979749@g.us`, ~2026-06-24 on).** Peter Warman set this group up as the R1/Insights feedback loop: Johan shares research/prototypes, Robert + Peter comment, conclusions go to the advisory board before execution. Robert's feedback overview landed well — Peter Warman voiced "complete agreement," independently flagged the same **source / confidence-level opacity**, and is "convinced AI+API is the route." **Johan already shipped a last-minute change to better define "measured" vs "modeled" off the feedback → re-test to confirm it's better.** Facts captured from the thread:
- Internal name for the agent = **"RankAI"**.
- Built by an external studio, **Zensai** (on summer vacation from ~2026-07-02; a few-week window remains to keep testing + shaping its behavior).
- **NEW data asset:** RankOne has saved a **daily snapshot of the entire games database + every game relation since early 2024**. This powers **trend / change-over-time tracking** within audiences (Johan's "Pulse" report direction) plus user/competitor **watchlists** — reframing the non-determinism concern from a bug into the actual recurring-use product.
- Participant `@lid` map: `237842437558414` = Peter Warman, `163483853291693` = Johan Tjäder, `31645352612046` = Robert.
- Open (Peter → Robert): 3-5 concrete cost/revenue-impact use cases; a value×moat matrix; user personas + how to expose the service without giving away the moat. Tracked in [[project_rankone]] / rko-003.
