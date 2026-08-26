---
project: hoj
status: in_progress
priority: high
type: epic
owner: Claude
created: 2026-07-13
updated: 2026-07-13
---

## Hooja — SDK/ad/IAP modernization + re-publish (Epic)

Aurora Punks F2P mobile auto-runner (Hooja music IP), Unity + ironSource LevelPlay + PlayFab. Delisted from both stores; this epic covers getting it modern, compliant, and re-published, and building a reusable port-and-publish pipeline (later reskinned to a horse-race title for MENA). Coding model: Fable 5. Full brief: `projects/hooja/hooja_modernization_brief.md`.

**Activity:**
- [2026-07-13] **GameDev**: Session 1 — investigation + scaffolding, no code changed / nothing published.
  1. Located repo `Aurora-Punks/Hooja` (Unity 2021.3.45f2). Fanned 3 Fable 5 agents over the real code: ad-funnel audit, IAP design spike, Unity-upgrade compat matrix. Consolidated into the brief + spike checklist + Milestone-1 ticket breakdown (hoj-002..009).
  2. Key technical findings: engine upgrade mandatory (Google target API 35 + 16 KB; iOS 18/Xcode 16); LevelPlay SDK ~3 yrs stale (7.3.0.1 vs 8.x) with no Android GDPR consent; IAP greenfield (Unity IAP 4.13+ / PlayFab validation), "Remove Ads" reframed as "Hooja VIP"; Android keystore committed to repo (hygiene flag).
  3. **Delisting cause — NOT bankruptcy (confirmed via mail):** Google Play REMOVED Hooja for the 2025 Unity Android CVE (CVE-2025-59489, email 9 Jun 2026). App Store went dark because the **Apple Developer Program membership expired 29 May 2026** (renew = fast unblock).
  4. **Store accounts:** Google Play = Aurora Punks AB (solvent; owner emelie@, hektor@ has access). Apple = qa@aurorapunks.com Google Group (Account Holder Robert). Both under solvent AP AB, so likely path = fix + update existing listings, NOT new-entity republish.
  5. **Payout entities need re-pointing:** Steam + PSN pay out to bankrupt APDS; Payoneer under WLBS. CorpBot (opus) produced entity/dev-account plan `czp/hooja_republish_entity_setup.md` (Phase 1 CZP Holding AB, Phase 2 subsidiary before MENA).
  6. Decisions: spike machines = Win/Linux (Android) + Mac (iOS); CorpBot on entity now, legal IP review held pending Robert↔konkursförvaltare; republish-first, template-later; prefix `hoj`; Fable 5 coding model (both written to config.json).

**Open questions / next steps:**
1. Robert renews Apple Developer membership (via qa@, watch 2FA) — immediate App Store unblock.
2. Robert confirms in Google Play Console + App Store Connect: account owner + current payout entity + exact removal/appeal state.
3. Robert speaks to konkursförvaltare (Ellen Berglund, Carler) re Hooja IP chain-of-title before any new-entity publish.
4. Send CorpBot the payout re-pointing workstream (audit + update payments profile across Google Play, App Store Connect, Steam, PSN).
5. Kick off hoj-003 (Fable 5 AP-package compat check) + install Unity Hub on both machines to start the spike.
6. Parked IAP decisions: child-directed (lean no), leaderboard fairness, save-sync, potion odds, price tiers, keystore rotation.
