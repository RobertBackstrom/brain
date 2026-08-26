# CUST - Admin User Guide

A short reference for running the BADASS Customisation (CUST) project in Jira. Skim the section you need.

## 1. How CUST is organised

One Jira project holds all customisation work. Every ticket is tagged five ways:

- **Client** - a component: E1 Series, Show Jumping, F1 VR, Blackbook, BMS
- **Type** - a component: AR Live Broadcast, VR Live Broadcast, AR App, Environment Production, Course Explainers, UEFN, Steam-Console, Format Explainer, XR Headset
- **Location** - a dropdown field: Dubrovnik, Como, Monaco, and so on
- **Fix Version** - the season, for example E1 2026 S3
- **T-shirt Size** - rough effort, XS to XL

Work sits under **Epics**. A Location Epic is one work-type at one venue, for example "AR Live Broadcast - Monaco".

Open the project: [CUST in Jira](https://badass-studios.atlassian.net/jira/software/c/projects/CUST).

## 2. The boards

| Board | What it shows | Open |
|---|---|---|
| CUST - All | Every ticket. Scrum board - carries the backlog and sprints. | [Open board](https://badass-studios.atlassian.net/jira/software/c/projects/CUST/boards/954) |
| CUST - Per Client | Work grouped by client. | [Open board](https://badass-studios.atlassian.net/jira/software/c/projects/CUST/boards/955) |
| CUST - Per Location | Work grouped by venue. | [Open board](https://badass-studios.atlassian.net/jira/software/c/projects/CUST/boards/956) |
| CUST - Templates | The master checklists. Reference only - never work these directly. | [Open board](https://badass-studios.atlassian.net/jira/software/c/projects/CUST/boards/957) |

## 3. Spin up a new location

The everyday task - cloning a template checklist into a new Location Epic:

1. Create an Epic in CUST.
2. Set five fields: Client component, Type component, Location, Fix Version, Template Source.
3. Save. **If the section-6 flow is switched on**, the template's task list clones in by itself about 30 seconds later, each task pre-tagged. If the tasks don't appear within a minute, the flow isn't live yet - see the note below.
4. Per ticket afterwards: set assignee, due dates, and any venue-specific detail.

**The auto-clone in step 3 only works once the section-6 flow is built and on** (it is, as of 2026-06-12). If nothing clones, check the flow's Audit log (section 6) - or ask the PM to run the clone by hand in the meantime.

## 4. Add a new Location or Client

Only when a genuinely new venue or client appears - not for every epic. Keep this with one person so the dropdowns stay clean and typo-free.

- **New Location:** Settings → Issues → Custom fields → open "Location" → edit options → add the value.
- **New Client:** Project settings → Components → add a component, named for the client.

The new value is then selectable on every ticket.

## 5. Filters and boards

**A filter** is a saved search - for a slice you want to look at.

1. Run an issue search and build the query.
2. Save as → name it "CUST - (slice)" → share it with the team, not private.
3. Find filters again under **Filters** in the left nav, not under the project. Star the ones you use.

A filter opens as a list.

**A board** is a filter plus columns - for a workflow you want to work in.

1. Make and share a filter first (above).
2. Create → Board → Kanban or Scrum → "from an existing saved filter" → pick it.
3. Set the board Location to the CUST project. This is what places it in the left menu with the other CUST boards. Miss it and the board lands in your personal space.
4. Tune it in Board settings: Columns, Swimlanes (by Epic gives one lane per work-type), Quick filters.

Rule of thumb: a filter for a slice to look at, a board for a workflow to work in. Each new board is a permanent line in the menu, so add one only when the team needs a focused shared view.

### Slice a board by client or venue (quick filters)

A **quick filter** is a one-click chip at the top of a board that narrows it on the fly - the right tool for "show me just Monaco" or "just E1". Add them in **Board → ••• → Board settings → Quick filters → Add quick filter** (name + JQL):

- **Per client** (on the Per Client board): name `E1 Series`, JQL `component = "E1 Series"` - repeat per client.
- **Per venue** (on the CUST - All board): name `Monaco`, JQL `labels = Monaco` - repeat per venue.

Venue slices run off the **label** (`labels = Monaco`), not the Location field, because boards sort/filter on labels. When you spin up a new venue (section 3), the spawn flow sets that label automatically; add a matching quick filter once and it's a permanent chip.

Already-made shortcuts: there's a shared saved filter per client and venue named **"CUST Client - …"** and **"CUST Venue - …"** (under Filters in the left nav) - star the ones you use to open any slice as a list in one click, without touching board settings.

## 6. One-time setup: the spawn flow

This is the automation that makes section 3 self-serve. Jira's newer automation UI calls it a **flow** (older screens/docs say "rule" - same thing). Build it once. It's already live in CUST as of 2026-06-12; these steps are for rebuilding or adapting it.

> **[Screenshot slot: the finished flow on the canvas - trigger → 3 conditions → edit → branch → create]**

**Getting to the right place:** the automation page is buried in the admin menus, so paste this straight into your browser address bar:

> https://badass-studios.atlassian.net/jira/software/c/projects/CUST/settings/automate

That opens CUST's automation page. Click **Create flow → Create from scratch**. (Skip the "Try these flows" / Rovo templates. Don't use the top-right gear → System - that's global config, not this.)

> **[Screenshot slot: Create flow dropdown → Create from scratch]**

Build the steps in order. After the trigger, each new step is added via the **+** below the previous one. Pick **"Skip tour"** on any popup.

**1. Trigger - "Work item created".** In the trigger picker, use the **search box** (the list is long and alphabetical - type "Work item created").

**2-4. Three conditions** - each one is a **"Work item fields condition"** (**+ → Condition → Work item fields condition**):
- **Work type** `equals` **Epic**
- **Template Source** `is not empty`
- **Summary** `does not contain`, value `TEMPLATE:`  *(keeps the flow off the master templates)*

> **[Screenshot slot: the three conditions stacked on the canvas]**

**5. Action - "Edit work item"** (tags the Epic with its venue label). **+ → Action → Edit work item → Choose fields to set → Labels**, then in the value box type `{{triggerIssue.Location}}` and press Enter so it becomes a chip.
- Why: the team tags every venue issue **twice** - the **Location field** (you set it by hand) and a **label** of the same name. The boards and quick filters sort by the **label**, not the field, so this step is what makes "sort by location" work.

**6. Branch - "Branch flow / related work items"** (loops over the template's checklist). **+ → Branch → Branch flow / related work items**, then:
- **Type of related work items:** `JQL`
- **JQL** - paste exactly, quotes included:
  > project = CUST AND component = TEMPLATES AND issuetype = Story AND "Template Source" = "{{triggerIssue.Template Source}}"
- ⚠️ **UNCHECK "Only include work items that have changed since the last time this flow executed."** Template stories never change, so if this stays ticked the flow finds nothing on every run after the first.
- The **quotes** around `{{triggerIssue.Template Source}}` are required - the value has spaces (e.g. "AR Live Broadcast") and unquoted it's invalid JQL that matches nothing. The unchecked box and these quotes are the two things that silently break this flow.

> **[Screenshot slot: branch panel - Type=JQL, the JQL, the unchecked "changed since" box]**

**7. Inside the branch - Action "Create work item"** (clones each checklist task). Click the **+ that sits inside/under the branch** (indented - not the main trunk), then **Add an action → Create work item**. Set:

   | Field | Value |
   |---|---|
   | Space | Same space |
   | Work type | Story |
   | Summary | `{{issue.summary}}` |
   | Parent | `{{triggerIssue.key}}` |
   | Components | `{{triggerIssue.components.name}}` |
   | Fix versions | `{{triggerIssue.fixVersions.name}}` |
   | Labels | `{{triggerIssue.Location}}` |
   | Location | `{{triggerIssue.Location}}` |
   | T-shirt Size | `{{issue.T-shirt Size}}` |

   **Smart-value rule:** inside this branch, `{{issue.…}}` = the **template story** being copied, and `{{triggerIssue.…}}` = the **new Epic**. Use exactly as above - mixing the two is the most common mistake. (Custom fields like Location and T-shirt Size are under "Choose fields to set..." / "More options".)

> **[Screenshot slot: the Create work item field list - Story + all 8 fields]**

**8. Save and enable.** Click **Save and enable** (top-right). It then asks for:
- **Flow name:** `CUST: Spawn template Stories on new Location Epic`
- **Who can edit this flow:** change from **Private** to a shared option, so the team (not just the builder) can maintain it.
- Click **Turn on flow**. A disabled flow won't fire - it must be ON.

> **[Screenshot slot: the name + edit-permission dialog]**

### Test it (once)

1. Click **Create** and make an Epic in CUST: Summary `RULE TEST - delete me`, Components `E1 Series` + `Course Explainers`, Location `TBC`, Fix Version `E1 2026 S3`, **Template Source = `Course Explainers`**. Set Template Source **on the create screen** - the flow checks it the instant the Epic is created, so adding it later by editing won't fire the flow.
2. Save. Within ~30 seconds **4 Stories** appear under the Epic, each with both Components, Location `TBC`, label `TBC` and the fix version - and the Epic itself picks up the `TBC` label.
3. **Delete the test.** ⚠️ The spawned stories are owned by **"Automation for Jira"**, not you, so deleting them needs **Delete-all-issues** permission - i.e. you must be a member of the CUST **Administrators** project role. If the delete is greyed out / refused, you're not in that role; ask the project admin to add you.

If nothing clones: open the **Audit log** tab at the top of the automation page - it names the failing step. Usual culprits: the JQL missing its quotes, or the "changed since last execution" box left ticked.

## 7. Portfolio Board views

The [Portfolio Board](https://badass-studios.atlassian.net/jira/plans/34) is the cross-project timeline (Jira Plans). It already spans all of Customisation plus the other BADASS projects, so it's where the high-level, cross-client views live. The views below are created with the build steps shown; once saved, open any of them from the view selector at the top of the board.

### Client timeline (engagement length)

One bar per client, showing how long each engagement runs - the relationship, not the tasks underneath.

- It reads from a single "ENGAGEMENT: (client)" epic per client, tagged `client-engagement`, with a Start and Due date.
- E1 Series is set and runs to end of 2028. Show Jumping, F1 VR, Blackbook and BMS each have their engagement epic ready - set a Start and Due date on each and its bar appears.
- Open: view selector → "Client Timeline". [Build: Create view → filter to label `client-engagement` → group by Component → timeline scale Quarters.]

### Per-venue and per-client views (slice the timeline to one venue or client)

The quickest way to browse the timeline by a single venue or client. Each is a saved view built from one filter:

**A venue view** (e.g. "Venue - Monaco"):
1. **Filter** (top toolbar) → on the **Label** row, set the value to the venue (e.g. `Monaco`). The timeline collapses to that venue's epics + stories.
2. View selector (the "… ▾" next to the view name) → **Save as** → name it `Venue - <name>`. Use **Save as**, not plain Save - plain Save overwrites the view you're currently on.

**A single-client view** (e.g. "Client - E1 Series"): same steps, but instead of the Label row use **Add filter → Component → is → <client>** - clients are *components*, not labels. Save as `Client - <name>`. (For all clients at once, just use the existing "Client Timeline" view above.)

Good to know:
- Freshly spawned location epics show as **rows without bars** until they have **Start + Due** dates - the slice is right, the bars just need dating.
- A venue with little work (e.g. Bahamas = 1 epic) correctly shows little - that's a real "this venue is barely planned yet" signal, not a bug. Build it out via section 3 and it fills in here automatically.
- These views are UI-only (no API). They live on the Plan's view selector and are shared with everyone on the plan, so build a venue/client view once and the team has it.

### Blocking view (dependencies)

Shows what is blocking what, as lines between bars.

- A line only appears once a blocker is recorded on a ticket (on the ticket: Link → "is blocked by"). Add these on live work and the picture builds within a sprint or two. Good first target: the current E1 race work.
- Open: view selector → "Dependencies". [Build: Create view → Settings → Dependencies → Lines.]

### Workload per person

Shows how much each person has on, across every client and venue, so overload and spare room stand out.

- Grouped by assignee, colour-coded by client. It counts work items today; once tickets carry time estimates it can show true capacity in hours.
- Open: view selector → "Workload by person". [Build: Create view → group by Assignee → colour by Component → filter out the `client-engagement` markers so they don't count as work.]

### Keeping the views useful

1. Set Start and Due dates on the four client engagement epics that don't have them yet (Show Jumping, F1 VR, Blackbook, BMS).
2. Ask the leads to log "is blocked by" links on live work so the blocking view fills in.
3. Add time estimates to tickets over time to unlock real capacity planning.

---

*Maintained by the PM. Last updated 2026-06-14.*
