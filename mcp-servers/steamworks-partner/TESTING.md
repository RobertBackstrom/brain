# Testing the Steamworks Partner MCP Server

## Prerequisites

1. Steamworks Publisher Key
2. Steam App ID for testing (or use 480 for Spacewar, Valve's test app)

## Quick Test with Claude Desktop

1. **Configure your API key:**

```bash
cp .env.example .env
# Edit .env and add your STEAMWORKS_API_KEY
```

2. **Add to Claude Desktop config:**

On Mac: `~/Library/Application Support/Claude/claude_desktop_config.json`  
On Windows: `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "steamworks-partner": {
      "command": "node",
      "args": ["/home/assistant/projects/mcp-servers/steamworks-partner/dist/index.js"],
      "env": {
        "STEAMWORKS_API_KEY": "YOUR_KEY_HERE"
      }
    }
  }
}
```

3. **Restart Claude Desktop**

4. **Test the tools:**

Try these prompts in Claude Desktop:

```
"List all my Steam apps using the Steamworks MCP"

"Get news for app 480 (Spacewar)"

"Fetch recent reviews for app 480"

"Show me build history for app 480"
```

## Manual Testing (CLI)

The MCP server uses stdio transport, so you can test it manually by piping JSON-RPC requests:

```bash
# Test list_tools
echo '{"jsonrpc":"2.0","id":1,"method":"tools/list"}' | node dist/index.js

# Test get_news tool
echo '{"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":"get_news","arguments":{"appid":480,"count":3}}}' | node dist/index.js
```

## Test App IDs

- **480** — Spacewar (Valve's test app, publicly accessible)
- **753** — Steam (Community items)
- Your own App IDs from your publisher account

## Expected Errors

### Missing Financial Key
If you try `get_sales_data` without `STEAMWORKS_FINANCIAL_KEY`:
```
ERROR: Financial API key not configured. Set STEAMWORKS_FINANCIAL_KEY environment variable.
```

### Invalid App ID
If you query an app you don't have access to:
```
HTTP 403 or empty response
```

### Rate Limiting
Steamworks API has rate limits. If you hit them:
```
HTTP 429 Too Many Requests
```

Wait a few minutes and retry.

## Debugging

Enable verbose logging:
```bash
NODE_ENV=development node dist/index.js
```

Check the MCP SDK debug output by adding to your .env:
```
DEBUG=mcp:*
```

## Phase 1 Tools to Test

- [x] `get_partner_apps` — List your apps
- [x] `get_app_details` — Store page data
- [x] `get_news` — News/announcements
- [x] `get_reviews` — Recent reviews
- [x] `get_wishlist_data` — Wishlist analytics (Partner API, may need special permissions)
- [x] `get_sales_data` — Revenue data (requires Financial API key)
- [x] `get_app_builds` — Build history
- [x] `get_app_betas` — Beta branches

## Next Steps

Once Phase 1 is tested, we can move to:
- **Phase 2:** Build deployment (SetAppBuildLive, SteamCMD wrapper)
- **Phase 3:** Monitoring integration (review sentiment, sales spike detection, Death Board integration)

## Troubleshooting

### "Cannot find module" errors
Run `npm run build` to recompile after any source changes.

### "STEAMWORKS_API_KEY not found"
Make sure your `.env` file is in the project root with:
```
STEAMWORKS_API_KEY=your_actual_key_here
```

### MCP server not showing up in Claude Desktop
1. Check config file syntax (must be valid JSON)
2. Restart Claude Desktop completely
3. Check Console/DevTools for errors
