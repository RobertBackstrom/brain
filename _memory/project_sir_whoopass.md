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
- **Watch item:** when MS unfreezes V2 reparenting, revisit the real ownership move of SW to AE's own Partner Center.
- Robert has Partner Center access: `finance@aurorapunks.com` = Manager(Windows), `robert@aurorapunks.com` = Developer-only.
- Konkurs context: gen-248. CZP Holding AB acquired the APDS assets incl. Sir Whoopass from the bankruptcy estate.
