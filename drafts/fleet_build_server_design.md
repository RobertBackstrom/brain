# Fleet + build-server design (Aurora Punks local infrastructure)

| | |
|---|---|
| **Date** | 2026-08-19 |
| **Author** | Assistant (DevOps), for Robert |
| **Status** | Draft for review |
| **Decisions locked** | Split-role topology (Robert, 2026-08-19). Brain = David Kruse's 96 GB Legion. Workstation = forge. |
| **Grounded in** | Nicolas Gerard's DevOps proposal + "DevOps and pipeline proposals" deck (2025), BADASS CI/CD epic (Horde + BuildGraph), the AP DevOps Documentation set on Drive, console-SDK reality from the 2022-2024 mail. |

## 1. The fleet (split roles, one box per job)

| Role | Machine | Specs | Why |
|---|---|---|---|
| **Workstation** | **forge** (ex-Petter, ASUS) | Ryzen 9 7950X3D 16c/32t, 64 GB, RTX 3060, 2x2TB | Robert's daily UE/Unity dev box. Rebooted/slept/GPU-loaded, so must not host 24/7 services. |
| **Brain (Assistant runtime)** | **David Kruse's Legion** | i5-11400F 6c/12t, 96 GB, RTX 3060 Ti, 2TB | 96 GB kills the RAG OOM problem. LLM is remote, so the modest CPU is fine. Always-on. |
| **Builder (heavy UE/Unity builds)** | **Tom Lindstrom's Ryzen 7 5800X** (see section 3) | 8c/16t, 32->64 GB, RTX 3070Ti | Best available desktop for compiles. |
| **Artifact + backup store** | **VCSBOY** (HPE MicroServer) | Pentium G6405 2c/4t, 16 GB, 10.6 TB RAID | 10.6 TB is the only bulk storage in the fleet. Weak CPU is fine for file serving. Long-term on its Rocky Linux side (Windows eval expired). |

All nodes join the tailnet (`tail648605.ts.net`) under the personal Google login, addressed by MagicDNS
name, key expiry off, Tailscale `--unattended` so they reconnect at boot.

## 2. The builder is the real open question

Console + UE builds are the CPU-bound, disk-hungry, licensing-gated part. Three sub-problems:

### 2.1 Compute (from the AVAILABLE pool, screenshot 2026-08-19)
forge and Basil are NOT in the available pool (forge = workstation). Ranked by build throughput of what
is actually available:
1. **Tom Lindstrom, Ryzen 7 5800X, 8c/16t, 32 GB, RTX 3070Ti** is the best available DESKTOP builder.
2. **Item 9 laptop, Ryzen 9 5900HX, 8c, 32 GB, RTX 3080 Laptop 16 GB, 2.75 TB** has strong specs but is a
   laptop (thermal throttling under sustained builds, poor for 24/7). Secondary/portable only.
3. Linus / Anastasia i5-12400F 6c 64 GB; Rickard i5-10400F 6c 16 GB; David i5-11400F 6c 96 GB (= brain).
   All 6-core, weaker for compiles.

### 2.2 Storage
Builds eat disk: each engine + platform SDKs run 150-300 GB, plus per-project DDC and packaged output.
- **Elias's box has the only 4 TB** in the pool; everything else is 2 TB.
- VCSBOY's 10.6 TB is the **artifact store**, not the build scratch disk.

### 2.3 Licensing (the hard constraint, not compute)
Console builds are gated, not just by hardware:
- **Unreal**: AP has console access on its Epic org (since 2022).
- **PlayStation**: SDKs via Sony DevNet under NDA (PS4 SDK 9 / PS5 SDK 4 per 2024 mail). Needs registered dev + devkits.
- **Xbox**: GDK (June-version-or-later for submission) via Microsoft Partner Center. WinGDK builds need the GDK installed.
- **Nintendo Switch**: EDEV/SDEV devkits (AP has had several via Kinda Brave / David Pennelle), SDK under NDA.
- **Consequence**: the builder must be a **registered, SDK-loaded machine**, and devkit inventory must be confirmed (several AP kits moved to other studios or were returned to Curve Games in 2024). **Action: inventory current devkit + SDK access before promising all-platform builds.**

## 3. Builder recommendation (three options)

1. **Best-value single builder: Basil's i7-14700KF (20c) + a 96 GB kit moved in + a large SSD.**
   Robert flagged that RAM/parts can move between boxes. Moving a 96 GB kit (from David or Elias) into
   Basil's 20-core chassis gives the strongest build CPU with server-grade RAM. Add a 2-4 TB SSD for
   engines/SDKs. This is the recommended dedicated builder.
2. **forge moonlights as builder.** Fastest to stand up (engines already on it), but couples heavy
   builds to Robert's workstation. Acceptable as an interim while Basil is prepped.
3. **Elias's box (96 GB, 4 TB) as builder.** Best storage as-is, but the 6-core CPU is the weak link.

**Recommendation (available pool):** **Tom Lindstrom's Ryzen 7 5800X desktop is the dedicated builder**
(most cores available, best desktop GPU, desktop chassis for 24/7). Upgrade its RAM 32 -> 64 GB (cheap
AM4 DDR4). forge can moonlight as builder-of-convenience in the very short term since its engines are
already present, but the durable builder is the 5800X. Keep brain (David) and builder separate so a long
console build never starves the Assistant runtime. Basil's 20-core box was the ideal on paper but is not
in the available pool.

## 4. CI system: Horde, not Jenkins/TeamCity (recommended)

Robert named Jenkins/TeamCity, but the evidence points to **Unreal Horde + BuildGraph**:
1. AP already started Horde for BADASS (BX-11 CI/CD epic, BuildGraph Platform_Dev.xml).
2. Horde is Epic's native system: built for UE, understands platform targets, integrates with Perforce
   and UGS, and is free.
3. Jenkins/TeamCity would re-implement what BuildGraph does natively for UE, and neither is Unity-aware
   either. For the Unity projects, a lightweight GitHub Actions self-hosted runner on the builder covers
   it without a second heavy CI server.
**Recommendation:** Horde + BuildGraph for Unreal (reuse the BADASS work); a self-hosted GitHub Actions
runner on the builder for Unity. Revisit Jenkins only if a client mandates it.

## 5. Pipeline shape (target)

1. **Source**: pull from our Perforce (VCSBOY / AuroraPunksPerforce) or client Perforce/Git. Nicolas's
   "modular, opt-in" principle: a client on Git can hook into our Perforce without migrating.
2. **Trigger**: changelist/commit or manual, with a **build-type flag (debug / development / shipping)**
   and a **platform matrix** (Win64, iOS, Android, Steam, PS5, XSX, Switch).
3. **Build**: on the dedicated builder, engine + platform SDK installed, shared DDC.
4. **Artifacts**: land on **VCSBOY's 10.6 TB** store, retention by build-type. Exposed to AP devs and
   the client for test download; shipping builds flow to 1st-party submission (Steam depot upload, Sony,
   MS, Nintendo portals).
5. **Access**: artifact store reachable over the tailnet; external client access via a gated share.

## 5b. forge disk hold (decided 2026-08-19)

forge's disk is packed with GZ (GZ_petter_Project 1.22 TB kept; C:\GZBuild 655 GB, DDC 427 GB,
HordeAgent 20 GB all regenerable but held). Robert's standing instruction: **no engine downloads and
no reclaim on forge until GZ has a new home.** forge is a prepped shell only, correct tooling + config,
zero heavy payloads. Epic Launcher is installed (small) but NO engines pulled. When a project actually
needs a specific engine, install just that one. The trigger for both engine installs and the ~1.1 TB
reclaim is the same event: GZ relocates to the build server / new store. Do not pre-download.

## 6. Open items before build automation is real

1. **Confirm current devkit + console-SDK access** (Sony/MS/Nintendo). This gates all-platform builds.
2. **Decide builder host** (recommend prep Basil, use forge interim).
3. **VCSBOY to Rocky Linux** for the durable artifact/backup role (Windows eval expired; see db-301).
4. **Move Perforce + Gitea off the expiring Windows** (either activate/rearm short-term, or migrate to
   the Rocky side).
5. **Read Nicolas's full deck + DevOps Documentation set** on Drive to reuse the Horde/BuildGraph work
   rather than rebuild it. NOTE: Nicolas is no longer available (2026-08-19), so the pipeline must be
   self-serve/automated; the Assistant sets it up. Reinforces Horde/BuildGraph over hand-tended Jenkins.
