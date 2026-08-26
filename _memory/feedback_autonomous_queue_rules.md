---
name: Autonomous queue processing rules
description: Rules for what Claude should do autonomously during scheduled 4am queue runs — process DB tickets without Robert's input
type: feedback
originSessionId: c5c9d0d8-ec34-463a-a129-295d61877ace
---
During scheduled queue runs (4am), Claude should also scan active DB tickets and do autonomous work. Rules:

### What Claude CAN do without asking:
- **Research**: Web searches, reading docs, summarizing articles, R&D ticket processing
- **Draft content**: LinkedIn posts, email drafts, content plans (never publish)
- **Check external state**: Gmail for replies, check if game DB listings exist, verify links
- **Code/tooling**: Build scrapers, update internal tools, fix DB dashboard code
- **Skill maintenance**: Update skill files, add missing sections, improve documentation
- **Prospect research**: Enrich trackers with public info, prep meeting materials
- **Data analysis**: Process reports, update sheets with available data

### What Claude must NOT do without Robert:
- Publish or send anything (social posts, emails, LinkedIn messages)
- Modify client systems (Jira boards, storefronts)
- Make spending decisions or commit to deadlines
- Close/resolve tickets that need Robert's sign-off

### How to process each ticket:
1. Read the full ticket including activity log
2. Read parent epic and related tickets
3. Check Gmail for relevant recent emails
4. Map to the right agent (PM, Content, Analytics, Outreach, GameDev)
5. Do the work, log activity to the ticket
6. If blocked on Robert's input, set needs_input: true with specific questions
7. Write agent learnings after completing work

**Why:** Robert wants maximum autonomous throughput. Many tickets sit idle because they need research or prep work that doesn't require his input. The 4am run should chip away at these so Robert wakes up to progress, not a stale board.

**How to apply:** During every scheduled queue run, after processing the regular queue, scan all in_progress/planned/backlog tickets and work on any that have autonomous work available. Prioritize by: overdue > high priority > oldest untouched.
