# BADASS Studios — Activity Log

## 2026-06-02 - PM Agent (CUST workflow statuses + default assignee — Sezar via Teams)

Sezar (Teams) couldn't move CUST-798 "Lap Confusion" (Story under Epic CUST-114 "Gaming Dubrovnik") to "In Preview" — diagnosed: that status simply didn't exist in the CUST workflow (only To Do/In Progress/Done). He then asked for **In Review, Blocked, Under Testing**, and flagged new tasks defaulting their assignee to Robert.

- **Workflow statuses (added):** one workflow covers all CUST issue types ("Software Simplified Workflow for Project CUST", entityId e3d04919-63af-46a7-8fc6-a8adfb237601, GLOBAL scope, isEditable). Reused existing GLOBAL statuses **In Review (10035)** + **Blocked (10361)**; created **Under Testing (10576)**. Added all 3 as GLOBAL transitions (ids 41/51/61, clear-resolution action like To Do/In Progress). Used new workflows API: validated via `/workflows/update/validation` (0 errors) then `/workflows/update` (200). Verified 6 statuses now live.
  - **API gotcha:** in the new workflow update payload, `statusReference` must be a generated **UUID**, not the numeric status id; the real id goes in the `id` field of each WorkflowStatusUpdate. Sending numeric refs → STATUS_REFERENCE_NOT_UUID + spurious NON_UNIQUE_STATUS_NAME + STATUS_MAPPING errors. Remap all toStatusReference to the UUIDs; `statusMappings: []` is fine when only adding statuses.
- **Default assignee (fixed):** project default was PROJECT_LEAD (=Robert) AND all 15 components also PROJECT_LEAD — components win when an issue has one, so everything landed on Robert. Flipped project + all 15 components to **UNASSIGNED** (`PUT /project/CUST` + `PUT /component/{id}` ×15, all 200, verified). Robert chose Unassigned over creator-auto-assign.
- Reply drafted for Sezar.

## 2026-05-29 - PM Agent (Portfolio Board — Nancy's 3 view requests)

Nancy (Teams, Tue) asked whether the Portfolio Board can do three high-level views: (1) client-relationship duration timeline, (2) dependency/blocking view, (3) workload-per-person across clients/locations.

- **Premise check (key finding):** Plan 34 "Portfolio Board" is **live** — `GET /rest/jpo/1.0/plans/34` returns 200; Jira Software is on a **Premium** tier (Plans/Advanced Roadmaps active). This **contradicts and supersedes** the 2026-05-20 Teams draft to Nancy that said we'd need to upgrade to Premium / offered a trial. Do **not** send that message. Plan 34 pulls from 11 sources incl. CUST (10672). Baseline fields: start=customfield_10015, end=dueDate.
- **Live CUST data state (763 issues):** 636 assigned / 127 unassigned; 230 due-dated; 192 start-dated; only **132 with hours estimate**; only **1 "blocks" link** across all 47 epics. Versions (E1 2025 S2, E1 2026 S3) carry **no dates**.
- **Per-view verdict:**
  - View 3 (workload) — buildable now, meaningful (group by Assignee, colour by Client). Count-of-items, not hours (estimates too sparse for capacity).
  - View 2 (dependencies) — view = 1 toggle, but ~no data (1 link). Decision: turn on + ask leads to log blockers from E1 Miami forward.
  - View 1 (duration) — no data source. ExtremeH/PFL aren't CUST clients; only E1 has dated work (2025-09-30→2026-06-13). Decision (Robert): use the 5 real clients only, date one parent each; ExtremeH/PFL/Demos deferred.
- **Built (View 1 data layer):** created 5 `client-engagement`-labelled Epics — **CUST-793** E1 Series (dated 2025-09-30→2028-12-31), **CUST-794** Show Jumping, **CUST-795** F1 VR, **CUST-796** Blackbook, **CUST-797** BMS (latter 4 undated, Nancy fills Start+Due). Created via Rovo MCP after explicit Robert approval (client-Jira write gate).
- **Remaining = UI click-work (Nancy owns board hygiene):** save the 3 Plans views + flip dependency setting to Lines. Plans saved-views/dependency toggle are **not** REST-exposed (`/views`, `/hierarchy` endpoints 404). Steps in `badass/drafts/portfolio_board_views_buildguide_2026-05-29.md`.
- **Deliverables:** reply draft `badass/drafts/nancy_portfolio_views_2026-05-29.md`; the views how-to was folded into the **already-shared** "CUST - Admin User Guide" GDoc as **section 7**, updated **in place** (same fileId `1sgy8...`, same link) via new helper `assistant/gdrive-update-doc.js`. No new client file (Robert: never share .md with clients; update shared docs in place — see [[feedback_no_md_to_clients]]). Local source guide `badass/drafts/portfolio_board_views_buildguide_2026-05-29.md` kept as internal working copy only.

## 2026-05-22 - PM Agent (CUST migration EXECUTED)

- **Migration run by Robert** in the Jira bulk-move wizard, three runs: F1 (19 issues), BMS (19), E12026 (627 incl. done history). 4m 5s for the big one. Live total in CUST: **731** issues.
- **Post-move API pass (PM):**
  - Stage A - stamped 37 of 38 §4 epics + their descendants with Components (E1 Series + Type), Location, Fix Version. **536 issues updated.** Failure: E12026-312 (404, deleted at some point before the wizard).
  - Stage B - F1 (19) tagged with F1 VR component, BMS (19) tagged with BMS component.
  - Stage C - 91 orphan E12026 movers (no §4 epic ancestor) tagged with E1 Series component. Zero CUST issues now without a component.
  - Stage D - label-to-Location normalisation: `como`, `dubrovnik` (typo), `Dubrovnik` labels resolved to Location field on 13 issues. `Formatexplainer` label dropped from 2 issues. **495 issues now have Location set** (66% of moved).
  - Stage F - 5 source projects archived: PFL, OR, E12026, F1, BMS. Old-key redirects verified working.
- **Plan 34 - manual UI step needed.** Plans API `POST /rest/api/3/plans/plan/{id}/issue-source` returned 404 (endpoint shape differs from the docs). Add CUST (project id 10672) as an issue source via Plans UI: Portfolio Board → Settings → Issue sources → Add → Project CUST.
- **SJ leftover - decision pending.** SJ-67 ("3D AR Assets", Epic, To Do) appeared in SJ post-wizard (reopened or newly created). SJ not archived. Two options: (a) tiny bulk-move wizard run to bring SJ-67 + any other SJ open into CUST, then archive; (b) archive SJ with the live ticket frozen.
- **132 E1 Series items still without Location.** No location label to derive from. Acceptable post-migration state - appears on the E1 Series board, just not on per-location views until content owners refine.
- **94 orphans (no Epic parent, non-Template).** All tagged with a Client component, but no Epic parent. Most are standalone Tasks/Bugs/Sub-tasks ("Improve Boat Turning Behavior", "Project Cleanup"). Either accept as standalone, or content owners attach them to a relevant Epic in a follow-up sweep.
- **Old keys redirect** - E12026-542 → CUST-129, E12026-657 → CUST-144, etc. Nothing the team has bookmarked breaks.

## 2026-05-21 - PM Agent (CUST migration sign-off + Nancy Q&A)

- **Trigger:** session resumed on the CUST migration dry-run, waiting on Robert's 4 sign-off answers.
- **4 decisions locked:** (1) full migration - 663 issues (625 E12026 incl. done history + 38 open SJ/F1/BMS); (2) Robert drives the bulk-move wizard; (3) timing Fri 22 May - brought forward from the weekend by Robert + Nancy on 2026-05-21 to free the weekend for fixes, heads-up posts Thu 21; (4) the 3 untyped Done coordination epics (E12026-1/-4/-416) stay Component E1 Series only, team heads-up approved as drafted.
- **Live state verified via badass API:** E12026 = 625 (354 done / 271 open / 314 sub-tasks); SJ 1 / F1 18 / BMS 19 open = 663 total. CUST currently 71 issues. CUST-63..67 confirmed as pilot test data.
- **Status map resolved from live counts:** E12026 issues sit in To Do (230) / In Progress (37) / In Review (2) / Testing (2) / Done (354). Blocked + Blocked by empty. Map: In Review + Testing → In Progress, rest pass through. **Blocked status NOT added to CUST** (Robert agreed) - nothing to migrate into it; CUST runs Jira's Simplified Workflow (statuses are board-column-driven, UI-only) so an add would be a board edit anyway.
- **Jira change executed:** Per Location board filter (11055) broadened from `Location = Dubrovnik` to `project = CUST AND component != TEMPLATES` - the board was a Dubrovnik-only pilot. Swimlanes-per-location deferred to the post-migration board pass (board-settings UI step).
- **Automation rule (self-serve template spawn):** Robert's call - Nancy owns it. She builds it from `cust_automation_rule_spec.md` (UI-only, ~15 min), PM on a call if useful. No migration dependency. Ownership ask added to the Nancy Q&A Teams draft.
- **Nancy's 7 CUST questions answered** - draft Teams reply at `badass/drafts/nancy_cust_qa_2026-05-21.md` (Robert sends). Q5 (client variation) bounced back to her to specify task-list vs status-workflow variation.
- **Dry-run plan updated to APPROVED** with locked decisions + a migration run sheet: `badass/drafts/cust_migration_dryrun.md`.
- **CUST - Admin User Guide created.** Drafted `badass/drafts/cust_admin_user_guide.md` (condensed manual: CUST structure, boards, spinning up a location, adding Location/Client values, filters vs boards, automation-rule build) and uploaded to BADASS Drive / Deliverables as Google Doc **CUST - Admin User Guide** (id 1sgy8vFEgKghS5vTA-skSlPG8DhFDR-_eVglgvpcuKPA). Supersedes the earlier single-topic `CUST - Automation Rule Build Guide` (1Yk_DJ8dsmudo1X6Z4_Y0MyL-u4N8a2ZyC41Ck2Oyz0E), now a redundant duplicate in the same folder - pending trash on Robert's OK.
- **CUST-63..67 pilot test data deleted** (5 × HTTP 204, 2026-05-21).
- **Open:** Robert + Nancy post the team heads-up today; migration Fri 22 May. Trash the superseded `CUST - Automation Rule Build Guide` doc pending Robert's OK. Per-location swimlanes + Plan 34 wiring are post-migration.

## 2026-05-20 — PM Agent (CUST scaffold executed — Phase 1 step b complete)

- **Trigger:** Nancy granted Robert global "Administer Jira" on badass-studios.atlassian.net (confirmed `ADMINISTER: true`). Unblocked the scaffold.
- **Project created:** CUST "BADASS Customisation" — id 10672, company-managed Software (Scrum template), lead Robert. Reverted to company-managed (not the team-managed permissions-workaround) since it matches E12026's shape and makes the later bulk Move migration cleaner.
- **14 Components:** Client — E1 Series, Show Jumping, F1 VR, Blackbook, BMS. Type — AR Live Broadcast, VR Live Broadcast, AR App, Environment Production, Course Explainers, UEFN, Steam-Console, Format Explainer. Plus TEMPLATES (hidden bucket). All lead=Robert, assigneeType=PROJECT_LEAD.
- **2 Fix Versions:** E1 2025 S2 (Jeddah legacy), E1 2026 S3 (current).
- **3 custom fields** (global context, single-select, added to both CUST screens 10726/10727, confirmed on Story create screen):
  - `Location` (customfield_10231): Dubrovnik, Como, Monaco, Lagos, Miami, Bahamas, Jeddah, TBC
  - `T-shirt Size` (customfield_10232): XS, S, M, L, XL
  - `Template Source` (customfield_10233): AR Live Broadcast, VR Live Broadcast, AR App, Environment Production, Course Explainers, UEFN, Steam-Console, Format Explainer
- **3 boards + filters:**
  - CUST - All (board 954, filter 11053, Scrum) — all work excl. TEMPLATES
  - CUST - Per Client (board 955, filter 11054, Kanban)
  - CUST - Per Location (Dubrovnik pilot) (board 956, filter 11055, Kanban)
- **Cleanup note:** Scrum template auto-created a default "CUST board" (id 953). Redundant with "CUST - All" — flag for deletion (left in place; deletion is destructive, confirm with Robert).
- **db-161** (2nd local Atlassian MCP for BADASS) marked pending_close — token now proven end-to-end via curl; durable wrapper still worth wiring.

### Step (c) — template Epics seeded (same session, 2026-05-20)

- **8 template Epics created** under the TEMPLATES + matching type component, with `Template Source` field set. Seed script: `badass/drafts/cust_seed_templates.py`. All children created as Story type (consistent, per proposal "canonical Stories"); `parent` field links Story→Epic fine in company-managed classic.
  - CUST-1 TEMPLATE: AR Live Broadcast — 20 Stories (CUST-2..21), ← E12026-542. Owner: Alex.
  - CUST-22 TEMPLATE: VR Live Broadcast — 17 Stories (CUST-23..39), ← E12026-657. Owner: John.
  - CUST-40 TEMPLATE: AR App — 6 Stories (CUST-41..46, incl. Vision Pro build), ← E12026-279/312. Owner: Ben.
  - CUST-47 TEMPLATE: Environment Production — 4 Stories (CUST-48..51), ← E12026-677. Owner: Marco.
  - CUST-52 TEMPLATE: Course Explainers — 4 Stories (CUST-53..56), ← E12026-396. Owner: Jake.
  - CUST-57 TEMPLATE: UEFN — 2 Stories (CUST-58..59), ← E12026-213. Owner: TBD.
  - CUST-60 TEMPLATE: Steam-Console — 1 Story (CUST-61, thin per proposal "seeded as patterns surface"), ← E12026-682. Owner: Sezar.
  - CUST-62 TEMPLATE: Format Explainer — 0 Stories (shell; source 185/186/421 are draft-iteration Epics, no clean checklist). Owner: TBD (Jake / Marketing).
- **Total: 62 CUST issues.** T-shirt Size left blank on all — content owners set sizes in their first sizing pass (per proposal's post-race retro model). Verified via approximate-count.
- **5th board added: "CUST - Templates" (board 957, filter 11056)** — `component = TEMPLATES`. Needed because "CUST - All" deliberately excludes TEMPLATES, so the template library wasn't visible anywhere. Content owners edit their template here.
- **Open / next:**
  1. UEFN + Format Explainer owners unassigned — needs Rosy/Alex to name them.
  2. Content owners do a first sizing pass (T-shirt Size) on their template.
  3. Step (d): wire the Jira Automation rule (new Location Epic with Template Source = X → clone that template's Stories), pilot on a throwaway Location Epic.
  4. Step (e): bulk-move E12026 (+ SJ/F1/BMS) into CUST. Irreversible — gated on (d) proving clean.

### Contract review + Exhibit B (2026-05-20)

- **Time breakdown reconstructed** — `badass/time_breakdown.md` (internal) + `badass/drafts/badass_time_summary_client.md` (client version). 17 itemised line items + standups; 40h fixed-price scope crossed mid-May-12; ~20.8h overage delivered at no charge. Published as a Google Sheet to `czp_projects/BADASS/Deliverables/` (id 1KZPG4PQ3RynbEXur_3cw5ekiXJ3dljS6BU68HSPPYKM), silent-shared with Rosy. **Nancy share failed** — `nancy@badass-studios.com` is not a Google account; Robert to resolve (her Google address, notify-share, or PDF). `projects/time_log.csv` created + seeded with 18 BADASS rows; time_tracking skill strengthened (all-agents logging, one-sentence notes).
- **Contract audit** — searched Drive "BADASS in title". Found: **Outsourcing Agreement** (signed 2025-10-17, Robert + Ben Douglas; effective 2025-09-25; Master Agreement, Swedish law, GBP, Net 10) and **NDA** (×3 copies). Key finding: the Master's only Exhibit A covers UEFN dev @ GBP 400/day — the PM engagement (40h @ GBP 65/hr) had **no signed Exhibit/SOW**.
- **Exhibit B drafted** — `badass/drafts/exhibit_b_pm_services.md`. PM Services Exhibit to the Master Agreement: retroactive from 2026-03-22; GBP 2,600 fixed for 40h to 2026-05-20 (+ ~20.8h goodwill, no charge); GBP 65/hr hourly from 2026-05-21, monthly invoicing. Signatory: Rosemary Lokhorst (CEO). Lawyer-agent draft; no separate review pass needed (scope/fee Exhibit, no new legal terms, checked vs Master for conflicts — clean).
- **Drive consolidation** — created `czp_projects/BADASS/Legal/` (id 1794paX-5Q5gv0heMR78_ePnzkou_h8Y9). Moved the **Outsourcing Agreement** there from the Partners Shared Drive (cross-Shared-Drive move — Partners-drive-only members lose access). Exhibit B GDoc created in the same folder (id 1I9nlmgE5XldF1mx-4xE2QFx4aCW-buVs1iQ7gj9yIVE).
- **Open:** NDA still loose in My Drive (3 copies) — not consolidated, flag for Robert.

### Contract rebuild — APDS bankrupt, new CZP Holding agreement (2026-05-20)

- **Robert flagged:** the upstream Outsourcing Agreement's contractor, **Aurora Punks Development Services AB (APDS, 559320-7466), is in konkurs** (estate handled by Advokatfirman Carler; konkursbouppteckning drafted Jan 2026). The PM work needs a contract with a live entity.
- **Decisions (Robert):** new standalone contract, Contractor = **Creation Zero Point Holding AB (559182-7471)**; PM-services only (UEFN dev work is finished + invoiced, stays with APDS); PM work is separate from the APDS contract so no continuation; BADASS already informed they'll re-paper with a separate entity. PM scope + fee in the main body, no Exhibit/amendment layering.
- **CZP Holding details** (from Feb 2026 registreringsbevis, ärende 67465/2026): postadress c/o NeCo Software, Brännkyrkogatan 10B, 118 20 Stockholm; säte Stockholm; sole styrelseledamot Robert Bäckström; firmateckning "firman tecknas av styrelsen".
- ⚠️ **Verksamhetsföremål mismatch:** CZP Holding's bolagsordning is holding-company-only (own/manage shares + kapitalförvaltning). PM consulting is outside its registered objects. Recommended fix: bolagsstämma broadening the articles + Bolagsverket filing (CorpBot), before signature.
- **Draft delivered:** `badass/drafts/czp_badass_pm_services_agreement.md` — full standalone Project Management Services Agreement, mirrors the Outsourcing Agreement structure, retroactive from 22 March 2026 (GBP 2,600 fixed for 40h to 20 May + ~20.8h goodwill; GBP 65/hr from 21 May), Swedish law, §12.1 explicit clean-break from any other party's agreement. Dropped UEFN/Epic + music-industry boilerplate from the old template.
- **Exhibit B superseded** — the earlier APDS-based Exhibit B GDoc in `czp_projects/BADASS/Legal/` is now dead; recommend deletion (pending Robert).
- **Finalised 2026-05-20:** Robert resolved the 3 open items — verksamhetsföremål mismatch accepted as-is (CZP has multi-year consulting revenue history; Robert's call, articles change not pursued); signatory = "Director"; registered office Brännkyrkogatan 10B confirmed. Clean GDoc created in `czp_projects/BADASS/Legal/` (id 1iW6nZ1e_f3ZkuEte3wCD_oMNNSEvE96fMglzWkDQalQ). Superseded Exhibit B GDoc moved to the BADASS Archive folder.
- **Open:** signing flow — proof-read round + Google Drive eSignature to Rosemary (CorpBot), pending Robert's go. Registered-office street spelling worth a final check against the registreringsbevis (OCR/typo variance: Brännkyrkogatan vs Brännkyrkagatan).

### CUST follow-ups from Nancy (2026-05-20)

- **Nancy granted CUST view access** — added as an explicit BROWSE_PROJECTS user grant on the CUST permission scheme (10132), grant id 14395. CUST's scheme had no general member/viewer role, so a per-user grant was the surgical fix.
- **XR Headset template added** — Nancy flagged Vision Pro / VR headset apps should be their own type. This reversed decision #5 (which had folded Vision Pro into AR App); Robert approved the split. Created: component "XR Headset" (10191), Template Source option "XR Headset", template Epic **CUST-68** + 4 stories (CUST-69 Spawning system, CUST-70 Manipulation system, CUST-71 UX tweaking, CUST-72 Distribute a version to Test Flight — deduped from Vision Pro V0.1.0 source epics E12026-324/335/342, owner Ben). Redundant CUST-46 ("Vision Pro app build") deleted from the AR App template; AR App component description corrected. Template count now **9**. `cust_spawn_location.py` COMP map updated.

### Step (d) — template engine built + piloted (same session, 2026-05-20)

- **Native Jira Automation rules can't be created via REST** (UI-only). So step (d) delivered as two interchangeable paths:
  1. **Script engine** — `badass/drafts/cust_spawn_location.py`. Clones a TEMPLATE Epic's Stories into a new Location Epic, stamping Client+Type components, Location, Fix Version. Works today; PM runs on request. Args: `--template --location --client --fixversion --epic-name --dry-run`.
  2. **Native rule spec** — `badass/drafts/cust_automation_rule_spec.md`. Click-by-click build guide for Nancy (trigger: Epic created + Template Source set → Lookup template Stories by JQL → branch-create each under the new Epic). The no-touch version.
- **Template Stories tagged with `Template Source`** — bulk-set on all 54 template Stories (previously only the 8 Epics carried it). Makes the Automation rule's lookup a single flat JQL.
- **Pilot run + verified:** spawned `CUST-63` "ZZ PILOT TEST - Course Explainers" → 4 Stories CUST-64..67. Verified field stamping: Epic carries components [E1 Series, Course Explainers] + fixVersion E1 2026 S3 + Location TBC + Template Source; Stories parented to CUST-63, inherit components/fixVersion/Location. Engine proven.
- **Cleanup pending:** CUST-63..67 are throwaway test data (clearly named "delete after verify") — delete once Robert has eyeballed them.
- **Open:** Nancy to build the native rule from the spec (optional; script covers it meanwhile). Then step (e) bulk move.

### Client handoff sent (2026-05-20)

- **CUST walkthrough legend forwarded to Nancy** via Teams (`badass/drafts/nancy_cust_legend_2026-05-20.md`). Covers: project structure (Client/Type components, Location field, Fix Version, T-shirt Size), the Templates board, how the spawn engine works, the 8 per-owner template Epic links for the scope-check + estimate pass, and "new venue/client goes through PM" to keep the controlled list clean.
- **Status: awaiting Nancy's response before next step.** Step (e) — E12026 (+ SJ/F1/BMS) bulk migration into CUST — is on hold until: (1) Nancy reviews the structure, (2) content owners complete the template scope-check + T-shirt sizing pass, (3) Robert + Nancy both sign off. Step (e) to be run as a reviewed dry-run first (irreversible operation).

## 2026-05-19 — PM Agent (CUST scaffold kickoff, blocked on Nancy admin grant)

- **Trigger:** Robert: "BADASS. Lets continue with the Jira setup according to plans shared with client." Rosy signed off on Phase 1 of the v2 proposal earlier (Teams). Step-by-step execution requested, Robert authorised API/Rovo mutations.
- **Read-only prep ([badass/drafts/cust_scaffold_prep.md](badass/drafts/cust_scaffold_prep.md)):**
  - Inventoried 37 E12026 Epics + labels (Dubrovnik 99+, como 58, Jeddah 15, Monaco 10, TBC 9, Miami 7, Lagos 7, Bahamas 5, racebird 4, Formatexplainer 2, dubrovnik 1 typo).
  - Mapped template seeds: AR Live BC E12026-542 (19 tasks), VR Live BC E12026-657 (17), AR App E12026-279+312 (5), Environment E12026-677 (4 — note: -514 is a Story child, not the Epic), Course Explainers E12026-396 (4), UEFN E12026-213 (thin, mostly Done), Steam-Console E12026-682 (new, Sezar).
  - Dormant project audit: BMS not fully dormant (BMS-94 touched 2026-05-04), PFL stale to 2025-12-08, OR has 0 open, F1 has 18 open + F1-25 overlaps Steam template, SJ has 1 Epic.
- **6 decisions Robert locked (2026-05-19):**
  1. BMS migrates as Component (will close from new setup, not dormant after all).
  2. F1 migrates as F1 Component for now (F1-25 stays under F1).
  3. Format Explainer = 7th template (E12026-185/186/421 race-wide drafts).
  4. Graphics + Live GP fold into AR Live Broadcast.
  5. Vision Pro AR App = all in one AR App epic, no split.
  6. Project type = Component (not custom field).
- **API access bootstrapped:**
  - Robert generated BADASS Atlassian API token; stashed at `~/.claude/.atlassian-credentials-badass.json` (mode 0600) as `badass.atlassian-api-token` (secrets_registry entry added).
  - Auth verified against badass-studios.atlassian.net — accountId 6061d442b30f0d007010a907 (global, same as aurora).
  - Permissions: ✅ CREATE_PROJECT, CREATE_SHARED_OBJECTS, ADMINISTER_PROJECTS; ❌ ADMINISTER (global), SYSTEM_ADMIN.
- **Scaffold attempt blocked:**
  - `POST /rest/api/3/project` (both classic Scrum and team-managed Scrum templates) returned "You must have global administrator rights in order to modify projects." Despite `mypermissions` reporting `CREATE_PROJECT: true`, the REST endpoint enforces global ADMINISTER.
  - **Pivot:** Robert to ask Nancy for global "Administer Jira" grant (NOT Site Admin — narrower) via admin.atlassian.com → BADASS → Users → Robert → Jira Administrators group. Replaces the two-step "create shell + 3 custom fields" handoff with a single permission bump that unblocks everything end-to-end.
- **Pre-built artifacts (ready to fire once Nancy grants admin):**
  - `badass/drafts/cust_post_shell_scaffold.sh` — idempotent script: 14 Components (5 client + 8 type + TEMPLATES), 2 Fix Versions (E1 2025 S2, E1 2026 S3), 3 filters + 3 boards (CUST-All / CUST-Per-Client / CUST-Per-Location Dubrovnik pilot).
  - `badass/drafts/nancy_cust_shell_request_2026-05-19.md` — legacy two-step ask (kept as fallback if Nancy can't grant global admin).
- **Followups filed:**
  - db-161 — wire 2nd local Atlassian MCP for BADASS (mirror db-141 wrapper pattern with the new token).
- **Open:** waiting for Nancy admin grant. Once granted, execute project create + scaffold script + custom fields + activity log update + Nancy/Rosy/Alex Teams confirmation.
- **Custom fields to add post-shell (3, all single-select):**
  - Location: Dubrovnik, Como, Monaco, Lagos, Miami, Bahamas, Jeddah, TBC
  - T-shirt Size: XS, S, M, L, XL
  - Template Source: AR Live Broadcast, VR Live Broadcast, AR App, Environment Production, Course Explainers, UEFN, Steam-Console, Format Explainer

## 2026-05-13 — PM Agent (Nancy unblock follow-up, label inheritance sweep)

- **Trigger:** Nancy Teams DM 09:35/11:39 — Dubrovnik Timeline view empty after yesterday's label cleanup. Then 12:53 — "Jake is missing his tasks" (screenshot of E12026-514 "Environment Production").
- **Diagnosis:** Board 678 (Dubrovnik) saved-filter `labels in (Dubrovinik)` (typo) — yesterday's relabel orphaned the board. Jake symptom = sub-tasks don't inherit parent's location label, so they fall outside every per-location board filter. Same systemic pattern as yesterday's Alex symptom.
- **Permissions:** Nancy promoted Robert to Project Admin + Create Project + Create Shared Objects on E12026 (NOT global "Administer Jira" — so Robert still can't mutate filters owned by Nancy/Ben). Nancy self-fixed the Dubrovnik filter to `labels in (Dubrovnik, Dubrovinik)` after I sent her the JQL.
- **Mutations executed (147 issues):**
  - 9 Jake-assigned items relabeled with parent's location label (Dubrovnik / como / racebird).
  - 138 project-wide items got parent's location label inherited via systematic sweep.
  - 2 leftover `Dubrovinik` typo labels swapped to `Dubrovnik` (typo label now at 0 items).
- **Result:** Dubrovnik board count 44 → 144 items. All 9 location boards populating per their saved filters.
- **Skipped / blocked:**
  - 4 sub-tasks under E12026-402 (Course Explainers Epic) — E12026-403/404/405/406 — return 404 to both API token and Rovo OAuth. Issue-level security set on them. Need Nancy or BADASS Jira admin to surface or relax.
  - 7 parent issues with no location labels themselves (E12026-105 "Broadcast Controls_Jeddah_UE5" looks like Jeddah, others are dormant Drafts). Their 13 children skipped by sweep — flag for Nancy review.
- **Filter ownership ask sent:** Robert messaged Nancy (and to-do for Ben) to transfer per-location filter ownership so Robert can self-serve future filter edits. Until then, every filter mutation needs Nancy/Ben.
- **Followup for proposal:** Today's 138-item sweep is exactly what Phase 1's Jira Automation rule replaces — clone-template-to-children with location-field auto-applied. Worth quoting the +100 number when sending the proposal up to Rosy/Alex as concrete validation.

## 2026-05-12 — PM Agent (Jira customisation-side overhaul, Nancy unblock + structural plan)

- **Trigger:** Nancy DM (15:00 CET) sharing E12026-542 "AR Broadcast Setup — Dubrovnik" — Alex's 20-task checklist not appearing on her Dubrovnik board. Root request: design a Jira setup for the customisation team that handles client/location rotation without the per-project duplication pattern.
- **Approved scope (Robert, 2026-05-12):** (A) full consolidation of client projects into one new CUST project; T-shirt sizing (XS–XL, Nancy-owned at intake, no team burden); (i) quick-fix Nancy's Dubrovnik board today, structural proposal end-of-week, execute next week.
- **Audit findings (Jira state pre-fix):**
  - 11 Jira projects on badass-studios.atlassian.net. Only **E12026** is actively worked (26 issues touched in last 60 days, 24 still open).
  - SJ/F1/OR/PFL/BMS combined: 173 issues total, 18 open, **zero activity in last 60 days** → all dormant.
  - E12026 has 35 epics scoped by location *labels* (typoed three different ways: `Dubrovinik` ×19, `Dubrovnik` ×5, `como` lowercase, `Dubrovnik` capitalised correctly only on Course Explainers epic).
  - Same recurring activities reappear per location with inconsistent naming ("AR Broadcast", "AR app V0.2.x", "Vision Pro app V0.1.0", "Course Explainers"). No template engine.
  - Two duplicate "Course Explainers" Dubrovnik epics: E12026-396 (correct label, 4 active children) and E12026-402 (typoed label, no children).
- **Quick-fix executed (Dubrovnik board unblock):**
  - 15 items relabeled `Dubrovinik` → `Dubrovnik` (E12026-279, 280, 312, 313, 317, 318, 324, 325, 326, 402, 510, 514, 515, 528, 645).
  - 1 placeholder Done task also relabeled (E12026-215, summary "Dubrovinik").
  - 21 items received the `Dubrovnik` label they were missing: parent epic E12026-542 + 20 children (E12026-543, 544, 545, 546, 547, 548, 571, 572, 574, 575, 576, 577, 599, 600, 602, 603, 604, 605, 633, 634).
  - Duplicate flag comment added on E12026-402 pointing to E12026-396 as canonical (Nancy to confirm closure).
  - **Verification:** `labels = "Dubrovnik"` JQL now returns 41 items (6 Epics, 13 Stories, 22 Tasks). `labels = "Dubrovinik"` returns 0.
- **Recommendation for CUST consolidation scope:** start with E12026 (only active project). Dormant 5 (SJ/F1/OR/PFL/BMS) can be folded in as historical Components or archived in place — minimal team disruption either way since no live work.
- **Next:** structural proposal GDoc (CUST schema + template engine + migration plan) end-of-week; execution next week post-approval.
- **Proposal v1 shipped:** https://docs.google.com/document/d/1D3Huv4Ibp8q4j6vjdmtjCltNNkDNTwG_6OgHMOImae0/edit (BADASS Drive → Deliverables). Two-phase scope.
  - **Phase 1 — Customisation Jira Restructure:** new `CUST` project (Client=Component, Season=fixVersion, Location=Epic with controlled-list custom field), template Epics per project type, Jira Automation for one-click location spawn, T-shirt sizing baked into templates. Steps 1.0–1.5 (quick-fix → sign-off → CUST scaffold → E12026 migration → dormant client triage → Nancy onboarding) over 19–23 May.
  - **Phase 2 — Standup → Jira Auto-Update:** point existing AP post-meeting-sweep at BADASS Teams daily standup. Read AI stays (already deployed, AP pipeline notetaker-agnostic), backup option Fireflies. Steps 2.0–2.4. ~1.5 days of AP work + 2 weeks shadow-mode tuning. Live ahead of Dubrovnik race 12–13 June.
- **Decisions locked by Robert (2026-05-12):**
  - D1: Archive PFL/BMS/OR; migrate SJ + F1 open tickets.
  - D2: Distributed template ownership (Alex/John/Ben/Marco/Jake/Sezar per template), PM as operator running post-race retros.
  - D3: T-shirt size defaults baked into templates.
- **Robert's v1 review pass on the GDoc (2026-05-12):** 2 comments + 31 suggestion edits. Applied all:
  - "Nancy" → "PM" globally (24 instances), with one intro mention "Project Manager (PM, Nancy)" in the header. Repositions the doc as a role-based proposal, not a consultant pushing a single staff member.
  - "K2C" → "another project" (anonymise prior-project references when externalising).
  - "Symptom (Nancy's screenshot, 2026-05-12)" → "Example" (anonymise illustrative incidents).
  - "the leverage" → "what matters" (AI-tell language stripped).
  - "they're being kept alive at zero benefit" → deleted (editorial AI commentary stripped).
  - All em-dashes (`—`) stripped from the doc per writing_voice_robert.md rule that was already documented but I'd violated.
  - "Nancy, Rosy, Alex" in Step 1.1 → "Stakeholders".
  - "Robert sends this doc to Nancy/Rosy/Alex" → "Robert and Nancy send this doc to Rosy and Alex". Big repositioning: Nancy is co-author, not recipient. The proposal is about her working environment; she co-signs before it goes up.
  - Dates removed from doc body ("target Thu 15 May", "target send: Tue 13 May AM"). Dates belong in the cover email.
  - TL;DR softened on Showjumping question — replaced "Only E12026 is live" with "E12026 is the only project with activity in the last 60 days; SJ and F1 each carry a handful of open tickets that may reactivate; PFL, BMS, OR look fully dormant".
- **Both comments resolved via Drive API.** Suggestion layer cleared on re-upload (HTML replaces content; suggestion markers don't re-attach to refreshed text).
- **Learnings saved to:** `writing_voice_robert.md` (proposal-document section + reinforcement of em-dash + "leverage" rules), `pm_learnings.md` (role-not-person framing, co-author with role-holder, dates-in-cover-not-body).
- **Nancy co-author handoff drafted:** `badass/drafts/nancy_proposal_handoff_2026-05-12.md`. Robert sends to Nancy first; she reviews + co-signs; then joint send to Rosy + Alex.

## 2026-05-11 — UIbot (org chart v2 for Rosy)

- **Goal:** Deliver v2-shape org chart to Rosy tonight, accompanying merged P&L.
- **Constraint:** v3 modular spec was rejected Sat May 9 — build the simpler v2 cost-center split (Platform UK/US, Customisation UK/US, GenMgmt, M&S, Comms, GenEng, HR, QA, Advisory).
- **Inputs:** Staff tab of `badass/drafts/Badass_PnL_Merged_2026-05-11.xlsm` (named current staff at rows 170-182) + `staff_roles_mapping_v2.md` (cost-center placement).
- **Format choice:** HTML/CSS rendered to PNG+PDF via puppeteer (no graphviz/mmdc available). Three-row grid: row 1 = Mgmt + M&S + Comms; row 2 = Platform UK + Platform US + Customisation UK + Customisation US; row 3 = GenEng + HR + QA + Advisory. CEO box pinned above.
- **Visual encoding:** Solid border = named current staff, dashed border = open hire. Q-flip pills (Q3-26 / Q4-26) on open-hire cards where dated. Group top-border color: Platform blue, Customisation rust-red, others neutral.
- **Marco + Jake stay on Platform UK** per Rosy's Saturday note ("currently should be going into components for the platform"). Marco's sheet entry "Mario Tosoni / US / Tech Artist" surfaced via merged P&L; chart uses corrected Marco Tosoni / UK / 3D Artist per Rosy's role descriptions.
- **Files:**
  - HTML source: `badass/drafts/org_chart_v2.html`
  - PNG (1800px wide, 2x DPI): `badass/drafts/org_chart_v2.png`
  - PDF: `badass/drafts/org_chart_v2.pdf`
- **Drive uploads (Deliverables folder):**
  - PNG: https://drive.google.com/file/d/1i6MMZyUI-dWHGZtk6dvvUIqpSegkM979/view
  - PDF: https://drive.google.com/file/d/1RdXbO7e_hVa9Rpn2E1dEBujXUWuWea40/view
- **Judgement calls:**
  - "Producer / Tech Lead" row on Platform UK marked Q4-26 (sheet line item, no Q-flip in v2 mapping doc — defaulted to Q4-26 to match other un-dated Platform UK opens).
  - Ben Jeffreys placed on Platform UK matching Dieter's sheet (v2 mapping flagged him as "pending Robert call" — chart shows current-state-of-record).
  - "Verse/UEFN Developer" in Customisation UK box labelled with "urgent · Fortnite Monaco" caption per Apr 22 demand notes.
  - QA section shows QA Lead gated on "QA > 10" + external pass-through QA, matching v2 mapping decision that internal QA wraps into Release Manager (Platform UK).
  - Advisory Board kept as a peer group (own card) rather than nesting under CEO — visually flatter, matches "Advisory Board" header in P&L Staff sheet (row 139).

## 2026-05-09 — PM Agent (live session with Robert + Dieter call prep)

- **Goal:** Rework BADASS staffing plan/budget into Dieter's modular team-unit shape (v3) ahead of 17:00 CEST Dieter call. Robert promised v3 to Dieter on May 5 by Thursday May 7 — slipped by 2 days, delivered today.
- **Approach:** 7-section walkthrough Q&A (taxonomy → per-template Core → Platform → Shared Services → existing staff retro-fit → scenarios → stakeholder choreography), each section locked progressively with TodoWrite tracking.
- **Output shape (per Robert's call):** structural spec GDoc only — no salary numbers, no quarter ramps, no scenario totals, no Cloud/AI cost figures yet. Lock shape with Dieter first, populate post-sign-off into the May 4 v2 P&L file.
- **5-group model locked:** Management / Marketing & Comms (new own group) / Platform / Customisation Core (5 templates) / Shared Services
- **5 templates:** AR Live Broadcast (E1, show jumping, sports, concerts) / VR Live Broadcast / AR App / UEFN / Steam-Console Game; Digital Twin folds into Broadcast templates
- **Load-bearing rules:** 50% threshold (>50% Core, ≤50% Shared Services); sub overflow scales projects (not FTE inflation); concurrent = full Core duplication; surplus FTE hours flow upstream to Platform; Customisation Team Lead = AP-supplied PM at 60% per template
- **Investor optics override:** Marco/Jake/Ben held on Platform per Rosy's Apr 27 direction (reusable artifact-producing work = Platform regardless of who pays); pending Alex discussion this week
- **Drive deliverable:** v3 spec doc uploaded to BADASS Drive → Deliverables (`https://docs.google.com/document/d/11eqVAkuuhjvjzFYAiPbvc7mtF5tids0KWasUJ2_xt54/edit`)
- **Drive hygiene:** April 15 P&L moved from Financials → Archive (root-level Archive folder `1XBCUg_UQ9oHyaC-z-Cmbpiwznkv20dtb`); May 4 v2 P&L stays live in Financials as numerical source-of-truth
- **Email drafts:** Cover to Dieter (CC Rosy+Alex) on Job Descriptions thread `19d9f3a4db17e64e` — Robert sent post-review; reply to Nancy on Role Descriptions thread `19e0694c0fa9ecb2` (6 v3-driven new role descriptions + 3 rename overlap checks + 2 sheet-backlog optionals) — Robert sent
- **Project memory drift fixed:** Nancy Imado/Herbert is Chief of Staff (not QA part-time as memory had her); updated `project_badass.md`
- **Next steps after Dieter call:** Build full Staff Sheet inside May 4 v2 P&L (yellow fill + Changes Log) once shape signed off; Scenario tab with disclaimer about limited business-case visibility; fold Cloud/AI cost from `badass-002`; Alex discussion on Marco/Jake/Ben Platform-vs-Customisation
- **Tickets:** `badass-004-staffing-plan-v3-modular` delivered (pending Dieter sign-off then close); `db-120-reply-to-dieter-badass-re-pnl-update-call-today` resolved via cover email send


## 2026-05-05 — PM Agent (live session with Robert, post-Dieter call)
- Dieter call ran 12:30 CEST, 30 min, no Gemini (Teams). v2 file (yellow fill + Changes Log preserved) confirmed as canonical, walkthrough done.
- **New direction from Dieter — staffing plan v3 redesign:** modular stackable Customisation team templates (Core team per project type + subcontractor overflow + shared Support teams). Platform near-untouched. Goal: Platform + Mgmt = fixed cost, Custom + Support scale with active project count. Investor-optics goal: clean SaaS-like product/services split.
- **Robert promised v3 P&L delivery by Thursday 2026-05-07.** Hard deadline, 2 working days.
- Adjusted sequencing: PM takes first-pass taxonomy + templates with documented assumptions, ships Thursday with sign-off questions called out inline. Rosy+Alex review post-delivery, not pre.
- Open: project-type taxonomy locked (AR Live Bcast / VR Live Bcast / AR App / UEFN / Steam game / Digital twin — proposed first cut, needs Rosy+Alex sign-off on file), subcontractor rates from Dieter, salary bands from Dieter, treatment of existing E1 staff in new templates.
- Pending from v2 still owed: Cloud/AI cost (Apr 15 brief item 2) — TBD whether Thursday includes it or stays separate.

## 2026-04-27 — PM Agent (live session with Robert)
- Continued the Apr 22 drafted reply to Dieter+Rosy on the Job Descriptions thread (it had been sitting unsent for 5 days)
- Applied the Apr 22 staff sheet changeset programmatically to a copy of Dieter's xlsm, saved as `badass/drafts/Badass_PnL_2026-04-27_proposal.xlsx` (file had no VBA, only printerSettings .bin → safe round-trip)
- Strategy: repurposed 0% open rows in-place (no row inserts) so SUM formulas in totals rows stay intact
- 39 cell edits applied; "Changes Log" tab inserted as sheet 1 with full audit trail
- Pending Dieter manual touch (flagged in Changes Log + email): Release Mgr 50/50 split, Ian full name (A175), Marco location (E7)
- Created BADASS Drive subfolders: Financials (`1HAuKDYqE5k3DZok6fH7AqlP_OE1fjuyq`) + Deliverables (`1hdEG5JhcjggvnsfThnOn_5sxfJW-vZzj`)
- Uploaded: P&L proposal xlsx (Financials), Staff Roles Mapping v2 GDoc + Staff Sheet Changeset GDoc (Deliverables)
- Deleted two stale Apr 22 drafts (orphan Rosy-only + the canonical 3-recipient one) before composing the refreshed Apr 27 reply
- New draft created via Gmail REST API (proper multi-recipient + thread headers), ID `19dcf0cba8720ffb`, threaded into Job Descriptions thread `19d9f3a4db17e64e` — pending Robert review/send
- Cloud/AI cost scoped: platform-only, all 4 AI buckets (broadcast AI runtime split into platform-build vs customisation-runtime), quarterly Q3-26 to Q2-31 — modeling next

## 2026-04-19 04:09 — PM Agent (4am sweep)
- Scaffolded `badass/` project directory (was missing from disk)
- Downloaded Dieter's P&L attachment (2026-04-15 version) to `badass/drafts/`
- Parsed Staff sheet: 197 rows, covers Q3-2026 through Q2-2031
- Audited Jira: E12026 active (30 issues updated in 30d, 18 Done, 7 In Progress, 5 To Do — environment/broadcast work). BX and PE quiet (PE last updated Apr 9, all Done)
- Gmail audit: reconstructed full timeline since Mar 26 (see below)
- Created `badass/drafts/staff_roles_mapping.md` — roadmap demand vs P&L gap analysis
- Updated ticket with current state and Robert's action items

## 2026-04-18 — Rosemary
- Shared job descriptions via Dropbox (partial — still needs: Finance, Data, AI Dev, BizDev, Sales, Partner Manager, UX/UI, QA, HR, onsite AR/VR broadcast producers)
- CC'd Ben Jeffreys and Nancy

## 2026-04-16 — Nancy
- Daily meeting cancelled (Como environment testing, Wed + Fri)
- Robert acknowledged, offered to join if needed

## 2026-04-15 — Roadmap/Financial call (Teams, 7pm CEST)
- Participants: Robert, Rosemary, Dieter, Alex
- Dieter sent follow-up email with P&L attachment (xlsm)
- Action items from Dieter: (1) Review + adjust Staff Roles to match Roadmap, (2) Estimate Cloud/AI costs
- Nancy sent Teams chat invite for ongoing Roadmap coordination
- Dieter available: limited Apr 18-26, back Mon Apr 27

## 2026-04-10 — Rosemary
- Responded positively to Robert's module-by-module breakdown: "This is great"
- Asked Dieter + Alex to find time for a walkthrough call
- Mentioned she's crafting Role/Job descriptions in parallel

## 2026-04-09 — Robert
- Sent full module-by-module role breakdown to Rosemary (Platform, Gaming, AR/XR, Broadcast, Environment, E1)
- Total demand: 42-71.5 PM in 2026 vs ~54 PM available
- Key gaps flagged: Verse/UEFN dev by May (Fortnite Monaco), 3D artist by June (Dubrovnik), PM asap
- Noted Dieter's staff sheet missing Verse/UEFN Dev and DevOps rows

## 2026-04-08 — Rosemary
- Emailed requesting module-by-module breakdown for business plan
- Referenced Robert's estimation report as "external viewpoint"

## 2026-04-01 — Call (Robert, Rosemary, Alex)
- Backlog walkthrough at 7:30pm CEST
- Originally scheduled for Mar 31, rescheduled by Rosemary

## 2026-03-26 — Robert
- Sent role-based breakdown + Option A engagement proposal to Rosemary
- Updated backlog sheet with Role column (578 rows tagged)
- Rosemary replied from flight: "Let's grab a time on Monday with Alex"

## 2026-03-25 — Rosemary
- Responded to estimation report: "Good report"
- Requested role-based breakdown for business plan + effort alignment with Excel

## 2026-03-24 — Robert
- Edited and shared estimation report via Google Doc
- Removed individual names, rewrote Como recommendation, added deadline push note

## 2026-03-22 — Claude
- Full Jira backlog audit: 1,673 issues across BX, PE, E12026
- Mapped 350 active items to platform architecture
- Identified 483 orphans, 7 junk tickets cleaned
