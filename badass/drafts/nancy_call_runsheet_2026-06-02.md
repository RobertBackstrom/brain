# Run-sheet — Nancy "show & tell": build the 3 Portfolio Board views

**Internal — Robert drives the call. ~20 min. Do NOT send to Nancy (the client-facing how-to is section 7 of the CUST Admin User Guide).**

Goal: build all three views live with Nancy so she owns them. Plan 34 = https://badass-studios.atlassian.net/jira/plans/34

---

## 0. Before the call (2 min, solo)
- Open Plan 34, confirm it loads and pulls CUST.
- Confirm the 5 engagement epics exist: search `project = CUST AND labels = client-engagement` → should return **CUST-793 (E1, dated)** + 794/795/796/797 (undated). These feed View 1.
- Have the other 4 clients' rough engagement windows in mind in case Nancy doesn't know them off-hand (E1 is the only one with dates today).

## 1. Frame it (1 min, say this)
"Three views, all on this one board. I'll build each one with you so you can do it yourself after. The board's already on the right plan, and I've pre-loaded the client bars - we just need to switch the views on."

---

## 2. View 1 — Client Timeline (engagement length) — ~6 min

**Build:**
1. Top-left **view selector** → **Create view** → name it **Client Timeline**.
2. **Filters** (toolbar) → **Label** → tick `client-engagement`. (Now only the 5 engagement bars show - no task clutter.)
3. **Group by** → **Component**.
4. Timeline scale (top-right) → **Quarters**.
5. **Save view**.

Only **E1** has a bar right now (runs to end of 2028). That's the cue for the hands-on bit:

**Hands-on with Nancy (this is the "help" she asked for):**
6. Click **CUST-794 (Show Jumping)** in the plan → set **Start date** + **Due date** inline (the engagement window). Repeat for **F1 VR (795)**, **Blackbook (796)**, **BMS (797)**.
7. **IMPORTANT:** edits are staged in the plan sandbox. Click **Review changes** (top-right) → **Save selected** → confirm. *Until you do this, the dates don't reach Jira and the bars won't stick.*
8. Each client now shows its own bar = relationship length. Done.

> If Nancy doesn't have dates for a client: leave it, the bar appears whenever she fills them. No harm.

---

## 3. View 2 — Dependencies / blocking — ~4 min

**Build:**
1. View selector → **Create view** → name it **Dependencies**.
2. **Settings** (gear, top-right) → **Dependencies** → set to **Lines**.
3. Group by **Component** (or Epic).
4. **Save view**.

**Say this (manage the expectation):** "This one's wired but near-empty on purpose - it only draws a line once someone marks a blocker, and almost nothing's linked yet."

**Show her how to create a link so she can coach the leads:**
5. Open any ticket → **Link** → **is blocked by** → pick the blocking ticket. Back on the board, the arrow appears.
6. Ask: get the leads to start tagging blockers on the **E1 Miami** work (CUST-743 area). It fills in within a sprint or two.

> Note: this is about issue *links* (blocks / is blocked by), not the new "Blocked" status Sezar added - different things. The status parks a ticket; the link draws the arrow.

---

## 4. View 3 — Workload per person — ~4 min

**Build:**
1. View selector → **Create view** → name it **Workload by person**.
2. **Filters** → **Label** → **exclude** `client-engagement` (so the 5 engagement markers don't count as work on someone's plate).
3. **Group by** → **Assignee**.
4. **More / Colour** → colour **by Component** (bars colour-coded per client).
5. (Optional) Filter by **Location** to focus a venue.
6. **Save view**.

**Say this:** "Now you see everyone's load across all clients and venues - overload and spare room jump out. Heads up, it counts work items, not hours. If we start putting time estimates on tickets, this turns into real capacity planning."

---

## 5. Wrap (1 min)
- All three live under the **view selector** - she flips between them.
- The how-to is in the **CUST Admin User Guide, section 7** (same doc/link she has).
- Three follow-ups to leave her with:
  1. Fill start/end on any client engagement epics she skipped.
  2. Leads start logging "is blocked by" on live work.
  3. Longer-term: time estimates on tickets → real capacity view.

## Likely questions (quick answers)
- *"Why only E1 on the timeline?"* → others need dates; we add them now (step 2.6).
- *"Why's the blocking view empty?"* → links aren't logged yet; here's how (step 3.5), then the leads keep it up.
- *"Can it show hours / who's over capacity in hours?"* → not yet, needs estimates on tickets; today it's item count.
- *"Can we add ExtremeH / PFL?"* → when they're live engagements: add a client Component + one `client-engagement` epic with dates. Same recipe.
- *"Do my date edits save automatically?"* → no - Review changes → Save (step 2.7). Easy to forget.
