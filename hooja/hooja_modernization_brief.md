# Hooja - SDK / Ad-Funnel / IAP Modernization Brief

**Date:** 2026-07-13
**Author:** GameDev agent (analysis fanned to 3x Fable 5 sub-agents on the real code)
**Repo:** `Aurora-Punks/Hooja` (private, C#, Unity 2021.3.45f2, dormant since 2025-10-23)
**Companion repo:** `Aurora-Punks/hooja-web` (JS landing/PR site, out of scope)
**Scope of this pass:** investigation + design only. No code changed, nothing published.
**Coding model for future implementation:** Fable 5 (recorded in `config.json` `project_model_policy.projects.hooja`).

Robert's chosen scope:
1. Unity upgrade - decide after a spike.
2. Ad funnel - update LevelPlay SDK + adapters, add mediated networks, improve funnel logic (with recommendations).
3. IAP - research + design spike only.

---

## 0. The headline

The game ships fine today but **cannot ship a new store update in its current state**. Three hard gates, all dated and live:

1. Google Play requires **target API 35** for updates (since 31 Aug 2025). Hooja is on **34**.
2. Google Play requires **16 KB memory-page support** for target-35 updates (since Nov 2025). Unity 2021.3 **cannot produce it** - this alone forces the engine upgrade.
3. App Store requires builds made with the **iOS 18 SDK / Xcode 16** (since Apr 2025). Unity 2021.3 is not qualified for Xcode 16.

A fourth gate is 8 weeks out: **target API 36** is expected ~31 Aug 2026, and only Unity 6 is on track to support it.

So this is not really three independent tasks - it's one modernization pass where the engine upgrade and the LevelPlay upgrade are both mandatory and must land together, and IAP is the additive revenue piece that rides on top.

---

## 1. Unity engine upgrade

### Current state
- Unity **2021.3.45f2**, Built-in Render Pipeline, IL2CPP Android (ARMv7 + ARM64), Android minSDK 22 / targetSDK 34, iOS min 12.0.
- 2021.3 LTS is **end-of-support**, no 16 KB backport, not Xcode-16 qualified. Dead end.

### Recommendation: target Unity 6 (6000.x LTS), using 2022.3 as a stepping stone

Rationale:
1. 2022.3 latest patch *can* technically hit API 35 + 16 KB + Xcode 16, and it's the cheaper migration. But 2022.3 is itself at/past end of support, and **API 36 lands ~Aug 2026** - upgrading to 2022.3 buys roughly one store cycle before repeating this whole exercise.
2. The expensive mandatory work (LevelPlay 8.x migration, adapter refresh, dead-SDK removal, Gradle template regen, EDM4U bump) is **identical on both targets**. The Unity-6-only extra cost is bounded and known: TMP/uGUI 2.0 merge + Febucci update, Addressables 2.x content rebuild, `FindObjectOfType` deprecation warnings.
3. Practical path: open once in 2022.3 to migrate serialized assets/Addressables in a smaller step and flush easy errors, commit, then reopen in Unity 6.

### High-risk items (must be checked in the hands-on spike)
1. **Three custom AP git packages** (`aurora-audio`, `aurora-scriptable-values`, `aurora-save`), all pinned to `#dev-package` **branches** (not tags), so the pin can move. Their Unity-version compatibility is unknown from here - someone with GitHub access must read each `package.json` `unity` field and grep for editor guards. `aurora-save` + MessagePack is the save-integrity risk: regression-test a save/load round-trip after upgrade.
2. **Addressables** 1.19.19 today (pulled in via Localization). 2022.3 = mild 1.21.x bump; Unity 6 = real 1.x->2.x migration (binary catalogs, full content rebuild).
3. **Committed 2021-only Gradle templates** (`Assets/Plugins/Android/gradleTemplate.properties` has a `**MINIFY_WITH_R_EIGHT**` placeholder removed in 2022+). Delete and regenerate from Player Settings, or template processing fails.
4. **TMP -> uGUI 2.0 merge on Unity 6** breaks the TMP package entry and puts **Febucci Text Animator 1.x** at risk (predates TMP 3.2 mesh changes; budget a paid asset update).
5. **EDM4U 1.2.169** must go to >= ~1.2.180 before Unity 6 (AGP 8 / Gradle 8).
6. **Dead Unity Mediation SDK** deps still in the project (`com.unity3d.mediation:*`) - the jfrog/cocoapods sources may 404 at resolve time and break the build regardless of editor. Remove during the LevelPlay migration.

Deprecated-API exposure in our own code is **minor**: only `FindObjectOfType` in ~6 files (warnings, not errors); no `WWW`/`LoadLevel`/Experimental namespaces; the 4 custom editor scripts use stable APIs.

### Minimum-version summary
- To ship the latest store SDKs **today**: 2022.3 latest patch (>= the 16 KB-support patch).
- To survive the **next 12 months** of store requirements: **Unity 6**.

### The spike (one afternoon on a Unity-Hub machine)
Full ordered checklist lives in `drafts/unity_upgrade_spike_checklist.md`. Summary: install 2022.3 + Unity 6 with Android+iOS modules, two working copies, check the 3 AP packages first, Hop 1 in 2022.3 (migrate, regen Gradle templates, force-resolve, build .aab + verify 16 KB alignment, Xcode 16 archive, save round-trip), Hop 2 in Unity 6 (TMP/Addressables/DOTween/Febucci, rebuild, build both platforms), record error-count + hours-to-first-build per hop as the decision input.

**Constraint:** this editor spike needs Unity Hub + licenses, so it runs on a dev machine, not this VPS. GameDev can prep everything and hand the checklist; execution needs a person at a Unity install.

---

## 2. Ad funnel (ironSource LevelPlay)

### Current state
- ironSource Unity plugin **7.3.0.1-r** (~Feb 2023). LevelPlay is on the **8.x** line - 5+ generations behind.
- Adapters all old: AdMob 4.3.32 / play-services-ads **21.3.0**, Meta AN 6.12.0, Unity Ads 4.4.1. EDM4U 1.2.169.
- **Legacy API throughout** (`Assets/Scripts/IronSource/AuroraIronSourceManager.cs`) - deprecated `IronSourceEvents`, wrapped in `#pragma warning disable CS0618` with the team's own `// TODO: Fix`. Inits REWARDED + INTERSTITIAL + OFFERWALL + BANNER but only ever shows rewarded. **OFFERWALL is discontinued** and will break on 8.x.
- **Rewarded-only, 5 placements:** (1) die-to-continue Revive + random powerup, (2) GoldHooja revive-tokens, (3) DoubleCoins post-run, (4) RunStart boost, (5) the "Hooja-Drycken" menu potion on a 5-min timer.

### Real problems found (not just "it's old")
1. **No GDPR/CMP consent on Android at all.** The "privacy popup" is only an age gate; consent is only ever set by the iOS ATT handler. No Google UMP, no TCF string. In 2026 EEA traffic, AdMob serves only limited ads without TCF consent - a direct revenue and compliance hit.
2. **iOS SKAdNetwork plist only contains ironSource's own ID** - mediated networks' SKAN IDs are missing, so mediated iOS fill underreports and underbids.
3. **Latent reward bugs:** a single untyped global `OnRewardCompleted` event with manual subscribe/unsubscribe; `lockAdClick` is reset on reward but **not on ad-closed**, so an early close can soft-lock ad buttons until a revive resets it. The potion ad uses an **empty placement string**, so the most-frequent ad in the game has no per-placement capping or reporting, and its first-time cassette grant can be triggered by any rewarded ad in that scene.
4. **No impression-level revenue tracking** (`onImpressionDataReady` unwired), so there's no ROAS/LTV signal feeding PlayFab telemetry.
5. Leftover dead `com.unity3d.mediation:*` resolver entries; app keys hardcoded in two places.

### Recommendations
1. **Upgrade** to LevelPlay **8.x latest** (verify exact latest against developers.is.com before scoping), migrate `AuroraIronSourceManager` to the unified `LevelPlay` init + `LevelPlayRewardedAd` API (small surface: 1 manager, 1 facade, 5 call sites, 4 scene-wired UnityEvents). Drop OFFERWALL. Refresh adapters (play-services-ads 24.x, Meta AN 6.19+, Unity Ads 4.12+).
2. **Add bidding-first networks**, in rough impact order for a casual EU-centric runner: **AppLovin** (near-mandatory second demand source), **Mintegral**, **Liftoff/Vungle**, then DT Exchange / InMobi as cheap incremental bidders. Also *fix Meta AN to actually bid* - on 6.12 without bidding it's likely earning nothing. Gate all behind the child-directed flags.
3. **Funnel-logic improvements** (Robert asked for suggestions):
   1. **Interstitial between runs** on the non-rewarded return-to-menu path, frequency-capped (e.g. min 2 runs + 60-90s apart, skip if a rewarded ad was watched that run, skip entirely for child profiles). Single biggest untapped lever; the unit is already inited.
   2. **Banner on the SpyBar menu** - low eCPM but pure incremental; the beer timer keeps players idling there.
   3. **Give the potion ad a real placement name** in all 4 scene wirings; set per-placement capping/pacing in the LevelPlay dashboard.
   4. **Fix the event plumbing** - per-placement reward routing (8.x hands you the placement), reset `lockAdClick` on ad-closed, unsubscribe on close-without-reward.
   5. **Wire `onImpressionDataReady` -> PlayFab telemetry** for per-impression revenue and LTV cohorts.
   6. **A/B ideas:** revive-timer length vs take-rate, double->triple coins test, beer cooldown 5/10min vs daily-charges, surfacing the already-rolled revive bonus powerup before the click (free UX win).
4. **Ship a CMP (Google UMP)** for EEA/UK on both platforms and pass TCF consent to LevelPlay before scaling ads; add mediated networks' SKAdNetwork IDs to the iOS plist.

---

## 3. In-app purchases (design spike only)

### Current economy
- Single soft currency **Coins (guld)**, 100% local (binary MessagePack save via `aurora-save`), zero server authority. PlayFab is used only for anonymous login, leaderboards, Title Data, seasonal events, and telemetry - **no catalog/virtual-currency/inventory** today.
- Existing shop sells powerup tickets/upgrades for Coins (Dunken 100 ... Plane 1500); mid-run revive costs `2^n` tokens; RunStart boost already offers "pay Coins or watch an ad" - the design-doc "köpa för guld eller en ad" is already built.
- **Latent gift:** `doubleMoneyBoosterActivated` / `doubleScoreBoosterActivated` flags exist in the save and are wired into coin/score logic, but are only settable via the cheat menu. Purpose-built to become IAP non-consumables.

### SDK: Unity IAP (`com.unity.purchasing`) 4.13+
Native fit for 2021.3+, bundles Google Play Billing 7 (required since Aug 2025), one `IStoreListener` for both stores, receipts arrive in exactly the shape PlayFab's validators want. RevenueCat/UDP/raw-StoreKit rejected (extra backend / deprecated / two codebases). Note: pulls Unity Gaming Services core; the project needs a UGS project ID linked (none today).

### Proposed catalog (product ID `com.aurorapunks.hooja.<sku>`, same on both stores)
1. **`starterpack`** (consumable, one-time) ~$2.99 - 3,000 Coins + 4 revive tokens + 1 potion. First-purchase converter.
2. **`goldpack.small/medium/large`** (consumable) ~$1.99 / $4.99 / $9.99 - 2,000 / 6,000 / 15,000 Coins with increasing value. Slot straight into the existing economy (`Coins += amount`), no new sinks needed.
3. **`doublegold`** (non-consumable) ~$3.99 - permanently sets `doubleMoneyBoosterActivated`. **Cheapest-to-build, highest-fit product in the list** - the code already exists; work is removing the cheat-only resets and gating on entitlement.
4. **`doublescore`** (non-consumable) ~$2.99 - same story (needs a leaderboard-fairness decision).
5. **`potionpack`** (consumable) ~$1.99 - 3 instant potion opens. Needs odds disclosure if reward values vary.
6. **`vip`** ("Hooja VIP", non-consumable) ~$5.99 - **the right shape instead of "Remove Ads."** Every ad is a rewarded opt-in, so removing ads would sell nothing and *punish* the buyer. VIP instead auto-grants the reward *without* the video (the existing `SKIP_ADS` code path proves this works), keeping every reward flow intact.

Skip for v1: powerup-ticket bundles (redundant with gold packs), cosmetic cassettes (progression/index-fragile).

### Receipt validation (client -> PlayFab, no custom server)
Unity IAP `ProcessPurchase` -> set Pending -> PlayFab `ValidateGooglePlayPurchase` (ReceiptJson+Signature) / `ValidateIOSReceipt` (base64) -> on success grant locally + `iap_purchase` telemetry -> `ConfirmPendingPurchase`; on network failure leave pending and retry next launch. PlayFab de-dupes each receipt per title (kills replay/sharing). Prereq: paste Google Play licensing RSA key + iOS bundle into PlayFab Game Manager. **Reality check:** validation protects the *purchase*, not the *balance* - the local save is trivially editable with or without IAP; acceptable for v1, mitigate with a PlayFab catalog for auditable grants. Full server-authoritative currency is out of scope.

### Store setup (longest-lead item is agreements)
Google Play: merchant account + payments/tax profile, products with `com.aurorapunks.hooja.*` IDs, BILLING-permission build, license testers. App Store Connect: **Paid Applications Agreement + banking/tax (blocks everything, do first)**, IAPs with matching IDs + localized sv/en names + screenshots, sandbox testers. PlayFab: Google package + licensing key, Apple bundle ID, optional Economy catalog.

### Effort (later pass)
Core IAP manager + validation + gold packs ~3-4 dev-days; VIP/booster entitlements ~1-2 days; IAP shop UI ~1-2 days; store + PlayFab config + sandbox passes ~1-2 days. **~6-10 dev-days**, biggest schedule risk is store-side review/agreements, not code.

---

## 4. Open questions for Robert (blocking the next step)

**IAP direction (needed before any implementation):**
1. **Merchant entity** - whose Google/Apple developer accounts and bank/tax details take the revenue (AP AB?). Longest-lead item; blocks the Paid Apps Agreement.
2. **Child-directed audience** - the game has `playerIsChild` COPPA handling. If the store listing is family/child-directed, both stores restrict IAP presentation. Hide IAP for child profiles?
3. **Leaderboard fairness** - is a paid permanent score-doubler (`doublescore`) acceptable with tournaments in the core loop, or cut it / keep it off tournament boards?
4. **Save sync** - consumable gold is lost on reinstall (local save, device-ID login). Ship PlayFab save-backup in the same milestone? (Recommended - refunds from lost gold cost more than the feature.)
5. **Potion odds** - flat-value rewards, or publish odds in-app for loot-box / EU consumer-rule compliance?
6. **Price points** - are ~25-119 SEK tiers right for a young/casual Swedish audience?

**Engine:**
7. Who runs the hands-on Unity spike, and on what machine? (GameDev preps + hands the checklist; execution needs a Unity install.)

**Housekeeping (not blocking, worth doing):**
8. **The Android signing keystore (`user.keystore`) is committed to the repo.** The password is *not* (loaded from an untracked file), but the keystore in git is a hygiene issue - recommend rotating it out of history. Flagging per standing security defaults.

---

## 5. Recommended sequencing

1. **Now:** Robert answers Q1-Q6 (IAP) and Q7 (spike owner). GameDev preps the AP-package compat check + spike machine.
2. **Milestone 1 (mandatory, unblocks shipping):** Unity upgrade spike -> pick 2022.3-stepping-stone -> Unity 6. Land LevelPlay 8.x migration + adapter refresh + dead-SDK removal + Gradle regen in the same milestone (all mandatory, editor-independent). Add CMP. Result: a build that can pass both stores again.
3. **Milestone 2 (revenue):** ad-funnel improvements (interstitial + banner + event-plumbing fixes + new networks) and IAP implementation (Unity IAP + PlayFab validation + the 8-SKU catalog), sequenced by the answers above. VIP + doublegold/doublescore first (cheapest, highest-fit), then gold packs, then store config.
