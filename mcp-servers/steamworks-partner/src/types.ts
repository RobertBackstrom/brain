/**
 * TypeScript types for Steamworks Partner API responses
 */

export interface SteamworksConfig {
  apiKey: string;
  financialKey?: string;
  baseUrl: string;
}

export interface AppDetails {
  appid: number;
  name: string;
  type: string;
  developer?: string;
  publisher?: string;
  platforms?: {
    windows?: boolean;
    mac?: boolean;
    linux?: boolean;
  };
}

export interface SalesData {
  date: string;
  units_sold: number;
  gross_revenue: number;
  net_revenue: number;
  currency?: string;
}

export interface WishlistData {
  appid: number;
  date: string;
  additions: number;
  deletions: number;
  balance: number;
  country_breakdown?: Record<string, number>;
  language_breakdown?: Record<string, number>;
}

export interface NewsItem {
  gid: string;
  title: string;
  url: string;
  contents: string;
  date: number;
  author: string;
  feedname?: string;
}

export interface Review {
  recommendationid: string;
  author: {
    steamid: string;
    playtime_forever: number;
    playtime_at_review: number;
  };
  language: string;
  review: string;
  timestamp_created: number;
  voted_up: boolean;
  votes_up: number;
  votes_funny: number;
}

export interface BuildInfo {
  buildid: number;
  description: string;
  creation_time: number;
  depot_id: number;
}

export interface BetaBranch {
  name: string;
  buildid: number;
  description: string;
  password_required: boolean;
}
