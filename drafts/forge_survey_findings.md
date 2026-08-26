# forge (ex-Petter desktop): Phase 1 survey results

| | |
|---|---|
| **Date** | 2026-08-14 |
| **Machine** | `forge` / `PetterBox`, ASUS, Win 11 Pro, Ryzen 9 7950X3D, 64 GB, 2x 2 TB NVMe, RTX 3060 |
| **Method** | Remote, over Tailscale + OpenSSH as local admin `PetterBox\robert` |
| **Runbook** | [petter_desktop_account_migration.md](petter_desktop_account_migration.md) |
| **Answers open questions in** | [monday_hardware_recovery.md](monday_hardware_recovery.md) |

## 1. The three finds that matter

1. **The console wrapper exists and is on this disk.** `D:\UnrealProjects\APConsoleSubsystem.cpp`
   (22.8 KB) and `.h` (3.6 KB), last written 2025-08-18. It is a UE `GameInstanceSubsystem` wrapping
   **console achievements and activities**: `DECLARE_LOG_CATEGORY_EXTERN(APAchievementLog)`,
   `APActivityLog`, `FAchievementDefinition` (name / stat / stat max), `EActivityOutcome`
   (Completed / Failed / Cancelled). This matches the artifact Eriksson described and that is absent
   from every GitHub org. **Already copied to `D:\_preserve\_critical\`.** Two loose files sitting
   outside any repo, which is exactly how this kind of thing gets lost.
2. **AP's self-hosted Git server is named.** `D:\UnrealProjects\unreal-punks-template` has remote
   **`http://git.aurorapunks.com/petter/unreal-punks-template.git`**. That hostname is what the
   recovery runbook could not find. It **does not resolve** from the VPS or from `forge` today, and
   there is no A record, while `aurorapunks.com` itself resolves fine to Cloudflare. So the box is
   gone from DNS, not the domain. Robert controls that DNS, so restoring the name is trivial once
   the machine is back. The `/petter/<repo>.git` path shape indicates Gitea or GitLab, not bare Git.
   That repo has **1 unpushed commit** (`6ea021d`, "Restructured core part for abstraction",
   2025-09-25) plus 7 uncommitted files, so this working copy is ahead of whatever the server holds.
3. **AP's Perforce workspace on this machine is empty.** `D:\Perforce\AP-Game\Project` exists and
   contains **nothing**. AP's Unreal game is not on this disk. Recovering it still depends entirely
   on the ex-ARK box.

## 2. Storage: the problem is far smaller than the raw numbers suggest

Volumes: **C: 1862.1 GB (116.2 free)**, **D: 1863.0 GB (362.3 free)**. Disks are a Seagate FireCuda
530 2 TB and a Kingston Fury Renegade 2 TB, both NVMe, both `Healthy`, wear counters at 0.

Roughly 3.14 TB is in use, but almost all of it is regenerable:

| Path | Size | Files | Verdict |
|---|---:|---:|---|
| `D:\Perforce\GZ\GZ_petter_Project` | 1219.8 GB | | **Regenerable.** `gzp4` server is LIVE (see §3). Third-party IP, see §5. |
| `C:\GZBuild` | 655.6 GB | 455 | Regenerable. Packaged build output. |
| `C:\UnrealData` | 427.6 GB | 1 384 381 | Regenerable. Derived data cache. |
| `D:\Perforce\GZ\UnrealEngine-5.6.0-release` | 247.2 GB | | Regenerable. Epic's engine source. |
| `C:\Git\UnrealEngine-Angelscript` | 169.1 GB | | Regenerable. Public Hazelight fork, and it has **no `.git`** so it is not even a repo. |
| `C:\Git\Soulwalker` | 155.4 GB | | On GitHub (`Eternal-Minds-AB/Soulwalker`). **0 unpushed**, 4 uncommitted files. |
| `C:\Users\PetterMikaelsson` | 78.4 GB | 153 211 | **Preserve.** Mostly AppData; real content is Documents 1.5, Desktop 5.5, Downloads 9.8. |
| `D:\UnrealProjects` | 29.7 GB | 17 746 | **Preserve.** Holds the console wrapper + `unreal-punks-template`. |
| `C:\HordeAgent` | 20.3 GB | 48 304 | Regenerable. Unreal Horde build agent working dir. |
| `C:\Git\block-em` | 4.8 GB | | On GitHub (`Aurora-Punks/block-em`). **0 unpushed**, 3 uncommitted. Branch `blocks-programming`, last commit 2026-01-07. |
| `D:\UnityProjects` | 0.8 GB | 8 196 | **Preserve.** `BuildTool` + `BuildVersionTest` (empty repo, no remote). |
| `C:\Git\ColdResponse` | 0.5 GB | | **Preserve.** No `.git`. Angelscript UE project (`Plugins`, `Script`, `Source`). |
| `C:\steamcmd` | 0.15 GB | 200 | Regenerable. |

**Conclusion: the irreplaceable set is under 100 GB, not 3 TB.** It fits in D:'s free space with room
to spare. No external drive is needed to make the account transition safe. An external is still worth
buying later if the GZ workspace or the build outputs are ever wanted offline, but that is a
convenience purchase, not a rescue.

Note on `block-em`: last commit 2026-01-07 matches the GitHub repo exactly, which confirms that
Wavedash's January-to-March browser porting work is **not** on this machine either.

## 3. Version control server map, recovered from `.p4qt` and `.gitconfig`

| Endpoint | ServerName | User | Reachable from `forge` |
|---|---|---|---|
| `ssl:192.168.50.106:1666` | **AuroraPunksPerforce** | `ap`, `admin` | **No.** Different subnet entirely: `forge` is on 192.168.32.0/24. |
| `ssl:185.107.97.197:1666` | `gzp4` (nfoservers, Frankfurt) | `petter` | **OPEN** |
| `ssl:falldamage.helixcore.io:1666` | `master.1` | `oskar.hansen` | No |
| `VCSBOY:1666` | legacy hostname, same fingerprint family as .106 | `admin`, `ap` | Does not resolve |
| `http://git.aurorapunks.com` | self-hosted Git | `petter` | Does not resolve, no A record |

Stored SSL trust fingerprints exist for `192.168.50.106:1666` and `185.107.97.197:1666`, which will
verify the AP server's identity when it comes back up.

**`VCSBOY` is very likely the ex-ARK box's Windows-era name, and `192.168.50.106` its address on the
old office LAN.** `forge` sits on 192.168.32.0/24 today, so that server is not merely powered down,
it is on a network this machine no longer touches.

An **OpenVPN Connect DCO adapter** is installed on `forge`, which is the likely route Petter used to
reach 192.168.50.0/24. The profiles directory
(`AppData\Roaming\OpenVPN Connect\profiles`) is **empty**, so no configuration survived.

## 4. Already preserved

`D:\_preserve\_critical\` (tiny, done):

1. `APConsoleSubsystem.cpp` + `.h` — the console wrapper.
2. `p4tickets.txt`, `p4trust.txt` — server list plus SSL fingerprints. **These contain live Perforce
   tickets and are credentials.** Register per [[feedback_secrets_registry]] before this leaves the box.
3. `.p4qt\` complete, including `connectionmap.xml` and `WorkspaceSettings.xml` for all four
   connections, plus `.p4v\`.
4. `.gitconfig` (user `PetterAP`, `petter@aurorapunks.com`), `sanct.log`.

`D:\_preserve\petter-profile\` and `D:\_preserve\ColdResponse\` — **done and verified 2026-08-14**,
`/COPY:DAT` so the copies inherit destination ACLs rather than Petter's Entra SID.

| | Dirs | Files | Bytes | Failed |
|---|---:|---:|---:|---:|
| petter-profile | 32 802 / 32 821 | 136 301 / 136 520 | 57.45 GiB | **216 (59.4 MB)** |
| ColdResponse | 722 / 722 | 2 887 / 2 887 | 472.7 MB | 0 |

The 216 failures are **entirely** `AppData\Local\Packages\*` (Microsoft Store app containers:
PowerToys, ScreenSketch, YourPhone, MSTeams, StartMenu, CrossDevice) and
`AppData\Local\Microsoft\WindowsApps\*` (zero-byte app-execution-alias reparse points, which cannot
be copied by design). Store app state and alias stubs, nothing of value. The gap between the
source's 153 218 files and robocopy's 136 520 is the deliberate `Temp` and `INetCache` exclusion.

D: free space went 362.3 GB → 304.2 GB. Spot-checked by reading `.gitconfig` and listing
`Documents\` (15 entries) out of the copy.

## 5. Flag: a lot of this is not AP's code

1. **`GZ` (1.2 TB)** comes from `gzp4` at a Frankfurt nfoservers VPS under user `petter`. That server
   is live and is not ours. Whoever owns it owns that IP.
2. **`Soulwalker` and `ColdResponse`** are `Eternal-Minds-AB` repos, which is Robin Hofström's
   company ([[project_eternal_minds]]).
3. `falldamage.helixcore.io` under `oskar.hansen` is a Fall Damage server.

Copying locally on a machine Robert possesses is one thing. **Taking any of it off the box, or
indexing it into the RAG wiki, is a different question and should not happen by default.** The RAG
extraction in Phase 7 should be scoped to AP-owned material only: the console wrapper,
`unreal-punks-template`, and `block-em`.

Related and still unresolved: whether the hardware and its contents are Robert's or APDS estate
property, given the device is Entra-joined to the APDS tenant ([[project_baremetal_migration]] §Entra).

## 6. What this changes for the ex-ARK recovery

The ARK box is now the only route to three things this machine does not have: AP's Unreal game
(the P4 depot), the self-hosted Git history behind `git.aurorapunks.com`, and whatever else never
left it. What we gained here is precision. When it powers on we know to look for a Perforce server
answering on **1666** with ServerName **AuroraPunksPerforce**, users `ap` and `admin`, a matching SSL
fingerprint, and a Gitea/GitLab-style Git service that was published as **git.aurorapunks.com**.
