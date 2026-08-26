#!/bin/bash
# Quick test script for Steamworks Partner MCP Server
# Tests if the server can start and list its tools

echo "Testing Steamworks Partner MCP Server..."
echo ""

# Check if .env file exists
if [ ! -f .env ]; then
    echo "❌ ERROR: .env file not found"
    echo "   Copy .env.example to .env and add your API keys"
    exit 1
fi

# Check if dist/ exists
if [ ! -d dist ]; then
    echo "❌ ERROR: dist/ directory not found"
    echo "   Run: npm run build"
    exit 1
fi

# Test list_tools
echo "Sending list_tools request..."
echo '{"jsonrpc":"2.0","id":1,"method":"tools/list"}' | node dist/index.js 2>/dev/null | python3 -m json.tool

echo ""
echo "✅ If you see a list of 8 tools above, the server is working!"
echo ""
echo "Next steps:"
echo "1. Add your Steamworks API key to .env"
echo "2. Add this server to Claude Desktop config (see claude-desktop-config.example.json)"
echo "3. Restart Claude Desktop"
echo "4. Try: 'List my Steam apps using the Steamworks MCP'"
