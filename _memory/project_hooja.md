---
name: project-hooja
description: Aurora Punks F2P mobile auto-runner (Hooja music IP); Unity + LevelPlay + PlayFab; SDK/ad/IAP modernization pass.
metadata: 
  node_type: memory
  type: project
  originSessionId: d0301f53-56bc-433c-b3ba-90b9a1139348
---

Aurora Punks F2P mobile auto-runner on the "Hooja" music-artist IP. Live since 2023 on Google Play (`com.AuroraPunks.Hooja`) and App Store (`id1659828753`). AP did full dev + live service. Prefix `hoj`. Project folder `projects/hooja/`.

**Stack:** Unity (Built-in RP, IL2CPP) - repo `Aurora-Punks/Hooja` (private, C#), was on 2021.3.45f2 as of 2026-07. Web site repo `Aurora-Punks/hooja-web`. Custom AP packages: aurora-audio, aurora-scriptable-values, aurora-save. Ads: ironSource **LevelPlay** rewarded-only. Backend: **PlayFab** (login/leaderboards/telemetry, no catalog). Coding model = **Fable 5** (per Robert 2026-07-13, in config project_model_policy).

**2026-07 initiative:** SDK modernization + ad-funnel update + IAP design. Engine upgrade is mandatory (Google target API 35 + 16 KB page + Xcode 16 gates; 2021.3 can't do 16 KB). Recommend Unity 6 via 2022.3 stepping stone; LevelPlay 7.3->8.x migration mandatory alongside. IAP greenfield (Unity IAP 4.13+ / PlayFab receipt validation); "Remove Ads" is wrong shape (all ads rewarded) -> use "Hooja VIP". Full brief: `projects/hooja/hooja_modernization_brief.md`. Owned by [[project-agent-registry]] GameDev agent. Android keystore committed to repo (hygiene flag).

**DELISTED - CAUSE CONFIRMED, NOT BANKRUPTCY (2026-07-13, from mail history):** Game is down on both stores. **APDS bankruptcy did NOT cause it.** Store accounts:
- **Google Play = Aurora Punks AB** (solvent, active - still getting normal Play service emails Jun 2026). Contacts hektor@ + emelie@aurorapunks.com. NOT APDS/WLBS (WLBS = old restricted org).
- **Apple = aurorapunks.com org account** (Robert CEO, renewed membership Apr 2024; admins christian@/fredrik@/hektor@/robert@; company address updated Jul 2024). Account Holder confirm in ASC.

**Backend access addresses (from mail):** Apple Developer/App Store Connect login = **qa@aurorapunks.com** (Google Group alias; gets all Apple/ASC mail incl. financial reports + membership notices; Account Holder = Robert; 2FA goes to a device, not the group). Google Play Console owner = **emelie@aurorapunks.com** (hektor@ also has access).

**Real delist causes - BOTH CONFIRMED, neither bankruptcy:** (1) **Google Play REMOVED Hooja** under Device & Network Abuse policy for the **2025 Unity Android runtime CVE (CVE-2025-59489)** - "Unity 2017.1+ for Android" (email 9 Jun 2026, status "Removed"). Fix = rebuild on patched Unity + resubmit (must also hit API 35). (2) **App Store: Apple Developer Program membership EXPIRED 29 May 2026** ("any content on the App Store is no longer available") - THIS removed Hooja from iOS. Trader status was already submitted (Hektor Jan 2025), so it's the expiry, not DSA. **Fix = renew membership (999 kr/yr) - immediate cheap unblock.**

**PAYOUT DETAILS point to bankrupt/old entities (Robert flagged; mail confirms):** Steam pays **APDS** (Valve notice 26 Jun 2026), PSN pays **APDS** (Sony PO 12 Jun 2026, vendor 6195104490), Payoneer under **WLBS** (Dec 2024). Store *listings* are under AP AB / AP-domain Apple acct, but *payout banking* underneath likely still APDS/WLBS - must be audited + re-pointed to a solvent entity in each console's payments profile before revenue flows. CorpBot workstream.

**Implication:** both accounts live under solvent AP AB -> likely path = **fix + UPDATE the existing listings** (keep ratings/installs/package ID), NOT a new-entity republish. Note: any resubmission must also hit target API 35 (16 KB), so the security fix + API-35 gate both = the same engine upgrade (no 2021.3 shortcut). CZP entity still relevant for the MENA title + APDS-tied Steam/PS titles (apb-026/apb-015), just NOT for Hooja mobile. IP chain-of-title (external-client vs Own-IP-50% + music-artist license) unconfirmed but gates only a *new-entity* path. See [[project-rlr-ip-dispute]]; entity plan `czp/hooja_republish_entity_setup.md`.

**Strategy:** Hooja = first repeatable port-and-publish pipeline (reusable for K2C/BlockEm) + framework to be **reskinned to a horse-race game for MENA** (mature IAP-led; keep clear of gambling mechanics, need Arabic/RTL - localization pkg already present, Huawei AppGallery + carrier billing matter).

**Decisions 2026-07-13:** spike machines = Windows/Linux (Android) + Mac (iOS, required for Xcode/iOS18); CorpBot scoping new CZP entity + dev accounts (`czp/hooja_republish_entity_setup.md`); legal IP review ON HOLD pending Robert<->konkursförvaltare; **republish-first, template-later**. Child-directed: lean NO (confirm w/ player-age data).
