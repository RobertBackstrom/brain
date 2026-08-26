# Hooja Unity Upgrade - Hands-on Spike Checklist

Runs on a machine with Unity Hub + licenses (NOT the VPS). ~one afternoon. Records the decision input for 2022.3-vs-Unity-6.

## Prep (30 min)
1. Install via Hub: latest **2022.3 LTS** patch and latest **Unity 6 LTS** (6000.x), each with Android Build Support (SDK+NDK+OpenJDK) and iOS Build Support.
2. Fresh **full** clone of Hooja (needs GitHub auth for the 3 AP git packages). Two working copies: `hooja-2022`, `hooja-u6`. Never spike on the main checkout.
3. Before opening: fetch the 3 AP repos (`aurora-audio`, `aurora-scriptable-values`, `aurora-save` on `#dev-package`), read each `package.json` `unity`/`unityRelease` field, grep for `#if UNITY_2021` / editor guards. Record.
4. In `hooja-u6` pre-emptively: update EDM4U to latest .unitypackage; delete `Assets/Editor/MediationAdapterDependencies.xml` (+ Mobile Dependency Resolver installer files); delete `com.unity.textmeshpro` from `manifest.json`.

## Hop 1 - 2022.3 (60-90 min)
5. Open `hooja-2022`, accept upgrade prompt. Capture full Editor.log; count errors vs warnings, screenshot first 20 errors.
6. Accept Addressables/package auto-upgrades. If Addressables prompts a schema upgrade, accept, then Build > New Build > Default Build Script for Android + iOS.
7. Delete `Assets/Plugins/Android/mainTemplate.gradle` + `gradleTemplate.properties`; re-enable Custom Main Gradle Template + Custom Gradle Properties in Player Settings (regenerates 2022-shaped templates); Assets > External Dependency Manager > Android Resolver > Force Resolve. Log any repo 404s.
8. Set Android target API 35. Build .aab (keystore pass per `AndroidKeystoreLoader` convention or manual). Record: build success, 16 KB alignment (`zipalign -c -P 16 -v 4` / `llvm-readelf`), Play Console pre-launch dry run if available.
9. Switch to iOS, build Xcode project, open in **Xcode 16**, archive. Record signing/linker errors.
10. Runtime smoke: Play Mode in start scene, **save/load round-trip** (MessagePack + aurora-save), LevelPlay test init, Localization tables load, a Febucci-animated text renders.
11. Commit migrated state on branch `spike/2022-3`.

## Hop 2 - Unity 6 (90-120 min)
12. Open `hooja-u6` (or hop-1 result) in Unity 6. Capture full log. Expect: TMP error if manifest not edited, Addressables 2.x prompt, DOTween setup prompt, `FindObjectOfType` warnings, possible `System.Runtime.CompilerServices.Unsafe.dll` duplicate.
13. Re-run DOTween Setup panel (update from Asset Store if pre-1.2.7xx). Update Febucci Text Animator if TMP compile errors appear.
14. Addressables 2.x: accept migration, rebuild content Android + iOS. Diff group settings vs hop-1.
15. Regenerate Gradle templates (Unity 6 shape incl. `settingsTemplate.gradle`), EDM4U Force Resolve, target API 35, build .aab, verify 16 KB alignment.
16. iOS: build Xcode project, archive with Xcode 16 / iOS 18 SDK.
17. Runtime smoke as step 10 + visual diff of 3-4 key scenes vs 2021 screenshots (sprites, post-processing, Cinemachine, tilemaps).
18. Record per-hop: error count at first open, hours-to-first-successful-build, any risk-matrix item that behaved worse than predicted. That table is Robert's decision input.

## Out of scope for the spike (schedule separately)
The actual ironSource 7.3 -> LevelPlay 8.x code migration. Steps 10/16 only prove the old plugin compiles; store compliance requires the new one.
