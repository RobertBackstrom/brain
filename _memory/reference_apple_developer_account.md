---
name: reference_apple_developer_account
description: "The one Apple Developer account behind Hooja, K2C and the TCG grading app — entity, Team ID, roles, renewal."
metadata: 
  node_type: memory
  type: reference
  originSessionId: 3f022e8f-51be-4a62-bb1e-184161556b8b
  modified: 2026-08-05T19:24:50.943Z
---

**Verified 2026-08-05 from Membership details, not inferred.**

- **Entity name:** Aurora Punks AB (org 559256-9718, the solvent parent). **Not** APDS 559320-7466, which went bankrupt 2025-12-12.
- **Team ID:** `SCALFR6L25` · **Person ID:** 17832561041
- **D-U-N-S:** `353420335` (35-342-0335), issued to AP AB 559256-9718 on 2022-03-15, ordered the same morning the account was enrolled (source: Bisnode confirmation, Gmail thread `17f8cea36fbbfd79`). **Trap:** `350685539` in the same thread is WLBS's (559217-4196, bankrupt) — never touch that record. Apple verifies Organization address changes against D&B: `support.dnb.com/?CUST=APPLEDEV`, ~2 business days before Apple sees the change.
- **Enrolled as:** Organization · **Program:** Apple Developer Program
- **Account Holder:** Robert Bäckström. Admins seen on the team: christian@, fredrik@, hektor@, robert@.
- **Notification address:** `qa@aurorapunks.com` (a Google Group; all Apple + App Store Connect mail lands there). **Purchases** are billed to `robert@aurorapunks.com` via the Apple Store account, which is a separate thing from the developer team.
- **Renewal:** 999 kr/yr, next 2027-08-06, **auto-renew ON since 2026-08-05**.

**Why auto-renew matters:** the membership lapsed twice (2023-03-18 and 2026-05-29) because renewal was manual and nobody owned it. Each lapse pulled every app off the App Store. Hooja (`id1659828753`) was down from 2026-05-29 until the renewal. Auto-renew removes the recurring failure.

**Known stale field:** the developer organisation's street address is still Timmermansgatan 43, 118 55 Stockholm (a private address). The registered address is c/o Bäckström, Bondegatan 31, 116 33 Stockholm. This matters because DSA trader status publishes the trader address to EU users. Fix via "Update your information" on the Membership details page (self-serve). Tracked in apb-043.

**Traps learned the hard way:**
1. The `developer.apple.com/contact/file-upload/?teamId=...` link is scoped to an **open** support case. It returns "your account isn't authorized to upload files" when the case is closed, even for the Account Holder. Don't read that as a permissions problem.
2. Apple cannot open Google Drive links; a document sent that way is silently not received (happened 2024-11-01, case 102345613725, never retried).
3. Robert is a board member of AP AB but **not** VD (Andreea-Mariana Chifu) and not sole signatory — firman tecknas två i förening. A legal-authority review would need a second signature. See [[project_aurora_punks]].

Publishing decision (2026-08-03): CZP and AP AB operate as one entity for now, so the TCG grading app publishes under **this** account. No App Transfer, no CZP enrollment, no new D-U-N-S. Related: [[project_hooja]], [[project_the_assistant]].

**Apps on the team** (read 2026-08-14 via the ASC API):
- `com.Aurora-Punks.Hooja` — Hooja, ascAppId **1659828753**, live.
- `com.aurorapunks.gradingtool` — Aurora Punks Grading Tool, ascAppId **6798422764**, created 2026-08-14. Ticket tcg-002.
- `com.aurorapunks.taninani` — TaniNani, ascAppId 1615016441.
- `com.aurorapunks.com` — "Cloke-simulator", ascAppId 6747255609. The bundle id is a **domain**, almost certainly a typo.
- `com.aurorapunks.hooja` — **"Inte Hooja"**, ascAppId 6443732516, stuck in PREPARE_FOR_SUBMISSION since 2022. A decoy: it looks like the real Hooja bundle id and is not. Any automation matching on bundle id must not grab it.

**API key:** a Team Key with Admin role exists (`CNMFDUU6J9`, issuer `4aa4c6cf-7813-404d-b8da-44c66639ab8a`), private key at `tcg_webshop/app/secrets/`, gitignored. It authenticates builds, submissions and TestFlight management with no password and no 2FA.

**Hard limit worth knowing before planning any release automation:** the App Store Connect API **cannot create app records** — `POST /v1/apps` returns 403, "The resource 'apps' does not allow 'CREATE'". Allowed operations are GET_COLLECTION, GET_INSTANCE, UPDATE. A human must create each new app once in the web UI; everything after that is automatable.
