---
name: Death Board feature state
description: Current Death Board server features, followup mental model, email scanning logic, dashboard behavior as of August 2026
type: project
originSessionId: 93fc1174-982b-4e98-904f-d5aa0584e5a7
---
## Followup Mental Model

A followup is NOT a task — it's a **connection node**. It links together:
- **VS Code sessions** where work happens (via ticket ID reference)
- **External agents** spawned from the dashboard (Execute button)
- **Incoming signals**: email threads, Discord chat entries, saved resources
- **Projects** in the workspace (`/home/assistant/projects/<folder>` on the VPS — see [[feedback_vps_operating_environment]]; this line said `C:\Users\johan\projects\` until 2026-08-17, a leftover from before the VPS migration)

The ticket ID (e.g. `eli-005`) is the handle Robert uses to pull on that thread from any context — in VS Code chat, on the dashboard, or in Discord.

**Why:** Robert thinks of the DB as a hub that connects work contexts, not a task tracker. Followups accumulate links and activity over time rather than being "completed."
**How to apply:** When building DB features, optimize for connecting contexts (sessions, mail, agents) rather than task management patterns. Don't add workflow/kanban features unless asked.


## WhatsApp ingest (db-086, live 2026-08-17)

The morning briefing has a **Phase 2.5 WhatsApp scan** between the Gmail scan and writing the
briefing, and `/process-deal-inbox` scans WhatsApp alongside Gmail. Scope is Robert-owned config at
`assistant/whatsapp-briefing-scope.json` (all DMs + event/industry groups; family/school denied;
groups matching nothing surface as "Unclassified groups" for filing rather than being dropped).

Tickets created from WhatsApp carry **`whatsapp_chat_id` + `whatsapp_msg_id`**, and `server.js`
dedups on `whatsapp_chat_id` exactly like `email_thread_id` — without it one nagging chat would mint
a fresh ticket every morning, since title-based `findDuplicate` loses to descriptive titles.
Deal snapshots land in `wiki/deals/raw/whatsapp/<chat_id>.md`, which is already a RAG-watched root.

**Why:** Robert does real biz-dev in WhatsApp; agents previously saw only half his correspondence.
**How to apply:** when adding any new ingest channel, add its stable-id dedup guard to `server.js` at
the same time as the scanning hook. See [[project_the_assistant]].

## Death Board Features (updated August 2026)

### Dashboard UI
- Ticket ID badges (e.g. `eli-005`) visible on every card, click to copy
- Status dropdown: icebox, backlog, planned, in progress, R&D, done, closed
- Default filter is "Active" — hides done items
- **Ask** button — writes question to `.assistant-inbox.jsonl`, polls outbox for response from The Assistant
- **Execute** button — writes task command to inbox, polls outbox (replaced headless agent spawning as of Apr 2026)
- Email link button when ticket has a Gmail thread
- Project folder mapping in config.json (`project_folders` section)

### Inbox/Outbox Message Queue (added Apr 2026)
- Kanban and Discord route all interactions through `.assistant-inbox.jsonl` / `.assistant-outbox.jsonl`
- The Assistant (persistent VPS Claude Code session) polls inbox and handles messages with full masterbrain context
- Eliminates headless agent spawning, removes Gemini API dependency, single billing model
- See `skills/assistant_inbox_workflow.md` for processing pattern
- Helper script: `assistant/inbox-handler.js` for programmatic and CLI access

### Email scanning (server.js)
- Scans ALL emails (inbox + archived), only trashed is skipped: `-in:trash newer_than:14d`
- No `is:unread` filter — reading on phone doesn't cause misses
- Filters out automated senders (noreply, devnet, mailer-daemon, notifications@, etc.)
- Deduplicates against existing followups by subject match
- Extracts explicit deadlines from email bodies (DD.MM.YYYY format)
- Auto-creates followups with correct due date and priority

### Receipt forwarding (daily 8 AM)
- Searches for receipts/invoices/kvitton in Gmail (last 2 days)
- Forwards to forward@fetch.pleo.io via gws +forward
- Archives originals (removes INBOX label)
- Tracks forwarded IDs in forwarded-receipts.json

### Sent mail scanning
- Scans `in:sent newer_than:14d` to detect replies Robert already sent
- Auto-closes matching followups when a sent reply is found

### Mark done → email enrichment
- When a followup is set to "done", server searches Gmail for related threads
- Logs all found emails into the followup's activity section

### New Project tab (`/new`)
- Web form at `board.runatyr.games/new` for starting projects from phone
- On submit: creates project folder, adds prefix to config.json, writes PROJECT_BRIEF.md, creates initial followup

### Discord Bot (`discord-bot.js`)
- Bot name: Death Board#3897, runs on "Deathboard" Discord server
- **Channels**: DEATH BOARD category (#briefing, #alerts, #inbox, #save, #done) + PROJECTS category (per-project channels)
- **Slash commands**: /overdue, /due, /done, /status, /new, /find, /briefing
- **Ticket-post actions (buttons, since 2026-07-14 · db-268)**: every ticket post carries a Discord button row - feed posts (#alerts/#brief, project channels) get `[✅ Done] [🔒 Close] [🗑️ Trash]`; #tasks embeds also get `[🔄 WIP] [⬜ Reopen] [🧠 Obsidian] [📌 Escalate]`. `customId=dbtask:<action>`, ID recovered from the message, owner-gated, `deferUpdate` then channel-send. Legacy **reactions** (checkmark → done, arrows → in progress, square → reopen, 🗑️ → dismiss) retained only for pre-button posts.
- **DM/inbox**: Type message to create followup with `[project:eli]` `[due:YYYY-MM-DD]` `[priority:high]` tags
- **#save**: Paste URL to queue for Claude processing

### Pages
- `/` — Dashboard (followup board)
- `/save` — Save resource (bookmark for Claude)
- `/new` — New project form
- `/wiki` — RAG knowledge search (added Apr 2026)
- Bottom nav on all pages: Board, Save, New, Filter, Stats

### Wiki / RAG knowledge index (Apr 2026, db-013)
- Local SQLite + sqlite-vec + FTS5; hybrid BM25 + voyage-3-large vectors fused via RRF, optional rerank-2.5.
- Sources indexed: skills/, memory/, agents/, assistant/followups/. Phase 3 will add Gmail (filtered labels) + all GDrives.
- Chokidar watcher (30s debounce) keeps the index live. Denylist for `secrets_registry.md`, `*-credentials.json`, `.env*` (path+title indexed, content not stored).
- Three surfaces: `/wiki` (gothic UI), `/api/wiki/{search,sources,doc}` HTTP, `mcp__rag__*` MCP tools (pre-approved across user + project settings).
- See `assistant/rag-{indexer,config,schema}.js`, `mcp-rag.js`, `wiki.html`. Voyage key in `.env` as `VOYAGE_API_KEY` (registry: `voyage.rag-embeddings`).

### Kanban redesign — epic-as-column + structured Q&A (May 2026, db-098)

**Column model:** Each `type: epic` ticket = one column (~30 today). Tickets inside grouped by status section (In Progress / Planned / Backlog / Icebox / Done / Closed). Done/Closed/Icebox sections collapsed by default; Backlog visible. Done/closed/empty epics auto-collapse to narrow strips on the right.

**Column ordering:** most-recently-touched (`meta.updated`) first → empty auto-collapsed → done/closed (rightmost). Recompute on every render.

**Orphan handling:** tickets with no `parent:` (62% of corpus pre-redesign) auto-render under `<prefix>-000-epic` at render time — no file edits. Tickets whose project lacks a `-000-epic` land in a single "Unparented" column on the right edge of active.

**Drag-and-drop:** drag = reparent (PUT /api/followups/:id/parent), NOT status change. Status changes via menu only. Epic cards are non-draggable.

**Canonical statuses (6, dropped rnd):** `icebox, backlog, planned, in_progress, done, closed`. Migration mapping: open/new/queued→backlog, scheduled→planned, active/testing/rnd→in_progress, blocked/awaiting_reply/waiting→in_progress + needs_input, complete/merged→done, moved→closed.

**Structured Q&A on tickets:** `meta.questions[]` array (YAML frontmatter), each entry `{id, q, a, asked_at, asked_by, answered_at}`. One row per question in the detail panel with its own answer textarea. Per-Q "Extract → new ticket" button. "Add question" button for Robert-authored questions. `meta.needs_input` derived: `questions.some(q => !q.a && q.asked_by !== 'robert')` (legacy explicit flag retained for backward compat). Replaces the wall-of-text "Claude needs your input" banner.

**Endpoints (all behind a per-ticket write-mutex `withTicketLock`):**
- `PUT /api/followups/:id/parent` — drag reparent
- `POST /api/followups/:id/questions` — add Q (body: `{q, asked_by}`)
- `PUT /api/followups/:id/questions/:qid/answer` — answer Q (body: `{a}`)
- `POST /api/followups/:id/questions/:qid/extract` — split Q into new ticket (inherits parent/prefix/priority)

**Agent IPC:** `ipc-helper.js` keeps the `askQuestion(cardId, q)` / `pollAnswer(cardId, qid)` API but internals swapped from `.question`/`.answer` file drops to HTTP against the structured-questions endpoints. Server still bridges any legacy `.question` file drops via `startIpcWatcher` → `addQuestion` for backward compat.

**Filters:** kept needs_input/overdue/has_draft view dropdown. Replaced project dropdown with horizontally-scrollable epic chip multi-select. Added "Me only" toggle (owner === robert).

**YAML parser:** swapped from 6 hand-rolled scalar-only copies (server.js, agent-registry.js, session-end.js, rag-indexer.js, migrate-statuses.js, backfill-tasktype.js) to one shared `assistant/frontmatter.js` using `js-yaml` with CORE_SCHEMA (dates stay strings, not coerced). Round-trip stable on all 433 ticket files (verify-frontmatter-roundtrip.js).

**See:** `assistant/output_log.md` (2026-05-02 entry), `db-098-kanban-redesign-epic-as-column-structured-q-a`, `/home/assistant/.claude/plans/moonlit-toasting-stallman.md`.
