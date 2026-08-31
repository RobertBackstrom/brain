---
name: sir-whoopass-atomic-elbow-publishing-support
description: "Console reports, sales insights, key art for events, and lite publishing support for Sir Whoopass (Steam 1240590) — client Atomic Elbow"
metadata: 
  node_type: memory
  type: project
  originSessionId: f70b1208-4d3d-4a12-8302-187620320155
---

## Sir Whoopass: Immortal Death — Publishing Support

**Game:** Sir Whoopass: Immortal Death (Steam app 1240590)
**Developer/Client:** Atomic Elbow
**Robert's role:** Biz-dev / lite publishing support (retainer + commission)
**DB prefix:** `swa`

### Scope
- **Console reports:** Parse Sony (SIEE/SIEA/Asia), Xbox, Nintendo royalty reports → FX convert → update Google Sheet
- **Sales insights:** Track and analyze sales performance across all platforms
- **Key art for events:** Create promotional art for Steam sales, console events, bundles
- **Lite publishing:** Help with event signups, bundles, promotions across storefronts

### Revenue Split
- Atomic Elbow: 45%
- Aurora Punks: 55%

### Platforms
- Steam (app 1240590)
- PlayStation (SIEE, SIEA, SIE Asia) — AE now has their own PS access
- Xbox — AE granted access 2026-08-17 by inviting support@atomicelbow.com into the AP Partner Center directory via finance@ (Manager), scoped to the Sir Whoopass product group. Workaround, not an ownership move: V2 reparenting still frozen, SW stays parented under AP/CZP. MSA Transfer and own-tenant routes both dead (swa-002).
- Nintendo

### Console Report Sheet
- Google Sheet ID: `1bwbbgWoAfml-AKvKjVi0IxPxQ62cYAQ-iYLnOrOHPnE`
- Layout: months as columns (May 2025→), rows per store (SIEE/SIEA/Asia/Xbox/Nintendo), with FX date/rate/SEK conversion
- Data current through ~Dec 2025, Jan-Mar 2026 missing

### Key Contacts
- **Niklas Karlsson** (niklas@atomicelbow.com) — primary contact, requests report updates
- **Per Berggren** (per@atomicelbow.com) — owner
- **Ellen Berglund** (ellen.berglund@carler.se) — financial compilation/accounting

### PC Rev Share Reports (GDrive)
- `FinancialReport_RevShare_SirWhoopass_Oct-25.xlsx` — master financial report
- Sheets: Report Sir Whoopass PC, Skuldberäkning (debt/repayment), Aurora Recoupable, Atomic Recoupable, Steam Monthly Reports
- Covers Sep 2023 onwards. Rev share changed from 35% Aurora to 25% Aurora
- Tracks: units, gross/net sales (USD), FX rate, SEK conversion, recoup amounts, invoicing status
- Stores tracked: Steam, Epic, GoG, Humble, Fanatical, GMG, Games Planet, Gamers Gate, Win Game Store
- Debt tracking (Skuldberäkning): Invoice 133 (593,804 SEK excl. moms), partial payments + kvittning from PC sales

### Sony Reports (Email → GDrive)
- **SIEA:** Monthly XLSX from no-reply-bi@sony.com → finance@aurorapunks.com. Vendor UB1314. 6 reports on GDrive
- **SIEE:** Monthly PO + statement from NO-REPLY-BI@sony.com → finance@aurorapunks.com. Vendor 6195104490
- Pre-Oct 2025 SIEE reports went to robert@aurorapunks.com under White Lines Black Spaces AB (vendor 6195102633)
- Latest available: SIEA Jan 2026, SIEE Feb 2026

### Key Resources
- Drive deliverables: `sir_whoopass/{steam,xbox,playstation,nintendo}` (platform subfolders) + "Sir Whoopass: Immortal Death - AP handover" folder
- Sales-insights tooling + art assets live on the VPS / SalesInsights project (not local Windows paths)

### Current Status (August 2026)
- **Xbox access solved 2026-08-17** via direct directory invite of `support@atomicelbow.com` scoped to the SW product group. Handover mail to Niklas + Per sent 2026-08-18. Pending: AE accepts the invite, confirms they can update the title, and that AP's other titles stayed hidden. Then close the loop with Reed Hunt (v-reedhunt@microsoft.com, ID@Xbox). Thread 19ddfcc812e25c3a.
- **Dead routes:** MSA Transfer (whole-account move would drag AP's other titles; SW-only LOI signed 2026-06-10 now obsolete) and the `auroraelbow.onmicrosoft.com` tenant (stalled on MS billing verification at step 7/10).
- **App Developer Agreement (löst 2026-08-31):** AE kunde skapa bundles och add-ons men **publiceringen** blockerades av det ogodkända uppdaterade utvecklaravtalet på kontonivå. Robert godkände **version 8.11** den 31/08/2026 i eget namn via Account settings -> Agreements, efter beslutet att godkänna först och byta entitet efteråt (kontot står i White Lines Black Spaces AB:s namn, inte APDS). Spärren är borta. Avtalshistoriken visar 8.9 (2024-11-07) och 8.10 (2025-09-30) accepterade av Hektor Andreasson, båda efter WLBS konkurs. Se apb-055 / swa-002.

**Xbox-royaltyn: inget betalningsstopp (utrett 2026-08-31).** Utbetalningarna upphörde efter 13 mars 2026 för att intäkten upphörde, inte för ett entitetsglapp. Kontrakt 7781010 gick från 1 584 enheter i januari till noll från maj, och saldot 140,16 USD ligger under kontraktets minimibelopp på 200 USD. Orsaken är att SW:s TLA gick till Atomic Elbow 1 februari 2026, alltså precis som avsett. Hela historiken finns i `aurora_punks/royalty/xbox/_index.md` och i RAG.

**Watch item:** when MS unfreezes V2 reparenting, revisit the real ownership move of SW to AE's own Partner Center.
- Robert has Partner Center access: `finance@aurorapunks.com` = **owner account** on the AP Partner Center (also carries Manager/Windows), `robert@aurorapunks.com` = Developer-only. Hektor's `andreassonhektor@gmail.com` is the legacy Owner MSA, but finance@ is an owner too, so Legal Info changes should be attempted from finance@ before anyone escalates to Hektor (Robert, 2026-08-31).
- Konkurs context: gen-248. CZP Holding AB acquired the APDS assets incl. Sir Whoopass from the bankruptcy estate.
