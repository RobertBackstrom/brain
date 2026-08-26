---
name: Always preserve OG links from dump
description: When creating tickets from the Discord #dump channel (or any user-shared resource), always capture the source URL in the ticket frontmatter
type: feedback
originSessionId: 4419c454-16c5-4b51-9b30-fe44ab10e18e
---
When tickets are created from the Discord #dump channel, X bookmarks, LinkedIn saves, or any other user-shared resource, the original URL must be preserved in the ticket's frontmatter (e.g., `source: https://...`).

**Why:** Robert reviewed gen-120 and asked "is there a link to the OG post" -- the ticket title referenced a LinkedIn post by Daniel Olmedo Nieto about a Google launch, but no URL was saved. Without the OG link, the research request becomes ambiguous and can't be acted on without going back to ask Robert.

**How to apply:**
- When intake processes a dump message, save the URL in the `source` frontmatter field
- When the URL is in the message itself, parse it out
- When creating tickets manually from emails/screenshots, ask for or infer the source URL
- Display the link prominently in the kanban/board ticket detail view (the Link icon button uses this)
