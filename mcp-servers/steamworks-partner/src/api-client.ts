/**
 * Steamworks Partner API client
 */

import axios, { AxiosInstance } from 'axios';
import type { SteamworksConfig } from './types.js';

export class SteamAPIClient {
  private client: AxiosInstance;
  private config: SteamworksConfig;

  constructor(config: SteamworksConfig) {
    this.config = config;
    this.client = axios.create({
      baseURL: config.baseUrl,
      timeout: 30000,
    });
  }

  /**
   * Make a request to the Partner API
   */
  async request<T>(
    endpoint: string,
    params: Record<string, any> = {},
    useFinancialKey = false
  ): Promise<T> {
    const apiKey = useFinancialKey && this.config.financialKey
      ? this.config.financialKey
      : this.config.apiKey;

    const response = await this.client.get(endpoint, {
      params: {
        key: apiKey,
        format: 'json',
        ...params,
      },
    });

    return response.data;
  }

  /**
   * Fetch app list for this publisher
   */
  async getPartnerAppList(): Promise<any> {
    return this.request('/ISteamApps/GetPartnerAppListForWebAPIKey/v2');
  }

  /**
   * Get sales/revenue data (requires financial key)
   */
  async getFinancialData(appid: number, startDate: string, endDate: string): Promise<any> {
    return this.request(
      '/IPartnerFinancialsService/GetSalesReport/v1',
      { appid, start_date: startDate, end_date: endDate },
      true
    );
  }

  /**
   * Get wishlist data
   */
  async getWishlistData(appid: number, dateRange?: { start: string; end: string }): Promise<any> {
    const params: any = { appid };
    if (dateRange) {
      params.start_date = dateRange.start;
      params.end_date = dateRange.end;
    }
    return this.request('/ISteamWishlist/GetWishlistData/v1', params);
  }

  /**
   * Get news for app
   */
  async getNewsForApp(appid: number, maxlength = 300, count = 5): Promise<any> {
    return this.request('/ISteamNews/GetNewsForApp/v2', {
      appid,
      maxlength,
      count,
    });
  }

  /**
   * Get app details from Store API (not partner, but useful)
   */
  async getAppDetails(appid: number): Promise<any> {
    const response = await axios.get(`https://store.steampowered.com/api/appdetails`, {
      params: { appids: appid },
    });
    return response.data[appid];
  }

  /**
   * Get reviews from Steam Store API
   */
  async getReviews(
    appid: number,
    cursor = '*',
    filter: 'all' | 'recent' | 'positive' | 'negative' = 'all',
    num = 20
  ): Promise<any> {
    const response = await axios.get(`https://store.steampowered.com/appreviews/${appid}`, {
      params: {
        json: 1,
        filter,
        cursor,
        num_per_page: num,
      },
    });
    return response.data;
  }

  /**
   * Get build history
   */
  async getAppBuilds(appid: number): Promise<any> {
    return this.request('/ISteamApps/GetAppBuilds/v1', { appid });
  }

  /**
   * Get beta branches
   */
  async getAppBetas(appid: number): Promise<any> {
    return this.request('/ISteamApps/GetAppBetas/v1', { appid });
  }

  /**
   * Set a build live on a branch (WRITE operation - use carefully!)
   */
  async setAppBuildLive(appid: number, buildid: number, branch: string): Promise<any> {
    return this.request('/ISteamApps/SetAppBuildLive/v2', {
      appid,
      buildid,
      beta_key: branch,
    });
  }
}
