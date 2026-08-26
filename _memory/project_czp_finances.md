---
name: CZP Finances
description: Creation Zero Point Holding corporate finance umbrella — tax/Skattekonto, multi-currency banking, Fortnox integration, Sifferrådet bookkeeping. AP-scoped P&L lives under AP Board (apb-002-pnl), not here.
type: project
originSessionId: e65977b1-d850-4955-9969-fd388ceb24ea
---
## CZP Finances

**Master sheet:** Google Sheet ID `1FxMQVb1l22iuOXiwBkZCQyUoBnOa5X-z`
**Local export:** `czp-finances/` (CSVs: PnL, 3.Revenue, 2. Simple Salary & Operational, Cashflow, Inputs)
**DB prefix:** `czp`
**Epic:** `czp-000-epic` (CZP-only ops umbrella since 2026-04-29 restructure)

**Scope (CZP-only):**
- Skattekonto / Kronofogden / social fees (`czp-001`)
- Multi-currency banking (SEK/USD/EUR) (`czp-002`)
- Fortnox integration (OAuth unresolved — DevOps)
- Sifferrådet bookkeeping coordination
- Master CZP P&L upkeep (multi-project, multi-currency)

**Out of scope (moved 2026-04-29):**
- AP-scoped P&L → `apb-002-pnl` under AP Board epic
- K2C intercompany push → folded into `apb-002-pnl`

**Structure of master model:**
- PnL sheet: Costs (salary + operational) vs Revenue (royalties + consulting), monthly columns Jan 2026 → Dec 2027
- Revenue: Two streams — Publishing/Capital (Steam Catalog, Strikeforce Heroes, BEEP, HeadUp, DR Shares, TBA) and Consulting (AP, Ark Island, Reactional, Elias, Malformation, Soulwalker, Shosha, Netlight, rents, Oskar Hansen)
- Costs: Salaries (Robert 55k, Gustav 53k + 5% annual raise), contractors (Nethash, Eternal Minds, Polycrunch, ML AB, Bra Liv, 7Wise, Zenland, AP Overhead, Oskar Hansen), business (legal, Sifferrådet accounting 2.5k, auditing), office, 5% margin of error
- Cashflow: Monthly OB/CB with tax flows (VAT, social fees)
- Inputs: FX rates via GOOGLEFINANCE, cost parameters (social security 31.42%, vacation 0.8%, pension 5%)

**Accounting:** Fortnox is the source of truth for CZP. Sifferrådet (Henrik Franzén, henrik@sifferradet.se) manages it. Fortnox remote MCP added to .mcp.json (https://fortnox-mcp.vercel.app/mcp) — needs OAuth browser auth on first use. Local bookkeeping system at `bookkeeping/` (SQLite, BAS accounts, SIE4 export) exists but is separate.

**Fortnox visible costs (from leverantörsfakturor screenshot, Mar 2026):**
- Bright Gambit AB (Oskar/WMAY): 45k × 2 (invoices 71, 72)
- Skokloster Konsult AB: 64,453 SEK
- Ha Bra Liv Stockholm AB: 6,000 SEK
- 7wise Advokatbyrå: 16,600 × 2 (WLBS Creation Zero)
- NeCo Software AB: 62,602 SEK
- Robert Bäckström: 42,450 SEK
- Petter Mikaelsson: 14,504 SEK
- Fortnox AB: 567 + 259 SEK
- Skattekonto: 595,000 + 10,000 SEK

**GDrive (recreated 2026-03-31):**
- AP Board folder: `15JWcx2V4lcOd9fz9RloDiUwVfijeGLSH` (inside CZP Projects_2 `1CAS46jrj9qsPip9tMYnlxL6otLysoqL7`)
- Financials subfolder: `1sfWNlGWSxXMSLU8sEkmtJSa6IEMasJCI`
- P&L file: `1cvidQBkyrnJ43rCUnBq15wX4M60aCTIE`
- Also has: Meeting Notes, Agreements, Deliverables subfolders

**Why:** CZP is the umbrella holding; AP is one of its subsidiaries with its own board-facing P&L. Keeping CZP corporate ops (tax, banking, Fortnox) separate from the AP board P&L (apb-002) avoids cross-scope confusion.
**How to apply:** CZP-level finance tasks (tax, banking, Fortnox, Sifferrådet) use czp-000-epic. AP P&L delivery, K2C IC, board-facing financial work → apb-002-pnl under AP Board. The czp-finances/ CSVs are formula-heavy exports — read live Google Sheet for actuals.

## CZP bank details (canonical, verified 2026-07-16)
**SEB** · clearing **5266** · konto **1032177** · BIC **ESSESESS** · IBAN **SE9650000000052661032177** · bankgiro **55329924**. Address: SEB, 106 40 Stockholm.
Corroborated across 2021 (Raw Fury share-sale) and 2024 (Soupmaster) mail threads. Needed for CZP's pending Steam financial onboarding (apb-026), which is gated until the app transfer lands. See [[reference_steam_partner_accounts]].

## Bankunderlag -> RAG (beslut 2026-07-21)

CZP **har** kontounderlag, och Robert har beslutat att de **ska in i RAG** sa agenter kan soka pa dem. Nya underlag tas fram **vid varje manadsavslutning**.

1. **Placering:** Financial Shared Drive -> CZP -> `Bank_Statements/` (`1A0upnEolWKzN0p8zoiu8zRmMwXyozUzt`). Filer utanfor Financial-driven indexeras inte som finansunderlag.
2. **Kadens:** lagg det nya underlaget dar vid varje manadsavslutning. 30-min-syncen plockar upp det automatiskt - ingen manuell reindex.
3. **Format spelar ingen roll:** CSV, Google Sheet, .xlsx och skannade PDF/bild blir alla innehallssokbara (CZP-driven har OCR pa). Se [[reference_rag_content_coverage]].
4. Samma rutin galler ovriga bolag - se [[reference_drive_folders]] for per-bolag mapp-ID:n. Zenland `Bank_Statements/` ar fortfarande tom.

Ticket: `czp-022`.
