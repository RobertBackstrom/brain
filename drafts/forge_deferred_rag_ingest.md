# Deferred RAG ingest from `forge` — waits for the bare-metal Linux host

| | |
|---|---|
| **Date** | 2026-08-14 |
| **Decision** | Robert, 2026-08-14: index scope is **everything on the disk**, but **hold most of it until the RAG moves off Hetzner onto the bare-metal Linux server** ([[project_baremetal_migration]]). Engine trees: **Angelscript fork yes, stock UE 5.6 release no.** |
| **Status of the data** | **Not at risk.** Everything below is preserved on `forge` (`D:\`), which stays powered on. Deferring the ingest defers indexing, not preservation. |
| **Source survey** | [forge_survey_findings.md](forge_survey_findings.md) |

## Why defer

Measured on the current Hetzner host, 2026-08-14:

1. `rag.db` is **8.7 GB** already.
2. The VPS has **8 GB RAM and 69 GB free disk**; `code-corpus/` is already 19 GB.
3. `rag-coverage-score.js` **OOM'd twice this July**: `db-284` when the index went 109 759 → 440 719
   docs (331k of the new ones were filename stubs), and `db-286` at a 6.9 GB `rag.db` with a 1.2 GB
   uncheckpointed WAL.

The deferred set below is ~94k source files plus ~275k binary asset names. Ingesting that into an
index that has already failed twice at this scale, on this hardware, is asking for the third failure.
The bare-metal box removes the constraint that caused it.

## Done now (small, AP-owned, nothing else holds it)

| Corpus entry | Files | Notes |
|---|---:|---|
| `code-corpus/repos/ap-console-subsystem/` | 2 | Petter's `APConsoleSubsystem`. Only copy outside `forge`. |
| `code-corpus/repos/unreal-punks-template/` | 66 | `PunksPort` console abstraction (PS5 / XSX / GDK). 1 commit ahead of the dead self-hosted Git. |

`block-em` was already in the corpus at 10 893 files, so it was not re-pulled. Its working copy on
`forge` has 3 uncommitted files that are not on GitHub; low value, noted for completeness.

## Deferred until the RAG runs on bare metal

| Tree | Source files | Source size | Binary assets | Notes |
|---|---:|---:|---:|---|
| `C:\Git\UnrealEngine-Angelscript` | 89 454 | 823.9 MB | | **Include.** Customised Hazelight fork; `ColdResponse` depends on it, so engine internals are retrievable-relevant. Has no `.git`. |
| `C:\Git\Soulwalker` | 3 452 | 21.0 MB | 45 163 (94.8 GB) | Eternal-Minds-AB. Fully pushed to GitHub. |
| `C:\Git\ColdResponse` | 1 183 | 6.7 MB | 206 | Eternal-Minds-AB. Angelscript project, **no `.git`** — this checkout may be the only copy. |
| `D:\Perforce\GZ\GZ_petter_Project` | 1 268 | 9.5 MB | 229 303 (944 GB) | Third-party, from `gzp4` (live). Almost pure content: 1.2 TB of assets, 9.5 MB of code. |
| `D:\_preserve\petter-profile\Documents` | 306 | 842.0 MB | | Unusually large for 306 text files (~2.7 MB average). Inspect before ingest. |
| `D:\_preserve\petter-profile\Desktop` | 55 | 7.7 MB | | |
| `D:\UnityProjects` | 27 | 0.5 MB | | `BuildTool` + `BuildVersionTest` (empty repo, no remote). |

**Excluded by decision:** `D:\Perforce\GZ\UnrealEngine-5.6.0-release` (88 281 files, 833.6 MB) —
stock upstream Epic source, byte-identical to a public clone, zero AP-specific signal.

**Excluded as machine-generated:** `C:\UnrealData` (1 384 381 DDC files), `C:\GZBuild` (655 GB of
packaged output across 455 files), `C:\HordeAgent` (20 GB build-agent working dir), `C:\steamcmd`.

## Two rules for when this runs

1. **Asset manifests are ONE document per project, never one document per asset.** Follow the
   `code-corpus/repos/curveball-bba/_ASSET_MANIFEST.txt` pattern. The ~275k `.uasset`/`.umap` names
   here are exactly the shape of stub that caused `db-284`; as 275k separate docs they would
   reproduce that OOM, as 4 manifest files they cost nothing.
2. **Stage it, do not ingest in one pass.** AP-owned first, then Eternal Minds, then GZ, then the
   Angelscript engine fork last since it is 95% of the file count. Check `rag.db` size and
   `rag-coverage-score.js` health between stages rather than discovering the new ceiling by hitting it.

## Retrieval prerequisite

`forge` must be reachable from whatever host runs the RAG. It is on the tailnet as
`100.117.186.92`, so a bare-metal host that joins the same tailnet
([fleet_network_tailscale.md](fleet_network_tailscale.md)) can pull directly over SSH with no
reconfiguration. **Address it by MagicDNS name, not the `100.x` IP** (rule 1 of the fleet design).
