# Output Log — RankOne

Track significant deliveries, drafts, and external posts here. Each entry: date, what, where it went, outcome.

| Date | What | Where | Outcome |
|------|------|-------|---------|
| 2026-06-15 | Project scaffolded (CLAUDE.md, output_log, web-scan, drafts) | `projects/rankone/` | Done |
| 2026-06-15 | Downloaded 5 RankOne source docs (State of RankOne, Cap Table, Share Register, Annual Report 2025, audit report) | `projects/rankone/source_pdfs/` | Done |
| 2026-06-15 | Created meeting "RankOne - Robert + Peter sync", Mon Jun 16 11:00–12:00 CEST, Google Meet, invited Peter Warman | Google Calendar (meet.google.com/izj-djtz-otb) | Invite sent, Peter needsAction |
| 2026-06-15 | Web scan on RankOne + Peter Warman | `web-scan.md` | Done |
| 2026-06-15 | Ingested source PDFs + web-scan into RAG | rag-indexer | (see entry below) |
| 2026-06-16 | Meeting moved to Wed Jun 17 10:00-11:00 CEST; invite updated | Google Calendar | Done; Peter had accepted |
| 2026-06-16 | Full mail+Drive sweep for Johan Tjäder + Peter Warman material | source_material_inventory.md | Done |
| 2026-06-16 | Saved investor decks (Introductory Jun'25, Future of Creation v2.1 Nov'25) | source_pdfs/ | Done |
| 2026-06-16 | Funding history added to wiki/company/rankone.md + RAG backfill | RAG | Done |
| 2026-06-17 | Lawyer: data-rights scoping memo for the AI-data pivot (GDPR lawful basis, purpose-limitation, anonymisation bar, Chapter V transfer, AI Act, review IP) | `drafts/rankone_data_rights_assessment.md` | Verdict: viable-with-conditions; gating issue = purpose limitation; next step = read live ToS/privacy policy |
| 2026-06-16 | Read full investor deck (Future of Creation v2.1); deck analysis + cap table + business model to prep note & RAG | drafts/, wiki | Done |
| 2026-06-16 | Scaffolded RankOne Drive folder (projects SD) w/ _legals/_financials/_deliverables (+_working/_archive) | Drive 1TdWJlHpSzEKcvx33wzXoG4vjjXhKdZHS | Done |
| 2026-06-16 | Published guidance one-pager as Google Doc | Drive _deliverables/_working (1yeKgQ...) | Done |
| 2026-06-16 | Placed core financial/legal/deck copies (AR2025, audit, cap table, share register, 2 decks, State of RankOne) | Drive _financials/_legals/_deliverables | Done |
| 2026-06-16 | Copied 13 Drive-scattered RankOne docs (SHA, SPA, round model, cap tables, ÅR2022, budget, PR) into _legals/_financials/_deliverables (current vs _archive) | Drive | Done (originals preserved) |
| 2026-06-16 | Added assistant/gdrive-copy.js helper (server-side copy, incl. shared-to-you files, Shared Drive aware) | assistant/ | Done |
| 2026-06-17 | Built "KPI dashboard ask for Johan" (7 metrics / 4 groups + first-cut 5) | drafts/rankone_kpi_dashboard_ask_johan.md | Draft, for 10:00 sync |
| 2026-06-17 | Confirmed pending sentiment numbers (iOS 0 ratings; Play 1K+ installs/no rating; Median webview wrapper; Discord invite dead) | prep note addendum | Done |
| 2026-06-17 | Captured Robert+Peter sync (Jun 17) RankOne outcomes — ops-execution gap + AI-data pivot + action items (contractor/org item was Aurora Punks, excluded) | wiki/company/rankone.md + project_rankone memory + rko-002 | Done |
| 2026-06-17 | AI-data licensing thesis one-pager (the asset, buyer set, model, defensibility, risks, validation plan) — artifact to walk Peter + Johan through | drafts/rankone_ai_data_thesis_onepager.md | Draft |
| 2026-06-17 | Ticketed AI-data pivot (rko-003), parked in backlog awaiting Peter's advisory-board kickoff; next steps captured, no further spend until then | assistant/followups/rko-003 | Parked |
| 2026-06-17 | Reconciliation analysis: what the AI-data-monetization pivot changes (KPIs, acquirer set, the fork) | drafts/rankone_ai_data_pivot_reconciliation.md | Draft |
| 2026-07-03 | Candid R1-agent feedback for the RankOne team (agent-POV, R1-tool-only) — from production use on the Curveball + Flightball pitches. Differentiated data (over-index/affinity/reachable profiles, Roblox coverage), inconsistencies (wide unlabeled ranges, proprietary-vs-modeled opacity, shifting n, non-determinism, prose-only output), prioritized fixes (ship API/MCP first, separate measured vs modeled, data-only mode, cut latency, expose confidence/n) | drafts/r1_agent_feedback.md | Draft — ready to forward |
| 2026-07-03 | One-page PDF of the R1 feedback for the devs (A4, dev-facing, no dashes) | drafts/r1_agent_feedback_onepager.pdf | Done |
| 2026-07-03 | Emailed the one-pager PDF to Johan Tjäder (Cc Peter Warman) — "Some honest feedback on the R1 agent", English, Robert's voice | Gmail (work) | **Sent by Robert** (corrected Cc to Peter Warman, not Spegel) |
| 2026-07-03 | Fetched all media from the Insights Feedback WhatsApp thread (Pulse "Pragmata Timeline v3" report PDF, trend-excerpt image, short video) + wrote structure README documenting the FROM/PAST/PRESENT/FUTURE trend feature | `r1_feedback_media/` (+ README) | Done. Added a `/messages/:id/media` endpoint to the WA bridge to make this possible |
| 2026-07-03 | Proposed answers to Peter Warman's 3 asks: 5 P&L-impact use cases, a value×moat matrix (taste graph / timeline / reachable / inflow), user personas + moat-safe access model | drafts/rankone_answers_to_peter.md | Draft — for Robert to review + bring to next Peter sync |
| 2026-07-03 | Sent the 3-part answer to Peter in the WhatsApp group (split per ask); Johan responded "infrastructure not a tool" + dumped RankOne's 15-use-case catalog | WhatsApp group `120363411382979749@g.us` | Sent (as Robert) |
| 2026-07-03 | Discovered Pim de Witte + Moritz Baier-Lentz co-founded General Intuition ($320M Series A @ $2.3B, Jun 2026; Moritz = Lightspeed gaming head). Wrote connection plan + forwardable Peter brief; narrowed Johan's catalog to 3 hero use cases | drafts/rankone_general_intuition_connection.md, drafts/rankone_usecase_catalog.md | Done (in RAG) |
| 2026-07-03 | **Sent** the intro-brief to the WhatsApp group handing Peter the forwardable GI blurb (opens both Pim + Moritz doors), Robert-approved | WhatsApp group `120363411382979749@g.us` | **Sent** (as Robert). Robert edited it tighter (joint "we" framing) + is working his own Swedish AI contacts in parallel. Awaiting intro |
| 2026-07-03 | **Sent** the use-case narrowing to the group (3 hero visualized features + agent for the long tail), Robert-approved | WhatsApp group `120363411382979749@g.us` | **Sent** (as Robert) |
| 2026-07-03 | Built the RankOne data pitch — general "human-curated gaming data" brief (NOT GI-specific), RankOne branding (Exo/Lato, purple #5142CA, logo). Gated | **pitch.aurorapunks.com/rankone** (`pitches/rankone/index.html`; auth rankone / g2oyPx3zBVh) | Live (verified 200) |
| 2026-07-03 | Pitch v2 per Robert: flipped to **dark** RankOne brand, **emphasized the 3 hero use cases** (numbered 01/02/03 centerpiece w/ P&L pills), embedded the **Pragmata Pulse test case** (assets/pulse-pragmata.jpg, framed). Clients section pending Robert's names (found only Limit Break Studio + "5 early-stage partners 2020" — won't fabricate) | pitch.aurorapunks.com/rankone | Live (200). Clients = open |
