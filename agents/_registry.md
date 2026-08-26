# Agent Registry

Central index of all named agents. Each agent accumulates learnings across projects.

## How to Use

1. When a task maps to an agent role, read the agent definition file first
2. Then read `agents/memory/<agent>_learnings.md` for cross-project knowledge
3. Then read the relevant project memory for project-specific context
4. After completing work, write any new learnings back to the agent's memory file

## Active Agents

| Agent | File | Role | Type | Projects |
|-------|------|------|------|----------|
| PM | [pm.md](pm.md) | Sprint planning, estimation, ticket management | On-demand | BADASS, K2C, GFF |
| Content Editor | [content_editor.md](content_editor.md) | Video/image editing, reel building, social posting | Both | ToA, SWA, DBL |
| Analytics | [analytics.md](analytics.md) | Steam data, sales reports, KPI dashboards | Scheduled + on-demand | SalesInsights, all |
| BizDev | [bizdev.md](bizdev.md) | Prospect research, pipeline management, outreach drafts, event prep, deal tracking | On-demand | Elias, Striden, BSC |
| GameDev | [gamedev.md](gamedev.md) | Engine MCP integration, build automation, dev workflow | On-demand | BADASS, K2C |
| DevOps | [devops.md](devops.md) | Death Board platform dev, infrastructure, agent tooling, MCP setup | On-demand | Death Board, all |
| UIbot | [ui.md](ui.md) | UI/UX design and implementation for the Hive and adjacent web surfaces | On-demand | Death Board (cc-hive), all |
| CorpBot | [admin.md](admin.md) | Corporate admin, accounting, invoicing, contracts, company secretary, corp comms | On-demand | CZP, Runatyr, Aurora Punks, all |
| Lawyer | [lawyer.md](lawyer.md) | Legal advisor — Swedish corp/tax/employment/IP law, contract review, redlines, drafting legal responses | On-demand | All |
| Index | [index.md](index.md) | GDrive + VPS asset index, query API for other agents (lookup by project/asset type/text) | Scheduled + on-demand | All |
| Lister | [lister.md](lister.md) | Secondary-market listing automation — photo intake, comp pricing, dual-listing to Tradera + eBay | On-demand | Personal Listings (later: TCG, Arbitrage, Miniatures) |
| ArtDirector | [artdirector.md](artdirector.md) | Logo & key-art briefing, AI concepting, Fiverr/freelance artist scouting | On-demand | Knives & Gutters (dry-run), all |
| Ticker | [ticker.md](ticker.md) | Market trends + trade ideas for SE/US gaming & tech equities; confirmation-gated execution of a small managed account (Saxo) | Both | Personal (Ticker account) |
| CM | [cm.md](cm.md) | Community manager — Discord onboarding, role-based channel access, invite hygiene, + Community Bot owner (cross-forum needs-response digest) | Scheduled + on-demand | Aurora Punks, all (Community Bot) |
| The Author | [the_author.md](the_author.md) | Voice editor — final-pass adaptation of near-final text so it reads exactly as Robert wrote it (channel + recipient aware). Other agents draft cheap; The Author does the short Fable voice pass. Owns the `skills/voice/` corpus. | On-demand | All (voice layer for every outward-facing message) |
| The Reviewer | [reviewer.md](reviewer.md) | Independent review pass — a strong second model (Fable) that gen-lyser a near-final work product against a domain lens (business case, legal, security, code) and returns an advisory memo. Other agents produce cheap; The Reviewer does the short adversarial Fable critique. Owns the `skills/review/` corpus. | On-demand | All (substance-review layer for consequential deliverables) |

## Review pass — route consequential deliverables through The Reviewer

Any agent (or the main Assistant) that produces a *consequential, near-final* work product — a
deal/business case, a contract or legal response, platform/webhook/IPC code, a pitch's numbers, a
go/no-go recommendation — can hand the *finished* artifact to **[The Reviewer](reviewer.md)** for
a short, adversarial second-opinion pass before it reaches Robert or a client. The Reviewer reads
to *refute*, ranks findings by severity, and returns an **advisory memo — it never blocks
delivery and never edits the work.** This keeps Fable (the expensive reasoning model) touching
only the finished artifact, not the long producing work. The Reviewer owns the `skills/review/`
corpus (per-lens rubrics). It is the substance sibling of The Author's voice pass — a
client-facing piece can want both. Sign-off stays with Robert (and, for legal, a real advokat).

## Voice pass — route final external copy through The Author

Any agent (or the main Assistant) that drafts an outward-facing message — mail, LinkedIn,
Discord, social, DM — should draft on its own normal/cheaper model, then hand the *near-final*
text to **[The Author](the_author.md)** for a short voice-adaptation pass before it reaches a
human. This keeps Fable (the expensive voice model) touching only the short final text, not the
long drafting. The Author owns the `skills/voice/` corpus (per-channel + per-person registers).
Skip the pass only for trivial internal text or where Robert asks to send as-is.

## Agent Types

- **On-demand**: Invoked during Claude Code sessions when Robert needs the expertise
- **Scheduled**: Runs autonomously on cron/webhook (like DB email scanner)
- **Both**: Has scheduled tasks but also invoked on-demand

## Learning Protocol

After completing a task, the agent should ask: "Did I learn anything here that would help me do this better next time, on any project?" If yes, append to `agents/memory/<agent>_learnings.md` with:
- The learning (what was discovered)
- Source project (where it was learned)
- Date (when)
- Category (estimation, process, tooling, client preference, etc.)
