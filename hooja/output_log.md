# Hooja - Output Log

## 2026-07-13 - Modernization investigation (SDK / ad funnel / IAP)
- Activated GameDev agent; recorded Fable 5 as Hooja coding model in `config.json`.
- Located repo `Aurora-Punks/Hooja` (private, Unity 2021.3.45f2, dormant since 2025-10-23); shallow-cloned for static analysis.
- Fanned 3 Fable 5 sub-agents over the real code: ad-funnel audit, IAP design spike, Unity upgrade compat matrix.
- Delivered `hooja_modernization_brief.md` (consolidated) + `drafts/unity_upgrade_spike_checklist.md`.
- Key findings: engine upgrade is mandatory (API 35 / 16 KB / Xcode 16 gates block new store updates); LevelPlay SDK ~3 yrs stale + no Android GDPR consent; IAP is greenfield with two near-free products already stubbed in code (double-gold/double-score cheat flags). Android signing keystore committed to repo (hygiene flag).
- Scope confirmed with Robert: Unity = decide after spike; ads = update+add networks+improve logic; IAP = design spike only.
- **Open:** 8 questions to Robert (merchant entity, child-directed, leaderboard fairness, save sync, potion odds, price tiers, spike owner, keystore rotation). No implementation started.

## 2026-07-13 (later) - Republish reframe + direction confirmed
- **Critical finding:** Hooja is **delisted from both stores** (both URLs 404). Cause: publishing entity **APDS (Aurora Punks Development Services AB) is in bankruptcy** (konkursförvaltare Ellen Berglund / Advokatfirman Carler) -> developer accounts terminated -> apps delisted. So this is a **re-publish under a new entity**, not a store update. New app listing, new package ID likely, loses old ratings/reviews/installs.
- **IP flag (blocking publish, not code):** Hooja ownership is unconfirmed in AP records ("external client vs Own IP 50%") + a music-artist license exists; APDS assets may be in the bankruptcy estate. Chain-of-title must clear before publishing.
- **Strategic framing:** Hooja = first effort to build a repeatable port-and-publish pipeline (reusable for K2C, BlockEm) + the framework will be **reskinned to a horse-race game for MENA** with mature IAP-led monetization.
- **Robert's decisions:** (1) Spike machines = Windows/Linux for Android + Mac for iOS (iOS needs macOS/Xcode). (2) Loop in **CorpBot now** for new CZP entity + fresh Google/Apple dev accounts; **legal IP review ON HOLD** until Robert speaks to the konkursförvaltare. (3) **Republish-first, template-later** (extract reusable template after).
- **Actions:** spawned CorpBot (opus) to scope entity + dev-account setup -> `czp/hooja_republish_entity_setup.md`. Wrote `drafts/unity_install_guide.md` (both machines). Child/family-targeting recommendation = tracked follow-up (lean: do NOT declare child-directed; confirm with player-age data).

## 2026-07-13 (correction) - delisting cause NOT confirmed as bankruptcy
- CorpBot flagged, and RAG confirms: the "APDS bankruptcy delisted Hooja" narrative is **not supported**. A Sept 2024 Google Play notification thread (Hektor <-> Robert) ties the mobile account to **WLBS / Aurora Punks AB**, not clearly APDS; **AP AB is solvent**. Corrected the confident claim I made earlier.
- **Most likely real cause:** target-API non-compliance unpublish (targetSDK 34 vs API 35 required since Aug 2025) and/or App Store stale-app removal - both benign vs bankruptcy.
- **Implication:** if the listing sits under a solvent account, the fix may be "update to API 35 -> re-publishes on the existing listing" (keeps ratings/installs), NOT the full new-entity republish. Could remove the 3-6wk account-setup critical path.
- **Decisive next step (Robert):** check the live **Google Play Console** (which org holds com.AuroraPunks.Hooja, status, unpublish reason) + **App Store Connect** (seller entity, removal reason). Consoles are login-gated - Assistant can't see them.
- CorpBot entity plan retained for Phase-2 MENA subsidiary + the in-flight Steam/PS APDS->CZP swap regardless. Technical modernization (API 35 / 16 KB / Xcode 16) needed either way. Corrected project memory.

## 2026-07-13 (mail investigation) - account owners + real delist cause CONFIRMED
- Searched both mailboxes for store-account ownership. Findings:
  - **Google Play = Aurora Punks AB** (solvent, active; Hektor 23 Sep 2024 "där Hooja är publicerat heter Aurora Punks AB"; still receiving Play service emails Jun 2026). Contacts hektor@/emelie@. NOT APDS/WLBS.
  - **Apple = aurorapunks.com org account** (Robert CEO + renewed membership Apr 2024; admins christian@/fredrik@/hektor@/robert@; addr updated Jul 2024).
- **Real Google delist cause = CONFIRMED:** 9 Jun 2026 Google Play email - Hooja **"App Status: Removed"** under Device & Network Abuse policy for the **2025 Unity Android runtime CVE (CVE-2025-59489)** ("Unity 2017.1+ for Android"). Fix = rebuild on patched Unity + resubmit. NOT bankruptcy.
- **Apple cause:** trader status WAS submitted (Hektor 24 Jan 2025), so likely stale-app removal, not DSA; confirm in ASC.
- **Bottom line:** both accounts solvent AP AB -> path is very likely **fix + update existing listings** (keep ratings/installs), NOT new-entity republish. Resubmission still needs API 35 so the engine upgrade remains the single fix path. CZP entity kept for MENA + APDS-tied Steam/PS only.
- **Robert's move:** confirm in Google Play Console (Removed notice + resubmit) + App Store Connect (removal reason + trader status). Corrected project memory.

## 2026-07-13 (mail investigation 2) - backend access addresses + Apple membership expiry + payout entities
- **Backend login addresses:** Apple Dev/App Store Connect = **qa@aurorapunks.com** (Google Group; receives all Apple + ASC financial-report/membership mail; Account Holder = Robert; 2FA -> device not group inbox). Google Play Console owner = **emelie@aurorapunks.com** (hektor@ also has access).
- **App Store delist cause = CONFIRMED different from earlier guess:** Apple Developer Program **membership EXPIRED 29 May 2026** ("content on the App Store no longer available"). Trader status was already submitted (Hektor Jan 2025), so expiry is the cause, not DSA/stale. **Immediate fix = renew membership (999 kr/yr).**
- **Payout details (Robert's Q confirmed):** Steam pays **APDS** (Valve 26 Jun 2026), PSN pays **APDS** (Sony PO 12 Jun 2026 vendor 6195104490), Payoneer under **WLBS** (Dec 2024). Store listings under AP AB but payout banking likely still APDS/WLBS -> must audit + re-point in each console's payments profile before revenue flows. -> CorpBot workstream (all 4 backends).
- **Next actions:** (1) Robert renews Apple membership via qa@ (watch 2FA). (2) Confirm account owner + payout entity in Google Play Console + App Store Connect. (3) Send CorpBot the payout re-pointing workstream. Corrected project memory.
