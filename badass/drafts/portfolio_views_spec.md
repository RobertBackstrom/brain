# CUST Portfolio Board (Plan 34) — View Specs for Nancy's 6 Queries

Built in response to Nancy's 2026-06-15 query list. Maps each ask to a concrete Plan 34
saved view or a data note. Plan views are UI-only (no API), so each is a Save-as in the
Plan 34 timeline. Open the plan, set the filters/grouping listed, then **Save as** a new view
(never plain Save — that overwrites the current view).

Plan: https://badass-studios.atlassian.net/jira/plans/34/scenarios/34/timeline

## Data layer set up 2026-06-15 (already done, via REST)
- **Label `core` / `bespoke`** on all 839 CUST issues. core = standard product suite (834);
  bespoke = one-off custom work (5): CUST-205, CUST-356, CUST-437, CUST-862 (PopUp Hotel),
  CUST-866 (City Props tool).
- **Story Points (indicative)** on 780 issues. Derived from issue type + title keywords
  (XS=1 / S=2 / M=3 / L=5 / XL=8), NOT real team estimates — directional only. 59 Epics left
  unsized so they roll up from their children. Field added to CUST screens + a CUST-scoped
  context so it applies to Story/Task/Sub-task/Bug.

---

## Query 1 — Client timeline, drill into one  ✅ already exists
View **"Portfolio — by client"** (built prior session): Filter → Label `is` `client-engagement`
→ one bar per client engagement epic (CUST-793..797, 862). Drill into a client = Add filter →
Component → is → <client>.
- **Reality check:** only **E1 Series** has dated work (705 issues). Show Jumping (1), F1 VR (18),
  Blackbook (1), BMS (7) have **no dated issues**, so their engagement bars only render once
  someone sets Start (cf10015) + Due on CUST-794/795/796/797. Not invented here.

## Query 2 — Products + locations per client  ▶ NEW VIEW
View name: **"Products & Locations — by client"**
1. Add filter → Component → is → (leave across all clients, or pick one).
2. Group by → **Component** (clients + types both show as components).
3. Add the **Location** column (label) + **Fix Version** column via the field/column picker.
4. Scale = Quarters. Save as.
- Per-client product mix reads off the Type components (AR Live Broadcast, VR Live Broadcast,
  AR App, UEFN, Steam-Console, Course/Format Explainer, Environment Production, XR Headset);
  venue spread reads off the Location label; version off Fix Version.

## Query 3 — Who's assigned to what, across all clients  ▶ NEW VIEW
View name: **"Workload — by assignee"**
1. Filter: none (all CUST), or exclude TEMPLATES (`Component != TEMPLATES`).
2. Group by → **Assignee**.
3. Add **Story Points** column (shows the per-person load).
4. Scale = Quarters. Save as.
- 652/839 issues are assigned; 187 unassigned will sit under an "Unassigned" group.

## Query 4 — Who's overloaded vs has capacity  ▶ NEW VIEW (indicative)
View name: **"Load — by assignee (indicative points)"**
1. Same as Q3 (Group by Assignee), then sort the Story Points column descending.
2. Roll-up: turn on the group-level Story Points sum so each person shows a total.
- **Caveat to state to Nancy:** points are indicative (auto-derived, not team-sized), so this
  ranks relative load — it does NOT compare against true available capacity. A real capacity
  view needs (a) the team to size the backlog properly and (b) per-person capacity config in
  Plan settings. Treat as "who's carrying the most issue-weight," not "who is over 100%."

## Query 5 — When to bring in extra people, and for what  ▶ REPORT, not a view
Not a native Plan view. It's a forecast on top of Q4 (load) + future-dated planned work, both of
which are thin today (no real estimates, only E1 is dated). Deliverable = a short forecast memo
once the sizing/dating pass is done. Flag to Rosy/Nancy as dependent on that pass.

## Query 6 — Core suite vs bespoke at a glance  ▶ NEW VIEW
View name: **"Core vs Bespoke"**
1. Filter → Label → is → (no filter; show all).
2. Group by → **Label** → the `core` and `bespoke` groups separate the portfolio.
   (Or set a colour rule: Label `bespoke` = a standout colour.)
3. Save as.
- bespoke currently = 5 issues incl. the PopUp Hotel "mirror moment" Nancy named.

## Investor-facing portfolio view
Use **"Portfolio — by client"** (Q1) cleaned to engagement bars only, scale = Quarters/Years,
hide assignee/status clutter. Share = Plan is visible to anyone on it; for an external snapshot,
export/screenshot the timeline (Plans has no public-publish, unlike a deck).

---

## Build path
- Playwright-driven build blocked this session (VPS browser locked + Jira SSO auth needed).
- Options: (a) drive via Playwright once the browser frees + Robert authenticates the session;
  (b) Nancy self-serves from these specs (she owns board hygiene). Fold into CUST Admin Guide §7.
