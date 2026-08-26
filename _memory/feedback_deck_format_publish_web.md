---
name: Publish slide decks to web by default
description: For any pitch/reference deck agents need to read, use Google Slides "Publish to web" as the default sharing mechanism
type: feedback
originSessionId: 807db031-95b3-4c3b-96f0-944ab455d70c
---
Default workflow for sharing slide decks with agents: **Publish to web.**

**Why:** Robert's pitches aren't sensitive enough to protect with private sharing friction. Publish-to-web gives agents a public URL + per-slide PNG export (`/export/png?pageid=<slide>`) which WebFetch and Playwright can consume directly. Updates auto-propagate.

**How to apply:**
- Default: `File → Publish to web` on any deck that needs agent consumption. Drop the link in the ticket.
- Exception (rare): if a deck IS sensitive (specific contract terms, financials, unreleased IP in a way that actually matters), gate it with email-access-required and add the gdrive MCP service account `service-account@claude-code-mcp-489713.iam.gserviceaccount.com` as a viewer.
- Don't propose PDF download workflows or "share with service account" as the default — publish-to-web is the standing preference.
