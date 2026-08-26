# Teams reply to Nancy — CUST Q&A

**Channel:** Teams DM
**Status:** Draft for Robert — answers Nancy's 7 questions (2026-05-21)

---

Hey Nancy, good questions. Going through them in order.

**Access** - bring the links that don't open to our call. My guess is it's a few tickets with issue-level security on them, not a general access problem. The migration clears that up either way.

**Cloning to a new location** - the one-click version is a Jira Automation rule: you create the Location Epic, set five fields (Client, Type, Location, Fix Version, Template Source), save, and the task checklist clones itself in about 30 seconds later, already tagged. I'd like you to own that rule - the build steps are in a short guide here: https://docs.google.com/document/d/1Yk_DJ8dsmudo1X6Z4_Y0MyL-u4N8a2ZyC41Ck2Oyz0E/edit (about 15 minutes in the UI), and I'll hop on a call to walk it through with you. Once it's yours you can adjust it whenever a template changes, with no bottleneck through me. Until it's live, ping me and I run the clone. What's pre-filled either way: every checklist task, components, Location, Fix Version, size. What you set per ticket after: assignee, due dates, anything venue-specific.

**Where boards appear** - a new Location Epic shows up automatically on CUST-All and Per Client. The Per Location board was built as a Dubrovnik-only pilot, so I'm rebuilding it as one board with a swimlane per location. New locations then show as their own lane.

**Single point of failure** - fair flag. The "one person" gate is only for adding brand-new dropdown values (a new Location, a new Client) - it stops the lists drifting back into the old typo mess. It doesn't gate everyday work: once the Automation rule is live, anyone can spin up a location. And for the rare "add a new value" job, you and Ben both have Jira admin - I'm writing a one-page runbook so either of you can cover it.

**Client variation** - templates are organised by work type (AR Live Broadcast, VR Broadcast, etc.), not by client. A client just uses whichever types fit. One thing I want to check: when you say different workflows, do you mean different task lists, or different status stages? Different task lists are handled - a spawned Epic's tasks are independent copies, so you add or trim freely without touching the master. Different status stages is a bigger change - one project runs one workflow today. Let me know which you meant.

**Sprints** - yes. CUST is a Scrum project, so CUST-All has a backlog and sprints. Per Client and Per Location are filtered views of the same tickets - a ticket in a sprint still shows on its client and location board. Sprint planning happens on CUST-All. Only open question is a team call: one shared sprint rhythm or looser per-client.

**Migration tickets without dates** - not a blocker. Tickets move with or without dates; the empty ones come across empty and get dated afterwards in CUST. Worth knowing the investor timeline needs dates to draw its bars, so dating those is part of the post-migration tidy-up.

Shout if any need more.

Robert
