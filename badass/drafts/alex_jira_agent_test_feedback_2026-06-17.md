# Devsquad reply to Alex — Jira VS Code Agent test (2026-06-17)

Tested it - works well. Made a task and it walked me through project, location, epic, dates, component, version one at a time, then parented it to the right epic. Clean.

On your two questions:

1. It did NOT try to create an Epic at any point. The guardrails are solid - it only offers Task/Story and tells you to go to an admin if you ask for an Epic.
2. The epic recommendation is good - it filters by location, so for a Monaco task it offers the Monaco epics. Confirmed it parents correctly.

Two small things for the reference doc when you get a sec:

1. The component table in AGENTS.md has Game Client and Mobile AR App both as "(confirm in Jira)". Real components are there - Game Client = Steam-Console, Mobile AR App = AR App. Two-line fix:

   `| Game Client ... | Steam-Console | Unreal Engine (C++) |`
   `| Mobile AR App ... | AR App | Unity |`

   Happy to PR it if you add me as a collaborator (forking's off and I'm read-only right now), or just paste it in - your call.
2. Heads-up on a dead-end: if someone picks a location that has no epic yet (a brand-new venue), it tells them to ask an admin to make the epic first. Working as designed, just flagging so we know to pre-spawn a venue's epics before pointing people at it.

Nice work - this is going to keep the board clean.
