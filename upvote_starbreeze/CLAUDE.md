# UpVote Starbreeze — CLAUDE.md

## Engagement
- **Role:** Product owner / prototype builder for UpVote community hub
- **DB prefix:** `upv`
- **Status:** active
- **Agent owner:** PM (kickoff/scoping), DevOps (implementation)

## Key People
- **Daniel Mesonero** — Development Director, Starbreeze (closer to production side)
- **Matt Dixon** — Provided initial HTML prototype, Robert's contact at Starbreeze

## Infrastructure / Resources
- HTML prototype: `C:\Users\johan\Desktop\Starbreeze\faq2_2.html` (Matt's original)
- No Jira board yet (Starbreeze side)
- No GDrive folder yet

## Why
Robert is pitching a community hub tool to Starbreeze for PAYDAY 3. Combines an upvote-style forum (bug reports, ideas, questions) with an AI chatbot that speaks in PAYDAY character voice and handles FAQ + structured bug intake. First deliverable is a polished working prototype to demo in a pitch meeting.

## Scope Decisions (confirmed 2026-04-14)
1. **Scope:** Polished working prototype for pitch, not production tool yet
2. **Chatbot:** Real LLM agent (Claude API) with PAYDAY character tone of voice, handles FAQ
3. **Bug reporting:** Chatbot guides structured reports, exports to CSV. Jira integration as stretch goal (pattern from K2C/BADASS)
4. **Project name:** UpVote (confirmed)

## Tech Stack (prototype)
- Frontend: PAYDAY-themed dark UI with orange accents, military/heist language (based on Matt's HTML)
- Chatbot: Claude API with PAYDAY character system prompt
- Bug export: CSV download
- Backend: TBD during implementation planning

## Conventions
- Deliveries logged to `output_log.md`, drafts to `drafts/`
- Writing voice per `skills/writing_voice_robert.md`
- Never publish or send to Starbreeze without Robert's approval
