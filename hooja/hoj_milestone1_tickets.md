# Hooja - Milestone 1 ticket breakdown (prefix `hoj`)

**Date:** 2026-07-13
**Milestone 1 goal:** get Hooja to a **compliant, green build on both platforms** (Android target API 35 + 16 KB, iOS 18 / Xcode 16) with a current, store-legal ad SDK. This is the work that unblocks *any* store return, and it's **identical whether we update the existing listing or republish under a new entity** - so it's safe to run now, in parallel with the console check and CorpBot's entity track.

**Coding model:** Fable 5 (per project policy). **Owner:** GameDev agent + Robert (spike/builds on his machines).
**Out of M1 (previewed at bottom):** ad-funnel *improvements* (new networks, interstitial/banner), IAP, and the actual store submission.

---

## Epic: hoj-001 - Hooja modernization & re-publish
Parent for all Hooja SDK/ad/IAP + re-publish work. Two milestones: M1 = compliant build (below); M2 = monetization (ad funnel + IAP); plus a blocked-on-entity publish gate.

---

## Milestone 1 tickets

### hoj-002 - Unity upgrade compat spike (2022.3 + Unity 6)
- **What:** Run the hands-on editor spike per `drafts/unity_upgrade_spike_checklist.md`. Two hops (2022.3 stepping-stone -> Unity 6), capture error-count + hours-to-first-build per hop as the decision input.
- **Owner:** Robert (his Win/Linux + Mac) with GameDev driving. Prereq: Unity Hub installed both machines per `drafts/unity_install_guide.md`.
- **Depends on:** hoj-003 (package check) ideally done first.
- **Acceptance:** documented go/no-go for Unity 6 vs 2022.3, with the per-hop error log attached.
- **Est:** 0.5-1 day. **Model:** n/a (human-run) + GameDev support.

### hoj-003 - Custom AP package compatibility check
- **What:** Fetch the 3 AP git packages (aurora-audio, aurora-scriptable-values, aurora-save on `#dev-package`), read each `package.json` `unity` field, grep for editor-version guards. Confirm they build on the target editor. Save-system round-trip is the key risk (aurora-save + MessagePack).
- **Depends on:** GitHub access.
- **Acceptance:** compat verdict per package + any required branch/tag pin fixes noted.
- **Est:** 0.5 day. **Model:** Fable 5.

### hoj-004 - Engine upgrade to Unity 6 (via 2022.3 hop)
- **What:** Execute the upgrade decided in hoj-002: open in 2022.3 to migrate serialized assets/Addressables, commit, then Unity 6. Regenerate Gradle templates, bump EDM4U, migrate Addressables, resolve TMP->uGUI 2.0 + Febucci, clear FindObjectOfType warnings as needed.
- **Depends on:** hoj-002, hoj-003.
- **Acceptance:** project opens clean (0 errors) in Unity 6, enters Play Mode, save/load round-trip passes.
- **Est:** 3-5 days. **Model:** Fable 5.

### hoj-005 - LevelPlay 7.3 -> 8.x migration + adapter refresh
- **What:** Migrate `AuroraIronSourceManager` to the unified LevelPlay 8.x API (init + `LevelPlayRewardedAd`), refresh adapters (AdMob/play-services-ads 24.x, Meta AN, Unity Ads), remove **OFFERWALL** from init, remove the dead `com.unity3d.mediation:*` deps. Preserve child-directed/ATT metadata. Keep the existing 5 rewarded placements working (name the empty potion placement).
- **Why in M1:** mandatory for API 35 / 16 KB compliance - the old SDK won't pass regardless of engine version.
- **Depends on:** hoj-004.
- **Acceptance:** rewarded ads load+show on a device test build via LevelPlay 8.x; no deprecated-API warnings; dead mediation deps gone.
- **Est:** 2-3 days. **Model:** Fable 5.

### hoj-006 - Android: target API 35 + 16 KB build green
- **What:** Set target API 35, produce a signed `.aab`, verify 16 KB page alignment (`zipalign -c -P 16`), pass a Play pre-launch dry run if available.
- **Depends on:** hoj-004, hoj-005.
- **Acceptance:** 16 KB-aligned `.aab` targeting API 35 builds and installs on a device.
- **Est:** 1-2 days (on Win/Linux). **Model:** Fable 5 + Robert.

### hoj-007 - iOS: iOS 18 / Xcode 16 archive green
- **What:** Export the Xcode project, run CocoaPods (LevelPlay/PlayFab pods), archive with Xcode 16 / iOS 18 SDK on the Mac. Bump iOS deployment target as needed.
- **Depends on:** hoj-004, hoj-005.
- **Acceptance:** signed iOS archive builds with the iOS 18 SDK and runs on a device.
- **Est:** 1-2 days (on Mac). **Model:** Fable 5 + Robert.

### hoj-008 - GDPR CMP + iOS SKAdNetwork compliance
- **What:** Add a real consent flow (Google UMP) for EEA/UK on both platforms, pass TCF consent to LevelPlay (today there's NO Android consent flow - only an age gate). Add mediated networks' SKAdNetwork IDs to the iOS plist.
- **Why in M1:** without TCF consent AdMob serves limited ads in EEA (revenue loss) and it's a compliance exposure; cleanest to land with the SDK migration.
- **Depends on:** hoj-005.
- **Acceptance:** consent prompt shows in an EEA test locale; TCF string reaches LevelPlay; iOS plist carries mediated SKAN IDs.
- **Est:** 1-2 days. **Model:** Fable 5.

### hoj-009 - Security: rotate committed signing keystore
- **What:** The Android signing keystore (`user.keystore`) is committed to the repo. Rotate it out of git history and move to a secure store (password already lives outside git). Coordinate with whoever holds the current upload key so store signing continuity is preserved.
- **Depends on:** decision on account/signing continuity (touches the console-check outcome).
- **Acceptance:** keystore removed from history; signing config documented; build still signs.
- **Est:** 0.5 day. **Model:** Fable 5 + Robert. **Note:** verify against the Play upload-key/Play App Signing setup before rotating.

---

## Milestone-boundary gate (blocked - do not start)

### hoj-010 - Store submission / re-publish (BLOCKED)
- **Blocked on:** (1) console check - which account holds each listing + real delist reason (Robert); (2) if a new entity is needed, CorpBot's account setup (`czp/hooja_republish_entity_setup.md`); (3) IP chain-of-title clearing Lawyer + konkursförvaltare. Path splits here into "update existing listing" vs "new-entity republish."

---

## Milestone 2 preview (not ticketed yet - after M1 build is green)
- Ad-funnel improvements: add AppLovin/Mintegral/Vungle, interstitial-between-runs + menu banner, fix reward-event plumbing bugs, wire `onImpressionDataReady` -> PlayFab.
- IAP: Unity IAP 4.13+ + PlayFab receipt validation, the 8-SKU catalog (VIP/doublegold/doublescore/gold packs/starter/potion), store product config. ~6-10 dev-days; blocked on the 6 IAP decisions in the brief.
- Child-directed decision (lean: no) + save-sync backup.

---

## Suggested sequence
1. Parallel now: hoj-003 (package check) + Robert installs Unity Hub both machines.
2. hoj-002 spike -> decision.
3. hoj-004 engine upgrade -> hoj-005 LevelPlay migration.
4. hoj-006 (Android) + hoj-007 (iOS) builds, then hoj-008 CMP.
5. hoj-009 keystore rotation once the console/account picture is known.
6. hoj-010 stays blocked until the entity/IP gate clears.
