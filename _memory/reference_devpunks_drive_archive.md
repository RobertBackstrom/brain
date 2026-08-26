---
name: reference_devpunks_drive_archive
description: "Drive DevPunks/ is the APDS project archive — full source checkouts that never reached GitHub. Check it before concluding source doesn't exist."
metadata: 
  node_type: memory
  type: reference
  originSessionId: 0fa0ea5b-5f33-483f-b4a0-d9b88dd9ae53
  modified: 2026-08-03T09:25:41.904Z
---

Found 2026-08-02 while building the GameDev code corpus, after twice wrongly
concluding from GitHub alone that UE source didn't exist.

On the **Aurora Punks shared drive** (`0ACOk67Zhg9zlUk9PVA`), folder **`DevPunks`**
(`1447LqpTPEaskWFmNx1TdfuTnhHOhijGA`) is the APDS working-projects archive: ~20
project folders, several holding **full source checkouts that are on no GitHub org**.

Contents: Innsmouth, Distant Bloom, GroundZero, RON (Ready Or Not), Strike Force
Heroes, BackPackHero, Chenso Club, Go Fight Fantastic, BlockEm, Telltale games,
Glowmade, Good Shepherd, Kredolis, Centum, KreatureKind, cloke, GB, TB, Neat, plus
shared `SDK/` (Xbox Series + PS5), `Plugins/` and `Templates/`.

**Depth varies per project — look before concluding:**
- **Innsmouth** — complete **UE 5.4** checkout at `DevPunks/Innsmouth/NR89/Innsmouth/main2`
  (`1YTkDfcHUe8diTw08Ilj0hAX05lMFf-B_`). `Source/`, `Content/`, `Config/`, `Plugins/`,
  `Innsmouth.uproject`, `.p4ignore`, `5.4.1_ConversionNotes.txt`. GAS-based, custom
  gravity movement. Source is only ~1.2 MB: Blueprint-heavy, thin C++ layer.
- **Distant Bloom** — UE 4.27. `Archived Project/` + `DistantBloom.zip` (14.9 GB),
  plus AP-authored evaluation notes and `DB_Project_TechInformation.xlsx`.
- **GroundZero**, **RON** — builds only, no source. RON is win64 build zips from 2023,
  consistent with the Ludeo SDK tech review rather than a port engagement.

Pull a subtree with `code-corpus/pull-drive-project.js <folderId> <destName>`, which
skips `Content/`, `Binaries/`, `Intermediate/`, `Saved/`, `DerivedDataCache/` by
default — that is where a UE project keeps its gigabytes and none of it is text.

**Why it matters:** searching GitHub and concluding "no source exists" was wrong twice
in one session. **How to apply:** for game source, check GitHub (Unity), then Drive
`DevPunks/` (both engines, the porting archive), then Perforce (live UE projects).
See [[reference_source_control_map]], [[reference_drive_folders]].
