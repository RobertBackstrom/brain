---
name: Deal Wiki Schema
description: Schema and workflows for the AI-maintained deal tracking wiki. Read this when running any /ingest-deal-email, /process-deal-inbox, /lint-deals, or /digest-deals command.
type: schema
status: phase-4-first-ingestion
---

# Deal Wiki — Schema & Workflows

Self-maintaining wiki for biz-dev deal tracking. Pattern: Karpathy LLM Wiki (April 2026). Layered on top of the existing RAG index (`assistant/rag.db`) — files here become a new `wiki` source alongside `skills/`, `memory/`, `agents/`, `followups/`, `gdrive`, `gmail`.

## Core principle

> "Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase."

You (the LLM) own everything under `deals/`, `contacts/`, `projects/`, and `_index.md`. You never modify anything in `raw/` — those are read-only sources. Robert never edits files under `deals/`, `contacts/`, `projects/`, or `_index.md` directly; if he wants to correct something, he tells you and you update.

## Folder layout

```
wiki/deals/
├── CLAUDE.md           ← this file (schema + workflows)
├── _index.md           ← dashboard you maintain (pipeline state, hot/cold prospects, recent activity)
├── raw/                ← READ-ONLY source material (you never write here)
│   ├── gmail/          ← email thread snapshots (one .md per thread, named <thread_id>.md)
│   ├── meetings/       ← meeting notes, Gemini summaries, call transcripts
│   ├── contracts/      ← contract PDFs (referenced by path; PDF body extracted by RAG indexer)
│   └── web/            ← web research, LinkedIn posts, articles about prospects
├── deals/              ← AI-maintained deal pages, one per company (lowercase-kebab.md)
├── contacts/           ← AI-maintained person pages, one per individual (firstname-lastname.md)
└── projects/           ← AI-maintained pipeline pages, one per biz-dev project (elias.md, striden.md, etc.)
```

## Page types

### Deal page (`deals/<company-slug>.md`)

One per prospect company. Auto-updated when new sources reference the company.

```markdown
---
type: deal
company: <full company name>
slug: <company-slug>
project: <bizdev project this deal belongs to — elias / striden / blue_scarab / knives_and_gutters / etc.>
status: <New | Contacted | Interested | Demo Scheduled | Evaluating | Won | Lost>
priority: <high | medium | low>
country: <country>
size: <studio size — solo / small / medium / large / AAA>
last_activity: <YYYY-MM-DD>
network_strength: <warm | medium | cold>
updated: <YYYY-MM-DD>
---

# <Company Name>

## Snapshot
One-paragraph summary: who they are, what they make, why they're a target, current temperature.

## Key People
- [[firstname-lastname]] — role, why they matter (links to contacts/firstname-lastname.md)

## Pipeline Status
Current status with date stamps. Status flow: `New → Contacted → Interested → Demo Scheduled → Evaluating → Won/Lost`.

- 2026-04-15: Status changed to Contacted (source: [[raw/gmail/<thread_id>]])
- 2026-04-22: Status changed to Interested

## What They Bring / What We Bring
Specific hooks. What this prospect needs that we can supply, and what we need from them.

## Activity Log
Reverse-chronological. Each entry cites its source.

- 2026-04-22 — Kristofer replied with availability for demo. Source: [[raw/gmail/abc123]]
- 2026-04-15 — Initial outreach sent. Source: [[raw/gmail/xyz789]]

## Open Questions / Next Actions
- [ ] Follow up on demo scheduling (target: 2026-04-30)
- [ ] Confirm budget cycle alignment

## Cross-links
Other deal pages or contact pages that reference this one. You maintain these via /lint-deals.
```

### Contact page (`contacts/<firstname-lastname>.md`)

One per individual. A person can be referenced by multiple deals (e.g., a contact who left Studio A for Studio B).

```markdown
---
type: contact
name: <Full Name>
slug: <firstname-lastname>
current_company: <company at time of last update>
role: <current role>
linkedin: <URL or "—">
email: <email or "—">
warmth: <warm | medium | cold>
updated: <YYYY-MM-DD>
---

# <Full Name>

## Role
Current role, prior roles. Career history relevant to deal context.

## Relationship to Robert
How they know Robert, shared history, mutual contacts.

## Deals
- [[deals/<company-slug>]] — current relationship
- [[deals/<previous-company-slug>]] — historical (when they were there)

## Voice/Style Notes
How this person communicates. Tone preferences. Things to avoid in outreach. Updated as more correspondence accumulates.

## Activity Log
- 2026-04-22 — Replied positively to demo pitch
- 2026-04-15 — Cold connect via Robert's network
```

### Project pipeline page (`projects/<project-slug>.md`)

One per biz-dev project (Elias, Striden, Blue Scarab, Knives & Gutters, etc.). Holistic pipeline view.

```markdown
---
type: project_pipeline
project: <project slug>
client: <client name>
contract_window: <e.g. "Mar 1 – May 31 2026">
updated: <YYYY-MM-DD>
---

# <Project Name> — Pipeline

## Current State
Pipeline summary: total prospects per status, top 3 hot leads, recent wins/losses.

## Active Deals (by status)

### Demo Scheduled / Evaluating
- [[deals/<company-slug>]] — one-line current state

### Interested / Contacted
- [[deals/<company-slug>]]

### New (untouched)
- [[deals/<company-slug>]]

## Recent Activity (last 14 days)
Reverse-chronological cross-deal activity log.

## Strategic Notes
Project-level context: positioning, contract terms relevant to deal qualification, no-go targets, etc.
```

### Index dashboard (`_index.md`)

Single rolling dashboard. Auto-updated by /digest-deals weekly and after every /ingest-deal-email.

```markdown
---
type: dashboard
updated: <YYYY-MM-DD>
---

# Deal Wiki — Dashboard

## Pipeline Snapshot
| Project | Total | New | Contacted | Interested | Demo | Eval | Won | Lost |

## Hot This Week
Cross-project list of deals that moved status or had meaningful activity in last 7 days.

## Stale (no activity > 30 days)
Deals that need attention.

## Recent Wins / Losses
Last 30 days, with brief lessons-learned per loss.
```

## Workflows

### /ingest-deal-email <thread_id>

Fed a Gmail thread ID. Steps:

1. Fetch the thread via `mcp__gmail__gmail_thread` (or `mcp__claude_ai_Gmail__get_thread`).
2. Save a snapshot to `raw/gmail/<thread_id>.md` with frontmatter (subject, participants, dates) and full body. **Never modify after creation** — this is the source of truth.
3. Identify which company/companies the thread relates to. Match by domain, signature, mention.
4. For each affected company:
   - If `deals/<slug>.md` exists, update Activity Log, Pipeline Status (if changed), and any other relevant section. Cite the source as `[[raw/gmail/<thread_id>]]`.
   - If it doesn't exist, create the page using the schema above.
5. For each named individual in the thread:
   - If `contacts/<slug>.md` exists, update voice/style notes, role if changed, activity log.
   - If not, create the contact page.
6. Update the relevant `projects/<project-slug>.md` pipeline page.
7. Update `_index.md` (Hot This Week, Pipeline Snapshot if status changed).
8. Refresh cross-links: every newly-mentioned page should be linked from the others that reference it.

A typical /ingest-deal-email touches 3–8 pages.

### /process-deal-inbox

Triages anything in `raw/gmail/` that hasn't been processed yet (no corresponding update on a deal page).

1. List unprocessed thread snapshots.
2. For each, run the same logic as /ingest-deal-email.
3. If a thread doesn't relate to any existing deal, propose either: (a) create a new deal page, (b) tag as not-deal-relevant and leave alone.

### /lint-deals

Health check. No content changes — produces a report.

1. Stale deals: any `deals/<slug>.md` with `last_activity` older than 30 days, sorted by priority.
2. Broken wikilinks: every `[[wikilink]]` should resolve to a real file.
3. Orphan contacts: contacts not referenced by any deal page.
4. Status inconsistencies: deal page says one status, project pipeline says another.
5. Missing source citations: activity log entries without a `[[raw/...]]` link.
6. Suggested research gaps: companies mentioned in raw sources but no deal page yet.

Output: a markdown report. Do not auto-fix unless explicitly told to.

### /digest-deals

Weekly synthesis run.

1. Update `_index.md` Pipeline Snapshot table from current deal page frontmatter.
2. Compute Hot This Week (deals with activity in last 7 days).
3. Compute Stale list.
4. Recent Wins / Losses with lessons-learned extracted from deal page Activity Logs and Open Questions sections.
5. Write the updated `_index.md`. Cite specific deal pages.

## Hard rules

1. **Never write to `raw/`** except when creating a brand-new snapshot file in `/ingest-deal-email`. Once written, raw files are immutable.
2. **Never delete a deal or contact page**, even for lost/dead deals. Mark `status: Lost` and keep history. The compounding value depends on retained history.
3. **Cite every claim**. Activity log entries, status changes, voice notes — all link to the `[[raw/...]]` source. If no source, don't write the claim.
4. **One company per deal page**. Don't combine sister studios into one page even if owned by the same parent. Cross-link instead.
5. **Slug rules**: lowercase, kebab-case, ASCII only, no special chars. `Tegna AB` → `tegna-ab`. `10 Chambers Collective` → `10-chambers-collective`.
6. **Frontmatter is the contract.** Tooling reads frontmatter (especially `status`, `last_activity`, `project`). Keep it accurate; the human-readable body can be looser.
7. **Voice match.** Any text that might end up in a draft DM or email follows `skills/writing_voice_robert.md`. Internal notes (Snapshot, Activity Log) can be neutral analytical voice.
8. **Search before creating.** Before creating a new deal page, search the existing wiki + RAG to confirm it doesn't already exist under a different slug.

## Boundaries (MUST-ASK)

You can create, update, and link pages. You cannot:
- Send emails, post to LinkedIn, or contact prospects directly. That's MUST-ASK per `skills/autonomous_decision_framework.md`.
- Update the deprecated manual prospect trackers (`umbrella/<project>_bizdev/prospect_tracker.md`) — frozen read-only history as of 2026-05-21; the deal wiki is canonical.
- Mark a deal `Won` or `Lost` without an explicit source (email, contract, Robert telling you).

## Integration with existing system

- **RAG index**: every `*.md` file under `wiki/deals/` is indexed automatically by `assistant/rag-indexer.js` once `wiki` source is enabled in `rag-config.js`. Searchable via `mcp__rag__rag_search source=wiki project=<slug>`.
- **Manual prospect trackers** (`umbrella/<project>_bizdev/prospect_tracker.md`) are **deprecated as of 2026-05-21** — the deal wiki is the single canonical pipeline source. Old trackers are frozen read-only for history; do not update them.
- **BizDev agent** uses this wiki via RAG search; doesn't write to it directly. Wiki maintenance is owned by the `/ingest-deal-email` etc. slash commands.

## Phase status

- **Phase 1** (scaffold): folder structure + CLAUDE.md schema + _index.md skeleton — ✅ shipped 2026-04-29
- **Phase 2**: `wiki` source added to RAG indexer — ✅ shipped 2026-04-29 (12 docs / 45 chunks indexed under `source=wiki` as of 2026-04-30)
- **Phase 3**: slash commands (`/ingest-deal-email`, `/process-deal-inbox`, `/lint-deals`, `/digest-deals`) — ✅ shipped 2026-04-29
- **Phase 4**: backfill — 🟡 in progress. First ingestions complete (Formula Drone, Arsenal Agency, AP project pipeline, 3 contacts, 3 raw gmail snapshots). Wider backfill from `umbrella/elias_bizdev/prospect_tracker.md` + gmail history pending Robert's go.
- **Phase 5**: soak + validation — ✅ complete 2026-05-21. The deal wiki is now the single canonical pipeline source; the manual prospect trackers are deprecated (frozen read-only). Cadence (`/lint-deals` + `/digest-deals`) — automation vs manual is still Robert's call.

## See also
- `skills/prospect_tracker_enrichment.md` — manual CSV tracker format (deprecated 2026-05-21 — historical reference only)
- `skills/writing_voice_robert.md` — voice rules
- `skills/autonomous_decision_framework.md` — what's CAN-DO vs MUST-ASK
- `agents/bizdev.md` — BizDev agent (consumes wiki via RAG)
- `assistant/followups/gen-213-someone-built-a-self-improving-knowledge-system-in.md` — origin ticket
