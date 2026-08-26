---
name: project_necrotic_dominion
description: AP/CZP Overwolf-funded ARK:SA premium mod; Elias Strandberg brought in 220 kr/h timanställd to fix bugs + ship content; prefix nd.
metadata: 
  node_type: memory
  type: project
  originSessionId: 0dc6f3ef-026a-48f5-9107-2f9c815fa5da
  modified: 2026-08-12T10:29:35.676Z
---

**Necrotic Dominion** — Aurora Punks' Overwolf-funded premium mod for ARK: Survival Ascended, live on CurseForge in two parts (ND map ~10K dl, ND:Armory ~16K dl). Re-activated 2026-06 by engaging **Elias Strandberg** (ex-APDS Level/Game Designer) on an hourly basis. Prefix **nd**; epic **nd-001**; folder `umbrella/necrotic_dominion/`; Drive folder `1Ire43dVh7PinTRf1eFiDgo_KenWEKyLG`.

- **Entity & funding:** contracted under **CZP Holding AB (dba Aurora Punks)** — NOT APDS (which is in konkurs, see [[reference_company_structure]]). Funded from monthly **Tebex** revenue.
- **Elias terms:** 220 kr/h (incl. 12% semesterersättning), timanställd, start 2026-07-17 tillsvidare, 14-day notice, 12-mo non-solicit, pnr 20010606-7036. Loaded CZP cost ~289 kr/h @ 45 h/month (~13 011 kr/mån run-rate). Rate 188→220, volym 60→45, start 07-01→07-17 updated 2026-07-15 per Robert (engagement had not begun). (Original salary/rate derivation in CorpBot learnings 2026-06-25.)
- **Scope (2 phases, 320h core):** Phase 1 = all reported bugs ≈ 20h (console/PS5 crash = LOD step, server-boot, teleport-mesh, Armory, materials); Phase 2 = 300h content (Magic Expansion roadmap + community + creator outreach).
- **Live-bug reality:** dominant issue is console/PS5 + dedicated-server can't launch — paying customers blocked. Feedback lives in Discord #ark-bugs (readable via Death Board bot, AP Official guild) + CurseForge comments ([[reference_company_structure]] unrelated; see db-233 for the reader, db-234 for the gsheet-style bug).
- **Contract (2026-07-15 → signed):** timavtal 220 kr/h / 45 h/mån / start 2026-07-17 (Doc `1LhZ5NA…`, budget Sheet `15G3O…`). Address **Skebokvarnsvägen 376, 124 50 Bandhagen**. OpenSign doc **`ZiR26oSoI2` is fully signed** (`isCompleted: true`, both parties; confirmation mail 2026-07-16). nd-002 closed.
- **Status (2026-08-02):** Elias **has started** — posted "Necrotic Dominion's Dev is Resurrected" in Discord `#ark-announcements` 2026-07-27, stability first, content after; he is fitting it around school so expect below 45 h/mån. Robert publicly promised the **next update mid-August**.
- **Tracker = Jira project `ND`** (`aurorapunks.atlassian.net/browse/ND`, id 10033, team-managed Kanban, lead Robert; 2nd project on the instance after KAN). 6 epics + 23 issues seeded 2026-08-02 from live Discord + CurseForge evidence (`assistant/nd-seed-backlog.js`). **Elias is NOT assignable** — no Atlassian licence yet.
- **Top live issue is now commercial, not technical:** the in-game **BUY button does not open the Tebex checkout** (ND-7, two reporters Jul 23 + Jul 29 2026) — new sales are blocked, and Tebex revenue is what funds the engagement. Then PS5 crash-on-load (ND-11, open ~7 months, refund/chargeback threats), dedicated-server boot failure (ND-14), Armory false "you don't own the map" (ND-9).
- **Feedback tooling:** `assistant/nd-discord-read.js` reads the four ARK channels via the Death Board bot. CurseForge comments remain scrape-blocked (db-233), but **CurseForge notification mails carry the comment text** (~100 chars) — search Gmail `from:noreply@curseforge.com`. CurseForge project members are added by **username, not email**, invitee must accept, and there is **no CurseForge session on the VPS**, so member changes are Robert-in-the-browser.
- **Access hygiene:** eight AP-linked CurseForge accounts (AuroraPunksBoss, robert_aurorapunks = Robert's *personal*, AP_Elias, APElliot, travis_aurorapunks, JohnKey, ankaAP, davidkruse), several departed staff — ND-27.
- **Ownership split (verified 2026-08-12):** map owned by **davidkruse** (transferred 2026-04-13), Armory by **robert_aurorapunks** (2025-12-17). Neither on the company account. Robert's call 2026-08-12: consolidate both under **AuroraPunksBoss**; David ask drafted, Robert sends.
- **Elias' CF access closed 2026-08-12** — no new account needed, he recovered `AP_Elias` and invited himself, so that account already carries member-management rights.
- **Money (verified 2026-08-12):** Overwolf IO (Mod Author = **Aurora Punks AB**) → PC via **Tebex** → wallet; console bypasses Tebex (platform → Wildcard → Overwolf). 25% Mod Author until Overwolf recoups $50K, then 50%. **CurseForge ownership does not control payout.** Tebex wallet live and healthy: $470.74 total, $459.56 withdrawable, unwithdrawn. PC run rate ~$60-105/mån vs Elias ~13 011 kr/mån.
- **Two deliberate parks (Robert, 2026-08-12), do NOT re-raise:** (1) the Tebex wallet's KYC identity is **Hektor Andreasson** (departed) and Tebex can't amend the Company once set — Robert's call is *leave it, it works*; (2) full revenue read incl. console/recoup — *not now*.
