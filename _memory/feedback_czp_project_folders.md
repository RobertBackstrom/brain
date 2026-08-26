---
name: CZP Drive folder convention
description: czp_<domain> top-level folders for non-project-specific files; czp_projects/<ProjectName>/<prefix>_<purpose> for project-specific. If no project folder, create one under czp_projects.
type: feedback
originSessionId: 32a2d705-9dd9-4dc6-9f12-32d4723d9284
---
**UPDATE 2026-06-01 (supersedes the project-specific part below):** Project folders have **moved out of `czp_projects` into the dedicated `projects` Shared Drive** (`0AESiGYhJVmCQUk9PVA`) and now use the **nested `_legals` / `_deliverables` / `_financials` model, each with `_working` + `_archive` children** — see [[czp_project_folder_structure]] / [[feedback_czp_project_structure]]. The non-project `czp_*` top-level zone (described below) is still valid for generic CZP files in the CZP drive.

The CZP Shared Drive (`0AAaQFbRZFdpKUk9PVA`) is split into two zones. Putting a file in the wrong zone causes other agents to miss it.

**Non-project-specific (top-level `czp_*` folders):**
- `czp_legal/` — generic templates, master MNDA, legal KB
- `czp_finances/` — CZP-entity finance docs
- `czp_company/` — company-level admin
- `czp_employee/` — HR / employee docs
- etc.

**Project-specific (under `czp_projects/`, id `1CAS46jrj9qsPip9tMYnlxL6otLysoqL7`):**
- Each project: descriptive folder name (e.g. `Kingdom2Crowns`, `formuladrone`, `Eternal Minds AB`)
- Inside each project folder, subfolders use a prefix slug:
  - `<prefix>_legals` — counterparty NDAs, signed contracts, legal correspondence
  - `<prefix>_deliverables` — client-facing share point
  - `<prefix>_meetings` — notes/agendas (when relevant)
  - etc.

**Why:** Robert grants client access at the project subfolder level. Mixing project-specific docs into `czp_legal/` or other generic folders breaks the access model and means the docs aren't linked to anything searchable. Equally, generic templates buried under a project folder are unfindable for the next project that needs them.

**How to apply:**
1. Project-specific doc → `czp_projects/<ProjectName>/<prefix>_<purpose>/`. **If the project folder doesn't exist, create it** (descriptive name) + the `<prefix>_<purpose>` subfolder before uploading.
2. Non-project doc → matching top-level `czp_<domain>/` folder.
3. Don't reuse another project's `<prefix>_legals` for an unrelated doc. (Lost Hive MNDA sat in `k2c_legals` because Lost Hive is a K2C subcontractor — the MNDA *was* K2C-scoped. Don't generalize that pattern.)

**Source:** Robert's correction 2026-05-06 after CorpBot misfiled the Formula Drone NDA into `k2c_legals` (mistakenly assumed it was a generic CZP legals folder). Convention codified into [[gdrive_workflow]] for all agents.

**Common gotcha:** Older memory referred to "CZP Projects_2" — folder is now named `czp_projects`. Same ID. Don't get tripped up by the old name in legacy notes.
