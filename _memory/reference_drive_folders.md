---
name: reference_drive_folders
description: "Complete Drive folder ID registry for instant RAG lookups - every key folder mapped to its Drive ID, organized by entity/project, with sharing info. Post-db-256-migration reality."
metadata: 
  node_type: memory
  type: reference
  originSessionId: a0d27c74-28b4-40f6-8f5d-1455fc6ad562
---

# Google Drive Folder Registry

**Purpose:** Map every important Drive folder to its ID so agents can upload/navigate on first try without searching. Update this whenever new shared folders are created or structure changes.

**Last updated:** 2026-08-25 (revisionsmappen `_deliverables_working` + behörighetsläget inlagt; se AP-blocket nedan). Basen är fortfarande 2026-07-17 - **db-256 Drive migration COMPLETE (all 8 phases).** Rewritten to post-migration topology (Option B: one Shared Drive per company/partner + one Projects drive + one Portfolio drive). Authoritative history: `umbrella/aurora_punks/drive_migration_plan_2026-07-08.md` (see the "MIGRATION COMPLETE" header + per-phase EXECUTION STATUS blocks). ID base = the 2026-07-13 metadata manifest + Phase 2-6 result JSONs at `/home/assistant/backups/drive/2026-07-13/`.

> **Note on IDs surviving moves:** every Phase 1-6 move preserved file/folder IDs (Drive keeps the ID on a move). So ID-form links (`/file/d/<id>`, `/open?id=<id>`) and every ID already in this registry keep resolving even where the folder path changed. What changed is *where* things live, not their IDs.

---

## Shared Drives Overview (post-migration)

**Membership rule (decision 3):** tight drive membership. **Robert is Manager on every drive.** Accountants are added by-need in that entity's content batch (deferred, not on empty drives); everyone else (board, partners, clients, co-owners in a disputed entity) gets an **item/folder share**, never drive membership (a drive member sees the WHOLE drive corpus). `all@aurorapunks.com` was removed from both AP drives on 2026-07-13; new access rules TBD.

| Shared Drive | ID | Status / purpose |
|--------------|-------|---------|
| **Aurora Punks AB (internal)** | `0ACOk67Zhg9zlUk9PVA` | **SURVIVING merged AP-internal drive** (Phase 4: AP Admin content merged in). Holds `Board_Governance/` `1cQxevJt22Kj4T8DDFyDQprzuMOk8hc7_`, consolidated `Templates/Contracts` `19Sg5FabNRw3VR47vKVpwysuaRiGEf6at`, Publishing (deduped), Presentations (deduped), + `Aurora Punks AB`/`IPs` folded to root pending sort. Membership: Robert (Manager) + Amer Alsalek (by-need). Board = item-share to `Board_Governance/` only. |
| **Aurora Punks Admin** | `0AM6InBfd-HOMUk9PVA` | **NOT retired.** Retains the freeze set (AP Konkurs, APDS estate folder, deletedUsersData, ARCHIVE) + Portfolio Companies husk (WLBS estate + RUNATYR-as-holding + 4 loose corp files) + emptied Publishing shell. Do not delete. |
| **Aurora Punks External** | `0AC1lH0hoMwSnUk9PVA` | Outward-facing item-shares (investor data room, partner/pitch folders). Membership: Robert only. `EXT Portfolio Companies` `12-r2AFJMwwl5qEno9ybBD5rYhk4lrbOs` confirmed EMPTY. |
| **CZP Holding AB** | `0AAaQFbRZFdpKUk9PVA` | Templated + financials/legal folded in (Phase 3). Membership: Robert (Manager) + Sifferrådet/Henrik Franzén (by-need). |
| **Runatyr AB** | `0AJbB97KnFqgnUk9PVA` | Templated + financials/legal folded in (Phase 3). Membership: Robert (Manager) + Ameer Alsalek (by-need). **Yasin Hillborg = NO access at all** (decided Robert 2026-07-08 - not a member, no item-share; RLR IP dispute). |
| **Zenland Games AB** | `0AG5ggAZpSdKLUk9PVA` | NEW 2026-07-14 (Phase 2), populated Phase 3. Membership: Robert + CorpBot/VPS in-house bookkeeping (no external accountant). FY ends 30 Jun. |
| **Aurora Punks Dev Services AB (APDS unit)** | `0AIxVfcR4Xlm-Uk9PVA` | NEW 2026-07-14 (Phase 2). **EMPTY SHELL** - APDS is its own company unit, but its estate/konkurs CONTENT is FROZEN (Financial SD + AP Admin), NOT moved in. Membership: Robert only. |
| **Portfolio** | `0AF1ubBnsLIXNUk9PVA` | NEW 2026-07-14 (Phase 2), populated Phase 5. 7 holdings at drive root (one folder per holding). Per-holding contacts = item-share only, no membership. |
| **Projects** | `0AESiGYhJVmCQUk9PVA` | **FLAT - 101 top-level project folders** (Phase 6 flattened the 3 legacy buckets to root). Clients/co-dev = item-share to their single project folder only, never membership. |
| **Financial** | `0AMBeS-GYxphsUk9PVA` | **LEGACY SOURCE - largely emptied of company financials** (Phase 3 moved them into each company drive's `_financials/`). Emptied source subfolders left in place (not deleted). No longer the books home. |
| **legals** | `0AI_AdW5gwShNUk9PVA` | **EMPTY** (0 items, confirmed in manifest). Templates consolidated to AP internal `Templates/Contracts`. Effectively dead. |

---

## czp_infra (db-309, 2026-08-22)

**`czp_infra` `1oeDSAPI7Z-TV5bCpJMxQzUTW8FyQuiMY`** in the CZP Holding drive (`0AAaQFbRZFdpKUk9PVA`),
following the existing `czp_<domain>/` convention alongside `czp_assets` and `czp_pitches`. Home for
infrastructure and fleet docs. First occupant: **"Agentiskt nätverk: allt som ska göras"**
`1OLLuT7imYPd319pkBaeTDj_xJyTQRKltGKoz_qyJD_Y`, the task tracker standing in for Death Board while
db-319 clears the board. Infra bills CZP, see [[reference_infra_billing_entity]].

---

## Kvitto-intake (db-279, 2026-07-21)

**`Kvitton_Inbox` `1xPRfNjgz9wQHEkdxWzpOwlREn4LJFYbJ`** — Robert's My Drive, phone-upload staging for receipts (NOT a company record; files leave it within the hour). Subfolders: `PLEO` `1JakJgFCdxCfqjO9jIJHpJ4oKv4qMUgwE` · `CZP` `1FbMoZC_9yKhxqjUA53XjGLtlufWOJm7R` · `RUNATYR` `1nS6xmljFCL6QuuTHtLQ5k-tgBHntPDc3` · `AP` `12LL23-g-0UkK2PEK3LDpE7q2_rAw7VRc` · `ZENLAND` `19bNKPUGDxiTxOkBvWIc9bkOE6ZjLOqPO` · `_needs_review` `1_VVgEJpjww7SrO3pSbBzqvRiXVHJdTTP` · `_processed` `1Y3P7Md4sPEP84pose4pZTCzS3-wwvB7g`.

**Receipt destinations** (used by `receipt-router.js`; note they are NOT uniform — AP has no `_financials` template): CZP `Bokföring/2026` `1AV4I0HnGE6E5CFhiySyfrRWw_R3Mi7-M` → `Utgifter/<YYYY-MM>` · Runatyr `Utgifter` `1U4O77QIy0eX2wmxc3Uww6yH34ag3t-1w` → `<YYYY-Qn>` · AP `Aurora Punks AB/Finance` `141qYiFwCNA71rGMHEsDiMjNVJ_q_04Cp` → `Bokföringsunderlag/<YYYY>/Utgifter/<YYYY-Qn>` · Zenland `Bokföring` `19ZQ5tdmnslK7a02KPfDDm5_3dwX7i6rl` → `FY<YYYY-YY>/Utgifter`.

**Legacy, do not write to:** `CZP_Expenses` `1JMuQs8E_fxtqYNmwmWlm7DP7HW832NGs` (inside CZP Bokföring/2026) — superseded by the intake pipeline, left read-only.

---

## DEAD / CONSOLIDATED (do not send new content here)

- **Company financials** are no longer in the **Financial SD** - each company's bank statements / bokföring / bokslut / skatt moved into that company's own drive `_financials/` (with the Swedish accounting subfolders `Bokföring` / `Bokslut_Årsredovisning` / `Skatt_Moms` / `Bank_Statements`). Financial-SD company folders now hold only emptied template shells.
- **`czp_finance`** (empty legacy shell) → folded into CZP `_financials/`.
- **`czp_legal`** (contract templates) → moved to CZP `_legals/` in Phase 3, then its `MNDA`/`Subcontracts` template subfolders consolidated to AP internal `Templates/Contracts` in Phase 6. `czp_legal`/`templates` husks emptied, left in place.
- **`czp_projects`** → trashed pre-migration (confirmed).
- **Runatyr legacy `Finance` + `Bank` folders** → folded into Runatyr `_financials/` (nested) / `_financials/Bank_Statements/`.
- **`Runatyr_Bokföring`** (old accounting folder) → its Financial-SD Runatyr content moved into Runatyr `_financials/`; the legacy `Finance/Runatyr_Bokföring` subtree travelled in nested.
- **AP `_deliverables_working` / `_financials`** (old Financial-SD homes) → emptied of financial docs into AP structures.
- **Templates: ONE home now** = AP internal `Templates/Contracts` `19Sg5FabNRw3VR47vKVpwysuaRiGEf6at`. Holds `MNDA/` `1JTqk3NoFHXc27C9oFCu5iVSkWh3mlQkO` + `Subcontracts/` `1G0JoYgHL3eRFMlpi5sI-c5El1cy-YxRe` (folded from CZP, IDs preserved so `reference_contract_templates.md` refs still resolve) + the 2 pre-existing ContractorAgreement master docs. The `legals` SD is NOT the templates home (it's empty).

---

## Per-company drive template (standard, decision 2)

Every company drive (AP internal, CZP, Runatyr, Zenland, APDS unit) uses:
`_legals/` (+`_working/`, `_archive/`) · `_financials/` (+`Bokföring`, `Bokslut_Årsredovisning`, `Skatt_Moms`, `Bank_Statements`) · `Deliverables/` · `Board_Governance/` · `Meeting_Notes/` · `_archive/`.

**Filing convention (Robert, 2026-07-14):** signed/executed files → `_legals/` **ROOT**; unsigned drafts/working docs → `_legals/_working/`; superseded material → `_archive/`.

### Key per-company folder IDs

**CZP Holding AB `0AAaQFbRZFdpKUk9PVA`** (Phase 3 template):
`_legals` `1gOABnFr3v_MQVwqFHcEfxXO4UgPWRq6a` (`_working` `1QqP291eZngSdQhfFunCuBziue3Ywc3B4`, `_archive` `1HUygJ9a2GwDqGCt_l8XHl_KMB829H16Y`) · `_financials` `1STnZGp1-q_VUc37k3O86iyXkS10beTul` (`Bokföring` `1nHZ7B5wE-u9UUIhzCIw3qn0TflTHB6pR`, `Bokslut_Årsredovisning` `11vVlZpt347o-UPAhbyWkyJol5bZsBASV`, `Skatt_Moms` `1nBnMY7Egz3oAbve2NJHE8YDzlYf2b8t8`, `Bank_Statements` `1ogAe7nErTBqGDbA9LHsU8PHdkJBQ2qEA`) · `Deliverables` `1FPK9pivVD5MKGGh6SU0teGSHSBEhmr_k` · `Board_Governance` `16CqTZa5jwlwNfCSzeZ0oep0FzoDL2tbH` · `Meeting_Notes` `1OHondiCeA5gpJr1qQxduDxQOBd9nEsXy` · `_archive` `10oLS9OVVWGd_R9zmwmOHS3Hv_mQpjS5X`. Left-in-place (not migrated): `czp_pitches`, `czp_assets`.

**Runatyr AB `0AJbB97KnFqgnUk9PVA`** (Phase 3 template):
`_legals` `1VSJ3qZVRt627b5U_ow7VSeexQr0LzPYx` (`_working` `1xyFvwOjYICtkcwfUdU-9invKnAsK8ljX`, `_archive` `1JN951j9QplkoZSMUDJ90cP57dWBd5Odt`) · `_financials` `1Tqnzj_xhtTFtHdV4KdzEEDQWqS7CLDNZ` (`Bokföring` `1p_lAQgY-cPM60nLhPIDb1vJgT6RulfBt`, `Bokslut_Årsredovisning` `1kW8b-e5mVEFUgUPl31YjQv7nn78AMMdu`, `Skatt_Moms` `1TOi0C2YQFjmvo-DLT98aEEyicbxFvsaV`, `Bank_Statements` `1aLW-EtHTduyL_E8BmGW0yYSwpVVJemrF`) · `Deliverables` `111ZzBp4LzSi5OquJ3x-ktbJlnar9S32w` · `Board_Governance` `1i0x_6PxI3zg6XzY1il3-3QPGMNDjX_et` · `Meeting_Notes` `1AmiEfkVWgO7Vm-9JbdYz07LsNFBFvghV` · `_archive` `1OkVXmyVKKW7k2pi3v7ugv_jEr3HXX8vQ`. Left-in-place + flagged: `Partners`, `Frida&TGN`, `CompanyInfo` (holds Årsredovisning 2019 + Registreringsbevis - corp/financial), `Docs` (executed NDAs + MNDA templates), presentation/proposal files.

**Zenland Games AB `0AG5ggAZpSdKLUk9PVA`** (Phase 3 targets):
`_financials/Bokslut_Årsredovisning` `11q8Ba1_QSuzhLsypHbdqJqdKzacvt4MW` · `_legals` root `1ZS1oV6Qz2l2jSgy2bUOTMcARmNxyfvdC` · `_financials/Bokföring` `19ZQ5tdmnslK7a02KPfDDm5_3dwX7i6rl` · `Deliverables` `1EshSvDunqu_AKyvLNZr3tZlvDtJcpJVR`.

**Aurora Punks AB internal `0ACOk67Zhg9zlUk9PVA`:**
`Board_Governance` `1cQxevJt22Kj4T8DDFyDQprzuMOk8hc7_` (holds Data Room `1B9eRQ8_9ZiscyvfMRmghM4mFXBV-lvuO` + Meeting notes `1Y5_A4DWuCleX0phcOJ6Dzr9oHPzneWzk`) · `Templates` `1vBe0J9csDHHbo_NEl7-UZUIuYy5XzLq_` → `Templates/Contracts` `19Sg5FabNRw3VR47vKVpwysuaRiGEf6at` · `Publishing` `1i_lPuA...` (deduped, 10 game folders) · `Presentations` survivor `1PICvI9...` · `Aurora Punks AB` `1vNtiAZ8x9BS8ia6MAjnZ4-jjm3PPf_0Z` (801 desc, folded to root, **pending sort into Board_Governance/_legals**) · `IPs` `1CfviWqWxdicDQglAFWRFdJpe1XmZWm5U` (folded to root, pending sort).

**Financial SD `0AMBeS-GYxphsUk9PVA` (legacy source, company folders now emptied of financials):** AP AB `15sO9GO6k9HMW4LDtss0vzDSHpfrNuQGq` · APDS `1XIIwBw2F9bcC5K_7x9XUDJ_aLshWRpU0` (**estate content FROZEN**) · CZP `1-E2baOPmhZw0iZ-rOoQPVNE-7rh3WQMg` · Runatyr `1wCCrmOjkScHeTMSBA1j5-CSsJB8x-7W4` · Zenland `1Xca1vvpRCHBk39OzMJomGQADy-zTfJsP`. AP AB `_legals` (Phase 1) `1K6g0CydsFfdJ-jCBE4HoHaxy5nkpQVwP` (holds the signed CZP/AP lånerevers; working Doc in `_legals/_working/` `1oe4l3OMZj6_0HqfFHDnKOCQ6W8L0ShO6`).

---

## Portfolio drive `0AF1ubBnsLIXNUk9PVA` (Phase 5, one folder per holding at root)

| Holding | Folder ID |
|---|---|
| EDDAHEIM Aps | `12SM2XSbQdfMahh5SlK5prK-6FoYqVJgF` |
| LOOTLOCKERInc | `10qA2xzqWKaiEatcBLqtMjR_hrzs160HV` |
| Nr89 | `14Al5gzAqKCKcDvb-HeKwpG8fvGGEoA0d` |
| Pixie Pie AB | `1HCh_u3VKzL0BOq0ci6rIw_wtvomfP0VO` |
| RED MARMOSET INC | `12QjYmmzrGurR1Gr9s2ucoj30IcVU2sVM` |
| WINDSWEPT AB | `1F-eNOUTnO-tMycBAJ76pRvLONzRmdVa-` (main external-share surface: WSA accountants + Behold/Rocketride investor cluster - all preserved) |
| UpstreamArcade (shortcut) | `1T29YLmi6usttAA6XdNYSLyK03yRvLuQG` |

Per-holding contacts get item-shares only. All top-level holding folders carry only the Robert-organizer baseline.

---

## Projects drive `0AESiGYhJVmCQUk9PVA` - FLAT (101 top-level folders)

Phase 6 flattened the 3 legacy buckets to root (root went 17 → 101). Clients/co-dev partners get an item-share to their single project folder, never drive membership.

**3 legacy buckets = emptied-but-NOT-retired** (no-delete rule leaves emptied husks + 1 shortcut in place; none could be deleted because each still holds a husk/shortcut):
- `AP Projects` `14fo-WpEla5905XB36OlEjLxQdpzk6hni` - 1 remaining (SirWhoopass emptied husk).
- `AP External Projects` `1b97qY0EKPmJDkQ9sQAt4fyGpMCs08zXe` - 3 remaining (Elric husk, Vessels-of-Decay emptied husk, WS-RLR shortcut).
- `Runatyr Projects` `1CJQKr7cMbbWA-pJsRfWG3HANKaOUcYiZ` - 1 remaining (Elric husk).

**Merged collisions (Phase 6 close-out; survivor promoted to root, non-survivor children moved in, husk left in place):**
- **Elric** survivor `14WWsKcP-EVWC8fPvzmEczwid-wy_mKPN` (merged AP-Ext `1wQZk-7qJnQ-gnXRg2MWY9-iVM2ou7zY3` + Runatyr `1I3pgh5x6bBSCjcnut3pm7MRuGeHW0JbF`).
- **Vessels of Decay** survivor `1SE3OJtg9nLITweNXsnVL2nddPxGAgDY7` (merged AP-Ext `1CRKxsSH8lO3T5gl_Tlnhc5jTJaqv-jIw`, case-only difference).
- **SirWhoopass** survivor `1s0bwjv-T8ojaeao9OS1wq53Nj7Vpft8z` (merged same-bucket dup `1o624R3-pjjQdn60XnRgpH8EsTKjPLrYc`).
- **WS - Robot Lord Rising** survivor FOLDER `1xyk09oty90ubhN8GVTfZAnIUFPuSL579`; AP-Ext `1sGgkpRv8PkCYwUYay5xQDaFO_OvnRyE4` is a **shortcut** to it (never merged, resolves via the surviving ID).

**Revisionsmappen AP ÅR 2025 (verifierad 2026-08-25):** `Aurora Punks Board/_deliverables_working` `1TmSqmdwPY115LXwlFHNDyCniQkEzxGCh` (Projects-drive) är den "drive" Robert delat för AP:s bokslut/revision 2025. Behörigheter: Robert organizer, **Amer = `amersalek@gmail.com`** (writer, INTE `amer@book-it.se`), Mattias Wiking writer, **Christine Lef (Parameter Revision) reader**. Innehåll: aktiebok, AP_1350_Aktieinnehav 2020-2025, Almi ackord + betalplan, revers DekoDu, VoD-nedskrivningsunderlag, registreringsbevis, IP/licenslista, undermapp `Protokoll`. Länken har aldrig mailats till Parameter, så räkna inte med att revisorn hittat mappen bara för att behörigheten finns.

**Board folder to route (by-need):** `Aurora Punks Board` `15JWcx2V4lcOd9fz9RloDiUwVfijeGLSH` sits at Projects root but may belong in AP internal `Board_Governance/`.

### Mapped project folders (IDs unchanged through the flatten)
- RankOne `1TdWJlHpSzEKcvx33wzXoG4vjjXhKdZHS` (`_legals` `1jVdShvyU_-Bm1ld8z6BI3iBFX_JXqPn9`, `_financials` `1m5hxql-m3Uy9krET-TM7voPo1A0jYBcn`, `_deliverables` `1l0JEnT6UKeIul2BvgA_wRojkASK5rme-`; guidance one-pager GDoc `1yeKgQRxgEyjcTzRjcvxo1gOPNO7XDXMY0rvnHcSjMc0`)
- BADASS `1hi4bKAWk-2M7lO6y7mlrlq5gca-NLzlj` (`_financials/_working` `1THZlzemWaFB1z2miOBhRQKmXSYvaJec0`, `_deliverables/_working` `1m5VCgeGBF0UVZb2QmpqRdLlbJDR0MGDH`, `_legals/_working` `19bAStrVOUDGF6m8d061rpGklJdIO7Ybq`)
- k2c_rf_ap `1l06e7S7finV0wneJbWBtOgMGTGA_R3Iu` (`_financials/_working` `1vA--z3zTyumwbYGpc95c_uwPzuiHNP-B`); k2c_rf_ap_project `17TiyvGLO4pXcxAIJ7Q5W1GBstlGn6y6D`; k2c_af_ap_workingdoc `1nc5U5wmGGRUPkJZx7UWfLeW0vK77VMlR`
- Elias `1bof4Q2uiG9FZXvzxO0tGl5R-llnCRzOs` (`_deliverables/_working` `1On4t3i4gKvefmgIaQHd1rR4NWZ4cqDBG`, `_legals/_working` `1gz0Q39xZtFBywwyYknyhkvhYk6soSL0c`, `_financials/_working` `1MFljoIE6MYhPwiJOUmxLLrk_y7mUvShP`)
- Blue Scarab `11hn9SdvY5bwQiqiFFAlBNJLZrqLBAgS5`
- 5 Fortress - Striden `18n4mxi_p1wKfMbnQKVpZJo3efYVIAEdN` (`_deliverables/_working` `1LrRnRH5mIZ5FSOE29rnFYdw4EiEkjnRo`, `_legals/_working` `1RAVeIBvHQEoC3z-xcox6L8R5AHSHGY9k`)
- Water Me & You: `WMY` `1avS2Lvhn4N_iWGNfOOL5SCqjKLJq2VsY` + `Water, Me and You` `1p0xtESY4IPALEe-k4JunrwjBnCUyiKpf` (**triple with My Drive `water_me_and_you` - reconcile**)
- Sir Whoopass: `Sir Whoopass` `1-aYoAzc1T2V1XjXhBJ7_Gw_2dJh-N_xe` (survivor) + SirWhoopass husk (see collisions) + My Drive mirror nodes (**reconcile**)

---

## My Drive / mirror (left alone)

- **Drive-for-Desktop mirror** = `My Computer/projects`, a backup mirror of the VPS masterbrain `/home/assistant/projects/` (contains CLAUDE.md, .git, node_modules, assistant/, skills/, vault/, .secrets). NOT touched - the VPS is the source of truth; do not pull nodes out of a sync mirror. `My Computer/projects/water_me_and_you` `1c0RhkJGLiPMiHCKZkr-Bk17KvnjxDBxx`, `My Computer/projects/sir_whoopass` `1_2qeAz274Q0yZ852kyWfw_57zM1AKpep`, `My Computer/projects/art/sir_whoopass` `1hj5W4vUs5g4tE3emVIDCqPBXR7EZuTkx`.
- **`Aurora Punks - Boardmeeting Notes`** `1f3_iGRpWvSDPcXhsaTMmpiINYBfqYLzD` - **owned by `mattias@mattiaswiking.com`**, so Robert can't transfer it into `Board_Governance/`. Needs Mattias to transfer if wanted.
- **There is no `umbrella` folder in Drive** - `umbrella/` is Robert's VS Code workspace-root prefix (a local path convention), not a Drive folder.

---

## FROZEN - insolvency/estate (Phase 7; DO NOT move/rename/re-share/delete)

Migrates only in a future run under written trustee/Lawyer direction. Full register in the migration plan's Phase 7 EXECUTION STATUS block.

| Object | ID | Location | Consent required |
|---|---|---|---|
| APDS estate/konkurs content | Financial-SD APDS `1XIIwBw2F9bcC5K_7x9XUDJ_aLshWRpU0` + AP Admin `Aurora Punks Development Services AB` `12IgZJteVOE2wQyDOs85FsvO-QiUf7_sA` | Financial SD + AP Admin | **Nils Åberg / Carler**, mål K 4429-25, Umeå TR (live bevakning - do not disturb) |
| WLBS AB estate | `12QkWSrN80DouEtv1v3sQmrVlVD9d119Q` | AP Admin `Portfolio Companies` `1ZZGaoL7bsNkrKqbiv-mGQT-dsbZ6gtqv` | **Petter Vaeren / 7wise**, mål K 16834-24, Sthlm TR |
| AP Konkurs | `143MZGE8RN1HvMMKtgDb7hG7vDYcSfBei` | AP Admin | Robert triage (may migrate after) |
| Trustee AP Hardware | `144m7Yb7uba9wfUz1q1zpuFuM9IAA-J-J` | AP internal | Nils Åberg / Petter Vaeren per content |
| ARCHIVE | `14T43BsiIPHw9-i5XB6rn6bTZXQdZgovO` | AP Admin | Robert/Lawyer triage |
| deletedUsersData | `1ia5xuh7c9woZ0drdBJJcRhDaYEdN4wOZ` | AP Admin | GDPR deletion review (NOT migration) |
| NEW STRUCTURE - DO NOT TOUCH PLZ | `1Oc_DsrGrzOnUysyk07LbyZe2ubqNQLWB` | AP internal | Robert (do-not-touch marker) |

---

## OPEN by-needs carry-forward (Robert's; NOT migration blockers)

1. `all@aurorapunks.com` still item-level writer on ~81 Projects items + WS-RLR → fold into new access rules.
2. Mattias-owned My Drive board-notes folder → needs Mattias to transfer if wanted in `Board_Governance/`.
3. Loose AP-corporate files in AP Admin `Portfolio Companies` (bolagsordning ×2, Limit_Break nybildning, Aktieinnehav) → route to `Board_Governance/`.
4. Duplicate pairs to reconcile: RUNATYR-AB-as-holding (`1KQFe88xsQ_PGjVWF6CmpH8_d2AHwSuFi`), Water Me & You triple, Sir Whoopass family.
5. `Aurora Punks Board` `15JWcx2V4lcOd9fz9RloDiUwVfijeGLSH` at Projects root → maybe `Board_Governance/`.
6. AP AB intact folder `1vNtiAZ8...` + IPs `1CfviWq...` at AP internal root → sort into Board_Governance/_legals.
7. Drive-for-Desktop mirror → leave (recommended) or retire; Robert's call.

---

## Maintenance Protocol

**When creating a new shared folder:** add entry here with folder ID + sharing info; append to the relevant project memory; append to admin_learnings if it's an accounting/legal handover folder.

**When uploading to a folder:** if the folder ID is unknown, search Drive, update this registry, THEN upload. Never guess - always verify the ID is current. Company financials go to that company's drive `_financials/`; project files stay in the project folder in the Projects drive; contract templates come from AP internal `Templates/Contracts`.

**Format:**
```
- **Folder Name** (shared: person1, person2): `folder-id`
  - Purpose: what goes here
```
