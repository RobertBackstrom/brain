#!/usr/bin/env node

/**
 * Steamworks Partner MCP Server
 *
 * First-ever MCP server wrapping the Steamworks Partner API.
 * Enables Claude to pull sales/wishlist analytics, manage builds, and monitor reviews.
 *
 * Phase 1: Core Analytics
 * - Sales/revenue data
 * - Wishlist tracking
 * - News/announcements
 * - Store page data
 * - Review monitoring
 */

import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import {
  CallToolRequestSchema,
  ListToolsRequestSchema,
  Tool,
} from '@modelcontextprotocol/sdk/types.js';
import * as dotenv from 'dotenv';
import { SteamAPIClient } from './api-client.js';
import type { SteamworksConfig } from './types.js';
import {
  generateBuildScript,
  uploadBuild,
  checkSteamCMDInstalled,
  prepareBuildUpload,
  type BuildScriptOptions,
  type SteamCMDConfig,
} from './steamcmd.js';

dotenv.config();

const config: SteamworksConfig = {
  apiKey: process.env.STEAMWORKS_API_KEY || '',
  financialKey: process.env.STEAMWORKS_FINANCIAL_KEY,
  baseUrl: process.env.STEAM_PARTNER_API_BASE || 'https://partner.steam-api.com',
};

if (!config.apiKey) {
  console.error('ERROR: STEAMWORKS_API_KEY environment variable is required');
  process.exit(1);
}

const steamClient = new SteamAPIClient(config);

// Define MCP tools for Phase 1
const tools: Tool[] = [
  {
    name: 'get_partner_apps',
    description: 'List all Steam apps managed under this publisher key. Returns app IDs and names.',
    inputSchema: {
      type: 'object',
      properties: {},
    },
  },
  {
    name: 'get_sales_data',
    description: 'Get sales and revenue data for a specific app and date range. Requires Financial API key. Returns units sold, gross revenue, net revenue.',
    inputSchema: {
      type: 'object',
      properties: {
        appid: {
          type: 'number',
          description: 'Steam App ID',
        },
        start_date: {
          type: 'string',
          description: 'Start date in YYYY-MM-DD format',
        },
        end_date: {
          type: 'string',
          description: 'End date in YYYY-MM-DD format',
        },
      },
      required: ['appid', 'start_date', 'end_date'],
    },
  },
  {
    name: 'get_wishlist_data',
    description: 'Get wishlist additions, deletions, and balance for a specific app. Includes country and language breakdowns when available.',
    inputSchema: {
      type: 'object',
      properties: {
        appid: {
          type: 'number',
          description: 'Steam App ID',
        },
        start_date: {
          type: 'string',
          description: 'Optional start date in YYYY-MM-DD format',
        },
        end_date: {
          type: 'string',
          description: 'Optional end date in YYYY-MM-DD format',
        },
      },
      required: ['appid'],
    },
  },
  {
    name: 'get_news',
    description: 'Get recent news/announcements for a Steam app. Returns title, date, author, and content.',
    inputSchema: {
      type: 'object',
      properties: {
        appid: {
          type: 'number',
          description: 'Steam App ID',
        },
        count: {
          type: 'number',
          description: 'Number of news items to fetch (default: 5, max: 20)',
          default: 5,
        },
        maxlength: {
          type: 'number',
          description: 'Max length of news content in characters (default: 300)',
          default: 300,
        },
      },
      required: ['appid'],
    },
  },
  {
    name: 'get_app_details',
    description: 'Get store page details for a Steam app. Returns description, screenshots, price, platforms, release date, etc. Uses public Store API.',
    inputSchema: {
      type: 'object',
      properties: {
        appid: {
          type: 'number',
          description: 'Steam App ID',
        },
      },
      required: ['appid'],
    },
  },
  {
    name: 'get_reviews',
    description: 'Fetch recent reviews for a Steam app. Returns review text, playtime, recommendation (positive/negative), votes. Uses public Store API.',
    inputSchema: {
      type: 'object',
      properties: {
        appid: {
          type: 'number',
          description: 'Steam App ID',
        },
        filter: {
          type: 'string',
          enum: ['all', 'recent', 'positive', 'negative'],
          description: 'Filter reviews by type (default: all)',
          default: 'all',
        },
        num: {
          type: 'number',
          description: 'Number of reviews to fetch (default: 20, max: 100)',
          default: 20,
        },
        cursor: {
          type: 'string',
          description: 'Pagination cursor (use * for first page, or cursor from previous response)',
          default: '*',
        },
      },
      required: ['appid'],
    },
  },
  {
    name: 'get_app_builds',
    description: 'Get build history for a Steam app. Returns build IDs, descriptions, creation timestamps.',
    inputSchema: {
      type: 'object',
      properties: {
        appid: {
          type: 'number',
          description: 'Steam App ID',
        },
      },
      required: ['appid'],
    },
  },
  {
    name: 'get_app_betas',
    description: 'List beta branches for a Steam app. Returns branch names, build IDs, descriptions, password status.',
    inputSchema: {
      type: 'object',
      properties: {
        appid: {
          type: 'number',
          description: 'Steam App ID',
        },
      },
      required: ['appid'],
    },
  },
  {
    name: 'set_app_build_live',
    description: 'Switch a specific build to live on a beta branch. WRITE OPERATION - use with caution! This immediately changes which build is live for players on that branch. Always verify buildid and branch name before calling.',
    inputSchema: {
      type: 'object',
      properties: {
        appid: {
          type: 'number',
          description: 'Steam App ID',
        },
        buildid: {
          type: 'number',
          description: 'Build ID to set live (use get_app_builds to list available builds)',
        },
        branch: {
          type: 'string',
          description: 'Beta branch name (e.g., "default" for main branch, or custom branch name)',
        },
      },
      required: ['appid', 'buildid', 'branch'],
    },
  },
  {
    name: 'generate_build_script',
    description: 'Generate a VDF build script for SteamCMD. This creates the configuration file needed to upload a build to Steam. Does not upload anything - only creates the script file.',
    inputSchema: {
      type: 'object',
      properties: {
        appid: {
          type: 'number',
          description: 'Steam App ID',
        },
        depotid: {
          type: 'number',
          description: 'Depot ID for this app',
        },
        content_root: {
          type: 'string',
          description: 'Absolute path to the directory containing build files',
        },
        output_path: {
          type: 'string',
          description: 'Absolute path where VDF script should be written',
        },
        build_description: {
          type: 'string',
          description: 'Description for this build (e.g., "v1.2.3 - Bug fixes")',
        },
        set_live: {
          type: 'string',
          description: 'Optional: branch to set live after upload (e.g., "default", "beta")',
        },
        local_content_path: {
          type: 'string',
          description: 'Optional: path relative to content_root (default: "*" for all files)',
          default: '*',
        },
      },
      required: ['appid', 'depotid', 'content_root', 'output_path', 'build_description'],
    },
  },
  {
    name: 'check_steamcmd',
    description: 'Check if SteamCMD is installed and accessible on the system. Returns true/false.',
    inputSchema: {
      type: 'object',
      properties: {
        steamcmd_path: {
          type: 'string',
          description: 'Optional: path to steamcmd executable (default: "steamcmd" in PATH)',
        },
      },
    },
  },
];

const server = new Server(
  {
    name: 'steamworks-partner-mcp',
    version: '0.1.0',
  },
  {
    capabilities: {
      tools: {},
    },
  }
);

// Handle list_tools request
server.setRequestHandler(ListToolsRequestSchema, async () => {
  return { tools };
});

// Handle call_tool request
server.setRequestHandler(CallToolRequestSchema, async (request) => {
  const { name, arguments: args } = request.params;

  try {
    switch (name) {
      case 'get_partner_apps': {
        const result = await steamClient.getPartnerAppList();
        return {
          content: [
            {
              type: 'text',
              text: JSON.stringify(result, null, 2),
            },
          ],
        };
      }

      case 'get_sales_data': {
        const { appid, start_date, end_date } = args as {
          appid: number;
          start_date: string;
          end_date: string;
        };

        if (!config.financialKey) {
          return {
            content: [
              {
                type: 'text',
                text: 'ERROR: Financial API key not configured. Set STEAMWORKS_FINANCIAL_KEY environment variable.',
              },
            ],
            isError: true,
          };
        }

        const result = await steamClient.getFinancialData(appid, start_date, end_date);
        return {
          content: [
            {
              type: 'text',
              text: JSON.stringify(result, null, 2),
            },
          ],
        };
      }

      case 'get_wishlist_data': {
        const { appid, start_date, end_date } = args as {
          appid: number;
          start_date?: string;
          end_date?: string;
        };

        const dateRange = start_date && end_date ? { start: start_date, end: end_date } : undefined;
        const result = await steamClient.getWishlistData(appid, dateRange);
        return {
          content: [
            {
              type: 'text',
              text: JSON.stringify(result, null, 2),
            },
          ],
        };
      }

      case 'get_news': {
        const { appid, count = 5, maxlength = 300 } = args as {
          appid: number;
          count?: number;
          maxlength?: number;
        };

        const result = await steamClient.getNewsForApp(appid, maxlength, count);
        return {
          content: [
            {
              type: 'text',
              text: JSON.stringify(result, null, 2),
            },
          ],
        };
      }

      case 'get_app_details': {
        const { appid } = args as { appid: number };
        const result = await steamClient.getAppDetails(appid);
        return {
          content: [
            {
              type: 'text',
              text: JSON.stringify(result, null, 2),
            },
          ],
        };
      }

      case 'get_reviews': {
        const { appid, filter = 'all', num = 20, cursor = '*' } = args as {
          appid: number;
          filter?: 'all' | 'recent' | 'positive' | 'negative';
          num?: number;
          cursor?: string;
        };

        const result = await steamClient.getReviews(appid, cursor, filter, num);
        return {
          content: [
            {
              type: 'text',
              text: JSON.stringify(result, null, 2),
            },
          ],
        };
      }

      case 'get_app_builds': {
        const { appid } = args as { appid: number };
        const result = await steamClient.getAppBuilds(appid);
        return {
          content: [
            {
              type: 'text',
              text: JSON.stringify(result, null, 2),
            },
          ],
        };
      }

      case 'get_app_betas': {
        const { appid } = args as { appid: number };
        const result = await steamClient.getAppBetas(appid);
        return {
          content: [
            {
              type: 'text',
              text: JSON.stringify(result, null, 2),
            },
          ],
        };
      }

      case 'set_app_build_live': {
        const { appid, buildid, branch } = args as {
          appid: number;
          buildid: number;
          branch: string;
        };

        const result = await steamClient.setAppBuildLive(appid, buildid, branch);
        return {
          content: [
            {
              type: 'text',
              text: JSON.stringify(result, null, 2),
            },
          ],
        };
      }

      case 'generate_build_script': {
        const {
          appid,
          depotid,
          content_root,
          output_path,
          build_description,
          set_live,
          local_content_path,
        } = args as {
          appid: number;
          depotid: number;
          content_root: string;
          output_path: string;
          build_description: string;
          set_live?: string;
          local_content_path?: string;
        };

        const scriptPath = await prepareBuildUpload({
          appId: appid,
          depotId: depotid,
          contentRoot: content_root,
          outputPath: output_path,
          buildDescription: build_description,
          setLive: set_live,
          localContentPath: local_content_path,
        });

        return {
          content: [
            {
              type: 'text',
              text: `Build script generated successfully at: ${scriptPath}\n\nTo upload, run:\nsteamcmd +login <username> +run_app_build ${scriptPath} +quit`,
            },
          ],
        };
      }

      case 'check_steamcmd': {
        const { steamcmd_path } = args as { steamcmd_path?: string };
        const isInstalled = await checkSteamCMDInstalled(steamcmd_path);

        return {
          content: [
            {
              type: 'text',
              text: isInstalled
                ? `SteamCMD is installed and accessible at: ${steamcmd_path || 'steamcmd (in PATH)'}`
                : `SteamCMD not found. Install from: https://developer.valvesoftware.com/wiki/SteamCMD`,
            },
          ],
        };
      }

      default:
        return {
          content: [
            {
              type: 'text',
              text: `Unknown tool: ${name}`,
            },
          ],
          isError: true,
        };
    }
  } catch (error) {
    const errorMessage = error instanceof Error ? error.message : String(error);
    return {
      content: [
        {
          type: 'text',
          text: `Error executing ${name}: ${errorMessage}`,
        },
      ],
      isError: true,
    };
  }
});

// Start the server
async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error('Steamworks Partner MCP Server running on stdio');
}

main().catch((error) => {
  console.error('Fatal error:', error);
  process.exit(1);
});
