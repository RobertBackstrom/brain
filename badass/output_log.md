# BADASS — Output Log

Significant deliveries/changes. Running detail lives in `activity_log.md`.

## 2026-06-17 — Built out Steam-Console (gaming) template + backfilled Monaco (Nancy urgent)
- Nancy flagged "Gaming missing for Monaco" + her new epic "only has one task." Diagnosed: the spawn automation was NOT broken — it cloned correctly. The **Steam-Console template (CUST-60) was a stub with one story** ("Import Environment to Game"). Template-health sweep: AR Live Broadcast 20, VR Live Broadcast 17, AR App 5, XR Headset/Env Prod/Course Explainers 4, UEFN 2, **Steam-Console 1, Format Explainer 0**.
- **Built out the template:** authored 12 game-build stories into CUST-60 (CUST-879..890): Track Spline & Racing Line, Course Boundary & Buoy Collision, Checkpoint/Lap/Timing, Grid Start & Spawn, Venue Lighting & ToD, Water Surface & VFX, Performance & LOD, Track Select & Loading UI, Minimap & Race HUD, Venue Audio, QA Playtest (Steam & Console), Build Packaging & Cert. Template now 13 stories. Drafted from E1 racing-game scope (Robert-approved source).
- **Backfilled Monaco** (CUST-877): added the same 12 stories (CUST-891..902), tagged Steam-Console / Monaco / E1 2026 S3, matching the spawn clone pattern. Monaco gaming epic now 13 stories. Authorized by Robert (plan-confirm).
- Future Monaco-style spawns of Steam-Console now clone the full set automatically. **Open:** Format Explainer template (CUST-62) is still empty — same one-task trap waits for whoever spawns it next.

## 2026-06-11 — Fixed Nancy's "can't access this board" filter lock
- Nancy (and anyone but Robert) couldn't open 4 of 5 CUST boards — their backing filters were **private to Robert** (no share permissions). Only the default board 953 (filter 11052, shared with project CUST) worked.
- Added a `project: CUST` share to the 4 private filters: 11053 (CUST - All), 11054 (Per Client), 11055 (Per Location), 11056 (Templates). Verified all now show `project/CUST`. Mirrors the one filter that already worked.
- Result: every CUST project member (Nancy, Rosy, Alex) can now see all 5 boards. Authorized by Robert (share-with-project chosen over Nancy-only).
- Follow-on: Nancy also reported "missing clients" on her Portfolio Plan. Investigated, briefly created 4 client components (PFL MMA / Racing Unleashed / WSX / Kiro) + extended the Per-Client filter - then Nancy confirmed via Teams she sees all clients (engagement epics CUST-793..797) now that the filter access is fixed. The "missing clients" WAS the same access problem. Robert: "no change needed." Reverted both (deleted the 4 empty components, restored filter JQL). Net structural change = none beyond the filter shares.

## 2026-06-11 — Spawned Monaco location epics + fixed the spawn-guide bug (Nancy blocked)
- Nancy couldn't get the Monaco template checklist to clone (following CUST Admin User Guide §3). Root cause: NOT a filter issue. The section-6 automation rule has never worked (zero location epics ever spawned project-wide), and the guide's §6 lookup JQL was **missing quotes** around `{{triggerIssue.Template Source}}` - with spaces in the value, unquoted JQL is invalid, returns nothing, so the Epic saves but no stories clone.
- **Unblocked Monaco** by running the script engine (`cust_spawn_location.py`) - the documented PM fallback. Spawned 5 Location Epics + 50 stories, all tagged E1 Series / Monaco / E1 2026 S3: CUST-805 (AR Live Broadcast, 20), CUST-826 (VR Live Broadcast, 17), CUST-844 (Environment Production, 4), CUST-849 (AR App, 5), CUST-855 (Course Explainers, 4). Authorized by Robert.
- **Fixed the guide** (CUST Admin User Guide GDoc, same link): added the required quotes to the §6 JQL + a note on why; rewrote §3 step 3 so the auto-clone clearly reads "only once the §6 rule is on, else ask the PM." Pushed in place via gdrive-update-doc.js.
- Old duplicate guide (1Yk_DJ8dsmudo1X6Z4_Y0MyL-u4N8a2ZyC41Ck2Oyz0E "CUST - Automation Rule Build Guide") confirmed trashed (was already in trash; reconfirmed on Robert's OK 2026-06-11).
- Label fix (Nancy follow-up): the spawn set the Location *field* but not the matching **label** - and the team convention is both (every Dubrovnik issue has Location=Dubrovnik AND label "Dubrovnik"; the label is what the Per-Location board/quick-filters sort on). Without it Nancy "couldn't sort by location." Backfilled label "Monaco" on all 55 spawned issues, patched `cust_spawn_location.py` to set `labels=[location]` on epic+stories going forward, and updated guide §6 so the automation rule copies Labels down + sets Label=Location on the trigger Epic.
- TODO (Robert + Claude, evening 2026-06-11): build the §6 spawn automation rule in the Jira UI together, using the now-corrected guide; test with a throwaway Epic, then delete the test. Until it's live, PM runs the clone by hand.

## 2026-06-12 — CUST spawn automation FLOW built + live (Robert drove UI, Claude guided + verified)
- Built the location-spawn automation in Jira's newer **Flows** UI (Robert clicked, I gave exact values + verified via API each step). Final design (cleaner than the old spec - dropped the redundant Lookup action): Trigger "Work item created" → 3 "Work item fields conditions" (Work type=Epic, Template Source not empty, Summary !contains TEMPLATE:) → Edit work item (Epic Labels = `{{triggerIssue.Location}}`) → **Branch flow / related work items, Type=JQL** (the quoted template-lookup JQL, "changed since last execution" UNCHECKED) → inside branch, Create work item (Story) with `{{issue.summary}}` + `{{triggerIssue.*}}` field copy-down incl. label+location. Named "CUST: Spawn template Stories on new Location Epic", edit-permission shared (not Private), enabled.
- **Tested green:** created RULE TEST epic CUST-870 (Course Explainers, Location TBC) → flow spawned 4 stories with correct parent/components/label/location/fixversion; epic got the TBC label. T-shirt blank only because Course Explainers templates have none. Test artifacts deleted.
- **Permission fix:** spawned stories are owned by "Automation for Jira", and Robert had only delete-own (the CUST **Administrators** project role had ZERO members - he admins via site-admin, not the role). The shared "Default software scheme" already grants Delete Issues to Administrators, so the fix was **adding Robert to the CUST Administrators role** (not touching the shared scheme). Orphan test stories then deleted.
- **Guide §6 fully rewritten** to the real Flows UI (Create flow → from scratch, the JQL-branch design, the two silent-failure gotchas: missing quotes + "changed since" box, the `{{issue}}` vs `{{triggerIssue}}` smart-value rule, name+edit-permission at enable, delete-needs-admin-role caveat) + screenshot slots Robert will paste into. Pushed in place. §3 wording aligned rule→flow.
- Outstanding: Robert to paste the build screenshots into the §6 slots in the GDoc; rename the flow's display title if desired (currently fine).

## 2026-06-12 — Board cleanup + per-client/venue filters
- Deleted redundant board **956 "CUST - Per Location (Dubrovnik pilot)"** + its filter 11055 — its JQL (`project = CUST AND component != TEMPLATES`) was identical to board 954 "CUST - All"; no location dimension, misleading name, stale pilot tag, not a Plan source. "Per Client" (955) kept — it's legitimate (`component in (5 clients)` ORDER BY component).
- Board quick filters confirmed **UI-only** on this Cloud instance (greenhopper endpoints 404). So created **12 shared saved filters** via REST instead (one-click slices): `CUST Client - <E1 Series/Show Jumping/F1 VR/Blackbook/BMS>` (filters 11122-11126) and `CUST Venue - <Dubrovnik/Como/Monaco/Jeddah/Miami/Lagos/Bahamas>` (11127-11133), all shared with project CUST. Venue filters run off `labels = X` (the sortable dimension).
- Guide §5 extended with the quick-filter recipe (per-client `component=`, per-venue `labels=`) + pointer to the saved filters, so Nancy can add board chips herself. Pushed.
- Drafted Nancy Teams wrap-up: `drafts/nancy_cust_wrapup_2026-06-12.md` (Monaco in + sortable, auto-clone live, client/venue filters). Robert to send.

## 2026-06-14 — Portfolio Plan (Plan 34) timeline views for Nancy
- Built per-venue timeline views on the Portfolio Board Plan (Robert drove UI, Claude guided). Mechanism: the existing "Client Timeline" view = Filter `Label is client-engagement` (only the 6 ENGAGEMENT epics carry it → one bar per client). Venue views = same pattern, swap Label value to the venue (`Monaco`, `Bahamas`, ...) → Save as new view. Saved Venue - Monaco + Venue - Bahamas (+ Robert added the real-work ones). Per-single-client drill-down would be Add filter → Component instead of Label (not built; documented).
- Findings surfaced: venues are wildly uneven (Como 11 / Monaco 8 / Dubrovnik 7 / Jeddah 4 / Miami 2 / Lagos 2 / Bahamas 1 epics) — Bahamas barely planned. New engagement epic CUST-862 "ENGAGEMENT: PopUp Hotel" appeared (new client/engagement since the 793-797 set). The 5 spawned Monaco epics show as rows-without-bars until dated.
- Documented the venue/client view recipe in guide §7 (label=venue, component=client, Save-as-not-Save, dating caveat, UI-only). Pushed.
- Client dimension already covered by the existing "Client Timeline" view (all clients, one bar each); per-client drill-downs optional, recipe documented. Robert: good for now.

## 2026-06-15 — Portfolio Board: data layer for Nancy's 6 queries
- Nancy sent 6 queries she wants Plan 34 to answer (timeline, products/locations, assignee workload, overload/capacity, hiring forecast, core-vs-bespoke) + an investor-facing portfolio view.
- **Premise check (saved a hollow build):** 0/839 CUST issues had Story Points, 2 had a T-shirt size; only E1 Series (of 5 clients) has dated work. So Q4 (overload) + Q5 (forecast) had NO data, and 4/5 client timeline bars can't be derived. Surfaced to Robert; he chose: rough-size now (indicative), drive views via Playwright, backfill core/bespoke.
- **REST writes done (verified):** (1) `core`/`bespoke` label on all 839 issues — 834 core / 5 bespoke (CUST-205/356/437/862 PopUp Hotel/866 City Props). (2) Indicative Story Points on 780 issues (type+keyword heuristic XS1..XL8; 59 Epics unsized to roll up). (3) Added Story Points (cf10033) to both CUST screens + created CUST-scoped all-issue-type context 10879 (the field was Story-only + off-screen).
- **View specs** (Q2/Q3/Q4/Q6 new; Q1 + venue views already exist) written to `drafts/portfolio_views_spec.md` — to fold into CUST Admin Guide §7.
- **Blocked:** Playwright view-build — VPS browser locked by another session + Jira SSO auth needed. Views pending: Playwright-when-unblocked OR Nancy self-serves from specs.
- Q4 caveat to relay: indicative points rank relative load, not true capacity. Q5 = forecast memo, dependent on a real sizing/dating pass.

## 2026-06-02 — CUST workflow + default-assignee fixes (Sezar requests, via Teams)
- Added 3 statuses to the CUST workflow ("Software Simplified Workflow for Project CUST", covers all issue types): **In Review** (reused 10035), **Blocked** (reused 10361), **Under Testing** (created 10576). All "In Progress" category, wired as global transitions (any→any), matching the existing To Do/In Progress/Done pattern. Done via the new Jira workflows update API (validated clean, then applied).
- Fixed CUST default assignee: project default + **all 15 components** flipped PROJECT_LEAD (= Robert) → **UNASSIGNED**. New tasks no longer auto-land on Robert. Verified.
- Both authorized by Robert (status add = "np fix" to Sezar + explicit gate confirm; assignee = "Unassigned" chosen). Drafted Sezar Teams reply confirming both.

## 2026-05-29 — Portfolio Board: 3-view setup for Nancy
- Confirmed Plan 34 is live on Premium (Plans active) — earlier "need Premium upgrade" message to Nancy is moot.
- Created View 1 data layer: 5 `client-engagement` Epics (CUST-793 E1 dated to 2028; CUST-794/795/796/797 awaiting Nancy's dates).
- Drafted Nancy Teams reply: `drafts/nancy_portfolio_views_2026-05-29.md`.
- Drafted 3-view build guide (UI click-steps): `drafts/portfolio_board_views_buildguide_2026-05-29.md`.
- Outstanding: Nancy saves the 3 Plans views + dependency toggle; fills dates on 4 engagement epics; leads start logging blockers.
