---
name: Contract templates
description: CZP contract template library — canonical location, MNDA + Subcontracts subfolders. Start here for any new subcontractor or client agreement.
type: reference
originSessionId: fa2f1009-25a5-4f75-a000-2c6fd10ad031
---
## Canonical location (as of 2026-07-17 — moved during db-256 Phase 6 close-out)

AP internal shared drive → `Templates/Contracts/` ([folder](https://drive.google.com/drive/folders/19Sg5FabNRw3VR47vKVpwysuaRiGEf6at)). Consolidated into ONE home (contract templates are AP-AB-mastered). **The MNDA and Subcontracts folder IDs survived the move**, so any earlier reference to them still resolves — only the parent path changed (from CZP `czp_legal/templates/` to AP internal `Templates/Contracts/`).

- `Templates/Contracts/MNDA/` ([folder](https://drive.google.com/drive/folders/1JTqk3NoFHXc27C9oFCu5iVSkWh3mlQkO)) — ID unchanged.
  - **MNDA Template — Aurora Punks AB** (master, Aurora Punks AB as named party with org no 559256-9718, Stockholm address, Robert as CEO signatory). Doc id `1DOlOQIP4B5VwZmFc34q3D74qoLYEqizTxrzgo8J_KOw`.
- `Templates/Contracts/Subcontracts/` ([folder](https://drive.google.com/drive/folders/1G0JoYgHL3eRFMlpi5sI-c5El1cy-YxRe)) — ID unchanged.
  - **Sub-Contractor Agreement Template — Aurora Punks (seed copy)** — pulled from FTG_RM, may still contain project-specific text that needs scrubbing on first use. Doc id `1RQCf5LUrenVLt3gFbO3b9u56Ble6JFVITlQiCobJusY`.
- `Templates/Contracts/` also holds the AP ContractorAgreement master docs (`ContractorAgreement_Master_AP <> Client_Project` `19s8EtXqsjdCtkm8E80tupKwh7UpWvliXryrEg---3NE` + a "Kopia av" copy).

**Note:** the CZP `czp_legal/templates/` parent folder (`1ykv_0lYLgf4DtzgshCO3KRzf5zNVE1A8`) is now an emptied husk left in place (not deleted). Don't add new templates there — use AP internal `Templates/Contracts/`.

## Use

For a new MNDA or subcontract: COPY the master into the project's legal folder (e.g. `czp_projects/Kingdom2Crowns/k2c_legals/`), then customise the copy via the Docs API (`replaceAllText` for placeholder strings). Don't edit the masters.

## Old location (deprecated)

`G:\Shared drives\CZP\Projects_2\FTG_RM` — original templates lived here. Robert is migrating away from per-project ad-hoc templates to the canonical `czp_legal/templates/` folder. If you find a template only at the old location, ask Robert before promoting it to the new one.

## Important — pick the right Aurora Punks entity

Robert has two entities that look related but aren't interchangeable:
- **Aurora Punks AB** (org no `559256-9718`, Timmermansgatan 43, 118 55 Stockholm) — the company that signs publishing / co-dev / outsourcing deals. Use this on K2C-style contracts.
- **White Lines Black Spaces AB** ("DBA: Aurora Punks", Drottninggatan 18, 961 35 Boden) — older entity behind some legacy contract templates.

The new MNDA template uses Aurora Punks AB. If you find an older NDA template that names White Lines Black Spaces AB (DBA Aurora Punks), it's the wrong template for current work — use the new master in `czp_legal/templates/MNDA/` instead.
