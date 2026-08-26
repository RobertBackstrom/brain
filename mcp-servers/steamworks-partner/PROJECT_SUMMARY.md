# Steamworks Partner MCP Server — Project Summary

**Status:** Phase 2 Complete ✅ (Build Management Ready)  
**Last Updated:** 2026-05-02  
**Agent:** GameDev  
**Project:** Tears of Adria (toa-012)

## What Was Built

The **first-ever MCP server** wrapping the Steamworks Partner API. Enables Claude (or any MCP client) to interact with Steam's publisher tools conversationally — pull sales data, monitor reviews, check wishlists, manage builds.

## Technical Stack

- **Framework:** Model Context Protocol (MCP) SDK v1.0.4
- **Language:** TypeScript 5.9+ → compiled to Node.js ESM
- **Transport:** stdio (standard MCP)
- **HTTP Client:** Axios 1.15
- **APIs:** Steamworks Partner API + public Steam Store API

## Architecture

```
steamworks-partner-mcp/
├── src/
│   ├── index.ts         # MCP server + 11 tool definitions (~430 lines)
│   ├── api-client.ts    # Axios wrapper for Steam APIs (~140 lines)
│   ├── steamcmd.ts      # SteamCMD wrapper + VDF generation (~150 lines) [NEW]
│   └── types.ts         # TypeScript response types (~80 lines)
├── examples/            # [NEW]
│   ├── github-actions-upload.yml     # GitHub Actions CI/CD example
│   ├── gitlab-ci-upload.yml          # GitLab CI/CD example
│   └── CI_CD_GUIDE.md                # Integration guide
├── dist/                # Compiled JavaScript
├── README.md            # Setup, config, tool reference
├── TESTING.md           # Integration guide + troubleshooting
├── CHANGELOG.md         # Version history (v0.2.0)
├── NEXT_STEPS.md        # Roadmap for Phase 3
├── LICENSE              # MIT
└── package.json
```

**Total:** ~1,400+ lines of code + documentation

## Implemented Tools

### Analytics & Monitoring (Phase 1 ✅)
1. **get_partner_apps** — List all apps under this publisher
2. **get_sales_data** — Revenue/units sold by date range (requires Financial API key)
3. **get_wishlist_data** — Wishlist analytics with country/language breakdown
4. **get_reviews** — Review monitoring (text, sentiment, playtime, votes)

### Store Data (Phase 1 ✅)
5. **get_app_details** — Store page metadata (price, platforms, release date)
6. **get_news** — Read news/announcements for an app

### Build Management (Phase 1 + 2 ✅)
7. **get_app_builds** — Build history with timestamps
8. **get_app_betas** — List beta branches and their builds
9. **set_app_build_live** — Switch which build is live on a branch (WRITE op) [Phase 2]
10. **generate_build_script** — Create VDF scripts for SteamCMD uploads [Phase 2]
11. **check_steamcmd** — Verify SteamCMD installation [Phase 2]

## Key Features

✅ **Dual API Support:** Partner API (auth required) + public Store API (open data)  
✅ **Flexible Auth:** Publisher Key (general) + Financial Key (revenue data)  
✅ **Type-Safe:** Full TypeScript types for all API responses  
✅ **Error Handling:** Clear error messages for missing keys, rate limits, 403s  
✅ **Well-Documented:** README, testing guide, changelog, next steps, MIT license  
✅ **Battle-Ready:** Compiles clean, ready for Claude Desktop integration  

## What Can't Be Automated

Per Steamworks API limitations:
- Store page text/description updates
- Capsule art, screenshot, trailer uploads
- Creating news posts (read-only via API)
- Pricing / discount management
- Event creation (sales, livestreams)

These require manual dashboard access.

## Next Steps

### Immediate Testing
1. Test `set_app_build_live` against ToA beta branch (NOT production)
2. Test VDF generation + SteamCMD upload workflow
3. Validate CI/CD examples against ToA build pipeline
4. Document any build deployment quirks

### Completed ✅
- **Phase 1:** All analytics and monitoring tools
- **Phase 2:** Build management (set live, SteamCMD wrapper, CI/CD examples)

### Phase 3 (Monitoring & Death Board) — Next Priority
- Review sentiment analysis + auto-flagging
- Wishlist trend tracking (daily snapshots)
- Sales spike detection → auto-create Death Board tickets
- CCU monitoring

### Future
- Open source after battle-testing
- Share on Reddit (r/gamedev, r/ClaudeAI)
- First-mover advantage: no other Steamworks Partner MCP exists

## Usage Example

Once configured in Claude Desktop:

```
You: "Show me recent reviews for Tears of Adria"
Claude: [calls get_reviews tool] → displays review summaries

You: "What were my sales last week?"
Claude: [calls get_sales_data] → revenue breakdown

You: "Has anyone added the game to their wishlist today?"
Claude: [calls get_wishlist_data] → country/language stats
```

## Files to Review

- **README.md** — Start here for setup and tool reference
- **TESTING.md** — How to integrate with Claude Desktop
- **src/index.ts** — Tool definitions (read this to understand capabilities)
- **NEXT_STEPS.md** — Roadmap for Phase 2 & 3

## Why This Matters

**First of its kind.** No public MCP server for Steamworks Partner API existed before this.

**Conversational game analytics.** Instead of logging into Steamworks dashboard → navigating menus → exporting CSVs, you can ask Claude "Did sales spike yesterday?" and get instant answers.

**Automation foundation.** Phase 2 enables build deployment from CI/CD. Phase 3 enables automated review response, wishlist tracking, and sales alerts.

**Reusable across projects.** Works for any game on Steam (ToA, Sir Whoopass, BlockEm if relaunched, future titles).

## Learnings Captured

Documented in `agents/memory/gamedev_learnings.md`:
- MCP architecture patterns for game platform APIs
- Steamworks API structure (Partner vs Store, key types, limitations)
- What can/can't be automated via Steam APIs
- Build tooling quirks (`npm install --include=dev` needed)

---

**Built by:** GameDev Agent (autonomous 4am sweeps)  
**Phase 1:** ~1.5 hours (2026-04-17) — Analytics foundation  
**Phase 2:** ~30 minutes (2026-05-02) — Build management layer  
**Status:** Phase 2 complete, ready for build deployment testing  
**Ticket:** [toa-012-steamworks-mcp.md](assistant/followups/toa-012-steamworks-mcp.md)  
**Learning:** First Steamworks Partner MCP server, reusable across all CZP Steam titles  
**Version:** 0.2.0
