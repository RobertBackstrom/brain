---
name: Agent Registry System
description: Named agents with cross-project learnings live in agents/ -- 16 as of 2026-07-22, incl. PM, Content Editor, Analytics, BizDev, GameDev, DevOps, Lawyer, CorpBot, The Author (voice pass), The Reviewer (substance pass)
type: project
originSessionId: a741bd10-9dc6-4a08-988d-6aad3e576458
modified: 2026-07-22T18:43:37.325Z
---
## What
CZP uses a named agent system at `agents/` in the project root. Each agent has:
- A definition file (`agents/<name>.md`) with role, rules, tools
- A learnings file (`agents/memory/<name>_learnings.md`) that accumulates across all projects

## Active Agents
- **PM** -- sprint planning, estimation, ticket mgmt (BADASS, K2C, GFF)
- **Content Editor** -- video/image editing, social posting (ToA, SWA, DBL)
- **Analytics** -- Steam data, sales reports, KPI dashboards (SalesInsights, all)
- **BizDev** -- prospect research, pipeline management, outreach drafts, event prep, deal tracking (Elias, Striden, BSC)
- **GameDev** -- engine MCP integration, dev workflow (BADASS, K2C)
- **DevOps** -- Death Board platform dev, infrastructure, agent tooling, MCP setup (DB, all)
- **UIbot** -- UI/UX for the Death Board kanban/board UI (`assistant/kanban.html`) and adjacent web surfaces (DB, all). NB: the Hive/cc-hive it originally owned was retired 2026-06-21 (db-223); the canonical surface is now the kanban.
- **CorpBot** -- corp admin, accounting, invoicing, contracts (CZP, Runatyr, AP)
- **Lawyer** -- Swedish corp/tax/employment/IP law, contract review (all)
- **Index** -- GDrive + VPS asset lookup API for other agents (all)
- **Lister** -- secondary-market listing automation (Personal Listings)
- **ArtDirector** -- logo & key-art briefing, AI concepting, Fiverr scouting (Knives & Gutters dry-run, all)

Source of truth is `/home/assistant/projects/agents/_registry.md` — this list can drift; check the registry file when in doubt.

## Why
Cross-project learning: when the PM agent learns from BADASS that "XR story points are 2x initial estimates," that knowledge automatically benefits K2C work. Skills = textbook knowledge, agent learnings = professional experience.

## How to apply
When a task maps to an agent role, read `agents/_registry.md` first. CLAUDE.md has the full protocol. After work, always write learnings back.

## GitHub repos explored (April 2026)
Key references for future agent improvements:
- CrewAI (crewaiinc/crewai) -- patterns borrowed for role definitions and memory
- VideoDB Director (video-db/Director) -- potential clip-indexer upgrade, has MCP server
- LangChain social-media-agent -- human-in-the-loop content approval
- Sales outreach automation (kaymen99) -- lead qualification patterns for BizDev agent
