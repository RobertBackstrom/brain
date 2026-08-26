# Changelog

All notable changes to the Steamworks Partner MCP Server will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2026-04-17

### Added - Phase 1: Core Analytics ✅

**MCP Tools:**
- `get_partner_apps` — List all Steam apps managed under this publisher key
- `get_sales_data` — Revenue and sales data by date range (requires Financial API key)
- `get_wishlist_data` — Wishlist additions/deletions with country & language breakdowns
- `get_news` — Recent news and announcements for an app
- `get_app_details` — Store page details (via public Steam Store API)
- `get_reviews` — Review monitoring with sentiment, playtime, votes (via public Steam Store API)
- `get_app_builds` — Build history for an app
- `get_app_betas` — List beta branches for an app

**Infrastructure:**
- TypeScript-based MCP server using @modelcontextprotocol/sdk
- Stdio transport for communication
- Environment variable configuration for API keys
- Axios-based API client with error handling
- Comprehensive TypeScript types for API responses

**Documentation:**
- README.md with installation, configuration, and tool reference
- TESTING.md with Claude Desktop integration guide and troubleshooting
- .env.example for configuration template
- LICENSE (MIT)

**Known Limitations:**
- Store page updates, news posting, pricing, and event management are dashboard-only (no API access)
- Financial data requires separate Financial API key with approval process
- Rate limiting not yet implemented (relies on Steamworks API limits)

## [0.2.0] - 2026-05-02

### Added - Phase 2: Build Management ✅

**MCP Tools:**
- `set_app_build_live` — Switch a specific build to live on any beta branch (WRITE operation)
- `generate_build_script` — Generate VDF build scripts for SteamCMD uploads
- `check_steamcmd` — Verify SteamCMD installation and accessibility

**SteamCMD Integration:**
- New `steamcmd.ts` module with build script generation
- VDF script templating for automated uploads
- Steam Guard authentication handling
- File validation and error handling
- Upload execution wrapper with proper error reporting

**CI/CD Examples:**
- GitHub Actions workflow (`examples/github-actions-upload.yml`)
- GitLab CI pipeline (`examples/gitlab-ci-upload.yml`)
- Comprehensive CI/CD integration guide (`examples/CI_CD_GUIDE.md`)
- Security best practices for credential management
- Staged rollout patterns and multi-platform build examples

**Documentation Updates:**
- README updated with Phase 2 features and new tools
- Security warnings for WRITE operations
- CI/CD workflow patterns and troubleshooting
- Complete VDF script reference

### Changed
- Updated architecture diagram to include steamcmd module
- Enhanced error messages for build deployment operations
- Improved TypeScript types for build-related operations

## [Unreleased]

### Planned - Phase 3: Monitoring & Integration
- Review sentiment analysis and flagging
- Wishlist trend tracking with daily snapshots
- Sales spike detection with configurable thresholds
- Death Board integration for auto-creating follow-ups
- CCU (Concurrent Users) monitoring

## Notes

This is the **first-ever MCP server** wrapping the Steamworks Partner API. It enables Claude (or any MCP client) to interact with Steam's publisher tools directly from conversation.

Built by Aurora Punks GameDev agent for the Tears of Adria project, April 2026.
