# Teams message to Nancy — CUST walkthrough

**Channel:** Teams DM
**Status:** Draft for Robert

---

Hey Nancy, the new customisation project is scaffolded. Quick legend so you know what you're looking at.

**Project:** CUST "BADASS Customisation" - one project replacing the six per-client ones. https://badass-studios.atlassian.net/jira/software/c/projects/CUST/summary

**How work is tagged (every ticket):**
- **Component = Client** (E1 Series, Show Jumping, F1 VR, Blackbook, BMS)
- **Component = Type** (AR Live Broadcast, VR Live Broadcast, AR App, Environment Production, Course Explainers, UEFN, Steam-Console, Format Explainer)
- **Location** (dropdown: Dubrovnik, Como, Monaco, etc) - replaces the free-text labels that kept breaking boards
- **Fix Version = Season** (E1 2026 S3)
- **T-shirt Size** (XS-XL) for rough effort

**Boards:** "Per Client" and "Per Location" scope the work two ways. "Templates" board holds the master checklists.

**Template library:** the Templates board has 8 template Epics, one per Type, each with its standard task list (AR Live Broadcast has the full 20-step broadcast checklist). These are masters - don't work them directly. https://badass-studios.atlassian.net/jira/software/c/projects/CUST/boards/957

**Spinning up a new location:** instead of hand-typing 20 tickets, you pick a template from the Templates board (https://badass-studios.atlassian.net/jira/software/c/projects/CUST/boards/957) and it clones the whole checklist into a new Location Epic with everything pre-tagged. I piloted it on CUST-63 (a test Epic, ignore it) - it works. For now I run the clone on request; we can wire it as a hands-off Jira rule next.

**New venue or client?** Ping me and I'll add it. New Location values and Client components go through one person on purpose - that's what stops the dropdowns drifting back into the typo mess the old labels had.

**Next step - template scope + estimates.** Before we migrate the live E12026 tickets, each owner checks their template Epic: does it hold every ticket we actually need, anything missing or extra? Then they add a T-shirt size to each ticket. Owner links:
- AR Live Broadcast - Alex: https://badass-studios.atlassian.net/browse/CUST-1
- VR Live Broadcast - John: https://badass-studios.atlassian.net/browse/CUST-22
- AR App - Ben: https://badass-studios.atlassian.net/browse/CUST-40
- Environment Production - Marco: https://badass-studios.atlassian.net/browse/CUST-47
- Course Explainers - Jake: https://badass-studios.atlassian.net/browse/CUST-52
- UEFN: https://badass-studios.atlassian.net/browse/CUST-57 (no owner yet)
- Steam-Console - Sezar: https://badass-studios.atlassian.net/browse/CUST-60
- Format Explainer: https://badass-studios.atlassian.net/browse/CUST-62 (no owner yet, and still empty)

Nothing moves on E12026 until that's done and you and I both sign off. Have a look and tell me what feels off.

Robert
