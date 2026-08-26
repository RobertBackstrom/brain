# Build machine prep: what to install before Monday 2026-08-10

| | |
|---|---|
| **Date** | 2026-08-04 |
| **Machine** | ASUS desktop (ex-Petter), Windows 11 Pro, Ryzen 9 7950X3D (16C/32T), 64 GB RAM, 2x 2 TB NVMe, RTX 3060 |
| **Purpose** | Item A6 of [execution_plan_agent_build.md](execution_plan_agent_build.md). Unblocks B1 (first build) and B2 (Blueprint export). |

## 1. Verdict on the hardware

Comfortably sufficient, and the CPU is the part that matters most.

| Part | Assessment |
|---|---|
| Ryzen 9 7950X3D, 16C/32T | The right bottleneck to have. UE compiles and shader compilation are CPU-parallel; 32 threads turns a full engine build into roughly an hour instead of an afternoon. |
| 64 GB RAM | Fine. UE 5.3 editor on a 5.2 GB content project sits well inside this. Shader compilation with 32 workers is the spike; if it ever thrashes, cap workers rather than buying RAM. |
| 2x 2 TB NVMe | Plenty. Budget ~150 GB engine source build, ~30 GB project with DDC, ~50 GB headroom. Put the engine on one drive and the project + DDC on the other so compiles and asset loads do not contend. |
| RTX 3060 | Adequate. This is a stylized arena game, not a Nanite/Lumen showcase. It matters for editor viewport and `GPULightmass` bakes, both of which it handles. |
| Windows 11 Pro | Required. UE packaging, Steamworks tooling and the console-adjacent toolchains are all Windows-first. |

## 2. Inventory the disk BEFORE installing anything

This machine was Petter's. Two things we are currently missing may be sitting on it, and both are
gone the moment someone reformats or does a clean Windows install. Do this first, take a copy, then
install.

1. **Any Git checkout, for its remote URL.** Aurora Punks used a self-hosted Git ("vår git", per
   Eriksson) that is not GitHub, is not on the VPS, and does not resolve under any known
   `runatyr.games` / `aurorapunks.com` hostname. A leftover clone's `.git/config` names the server
   outright, which is cheaper than trying to find the box. Run this before touching anything:

   ```powershell
   Get-ChildItem -Path C:\,D:\ -Filter config -Recurse -Force -ErrorAction SilentlyContinue |
     Where-Object { $_.DirectoryName -like "*\.git" } |
     ForEach-Object { Select-String -Path $_.FullName -Pattern "url\s*=" }
   ```

2. **The Unreal console tool.** Eriksson recalls Petter and Gustav building a console tool for
   Unreal, documented, last touched by Petter. It is not in `Aurora-Punks/AP-Tools` (whose `Unreal/`
   folder holds only a `dummy.txt`, single branch), not anywhere else in the Aurora-Punks or
   BADASS-Studios orgs, and not under Petter's GitHub account (`ap-petter`, created 2024-10-31, 15
   commits total, zero own repos). If he worked locally and never pushed, it is on this disk.
   Check `Documents`, `source`, `repos`, `Perforce`, `Unreal Projects`, and any workspace roots.

3. While there: Perforce workspace files (`.p4config`, `P4CLIENT` in the environment) would also name
   the P4 server and his client spec.

Copy anything found to the VPS before the machine is repurposed. Do not rely on being able to come
back to it.

## 3. Install list, in order

1. **Visual Studio 2022** with the *Game development with C++* workload, plus *.NET desktop
   development*, *Desktop development with C++*, MSVC v143, Windows 10/11 SDK, and the *Unreal
   Engine installer* component. UE 5.3 wants VS 2022 specifically; VS 2026 is not a supported
   toolchain for 5.3 and will cost a day if someone installs it by reflex.
2. **Unreal Engine 5.3, source build, from GitHub** (Epic Games account linked to the
   EpicGames/UnrealEngine org). Not the launcher build. Reasons: the project ships dedicated-server
   targets that need engine source to compile, engine-level debugging becomes possible when the first
   build inevitably fails somewhere unexpected, and it keeps the door open for Epic's MCP plugin
   later, which requires a source build. On this CPU the build is roughly an hour, so the flexibility
   is nearly free. Run `Setup.bat`, then `GenerateProjectFiles.bat`, then build `Development Editor
   | Win64`.
3. **Git for Windows + Git LFS.** LFS matters: the content tree is 5.2 GB of binary assets.
4. **Python 3.11** on PATH, for the editor-scripting export in B2. Note UE 5.3 also embeds its own
   Python for `-run=pythonscript`; the system install is for tooling around it.
5. **Steamworks SDK** (latest), for the SteamSockets and session work in Phase 1.
6. **7-Zip**, for the 5.6 GB project archive.
7. Optional but worth it: **Rider for Unreal** or at least VS with UnrealVS. Faster than raw VS for
   navigating a UE codebase.

## 4. Settings that save time later

1. **Exclude the engine, project and DDC directories from Windows Defender real-time scanning.**
   This is the single biggest easy win on UE build times; scanning every intermediate object file can
   cost 30 to 40 percent.
2. **Set a shared DDC path** on the second NVMe (`UE-SharedDataCachePath`). Shader compilation is the
   slowest part of a first project open and this makes it a one-time cost.
3. **Enable long path support** (`git config --system core.longpaths true` plus the Windows group
   policy). UE plus Perforce-era paths hit the 260-character limit routinely.
4. Leave `Saved/`, `Intermediate/` and `DerivedDataCache/` out of any backup or sync tooling.

## 5. Access needed on the machine, not just software

1. GitHub account with access to the AP org, and linked to Epic Games for the engine source.
2. Steam account with the Curveball app in its library once the app ID question is resolved, plus
   Steamworks partner access for depot uploads later (WP3.3).
3. Whatever The Gang gives us for source: p4 client and credentials if Perforce, otherwise the zip.
4. Remote access for me. This is the open item below.

## 6. Division of labour with the Linux server

Settled with Robert 2026-08-04: **there is a separate Linux server**, so this Windows box is the
build machine and nothing else. That is the right split. The Death Board, the scheduler, the RAG
index, the MCP fleet and the systemd timers are all Linux-native, and no attempt should be made to
fold them onto a Windows desktop (dual-boot cannot host 24/7 and build UE at the same time; WSL2 as
a production host puts the Assistant behind Windows update reboots).

So:

| Workload | Host |
|---|---|
| UE 5.3 editor, compiles, packaging, Blueprint export, Steam depot uploads | **this Windows machine** |
| Grant service (WP2.1), RAG index, Death Board, scheduling, agent runs | **Linux** (VPS today, the Linux server when that migration happens) |

The grant service is being written portable (Node, no host-specific assumptions, config via env) so
it can be stood up on the VPS now and moved to the Linux server later without a rewrite. No decision
needed before it is built.
