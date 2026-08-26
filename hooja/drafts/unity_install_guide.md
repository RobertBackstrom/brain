# Unity Install Guide - Hooja spike & builds

**Setup Robert confirmed:** a Windows/Linux machine for Android + a Mac available for iOS. Split the work: **Android on the PC/Linux box, iOS on the Mac.** iOS builds require macOS + Xcode - there is no way around that.

**Versions to install (both machines):** latest **Unity 6 LTS (6000.x)** = the target, and latest **2022.3 LTS** = the stepping-stone hop. Install both via Unity Hub so we can do Hop 1 (2022.3) then Hop 2 (Unity 6) per `unity_upgrade_spike_checklist.md`.

---

## 1. Windows or Linux box (Android half)

1. **Unity Hub**
   - Windows: download Unity Hub from unity.com/download, run the installer.
   - Linux: Unity Hub ships as an AppImage (or the `unityhub` apt repo on Ubuntu/Debian). `chmod +x UnityHub.AppImage` and run. On a headless VPS you can install the Editor via Hub CLI, but note the spike wants the GUI console - a desktop session (or X forwarding) makes Hop 1/Hop 2 far easier. Pure-headless is fine for the eventual CI `-batchmode` builds, not for the interactive spike.
2. **Sign in** with the Unity ID tied to the correct license (Personal is fine for this; confirm entitlement).
3. **Install Editors** - in Hub > Installs > Install Editor, add BOTH latest 2022.3 LTS and latest Unity 6 LTS. For each, tick these modules:
   - **Android Build Support** (this pulls **Android SDK & NDK Tools** + **OpenJDK** - tick both sub-items).
   - **Linux/Windows Build Support (IL2CPP)** as needed.
   - Skip iOS module here (it's inert without macOS).
4. **Android SDK target 35 / NDK / 16 KB:** Unity 6 ships an SDK/NDK new enough for target API 35 + 16 KB pages. If a build complains about the target SDK, in Hub the installed Editor's Android SDK can be updated, or point Unity at a newer SDK via Preferences > External Tools. Verify 16 KB alignment on the output `.aab` with `zipalign -c -P 16 -v 4 app.aab` (or `llvm-readelf` on the `.so`s).
5. **JDK/Gradle:** let Unity use its bundled OpenJDK + Gradle (do NOT point at a system JDK 8). Unity 6 uses Gradle 8 / AGP 8 - the committed 2021-era Gradle templates must be deleted and regenerated (see spike checklist steps 7 and 15).

## 2. Mac (iOS half)

1. **Xcode 16** from the Mac App Store (or Apple Developer downloads). Launch once to install components; run `sudo xcodebuild -license accept`. Xcode 16 = the iOS 18 SDK, which the App Store now requires.
2. **Unity Hub** for macOS (unity.com/download).
3. **Install the same two Editors** (2022.3 LTS + Unity 6 LTS) with the **iOS Build Support** module ticked. (Add Mac build support too if you want to run in-editor.)
4. **CocoaPods** - the LevelPlay/PlayFab iOS pods need it: `sudo gem install cocoapods` (or via Homebrew `brew install cocoapods`). Unity's EDM4U runs the pod install during the Xcode-project export.
5. Apple Silicon note: everything is native arm64; no Rosetta needed for Unity 6 / Xcode 16.

## 3. Which machine does what

| Step | Machine |
|---|---|
| Open project, migrate 2022.3 -> Unity 6, fix console errors, save round-trip smoke | Either (do it once on the PC/Linux box) |
| Android `.aab` build + 16 KB alignment check + target API 35 | Windows/Linux |
| Xcode project export, archive, iOS 18 SDK build | **Mac only** |
| Later: LevelPlay 8.x pods, IAP StoreKit testing | Mac for iOS side, PC for Android side |

## 4. Before you open the project (from the spike checklist)
- Fresh **full** clone (needs GitHub auth for the 3 AP git packages: aurora-audio, aurora-scriptable-values, aurora-save).
- Two working copies (`hooja-2022`, `hooja-u6`), never spike on the main checkout.
- Read each AP package's `package.json` `unity` field first.
- In the Unity 6 copy: update EDM4U, delete the dead Unity Mediation dep xml, delete the TMP manifest entry.

Then follow `unity_upgrade_spike_checklist.md` Hop 1 (PC/Linux, Android) and Hop 2, running the iOS archive steps on the Mac.

**I (GameDev) can drive this with you screen-by-screen once Unity Hub is installed on both machines - or prep a `-batchmode` CI variant later for repeatable builds.**
