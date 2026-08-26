---
name: reference_source_control_map
description: "Where game source actually lives: GitHub orgs vs the AP Perforce server vs Drive build archives."
metadata: 
  node_type: memory
  type: reference
  originSessionId: 0fa0ea5b-5f33-483f-b4a0-d9b88dd9ae53
  modified: 2026-08-05T22:08:25.628Z
---

Verified 2026-08-02 while scoping the GameDev agent corpus.

**GitHub** (Robert's token, `RobertBackstrom`, reaches `Aurora-Punks` + `BADASS-Studios`):
- `Aurora-Punks` = 32 repos, **all Unity/C#** except `elric` (C++). 90.6 MB of actual source; the ~6.5 GB is binary assets. Porting library = `apds-console-wrapper` (1.81 MB C#), whose `DevPunksSaveGame.ConsoleWrapper` namespace appears in shipped titles' `RuntimeInitializeOnLoads.json`. **It is Unity-only and does not apply to Unreal projects** (verified 2026-08-04: `Assets/`, `ProjectSettings/`, 566 `.cs`, `com.unity.gamecore`, `com.unity.inputsystem.gxdk`; no `.uplugin`/`.uproject`/`.Build.cs`). That is not a gap: UE console support is first-party via Epic's platform extensions, which AP gets as a licensed developer, so there is no wrapper to write. What transfers from APDS console work to a UE port is process knowledge (cert, TRC/XR/lotcheck, save and achievement semantics), not code.
- `BADASS-Studios/UnrealEngine-Angelscript` = 11.9 GB UE tree + Angelscript (`Samples/`, `Script-Examples/`, `Templates/`). The only substantial UE codebase on GitHub. `WSX` is brand assets, not code.
- `Eternal-Minds-AB` (Robin's, public): `RTXGI-UE-Plugin` (11 MB, real); `ColdResponseScripts` / `ColdResponseWorldBuilder` are 1-2 KB README stubs.

**There is a third location, and it is the one that catches people out: AP ran its own self-hosted Git server.** Established 2026-08-05 (Eriksson, Discord). It sat on the **same physical Linux box as Perforce**, the one that used to run the ARK server. Old hostnames no longer resolve and the machine is powered down; Robert regains access **2026-08-10**. This is why a GitHub-only search returns nothing for work people clearly remember doing: the **console wrapper/tool by Petter Mikaelsson** is not in `Aurora-Punks` or `BADASS-Studios` at all (`ap-petter`, created 2024-10-31, 15 commits total, zero personal repos; `AP-Tools/Unreal/` is a `dummy.txt` placeholder). **Name trap:** the GitHub `apds-console-wrapper` is **Peter Vestman's** 2022 work, later touched by Linus Augustsson (2024-06-07), and is a different artifact by a different person. Recovery runbook: `drafts/monday_hardware_recovery.md`. Bare Git repos clone straight off disk, so the service never needs reviving; mirror them to GitHub before the box is repurposed. See [[project_baremetal_migration]].

**Perforce is where the UE game projects live.** AP runs its own P4 server: admin is **greger@aurorapunks.com**, six registered users, free-tier temp key issued 2026-04-22, `db.have` corruption incident handled in Perforce case #01574233 (Apr 2026). Alara Prime (Fall Damage, co-dev signed Sep 2025, dev paused Dec 2025) and Cold Response (Eternal Minds) are not on GitHub, so P4 is the presumed home. Separately, **Blue Scarab granted Robert + Oskar P4 access** under MNDA (Apr-May 2026) for the Equinox porting code review. No `p4` client is installed on the VPS.

**Google Drive holds builds, not repos** — with one checked exception. `BBA_dev.zip` (Curveball, UE 5.3, 5.6 GB) turned out to be a **full project tree**, not a cooked build, and was pulled onto the VPS 2026-08-04 into `code-corpus/repos/curveball-bba/` (Source/Config/Plugins indexed; Content listed by name only). Worth range-reading a zip's central directory before assuming "Drive = builds": the index sits at the end of the file, so two ranged GETs list every entry without downloading gigabytes. Other large archives really are shipped artifacts: `GFF_CERT_PS5_20250108.zip` (5.4 GB) and `GFF_CERT_PS4_20250108.zip` (3.9 GB) cert submissions, Chenso Club Xbox builds, Robot Lord Rising asset dumps. Useful as source-to-port pairings, useless as a source corpus.

**How to apply:** when a task needs game *source*, check GitHub for Unity and Perforce for Unreal. Don't assume Drive has a repo snapshot; it has builds. See [[project_the_assistant]], [[reference_drive_folders]].
