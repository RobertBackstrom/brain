---
name: reference_vps_web_collection_limits
description: "Which public sources can and cannot be scraped from the VPS — Reddit and YouTube comments are blocked at the IP level, what to use instead for player-sentiment research"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 2e8cd21b-fca1-4951-94a4-ae2f6cee3530
  modified: 2026-08-17T23:10:45.322Z
---

# What the VPS can and cannot collect from the open web

Established 2026-08-17 during Irons 2 sentiment research ([[project_starbreeze_irons2]]), after a full agent pass tried every available route. Check this before promising anyone a sentiment sweep.

**Blocked, do not burn time on it:**
1. **Reddit — every route.** HTTP 403 against the server's datacenter IP. Tried and failed: `www.reddit.com`, `old.reddit.com`, the `.json` endpoints (`/r/<sub>/search.json`, `/comments/<id>.json`), and a full Playwright browser session with a realistic desktop user agent and viewport. The block is on the IP, not on the tool, so no amount of header or browser realism fixes it. Search-engine indexing of the relevant threads was also thin, so the usual workaround of reading Reddit through search results did not substitute.
2. **YouTube comment sections — by scraping.** Sign-in bot check for both Playwright and `yt-dlp`, escalating to a captcha wall during collection. Video **titles, descriptions and view counts are collectable**; the comments underneath them are not. **But see the API note below before concluding YouTube comments are unreachable.**

**Not blocked, but broken for other reasons (clarified 2026-08-19):**
- **YouTube comments via the official Data API v3 are NOT IP-blocked.** `assistant/youtube-tracker.js` uses an API key, which is a completely different route from the scraping above, and the key has been provisioned in `assistant/.env` all along. It nevertheless produced nothing for months, for two unrelated reasons: (a) cron ran `node youtube-tracker.js` with a bare environment and the script read `process.env` without loading `.env`, so it logged `YOUTUBE_API_KEY not configured` 11,230 times — **fixed 2026-08-19**; (b) no project lists anything to watch (`tears_of_adria/community_config.json` has `youtube.channel_ids: []` and `video_ids: []`), and the tracker correctly skips a project with both empty — **still open, needs channel/video IDs**. So the honest line is "YouTube comments are reachable via the API once someone says which channels to watch", not "YouTube is blocked". Quota is the real API constraint, not our IP.
- **Reddit's block is confirmed and structural**, not a config gap: 22,414 consecutive HTTP 403s and zero events ever emitted. `reddit-tracker.js` was **disabled in the crontab 2026-08-19** with the reason inline, because changing the cadence of a job that has never worked is pointless. See [[scheduled_jobs_inventory]].

**Works fine:**
1. **Steam community forums** (`steamcommunity.com/app/<id>/discussions`), both the game's own forum and adjacent titles. This was the only PUBG-native player channel reachable for Irons 2 and it carried real first-hand accounts.
2. Steam store pages, SteamCharts, news sites, company IR and earnings coverage, developer interviews, general WebSearch and WebFetch.
3. Playwright-driven authenticated tools where we hold credentials, e.g. the RankOne agent ([[reference_rankone_agent]]).

**How to apply:**
- Plan sentiment research around Steam forums plus creator-level signal (titles, view counts, video descriptions) rather than around Reddit. Say so up front when scoping, so nobody expects a subreddit sweep.
- **Report the gap rather than filling it.** Robert would rather read "we could not sample console sentiment" than an invented consensus, especially when the numbers may reach a client. This is the same standard as [[feedback_check_web_before_asking]]: verify or say you could not.
- Console-player sentiment is structurally hard for us, since console players are absent from Steam forums and live mainly on the blocked platforms. Treat any console sentiment claim as unsourced unless someone collected it manually.
- The only way to close the Reddit and YouTube-comment gap is a **manual pass from Robert's own residential browser**, which takes well under an hour for a focused question. Offer that as an explicit option instead of retrying automation.
- If a future task genuinely depends on Reddit at scale, the durable fix is a residential proxy or an official API key, which is a DevOps decision ([[feedback_devops_tooling]]) and not something to improvise mid-task.
