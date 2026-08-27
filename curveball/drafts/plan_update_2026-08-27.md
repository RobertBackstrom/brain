# Curveball: plan update after The Gang's answer on version control

| | |
|---|---|
| **Date** | 2026-08-27 |
| **Author** | GameDev agent |
| **Supersedes** | [source_integration_plan.md](source_integration_plan.md) sections 1, 3 and 4. Revises [execution_plan_agent_build.md](execution_plan_agent_build.md) Lane B. |
| **Trigger** | Olle Brännström's answer 2026-08-19 (Gmail `19e889144ac3e56a`): there is no Perforce left. |
| **Status** | Decisions D3 to D5 taken by Robert 2026-08-27. One prerequisite outstanding, see section 5. |

## 1. What The Gang actually said

1. **No Perforce.** They switched to GitHub outright and MLC was never ported there. The 4 June zip
   is the only copy of the project that exists outside Olle's own workspace.
2. **The zip opens clean in UE 5.3 at their end.** Olle tried it. The `MajorLeagueCurveball`
   reference is a leftover from a rename, not a missing build target.
3. **Their backend also sits on AWS.** He does not know the details and offered to dig. Robert
   declined, since that layer gets replaced.
4. **Steam app ids settled:** 2805120 is the real store page, 2981120 a playtest branch, 3371540 the
   demo used at NextFest.
5. **Still unanswered since 19 August:** LootLocker admin or server access (`a86igukp`), whether
   anything is still running on AWS and who pays for it, and whether the zip is head.

The load-bearing consequence is that the earlier plan's preferred outcome is gone. It assumed we
would either get into their depot or reconcile against it later. There is nothing to reconcile
against. **AP is the version control from here.**

## 2. What the build machine looks like today, measured

Checked on `forge` (100.117.186.92) on 2026-08-27.

1. **Unreal is still not installed.** `D:\UE` is empty, there is no `C:\Program Files\Epic Games`,
   and no `UnrealEditor.exe` for 5.3 anywhere. Every item in Lane B has been waiting on this since
   19 August. The blocker is on our side, not The Gang's.
2. **The toolchain is otherwise ready.** VS 2022 is installed with the C++ workload, plus a VS 18
   that must not be pointed at 5.3. Free space is 87 GB on C: and 273 GB on D:.
3. **The project is unpacked** at `D:\Curveball\BBA\olle_dev`, 8.8 GB on disk, with the original
   `BBA_dev.zip` alongside it (sha256 verified identical to the VPS copy on 19 August).
4. **Measured tree, which is what the repo design below is built on:**

   | Folder | Size | Files | Goes in the repo |
   |---|---|---|---|
   | `Content` | 4.91 GB | 5,469 | yes, LFS (5,186 `.uasset` = 4.58 GB, 179 `.umap`, 55 `.fbx`) |
   | `Plugins` | 0.87 GB | 2,592 | yes, mixed text and LFS |
   | `BuildUtils` | 0.18 GB | 3,675 | yes |
   | `Source` | ~1 MB | 192 | yes, text |
   | `Config` | ~1 MB | 18 | yes, text |
   | `Saved` | 2.79 GB | 2,608 | no, autosaves and crash dumps |
   | `Intermediate`, `Binaries`, `DerivedDataCache` | 0.06 GB | 28 | no |

   Committed size lands at roughly **6 GB**. Largest single file is a 292 MB `BuiltData.uasset`,
   comfortably under GitHub's 2 GB per-file LFS ceiling. The three 348 MB retargeting autosaves are
   in `Saved` and are excluded.
5. **Git on forge reaches public GitHub but has no credential for a private repo**, and the Windows
   credential store fails in a non-interactive session. That matters for the engine source build,
   see section 5.
6. **The machine carries another client's material.** `D:\Perforce` holds a workspace against
   `ssl:falldamage.helixcore.io:1666` as user `oskar.hansen`, with a Fall Damage project tree and a
   fully built UE 5.6 source engine under it. Two things follow: the toolchain here demonstrably
   builds an engine from source, and there is an NDA hygiene item to settle, same shape as the
   borrowed devkit that still had another publisher's title installed.

## 3. Decisions taken 2026-08-27

**D3. Version control is a private Git repo in AP's GitHub org, with LFS.**

The alternatives were a repo inside The Gang's own org, or self-hosted Helix Core on Nitro. AP's
GitHub wins on time to first commit and on access control we own. It also matches where The Gang
themselves ended up, so a later hand-back is a repo invite rather than a migration.

**D4. UE 5.3 as a source build on forge, installed by the Assistant.**

The launcher build would have been faster. Source keeps engine-level debugging available for the
first build failure, and keeps the console door open without a second migration.

**D5. Build first, discover access needs from the work.**

No nudge to Olle now. LootLocker, AWS status and the head question stay open, and the plan is written
so none of them blocks the next two weeks.

## 4. Repo design

**Repo:** private, `Aurora-Punks/curveball-mlc`. AP-owned account, The Gang's IP. Access limited to
Robert, the Assistant's deploy credentials and the build machine until the co-dev agreement says
otherwise.

**Baseline discipline, kept but repurposed.** The vendor branch was originally there so our diff
could be replayed onto their depot. There is no depot, so its job changes: it becomes the record of
what The Gang delivered versus what AP added. That is now a contract artifact, not just hygiene.

1. First commit is the **zip contents verbatim**, extracted fresh from `BBA_dev.zip` rather than from
   Olle's workspace copy, so no crash dumps or autosaves leak in. Branch `vendor`, tag
   `vendor/bba-zip-2026-06-04`, with the sha256 recorded in the tag message.
2. `main` branches off that tag. All AP work lands there.
3. If a newer state from The Gang ever appears, it goes on `vendor` as `vendor/thegang-<date>` and
   the difference is visible instead of guessed. The cost of D5 being wrong is bounded by this.

**LFS.** `.gitattributes` marks `*.uasset *.umap *.fbx *.mp4 *.png *.wav *.dll *.lib *.pdb *.exe`
as `filter=lfs diff=lfs merge=lfs -text`. One GitHub data pack (about $5 per month for 50 GB storage
and 50 GB bandwidth, worth confirming against current pricing at purchase) covers a 6 GB repo with
room for iteration. LFS file locking is available if anyone besides the Assistant starts editing
assets; not needed at one implementer.

**Ignored:** `Binaries/`, `Intermediate/`, `Saved/`, `DerivedDataCache/`, `.vs/`, generated `.sln`.

**Secrets.** Three cleartext keys ride along in `Config` (LootLocker server key, Tolgee API key, and
the Steam app id block). They are The Gang's dev keys and they are already in every copy of the zip.
They go into the repo as delivered on the `vendor` tag, because rewriting the vendor state would
defeat its purpose, and get moved out of `Config` on `main` as part of the first work package.
`SECRETS.md` records where they were.

**Text mirror for review and RAG** stays as it is today: `Source/`, `Config/`, `Tools/` and the
coming `BlueprintExports/` indexed on the VPS. No change.

**Hand-back.** With no upstream, AP holds the only version-controlled copy of a game AP does not own.
The co-dev agreement needs to say who gets the repo and when. That is a CorpBot and Lawyer item, and
it should not wait until delivery.

## 5. Lane B, revised critical path

**B0. Engine source access. This is the one prerequisite that is not in place.**

The UE source repo is private and requires Robert's GitHub account to be a member of the EpicGames
org, linked from the Epic account connections page. Forge currently cannot read it and has no stored
credential, and the Windows credential manager does not work over the SSH session the Assistant uses.
The mechanism that works is a fine-grained PAT in a file-based credential store on forge, or an SSH
deploy key. Half an hour of Robert's time, and the fallback if the Epic link turns out not to exist
is the launcher build, which unblocks the same day.

**B1. Engine build.** Clone the 5.3 branch shallow, run `Setup.bat`, `GenerateProjectFiles.bat`, then
build the Development Editor. Mostly unattended, roughly half a day of wall clock on 32 threads, and
about 150 GB on D:. Sits on the same drive pattern as the existing 5.6 build, which proves the path.

**B2. First project build. Revised down from 16 to 32 hours to 8 to 16 hours.** Olle opening the zip
cleanly removes the "what else is missing" tail risk, and the dead build target turns out to be a
config string rather than an absent file. What remains is 11 marketplace plugins meeting a source
engine, and most of the heavy ones (`awsSDK`, `GameLiftRegionLatency`, `TGEAC`) are removed by the
plan anyway, so a plugin that fights the source build is a candidate for deletion rather than repair.

**B3. Blueprint export**, using `D:\Curveball\Tools\export_blueprints.py`, already written and
waiting. This is still the checkpoint every estimate hangs on. Nothing in Phase 1 gets re-estimated
before it runs.

**B4. LAN listen-server smoke test**, then QA1 with Robert.

**Parallel, no engine needed:** the repo scaffolding and the vendor import can run while the engine
downloads. Both are done from forge, since that is where the full tree lives; the VPS only holds the
466 MB text subset.

## 6. What this changes in the earlier documents

| Document | Change |
|---|---|
| `source_integration_plan.md` §1, §3 | "Use their Perforce if offered" is dead. Git plus LFS is the plan, not the fallback branch. |
| `source_integration_plan.md` §2 | Vendor branch survives, with a new purpose: evidence of the delivered baseline for the contract. |
| `source_integration_plan.md` §4 | The drift risk mostly evaporates. There is no moving upstream to drift from, only Olle's workspace. |
| `source_integration_plan.md` §5 | Upgraded from "worth making sure the agreement says this" to a required clause: repo ownership and hand-back. |
| `execution_plan_agent_build.md` §2 Lane B | Start date moves from 2026-08-10 to whenever B0 clears. B1 estimate halves. |
| `execution_plan_agent_build.md` §4 risk 3 | "The Gang not answering on source" is resolved, not mitigated. Replaced by risk 1 below. |
| `dev_plan_p2p_steam.md` | Technical plan unchanged. |

## 7. Risks after this change

1. **AP becomes the only holder of a version-controlled copy** of someone else's game. GitHub is one
   leg. A second copy belongs in the encrypted Drive leg of the brain backup, or at minimum the forge
   working tree stays untouched until the repo is verified complete.
2. **LFS bandwidth** is consumed per clone of the binary objects. With one build machine and one
   VPS mirror this is noise, but a habit of fresh clones is what burns a data pack.
3. **Another client's NDA material sits on the build machine** (`D:\Perforce`, Fall Damage). Decide
   whether it moves off or stays with Oskar's knowledge, before more people touch forge.
4. **Access discovery deferred by design (D5).** The grant service is built against a LootLocker mock,
   so integration risk shifts right rather than disappearing. First thing that genuinely needs real
   access is grant verification, which lands with WP2.2.

## 8. Immediate next actions

| # | Action | Owner | Blocks |
|---|---|---|---|
| 1 | Confirm the EpicGames org link and get a credential onto forge | Robert | B1, everything after |
| 2 | Create `Aurora-Punks/curveball-mlc`, buy one LFS data pack | Assistant | vendor import |
| 3 | Fresh extract from `BBA_dev.zip`, `.gitattributes` + `.gitignore`, vendor commit and tag | Assistant | all AP work |
| 4 | Clone and build UE 5.3 from source on forge | Assistant | B2 |
| 5 | B2 first project build | Assistant | B3 |
| 6 | B3 Blueprint export, then re-estimate Phase 1 and 2 | Assistant | the honest schedule for Magnus |
| 7 | Repo ownership and hand-back clause into the co-dev agreement | CorpBot, Lawyer | signature |
| 8 | Decide what happens to `D:\Perforce` on forge | Robert | nothing, but it is an open NDA item |
