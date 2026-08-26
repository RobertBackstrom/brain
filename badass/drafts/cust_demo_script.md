# CUST demo — 15-minute walkthrough for Nancy

Step-by-step script for Robert to dry-run before the call. Times are a guide, not a stopwatch.

## Before the call — open these tabs

1. CUST summary — https://badass-studios.atlassian.net/jira/software/c/projects/CUST/summary
2. Templates board (957) — https://badass-studios.atlassian.net/jira/software/c/projects/CUST/boards/957
3. CUST-1 (AR Live Broadcast template) — https://badass-studios.atlassian.net/browse/CUST-1
4. CUST-63 (the pilot spawn) — https://badass-studios.atlassian.net/browse/CUST-63
5. The Create dialog (just know where the "Create" button is)

Screen-share the Jira tab. Have this script on a second screen.

---

## 0:00-2:00 — The why (set the frame)

Say, roughly:
- "Before this, the customisation team had six separate per-client Jira projects, and location was tracked in free-text labels - which kept breaking boards every time someone typo'd 'Dubrovnik'."
- "CUST replaces all of that with one project. Show the CUST summary tab."
- "The whole point: one place, consistent structure, and new race venues spin up in seconds instead of hand-typing 20 tickets."

## 2:00-6:00 — How work is structured

Open the **Create** dialog (or any CUST issue) and point at the fields:
- "Every ticket carries two Components - the **Client** (E1 Series, F1 VR, Blackbook...) and the **Type** of work (AR Live Broadcast, AR App, Environment...)."
- "**Location** is now a dropdown, not a label - Dubrovnik, Como, Monaco. This is what stops the typo problem."
- "Plus **Fix Version** for the season and **T-shirt Size** for rough effort."

Then the boards (left nav → Boards):
- "Same work, sliced two ways - **Per Client** and **Per Location**. Pick whichever view you need."
- "And the **Templates** board, which is the clever bit - next."

## 6:00-11:00 — The template engine (the centrepiece - spend time here)

Open the **Templates board (957)**:
- "Nine template Epics, one per type of work. These are masters - nobody works them directly."

Open **CUST-1 (AR Live Broadcast)**:
- "This is the full 20-step live-broadcast checklist - camera rig, calibration, fibre test, the lot. Built once, correctly."

Open **CUST-63 (the pilot)**:
- "Here's what happens when we spin up a venue. I ran a test: picked the Course Explainers template, and it cloned the whole checklist into a new location epic - 4 stories, every one already tagged with the location and components. Zero hand-typing."
- "So the PM workflow becomes: create one epic, set four fields, and the checklist appears. That's the entire intake for a new venue."

## 11:00-14:00 — What's next

- **Migration:** "Next we bring the live E12026 work into CUST. We'll do it in two passes - the dormant and non-Dubrovnik work first, then the live Dubrovnik tickets *after* the race, so nothing gets re-keyed while the team is mid-prep."
- **Automation:** "Right now I run the template clone on request. It can be wired as a hands-off Jira rule - there's a spec ready when you want it."
- **Your dashboard ask:** "The all-projects timeline - I'm scoping that, will come back with options this week."

## 14:00-15:00 — Questions

Likely questions from Nancy, and the answers:

- **"How do I add a new venue or client?"** → Ping Robert/PM - new Location values and Client components go through one person on purpose, so the dropdowns stay clean.
- **"What happens to the old E12026 board?"** → Archived read-only after migration. Nothing lost.
- **"Can the team see CUST now?"** → Nancy can (just granted). The wider team gets access at migration.
- **"When is the migration?"** → Two passes; live Dubrovnik tickets move after the 12-13 June race.
- **"Who owns keeping the templates correct?"** → Each type has a content owner (Alex, John, Ben, Marco, Jake...); they review after each race week.

---

## Note for Robert

CUST-63 is currently named "ZZ PILOT TEST - Course Explainers (delete after verify)". For the demo it reads cleaner if renamed - say the word and I'll rename it to something like "Sample spawn - Course Explainers" before the call. Or just present it as "a test I ran", which is honest and fine.
