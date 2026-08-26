# Portfolio Board — 3-view build guide (Plan 34)

> **INTERNAL working copy only.** The client-facing version is section 7 of the shared "CUST - Admin User Guide" GDoc (updated in place 2026-05-29). Never send this .md to the client — see [[feedback_no_md_to_clients]].


**For:** whoever configures the saved views (Nancy owns board hygiene; Robert/PM can drive)
**Date:** 2026-05-29
**Plan:** Portfolio Board, plan id 34 — https://badass-studios.atlassian.net/jira/plans/34
**Status:** ready to execute. Saved views in Plans are UI-only (no REST), so these are click-steps.

## Context / live state checked 2026-05-29
- Plans is **live** (Jira Software is Premium-tier on badass-studios). No upgrade needed; the May 20 "need Premium / trial?" message to Nancy is moot.
- Plan 34 pulls from 11 sources, including **CUST** (project 10672) plus 10 legacy projects/boards.
- CUST has 763 issues: 636 assigned / 127 unassigned; 230 with due date; 192 with start date (customfield_10015); only **132 with an hours estimate**; only **1 "blocks" link** across all 47 epics.
- Plan baseline fields: start = `customfield_10015`, end = `dueDate`.

---

## View 1 — Client relationship timeline (engagement length)

**Goal:** one bar per client showing how long the engagement runs, not the tasks underneath.

**Data prerequisite — DONE (created 2026-05-29):** one dated "engagement" parent per client, Epic tagged `client-engagement`, summary `ENGAGEMENT: <Client>`, Start (customfield_10015) + Due = relationship span.
- CUST-793 E1 Series — dated **2025-09-30 → 2028-12-31** (start = first dated E1 work; end per Nancy "ongoing until 2028"). ✓ shows a bar now.
- CUST-794 Show Jumping / CUST-795 F1 VR / CUST-796 Blackbook / CUST-797 BMS — labelled + tagged, **dates blank** (no dated work exists). Nancy sets Start + Due on each and the bar appears.

**View setup:**
1. Open Plan 34 → top-right view selector → **Create view** → name it "Client Timeline".
2. **Filter** → by label → `client-engagement` (so only the 5 engagement bars show, no task clutter).
3. **Group by** → Component (Client).
4. **Timeline scale** (top-right) → Quarters (or Months).
5. Fields shown: Summary + the bar. Save.

Result: 5 bars, one per client, lengths = relationship spans. (Bars appear only once start+end are set, so the 4 undated clients show once Nancy fills dates.)

---

## View 2 — Dependencies / blocking

**Goal:** see at a glance what's blocking what.

**Data prerequisite:** "blocks / is blocked by" links must exist. **Only 1 exists today**, so the view starts near-empty. Ask the leads to log blockers, starting with the E1 Miami sprint (CUST-743..CUST-761).

**View setup:**
1. Plan 34 → **Create view** → "Dependencies".
2. Settings (gear, top-right) → **Dependencies** → set to **Lines** (draws arrows between blocked/blocking bars). Also tick "Show dependency report" if you want the side panel.
3. Group by → Component (Client) or Epic, whichever reads better.
4. Save.

Result: arrows between bars wherever a blocks-link is set. Fills in as the team links work.

---

## View 3 — Workload per person

**Goal:** how much work each person has across clients and locations; spot overload.

**Data:** ready now — 636 of 763 issues are assigned.

**View setup:**
1. Plan 34 → **Create view** → "Workload by person".
2. **Filter** → exclude the engagement markers: label **is not** `client-engagement` (they're high-level bars, not real work — leaving them in would show 5 phantom items under their assignee).
3. **Group by** → Assignee.
4. **Colour by** → Component (Client) — bars colour-coded by client so cross-client load is visible.
5. (Optional) **Filter** → Location field to focus a venue.
6. Save.

**Caveat:** this is a count-of-work-items read, not an hours/capacity heatmap (only 132 issues carry estimates). To get true capacity later, start logging Original Estimate on tickets and the Plan's Capacity view becomes meaningful.

---

## Follow-ups to flag to Nancy / leads
1. Fill start+end dates on the 4 undated client-engagement epics (Show Jumping, F1 VR, Blackbook, BMS).
2. Leads: start tagging "blocks / blocked by" on E1 Miami work so View 2 fills in.
3. Longer-term: log Original Estimate on tickets to unlock true capacity planning.
