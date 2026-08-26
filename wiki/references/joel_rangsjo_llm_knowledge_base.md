---
title: "Joel Rangsjö - LLM Knowledge Base (Karpathy-inspired)"
source: linkedin
author: Joel Rangsjö
date: 2026-04-11
tags: [rag, knowledge-management, obsidian, mcp, claude-code]
url: https://www.linkedin.com/posts/joel-rangsj%C3%B6-408342134_jag-jobbar-p%C3%A5-en-grej-en-grej-som-kr%C3%A4ver-share-7448072452695375872-5Orc
repo: https://github.com/Pluggentipsar/llm-knowledge-base
---

# Joel Rangsjö's LLM Knowledge Base

Inspired by Andrej Karpathy's "LLM Knowledge Bases" concept. Everything stored as text files in folders, AI organizes them into a personal wiki.

## Architecture

### Collection Phase
- Raw materials (PDFs, articles, videos, notes) go into a `raw/` folder
- Obsidian Web Clipper captures articles automatically
- Custom MCP service syncs content daily from LinkedIn, YouTube, and podcasts

### Research Phase
- Claude Code searches five academic databases simultaneously: OpenAlex, CrossRef, arXiv, Semantic Scholar, and DIVA Portal
- Microsoft's markitdown converts PDFs and Word documents to markdown
- Results include author names, abstracts, and relevance scores
- Integration with Zotero for reference management

### Compilation Phase
- AI processes raw material to create summaries and concept articles with interconnected links
- Chronological logging tracks all activity
- Weekly health checks identify gaps and inconsistencies

### Access
- Obsidian interface with Graph View visualization
- GitHub synchronization across devices
- Mobile capture syncs to knowledge base by morning

## Key Insight

The system creates a feedback loop where each query and saved article strengthens the knowledge base over time. Very similar to our own RAG + skill graph architecture.

## Relevance to Our System

Parallel approaches worth noting:
- Their `raw/` folder = our Death Board intake (LinkedIn posts, articles sent to DB)
- Their Obsidian + Graph View = our skill graph with wikilinks
- Their MCP service for daily sync = our rag-external-indexer (Gmail, GDrive)
- Their weekly health checks = our weekly ticket review + setup sanity audit
- Their Claude Code academic search = potential expansion for our RAG sources
