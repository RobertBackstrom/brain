---
name: project_baremetal_migration
description: "Planned move off the Hetzner VPS onto a local bare-metal box that can run the UE5 editor; changes what 'the VPS is the runtime' means"
metadata: 
  node_type: memory
  type: project
  originSessionId: 0fff744a-24ad-487d-a6e4-a5c826b165f8
  modified: 2026-08-24T09:25:15.714Z
---

Robert, 2026-08-04 (during the Curveball P2P scoping): the whole stack is moving
off the Hetzner VPS onto **a local bare-metal machine that hosts everything and
is capable of running the UE5 editor**. No date given yet, framed as "soon".

**Why it matters:** the foundational rule in `CLAUDE.md` is "the VPS is the
runtime", and several architecture calls follow from the VPS being headless
Linux, 8 GB, no GPU (see [[reference_vps_capacity]]). Bare metal with an editor
removes that constraint and makes previously-rejected options viable:

- **UE5 editor workloads on the host itself** — engine MCP servers, Blueprint
  export commandlets, cooks, automated builds, PIE-based tests. All of these
  were "must run on someone's Windows box" while we were on the VPS.
- Anything else that was shaped around 8 GB and no GPU (concurrent session
  limits, local model inference, heavy asset processing).

**The box is not blank, and that is load-bearing.** Identified 2026-08-04: it is the same physical
machine that used to run the ARK server, and it hosted **both Aurora Punks' self-hosted Git server
and Perforce**. It is currently powered down; Robert regains access **2026-08-10** along with Petter
Mikaelsson's Windows desktop (the intended UE build machine). Old hostnames will not resolve, which
does not matter: bare Git repos clone straight off disk without reviving the service.

**Two of those unknowns were resolved 2026-08-14 from Petter's desktop** (full survey:
`drafts/forge_survey_findings.md`):
- **The self-hosted Git server was `http://git.aurorapunks.com`** (path shape `/petter/<repo>.git`,
  so Gitea or GitLab, not bare Git). It has **no A record today** while `aurorapunks.com` itself
  resolves to Cloudflare, so the name is simply gone from DNS and Robert controls that DNS. Found via
  the remote on `D:\UnrealProjects\unreal-punks-template`, which is **1 commit ahead** of it.
- **AP's Perforce is `ssl:192.168.50.106:1666`, ServerName `AuroraPunksPerforce`**, users `ap` and
  `admin`, legacy hostname `VCSBOY`, with a stored SSL trust fingerprint to verify it by. Note it
  lives on **192.168.50.0/24**, a different subnet from where Petter's desktop now sits
  (192.168.32.0/24), so it is off-network as well as powered down.
- **Petter's console wrapper was found on the desktop, not the server**: `APConsoleSubsystem.cpp/.h`,
  a UE `GameInstanceSubsystem` for console achievements and activities. Preserved. But
  `D:\Perforce\AP-Game\Project` on that machine is **empty**, so AP's Unreal game still exists only
  on the ex-ARK box.

**Do not reinstall it before recovering it.** It is the only known copy of AP's internal Git history,
including a console wrapper/tool written by Petter Mikaelsson that exists nowhere on GitHub (verified:
no `ap-petter`/`petter` commits in `apds-console-wrapper`, `AP-Tools/Unreal/` is a `dummy.txt`
placeholder, zero personal repos). Note the name trap: the GitHub `apds-console-wrapper` is **Peter
Vestman's** 2022 work, a different artifact and a different person. Runbook:
`drafts/monday_hardware_recovery.md`. Mirror the Git repos to GitHub and take a `p4d` checkpoint
before the machine becomes the Assistant host.

**How to apply:** the durability principle is unchanged, it is the *host* that
changes, not the philosophy. Keep designing for "hosted, persistent, reachable
from any session, never depends on Robert's laptop being awake". But when an
option is rejected *only* because the VPS cannot run a GPU or an editor, park it
as a later-step option instead of discarding it, and say so. Do not build for
bare metal before it exists; build what works now and note the upgrade path.

**Petter's desktop is Entra-joined to the APDS tenant (verified 2026-08-14 via `dsregcmd /status`).**
Device `PetterBox`, account `AzureAD\PetterMikaelsson` = `petter@aurorapunks.com`, tenant
**"Aurora Punks Development Services AB"**, TenantId `188feaae-5e51-4d0d-b59e-5e0af8659fc2`. APDS is
the entity in konkurs (trustee Nils Åberg / Carler, mål K 4429-25 — see [[project_wlbs_apds_litigation]]).
Consequences that matter:
- **No BitLocker on either volume** (C: 1862 GB OS, D: 1863 GB data, both `Protection Off`, no key
  protectors). The usual "keys escrowed in a tenant we don't control" trap does not apply here, and a
  drive can be pulled and read in another machine as a last resort.
- **`MdmUrl` is empty, so the device is NOT Intune-enrolled.** No remote-wipe path.
- **`AzureAdPrtExpiryTime` was 2026-08-28.** The Primary Refresh Token auto-renews only while the
  tenant still authenticates. If the APDS tenant lapses (unpaid Microsoft billing during konkurs),
  Entra sign-in on this box can stop working. A **local** admin account is therefore not a
  convenience, it is what decouples the machine from a bankrupt entity's directory.
- Win32-OpenSSH does not authenticate Entra accounts cleanly (domain-qualified usernames give
  "connection reset"), so remote access also depends on a local account existing.
- **Open question flagged to Robert 2026-08-14:** whether the hardware and its data are his/AP's to
  take or are APDS estate property under KL 3:1. Not blocking, but unresolved.

**Not to be confused with Robert's Legion.** Confirmed 2026-08-06: Robert's Lenovo Legion is a
**Windows 11 laptop, his mobile machine**, and is a different physical box from the bare-metal host
above. When he says "the hardware we are on" in a VS Code SSH session he may mean the Legion, but
that session actually runs on the Hetzner VPS (KVM guest: no `hwmon`, no fan or thermal sensors,
`/sys/class/thermal` has only virtual `cooling_device*` stubs). Nothing about the Legion's fans,
temps or power state is readable from the VPS, and there is no tunnel to it (no Tailscale, empty
`~/.ssh/config`, `known_hosts` is GitHub only). Legion diagnostics have to run locally on Windows.

Related: [[feedback_vps_operating_environment]], [[project_the_assistant]],
[[reference_vps_capacity]], [[project_curveball]].

## 2026-08-18: host decided. David Kruse's 96 GB Legion, not VCSBOY, not forge.

Robert has a pool of ex-APDS employee desktops in hand (Hardware_Inventory sheet). Decision:

- **Assistant runtime host = Item 30, David Kruse's Lenovo Legion T5**: i5-11400F (6C/12T),
  **96 GB RAM**, 2 TB NVMe, RTX 3060 Ti. Chosen because the Assistant's real constraint has always
  been RAM (the RAG OOMs at 8 GB); 96 GB buries it, 12 threads matches the current VPS, and a
  dedicated desktop runs 24/7 with nothing competing. It inherits the `brain` role name on migration.
- **forge** (7950X3D, RTX 3060, 64 GB) stays the UE5/Unity workstation, NOT the runtime (it is
  actively used, slept, rebooted; proven fragile as an always-on host on 2026-08-18).
- **VCSBOY** (HPE MicroServer, Pentium G6405 2C/4T, 16 GB) is FREED after its Perforce + Git are
  copied off, repurposable as a game server / NAS / archive. It was rejected as host: 2 cores is a
  downgrade from the 8-vCPU VPS.
- **Spare pool also in hand:** Linus's i5-12400F/64 GB/2.7 TB, Tom's Ryzen 7 5800X 8C/16T/32 GB,
  Anastasia's i5-12400F/64 GB. Candidates for build agents / game servers later.

**Sequence:** (1) recover VCSBOY data (db-301): mirror Gitea to GitHub now, then checkpoint + cold-copy
the ~7 TB Perforce depot to an 8 TB+ external drive. (2) stand up David's Legion: wipe, install Linux,
join tailnet as `brain`, migrate the Assistant stack off Hetzner. (3) free VCSBOY. Tracks (1) and (2)
are independent; (1) gates only the final repurpose of VCSBOY.

## 2026-08-20: burken är på tailnet, men fortfarande Windows och utan väg in

Mätt läge denna dag: noden **`David96GB` (100.90.140.53)** joinade tailnet 2026-08-20 17:14 UTC.
Online, men **bara via DERP-relä** (`direct connection not established`), kör **Windows**, och port
**22 och 3389 är båda stängda** från tailnet. Alltså finns ingen fjärrväg in ännu. Nodnamnet `brain`
pekar fortfarande på Hetzner-VPS:en (100.94.230.77).

**Ingen Death Board-ticket finns för själva brain-flytten.** db-300 = forge-övertagandet,
db-301 = VCSBOY. Migrationsspåret lever bara i denna memory + `drafts/fleet_build_server_design.md`.
Det är sannolikt varför spåret glider medan db-301 sväller.

**Robert 2026-08-20, valt scope: "bara fjärråtkomst först".** Ingen wipe, ingen Linux, ingen
stackflytt, ingen ticket. Runbook för det steget: `drafts/david_brain_remote_access.md` (samma
bootstrap-mönster som fungerade på forge). `~/.ssh/config` har nu fleet-poster så namn→100.x mappas
på ett ställe, eftersom MagicDNS inte resolvar från VPS:en (`brain` kör `--accept-dns=false`).

**Två spärrar innan wipe:** (1) inventera disken, samma fråga som på forge om AP-material eller
klient-IP finns bara där. (2) den olösta KL 3:1-frågan om ex-APDS-hårdvaran är Roberts/AP:s eller
konkursboets egendom gäller även denna burk.

## 2026-08-20 (later): host REASSIGNED. David96GB -> ARK toolkit, NOT the Brain.

Robert reviewed project hardware needs and reassigned david96gb. Supersedes the 2026-08-18 "David's
Legion = Brain" decision.

- **david96gb (96 GB) stays WINDOWS, reserved for the ARK: Survival Ascended Dev Kit** (UE5 editor
  needs ~96 GB), i.e. the Necrotic Dominion / Overwolf ARK mod work with Elias Strandberg. It is NOT
  the Brain. SSH/firewall bring-up on it was left half-done (sshd port 22 dropped by Windows Firewall
  on the Tailscale/Public profile); parked, we can finish it later for ARK build tooling, not needed
  headless.
- **Brain host = a spare Linux box.** Robert (AskUserQuestion 2026-08-20) = "I have a spare machine."
  Strong candidate is **Linus's i5-12400F / 64 GB / 2.7 TB** from the spare pool listed above ("setup
  Linus['s] cabinet for the brain" - likely his machine, not just "Linux" the OS; confirm on onboard).
  64 GB is exactly the recommended Brain spec; i5-12400F matches the VPS core count; **no GPU needed**
  because Claude is API-based. If it arrives on Windows, do a fresh **Ubuntu Server** install (native,
  headless, lighter than WSL) since it is dedicated to the Brain.
- **Two agent networks on ONE box.** Robert wants the Claude network AND a second network on a
  DIFFERENT LLM, running in tandem and cross-reviewing each other's work regardless of task. Decision
  (AskUserQuestion): the 2nd LLM is **API-based** (GPT/Gemini/etc.), co-hosted on the same Brain box as
  separate users/containers. So NO GPU cabinet, no second machine. A GPU box would only be needed if
  the 2nd LLM were locally-hosted open-weights (rejected for now). The cross-feedback is an
  orchestration/message-passing layer (software), the miniature of which is Claude Code's Reviewer
  agent. Drive both networks from **VS Code Remote-SSH**, one window.
- **Urgency:** the Hetzner VPS is now actively OOMing (8 GB, ~1 GB/session), so the Brain migration is
  no longer "soon", it is the current priority. Stopgap if the spare box lags: bump the VPS a RAM tier.
- **Onboarding runbook** unchanged from the pattern that worked on apservices/forge: Tailscale up +
  Win32/OpenSSH or Linux sshd + authorize the VPS key `assistant-vps`. Then inventory disk (KL 3:1
  + client-IP question), then fresh Ubuntu, then lift-and-shift the stack off Hetzner.
## 2026-08-21: Brain migration IN PROGRESS — target is the Nitro (apservices), not Linus's box

Robert changed the Brain host again: **run the Brain on the Nitro (apservices, i5-12400F) dual-role
with TeamCity**, to avoid tying up a GPU cabinet. Reality check done: the Nitro is **16 GB, not 64**
(he misremembered), and the board **caps at 32 GB** (2 DIMM slots, SMBIOS max). Still fine, 16 GB
already doubles the OOMing 8 GB VPS; plan a 2x16 GB kit for 32 GB comfort. Keep the VPS ALIVE as
authoritative + backup until the migration is proven (Robert's explicit instruction).

**Big scope finding:** the VPS runs more than the Brain — **OpenSign (5 Docker containers) + Plane
(~8 containers)**, the likely main OOM drivers. Staged plan: (1) Brain to Nitro now; (2) cron +
dashboards next, DISABLED until cutover so nothing double-fires; (3) OpenSign+Plane STAY on the VPS
for now (Nitro 16 GB can't hold them + Brain + TeamCity) — permanent home decided later.

**Migration facts / access:**
- Nitro on tailnet `100.77.150.9`, users `apservices` (NOPASSWD sudo, `/etc/sudoers.d/99-apservices`)
  and now `assistant` (VPS key `assistant-vps` authorized; home `/home/assistant`, matches VPS paths).
- Masterbrain = **34 GB** (`/home/assistant/projects`; 19 GB code-corpus, 13 GB assistant). VPS runs
  **node v22.22.2 at /usr/bin/node** (cron jobs hardcode that path).
- **apt on the Nitro is BROKEN** (half-built nvidia kernel module for kernel 7.0.0-29 fails dpkg).
  Worked around: node v22.22.2 installed from official tarball to /usr/bin/node. Fix apt later
  (purge the failing nvidia pkgs; GPU irrelevant to the API-based Brain).
- MCP servers (all under `assistant/`, need `npm install` on Nitro after copy): gdrive
  (mcp-gdrive-fork/dist), gmail + gmail-personal (mcp-gmail.js), rag (mcp-rag.js), whatsapp
  (whatsapp/mcp-whatsapp.js), atlassian-jira/confluence (bin/*.sh). Creds live in `~/.claude/*` +
  `assistant/.env` (both copied/copying).

**DONE so far:** node v22 on Nitro; `assistant` user + SSH login; `~/.claude` creds + `~/.claude.json`
copied; Claude Code CLI installed (v2.1.238) at `~/.local/bin/claude`; PATH in .bashrc; masterbrain
rsync running (~9/34 GB) via `rsync --rsync-path="sudo rsync"` then chown assistant.
**NEXT:** finish rsync -> `npm install` MCP servers -> live-test a claude session with tools on the
Nitro -> Stage 2 (replicate crontab DISABLED, bring up node dashboards) -> cutover VS Code, VPS to
standby. Do a final delta-rsync at cutover (pause RAG/writes for a clean snapshot).

**Stage 2 step 1 DONE 2026-08-24 (reconcile VPS->Nitro):** Nitro is now authoritative, but the VPS
kept generating content after the code.runatyr repoint (21 aug). Reconciled additively (`rsync --update`,
newer-wins, no `--delete`): 25 followup files (11 new incl. `evt-081..084`, `db-309/310`, `gen-292/293`,
`k2c-049`, `sec-025`, `apb-050`; 13 updated), plus 8 authored artifacts (`wiki/deals/_index.md` = VPS's
newer Aug-24 weekly-reflection cycle, `daily_briefing.md`, cm-digest, ticker digests, k2c catchup-logs).
Both agent-learnings files (`admin`, `ticker`) were byte-identical, no divergence. Followups now 1093,
fully in sync (verified dry-run empty). **NOT yet done:** these reconciled files are on disk but NOT
re-indexed into Nitro RAG, because the RAG watcher is booted by `server.js` (Death Board), which isn't
running on Nitro yet. That is a Stage-2 step-2 dependency: when Death Board starts on Nitro, its watcher
indexes them. Remaining Stage 2: move Death Board + cron to Nitro (repoint board/hive/kanban CF, stop VPS
Death Board+cron), sunset Plane (11 containers), keep OpenSign on VPS but reachable + wire signed-contract
-> _legals archive + RAG. VPS state at reconcile: load 0.56, 4.7 GB RAM free (earlier "33" was transient).

**Stage 2 step 2 DONE 2026-08-24 (Death Board + cron move):** The split Robert chose: **public-facing
content (websites aurorapunks.com/robotlordrising.com, pitches, OpenSign) + backup STAY on the Hetzner
VPS; only the Brain (Death Board + automation) moves to Nitro.** cloudflared also stays on the VPS as the
router (single tunnel 769d4523). Did NOT move the web servers (pitches/clients/static-sites/grade) — they
stay on VPS.
- **Death Board:** now runs on Nitro (`deathboard.service`, enabled + linger, binds `*:3777`). VPS
  `deathboard.service` STOPPED + DISABLED (so a VPS reboot can't restart it and re-collide). CF ingress
  repointed for the 4 Brain hostnames (`board.runatyr.games`, `hive.runatyr.games`, `kanban.aurorapunks.com`,
  `internal.aurorapunks.com`) from `localhost:3777` -> `http://100.77.150.9:3777` (Nitro tailscale IP);
  VPS cloudflared routes to Nitro over tailnet, same pattern as `code.runatyr.games`. Config backup at
  `/tmp/tunnel-config-backup-*.json` on Nitro. All 4 verified 200 through CF Access. Everything public
  still `localhost` on VPS, untouched.
- **Boot-collision gotcha (watch for this on any future DB move):** starting the Nitro Death Board while
  the VPS one still ran = BOTH Discord bots connected on the same token + both schedulers. The Nitro
  instance posted channel legends (cosmetic dup, happens every restart) and processed one `create_from_mention`
  ("create a jira") from Robert. VERIFIED no double-Jira (VPS instance never processed it). Lesson: stop the
  old DB *before or immediately after* starting the new one; do not leave both running.
- **Cron split:** ~16 Brain/RAG/Gmail/community/ticker jobs installed in the **Nitro** crontab (cron daemon
  active; `/usr/bin/node` is symlinked to `/usr/local/bin/node` so VPS lines work unchanged). VPS crontab
  TRIMMED to 4 lines: `opensign-backup`, `opensign-watch` (both OpenSign-local), and `steam-payout-watcher`
  x2 (czp-023, time-critical Aug24-Sep15, STAYS on VPS because **playwright/chromium is NOT installed on
  Nitro** — module load fails). healthz-monitor ran clean on Nitro (exit 0).
- **RAG watcher** is now running on Nitro (booted by server.js), so step-1's reconciled files get indexed.
- **KNOWN CAVEATS / next:** (1) `opensign-watch` still writes contract archives to `_legals`+RAG on the VPS
  (now the stale copy) — no contract is out right now, but before relying on it, move it to Nitro pointing
  at VPS OpenSign over tailscale (`OPENSIGN_BASE_URL` -> `http://100.94.230.77:3782/...`, verify 3782 is
  tailnet-reachable). (2) steam-payout-watcher writes state to VPS masterbrain until playwright is installed
  on Nitro and it's moved. (3) Public web servers (pitches/clients/static) read content from the masterbrain;
  since they stay on VPS but the masterbrain is authoritative on Nitro, new pitch/site content authored on
  Nitro must sync Nitro->VPS to appear live (reverse of the old direction).

- **Checkpoint milestone (db-301) done 2026-08-20:** VCSBOY got its first-ever Perforce checkpoint
  (`checkpoint.4.gz`, 372 MB, clean exit 0 = db healthy), pulled off-box to the VPS and uploaded to
  Google Drive folder **VCSBOY-Backups** (`1m0dV2XtuHbcJhE28Q0NH2Adkgmrarw29`). Reusable resumable
  Drive uploader written: `assistant/gdrive-upload-resumable.js` (chunked, low-memory, for large files
  the multipart `gdrive-upload.js` can't handle).

**Operativ konsekvens som bet 2026-08-26: publika webbsidor ligger kvar på Hetzner och
ssh-aliaset dit är `edge`, inte `brain`.** Efter splitten författas allt på Nitron, men
`pitches/` serveras från Hetzner-boxen. `assistant/sync-pitches.sh` pekade fortfarande på
`brain:`, ett namn som inte längre resolvar, så skriptet hade tyst slutat fungera för
**alla** slugs och redigeringar i `pitches/` nådde aldrig den publika sidan. Lagat.

**Att redigera `pitches/<slug>/` är inte att publicera.** Kör
`./assistant/sync-pitches.sh --apply <slug>` och verifiera sedan mot den publika URL:en.
`assistant/pitch-auth.json` omfattas **inte** av synken, så en lösenordsskyddad slug behöver
sin post tillagd på `edge` separat, annars 404:ar sidan eller serveras ogatad.

