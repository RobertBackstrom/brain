# Steamworks Partner MCP Server

**First-ever MCP server wrapping the Steamworks Partner API.**

Enables Claude (or any MCP client) to pull sales/wishlist analytics, manage build deployments, and monitor reviews — all from conversation.

## Features

### Phase 1: Core Analytics ✅
- **Sales/Revenue Data** — Query IPartnerFinancialsService for units sold and revenue by date range
- **Wishlist Analytics** — Track additions, deletions, balance with country/language breakdowns
- **News/Announcements** — Read existing Steam news posts for your apps
- **Store Page Data** — Fetch app details, pricing, screenshots, platforms
- **Review Monitoring** — Pull reviews with sentiment, playtime, votes
- **Build History** — View past builds and their deployment times
- **Beta Branches** — List beta branches and their current builds

### Phase 2: Build Management ✅
- **Set Build Live** — Switch a specific build to live on any branch (`set_app_build_live`)
- **Generate Build Scripts** — Create VDF build scripts for SteamCMD uploads (`generate_build_script`)
- **SteamCMD Integration** — Check SteamCMD installation and prepare uploads (`check_steamcmd`)
- **CI/CD Examples** — GitHub Actions and GitLab CI templates for automated deployments

### Phase 3: Monitoring & Integration (Planned)
- Review sentiment tracking
- Wishlist trend analysis
- Sales spike detection
- Death Board integration for auto-creating follow-ups

## Installation

```bash
npm install
npm run build
```

## Configuration

Create a `.env` file (see `.env.example`):

```bash
# Required: Steamworks Web API Publisher Key
# Get from: https://partner.steamgames.com/doc/webapi_overview/auth
STEAMWORKS_API_KEY=your_publisher_key_here

# Optional: Financial API Group Key (required for sales/revenue queries)
# Request from: Steamworks Partner > Users & Permissions > WebAPI
STEAMWORKS_FINANCIAL_KEY=your_financial_key_here

# Optional: Default app ID for testing
STEAM_APP_ID=480
```

### Getting API Keys

1. **Publisher Key** (required):
   - Go to Steamworks Partner dashboard
   - Navigate to Users & Permissions > WebAPI
   - Generate a new publisher key
   - Has access to app management, builds, news, etc.

2. **Financial API Key** (optional, for sales data):
   - Same location as above
   - Request Financial API Group permissions
   - Required for IPartnerFinancialsService endpoints
   - Approval may take 1-2 business days

## Usage

### Standalone

Run the MCP server:

```bash
npm start
```

The server communicates via stdio (standard MCP transport).

### With Claude Desktop

Add to your Claude Desktop config (`~/Library/Application Support/Claude/claude_desktop_config.json` on Mac):

```json
{
  "mcpServers": {
    "steamworks-partner": {
      "command": "node",
      "args": ["/path/to/steamworks-partner-mcp/dist/index.js"],
      "env": {
        "STEAMWORKS_API_KEY": "your_key_here",
        "STEAMWORKS_FINANCIAL_KEY": "your_financial_key_here"
      }
    }
  }
}
```

### With Claude Code

Add to your MCP settings in Claude Code.

## Available Tools

### `get_partner_apps`
List all Steam apps managed under this publisher key.

**Returns:** App IDs and names

### `get_sales_data`
Get sales and revenue data for a specific app and date range.

**Requires:** Financial API key  
**Parameters:**
- `appid` (number) — Steam App ID
- `start_date` (string) — Start date in YYYY-MM-DD format
- `end_date` (string) — End date in YYYY-MM-DD format

**Returns:** Units sold, gross revenue, net revenue

### `get_wishlist_data`
Get wishlist additions, deletions, and balance for a specific app.

**Parameters:**
- `appid` (number) — Steam App ID
- `start_date` (string, optional) — Start date in YYYY-MM-DD format
- `end_date` (string, optional) — End date in YYYY-MM-DD format

**Returns:** Wishlist balance, country/language breakdowns

### `get_news`
Get recent news/announcements for a Steam app.

**Parameters:**
- `appid` (number) — Steam App ID
- `count` (number, optional) — Number of news items (default: 5, max: 20)
- `maxlength` (number, optional) — Max content length in chars (default: 300)

**Returns:** News title, date, author, content

### `get_app_details`
Get store page details for a Steam app (uses public Store API).

**Parameters:**
- `appid` (number) — Steam App ID

**Returns:** Description, screenshots, price, platforms, release date

### `get_reviews`
Fetch recent reviews for a Steam app (uses public Store API).

**Parameters:**
- `appid` (number) — Steam App ID
- `filter` (string, optional) — Filter: 'all', 'recent', 'positive', 'negative' (default: 'all')
- `num` (number, optional) — Number of reviews (default: 20, max: 100)
- `cursor` (string, optional) — Pagination cursor (default: '*')

**Returns:** Review text, playtime, recommendation, votes

### `get_app_builds`
Get build history for a Steam app.

**Parameters:**
- `appid` (number) — Steam App ID

**Returns:** Build IDs, descriptions, creation timestamps

### `get_app_betas`
List beta branches for a Steam app.

**Parameters:**
- `appid` (number) — Steam App ID

**Returns:** Branch names, build IDs, descriptions, password status

### `set_app_build_live`
Switch a specific build to live on a beta branch. **WRITE OPERATION** - use with caution!

**Parameters:**
- `appid` (number) — Steam App ID
- `buildid` (number) — Build ID to set live (use `get_app_builds` to list available)
- `branch` (string) — Beta branch name (e.g., "default" for main, or custom branch)

**Returns:** Success confirmation

⚠️ **Warning:** This immediately changes which build is live for players. Always verify parameters before calling.

### `generate_build_script`
Generate a VDF build script for SteamCMD. Creates the configuration file for uploading builds.

**Parameters:**
- `appid` (number) — Steam App ID
- `depotid` (number) — Depot ID
- `content_root` (string) — Absolute path to build files
- `output_path` (string) — Where to write VDF script
- `build_description` (string) — Description for this build
- `set_live` (string, optional) — Branch to set live after upload
- `local_content_path` (string, optional) — Path relative to content_root (default: "*")

**Returns:** Path to generated VDF script, instructions for upload

### `check_steamcmd`
Check if SteamCMD is installed and accessible on the system.

**Parameters:**
- `steamcmd_path` (string, optional) — Path to steamcmd executable (default: "steamcmd")

**Returns:** Installation status and download link if not found

## API Coverage

### Implemented (Phase 1 ✅)
- ✅ `ISteamApps/GetPartnerAppListForWebAPIKey` — List apps
- ✅ `IPartnerFinancialsService/GetSalesReport` — Revenue data
- ✅ `ISteamWishlist/GetWishlistData` — Wishlist analytics
- ✅ `ISteamNews/GetNewsForApp` — News/announcements
- ✅ Store API: `appdetails` — App metadata
- ✅ Store API: `appreviews` — Review data
- ✅ `ISteamApps/GetAppBuilds` — Build history
- ✅ `ISteamApps/GetAppBetas` — Beta branches

### Implemented (Phase 2 ✅)
- ✅ `ISteamApps/SetAppBuildLive` — Switch live build
- ✅ SteamCMD wrapper — Generate VDF scripts, upload builds
- ✅ CI/CD integration examples — GitHub Actions & GitLab CI

### Planned (Phase 3)
- ⏳ Review sentiment monitoring — Periodic pulls, flag negative reviews
- ⏳ Wishlist trend tracking — Daily snapshots for analytics
- ⏳ Sales spike detection — Alert when sales exceed threshold
- ⏳ Death Board integration — Auto-create follow-ups

### Dashboard-Only (No API)
These cannot be automated via API:
- Store page text/description updates
- Capsule art, screenshot, trailer uploads
- Creating news/announcement posts
- Setting up events (sales, livestreams)
- Managing pricing/discounts

## Architecture

```
steamworks-partner-mcp/
├── src/
│   ├── index.ts          # MCP server entry point, tool definitions
│   ├── api-client.ts     # Axios wrapper for Steamworks Partner API
│   └── types.ts          # TypeScript types for API responses
├── dist/                 # Compiled JavaScript (auto-generated)
├── .env                  # API keys (not committed)
├── .env.example          # Template for configuration
├── package.json
├── tsconfig.json
└── README.md
```

## Resources

- [Steamworks Web API Docs](https://partner.steamgames.com/doc/webapi)
- [OpenAPI Spec for Steamworks](https://github.com/ceva24/openapi-steamworks-web-api)
- [Undocumented Endpoints](https://steamapi.xpaw.me/)
- [Partner API Examples](https://gist.github.com/BadgerCode/180d9b361af0c8a5c9b9d98c51f720ac)
- [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)

## Contributing

This is the first public Steamworks Partner MCP server. Contributions welcome!

Before adding new tools:
1. Check if the endpoint requires Financial API key or standard Publisher key
2. Add types to `src/types.ts`
3. Add API method to `src/api-client.ts`
4. Add tool definition + handler to `src/index.ts`
5. Update README

## License

MIT License - Aurora Punks

## Credits

Built by the GameDev agent at Aurora Punks for the Tears of Adria project.
First-ever MCP integration for Steamworks Partner API.
