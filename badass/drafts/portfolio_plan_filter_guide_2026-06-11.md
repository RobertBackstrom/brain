# Portfolio Plan: filter-by-client guide + how it differs from the CUST boards

_For Robert, 2026-06-11. BADASS / CUST._

## Part 1 - Plan vs Boards (what you're actually looking at)

Your sidebar has two different kinds of thing, and they are NOT the same tool:

| | **Portfolio Board** (under "Plans") | **CUST - xxxx** (under the BADASS Customisation space) |
|---|---|---|
| What it is | An **Advanced Roadmaps Plan** (timeline / roadmap) | **Boards** (Kanban/Scrum) inside the CUST project |
| Organised by | **Time** - horizontal date bars | **Status** - vertical columns (To Do / In Progress / Done) |
| Scope | **Many projects at once** (CUST + legacy archived projects + a couple of boards) | **One project** (CUST only), each board just a different saved filter on the same issues |
| Answers | "*When* does each client's work happen across the year, what depends on what, who owns it" | "*What state* is each task in right now for this client" |
| Owns the data? | No - it's a lens over issues that live in the projects | No - also just a filtered view of CUST issues |
| Dependencies | Yes - draws lines between linked issues | No timeline dependencies |

**The one-liner:** the **boards** are your day-to-day "where is each task in the workflow" view. The **Portfolio Plan** is your planning/exec "when does it land and what blocks what" view. The five CUST boards are five saved filters over the *same* CUST issues (Per Client, Per Location, Templates, default, All). The Portfolio Plan sits above all of it and pulls from multiple projects into one timeline.

The name "Portfolio **Board**" is misleading - it's a Plan, not a board. That's just what it was named.

## Part 2 - Filtering the Portfolio Plan by client (with dependencies + owners)

Open **Plans -> Portfolio Board**. Everything below is in the plan's top toolbar / settings - it's all UI (there's no API for these view settings), so this is the manual path.

### A. Filter to one client
1. In the top toolbar, click **Filters**.
2. Open the **Component** filter and tick the client (e.g. `E1 Series`). The timeline collapses to just that client's issues.
3. Untick to go back to all. (Client = Component in CUST, so the Component filter *is* the client filter.)

### B. See every client grouped (instead of filtering one at a time)
1. Top toolbar -> **Group by** -> choose **Component**.
2. Now each client is its own collapsible band on the timeline. Collapse the ones you don't care about. This is usually nicer than filtering one client at a time.

### C. Turn on dependencies (the lines between tasks)
1. Click **View settings** (the sliders/gear icon, top-right of the plan).
2. Toggle **Dependencies** ON.
3. Lines now connect blocked/blocking issues.
   - Caveat: a dependency line only appears if the two issues actually have an issue **link** ("blocks" / "is blocked by") set. No link = no line. If lines are missing, the links aren't there yet, not a display bug.

### D. Show who owns each item
1. Same **View settings** panel -> **Fields** (show/hide) -> enable **Assignee**.
2. The assignee avatar now shows on each bar.
   - Or **Group by -> Assignee** to reorganise the whole plan by owner. Note grouping is single-level: you can group by Component **or** Assignee, not both. So the usual setup is group by Component (client) and show Assignee as an avatar on the bars.

### E. Save it so Nancy doesn't redo this each time
1. With the filter + grouping + dependencies set how you want, use the **Views** dropdown (top-left of the plan) -> **Save as** -> name it (e.g. `By Client (all)`).
2. Optional: make one saved view per client (`E1`, `Show Jumping`, ...) each with the Component filter pre-set, so she switches clients with one click.

**Recommended default for Nancy:** one saved view = *Group by Component + Assignee shown + Dependencies on + scale Weeks/Months*. Then per-client saved views if she wants quick drill-down.

## Important caveat - empty bars = missing dates
Each client shows on the timeline via its **engagement epic** (`CUST-793..797 = ENGAGEMENT: E1 / Show Jumping / F1 VR / Blackbook / BMS`). A bar only renders if that epic has a **Start** (Target start, `customfield_10015`) and **Due** date. CUST-793 (E1) is dated; the other four were last seen waiting on dates from Nancy. So if a client's lane looks blank, the fix is filling Start + Due on its ENGAGEMENT epic, not a filter setting.

## Note on the archived clients (PFL, Racing Unleashed, WSX, Kiro)
Those live only in **archived** projects. Archived = excluded from Plans and from search entirely, so they will not appear on the timeline no matter how you filter. If you ever want them back, that's a separate consolidation job (unarchive -> bulk-move into CUST), not a view setting. Per your call, no change made there.
