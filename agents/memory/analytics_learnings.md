---
name: Analytics Agent Learnings
description: Cross-project knowledge accumulated by the Analytics agent from sales data, Steam metrics, and reporting
type: agent_memory
agent: analytics
---

# Analytics Agent Learnings

## Console Reports

- Sony reports arrive as XLSX via email; format differs by region (SIEE/SIEA/SIE Asia/SIEJ) [SalesInsights, 2026-03]
- Xbox and Nintendo require manual portal downloads [SalesInsights, 2026-03]
- IndieArk sends PDF reports via email [SalesInsights, 2026-03]
- FX conversion: always use rate from report date, not current rate [SalesInsights, 2026-03]

## Revenue Splits

- Sir Whoopass: AE 45% / AP 55% [SalesInsights, 2026-03]

## Steam

- Steamworks scraper exists at `umbrella/sales-insights/steam/scraper.py` — Playwright-based, supports TOTP login, session caching, publisher switching, scrapes sales/wishlists/traffic [SalesInsights, 2026-04]
- 10 publisher orgs mapped in scraper: Valiant, Headup, White Lines Black Spaces, Red Marmoset, Duck Tape, Ark Island Studio (ToA: appid 2561500), Windup, EPOCH MEDIA, Aurora Punks Dev Services, Eternal Minds [SalesInsights, 2026-04]
- Scraper paths are Windows-hardcoded (`C:\Users\johan\...`), needs porting for cross-platform use [SalesInsights, 2026-04]
- SIEA parser pipeline exists (5 scripts, multiple iterations) — parses base64 XLSX from MCP/GDrive, searches for Sir Whoopass/UB1314/Aurora Punks rows [SalesInsights, 2026-04]
- Missing: SIEE/Asia/SIEJ parsers, Xbox parser, Nintendo parser, IndieArk PDF parser, Google Sheets writer [SalesInsights, 2026-04]

## IndieBI

- IndieBI Direct Data Access: paid add-on, $299/mo (discounted) or $2,990/yr. Provides parquet or CSV files. 30-day free trial available. Contact: Marcin Graczyk. Robert hasn't responded since Mar 20 — Marcin followed up Mar 23. [SalesInsights, 2026-04]
- IndieBI free tier has manual data export in-app but requires human to download daily [SalesInsights, 2026-04]
- IndieBI finance account: finance@aurorapunks.com [SalesInsights, 2026-04]

## Reporting

- For inbound publishing/co-dev pitch reviews where the game has no public Steam/Meta page yet, build the KPI table around the *studio's prior shipped title* as a commercial proxy (review score, follower count, owners band, post-launch fate like delisting). Note explicitly which channels were checked and returned nothing — absence of footprint is itself a signal. [GEN-012 Goblin's Healer, 2026-04-16]
- Always confirm whether a pitch deck actually exists in the email thread before assuming there's material to evaluate; ack emails should ask for deck + partnership type + platforms when missing. [GEN-012 Goblin's Healer, 2026-04-16]

## Demo → Launch Review-Score Estimation

- Method for forecasting EA/launch Steam review % from a demo: (1) Pull demo telemetry — avg playtime vs the 7-38 min median demo benchmark (60+ min = very strong), day-7 retention, returning-vs-new crossover, session depth/outliers. Deep engagement = the loop holds = positive-review precondition. (2) Classify the criticisms: "completeness/polish/stability" (fixable, doesn't reject the design) vs "design rejection" (fundamental). Only the latter caps the score hard. (3) Discount self-selected demo/itch.io/Discord sentiment when mapping to Steam — Steam review culture is harsher and a paid price raises the bar; ~85% itch positivity ≠ 85% Steam. (4) Stability (crashes + missing save) is the #1 EA review killer — weight it above everything else. (5) Week-1 reads ~5-8 pts HIGH because the first reviewers are wishlist superfans; it settles lower over the first month as broader buyers arrive. State week-1 and settled separately. [Dig In / Cold Pixel, 2026-06-11]
- Chinese localization is a review-% lever, not just a market lever: Chinese players are review-sensitive to loc quality. Good loc removes a common negative-review driver and adds positive volume (~+2-4 pts), BUT only if paired with a low-end-hardware performance pass — "heavy on graphics" + good loc still gets review-bombed by lower-spec Chinese rigs. [Dig In / Cold Pixel, 2026-06-11]
- Demo avg-playtime can be content-capped: a time-limited demo (e.g. 1-3h of content) makes a high avg playtime partly a ceiling artifact, not pure retention. Still valid as a low-bounce signal, but cite the cap and lean on retention + long-session outliers (17h on a 1-3h demo) for the real depth read. [Dig In, 2026-06-11]
- itch.io demo telemetry beats SteamDB for review-score forecasting: itch gives playtime/retention/session data that SteamDB CCU never exposes. When SteamDB is Cloudflare-walled (WebFetch 403), the studio's own itch/analytics report is the better source anyway. [Dig In, 2026-06-11]
- Large Drive files (Office .docx/.pptx uploads, image-heavy PDFs) return base64 blobs via gdrive_read_file and blow the token limit. For PDFs: download bytes via Drive API `?alt=media` to /tmp, then use the Read tool's native PDF/vision support (max 20 pages/call). Native Google Docs/Sheets read cleanly; uploaded binary Office files do not. [Dig In data room, 2026-06-11]

## Reading a Publisher PnL for Investor ROI

- Reading a publisher PnL for an investor ROI: (a) ROI is a RATE — present it as % so it's invariant to ticket size; reconcile FX (e.g. 9% of $700k vs 500k SEK) separately, and never let a currency mismatch block the analysis. (b) Read the recoup waterfall explicitly — "X% rev share until recoup, flips to Y after" PLUS who holds recoup priority IS the downside-protection story (recoup-priority investors get most/all principal back even in a bear case unless the game fails to ship/flops). (c) Build down/base/up by rescaling the pitch model's quarterly investor cashflow and re-anchoring to the REAL launch date when the model's dates are stale — a pitch PnL is almost always the bull case, so label it as such and stress-test around it. [Dig In / Cold Pixel, 2026-06-11]

## Documentation & Skill Maintenance

- Batch updates to skill files benefit from systematic auditing first: count missing sections, prioritize by usage frequency, draft changes before executing [Gen-118, 2026-04-15]
- "When to Use" + "NOT for" sections significantly improve skill discoverability and prevent misapplication (technique from Anthropic's Complete Guide to Building Skills for Claude, Jan 2026) [Gen-118, 2026-04-15]
- When splitting oversized reference files (>300 lines), propose split approach with specific line counts and structure before executing - better to confirm structural changes even when approved [Gen-118, 2026-04-15]

## Ticket Hygiene

- When a ticket has been verified complete but can't be closed by the agent (needs Robert's sign-off), add `agent_eligible: false` to frontmatter to prevent 4am sweep from re-picking it. This stops redundant agent runs on already-handled tickets. [ToA-016, 2026-04-30]
- Community Bot tickets asking product/roadmap questions (e.g., "Will there be DLC?") are misrouted to Analytics via keyword fallback — these are community management tasks, not analytics. If developer has already responded on the forum, no Analytics action needed. [ToA-016, 2026-04-30]
- Bank compliance, financial holds, and corporate documentation tasks (e.g., Nintendo bank compliance details) arrive with "analytics" routing via keyword fallback but belong to CorpBot instead. Mark as `needs_input: true`, `agent_eligible: false`, recommend CorpBot in activity log. [apb-013, 2026-05-29]
- Education/HR supervisor reports (internship evals, performance attestations) are misrouted to Analytics via keyword fallback but require Robert's direct judgment about a student's performance/grade. These cannot be autonomously filled out by any agent — mark `needs_input: true`, set `agent_eligible: false`, route to CorpBot or Robert directly. [apb-016, 2026-05-29]

## Multi-Title Invoicing

- Kinda Brave epic (GFF + DBL) royalty calculation: sum Steam Revenue Share + Console Net Sales, then apply title-specific rate (DBL 35%, GFF 20%). Combine console platforms by title before applying rate. Use FX rate from previous month's closing date for consistency across invoices. [gff-000, 2026-06-01]

## Steam Showcase Event Coordination

- Steam showcase events (e.g. Baltic Showcase) run for ~7 days but have a shorter "main page featuring" window (48-72 hours) for regional featured homepage visibility — this is the peak moment for social/announcement pushes [K&G Baltic Showcase, 2026-06-03]
- Event curators (like DevGAMM) provide promo assets and explicitly request advance notice of any announcements/updates planned during the event window; treat curator email asks (especially post-confirmation) as soft deadlines for content planning [K&G, 2026-06-03]
- Steam showcase participation can include optional custom discounts via the Discount Management Tool in Steamworks dashboard — curators often flag this availability post-confirmation [K&G, 2026-06-03]
- Effective social cadence for a ~7-day showcase: announcement push 2-3 days ahead (72-hour window, platforms: Twitter, LinkedIn, Discord), then boost during main-page featuring window (48-72 hours, focus on Steam news + social clips/shorts) [K&G, 2026-06-03]
- Steam news announcements for showcase events should be short + atmospheric, matching the game's positioning voice; lead with the event hook (dates, visibility window) and a soft CTA (sentiment-driven, not hard pitch) [K&G, 2026-06-03]

## Announcement Drafting & Multiplatform Content

- When preparing Steam showcase announcements, draft complete templates for ALL platforms in a single `.md` file: Steam News Post (500-600 words, detailed), Twitter/X variants (3-4: announcement hook, community angle, early teaser with different tone), Discord (community-focused, emoji-friendly), Instagram (hashtag-rich, visual-first caption). Include timing schedule table, baseline metrics section (with TBD fields), and implementation notes. Robert can then publish directly from templates without repeating work across channels. [toa-025, 2026-06-03]
- For multi-game showcase participation (e.g., ToA + K&G both in Baltic Showcase), create separate announcement drafts but mirror the structure/timing — allows batch review by Robert and creates natural cross-linking opportunities in Discord threads ("Our sister title..."). [toa-025 + kng-003 parallel tickets, 2026-06-03]
- Announcement tickets arriving via keyword fallback to Analytics (e.g., "Steam + socials") are content/community work, not analytics — mark `agent_eligible: false` after drafting, since publishing requires Robert's approval. Include TBD fields (Steam ID, Discord URL, current metrics, pricing) so Robert knows what info to gather before publishing. [toa-025 & kng-003, 2026-06-03]

## Weekly Reflection Process

- Weekly reflection tickets (gen-NNN-weekly-reflection-YYYY-WNN) are one-shot reports created and completed by the Sunday 05:00 reflection run. Once the report is appended (confirmed by "Reflection agent completed" activity log entry), immediately set `agent_eligible: false` to prevent re-spawns. The ticket needs Robert's review/closure but should never be picked up by the 4am sweep again. [gen-242 W21, 2026-06-06]
- The irony: the W21 reflection diagnosed the exact problem it later suffered from — the 4am scheduler not filtering already-complete tickets. This validates the report's Action #1 (fix scheduler filter for `needs_input`/`pending_close`). [gen-242, 2026-06-06]

## Xbox Royalty Statements

- Microsoft sends "New statement available" email notifications to robert@aurorapunks.com (and sometimes hektor@aurorapunks.com) when royalty statements are ready. Emails contain no attachments - just a notification to log into the portal. [sigh-006, 2026-06-06]
- Portal URL: https://royalty.microsoft.com/ (Microsoft Royalties Statement Management portal). Account: robert@aurorapunks.com. Vendor org: Aurora Punks Development Services (0003066327). [sigh-006 + gen-024, 2026-06-06]
- Download workflow is manual until sigh-004 (Microsoft Entra ID setup) completes - then we can automate via Partner Center API. Until then, draft download instructions and set needs_input for Robert to execute manually. [sigh-006, 2026-06-06]
- Past access issues (2FA unavailable, login loop) were documented in gen-024 but resolved by Apr 23, 2026. [gen-024, 2026-06-06]

## PlayStation Royalty Automation Pipeline

- Built full integration pipeline connecting parsers → sheets writer: `umbrella/sales-insights/pipeline.py` handles period extraction, amount extraction, currency formatting, platform normalization, and generates MCP update plans. [sigh-000, 2026-06-09]
- Pipeline supports all three PlayStation regions (SIEA/SIEE/SIEAsia) with unified interface. Same process flow for each: parse → extract → format → generate update plan. [sigh-000, 2026-06-09]
- Period extraction handles multiple formats: "January 2026", "Jan-2026", "2026-01", "ROYALTY_JAN-2026_...", "Statement Period: January 2026". Robust month/year parsing with fallback patterns. [sigh-000, 2026-06-09]
- Currency formatting uses region-appropriate symbols: USD/EUR/GBP prefix symbol ($€£), SEK suffix (kr). Amounts formatted with thousands separator and 2 decimals. [sigh-000, 2026-06-09]
- Test suite at `umbrella/sales-insights/test_pipeline.py` provides end-to-end validation with example reports from GDrive (SIEE: 1OMVcoZPNNzNr_JqhacsnZn9m4nFCIKug, SIEAsia: 18Pb2azu2MTpTZlfh_fW-QJlzgPruvkpP). [sigh-000, 2026-06-09]
- Infrastructure fully complete for PlayStation automation (all 6 components ready): SIEA parser, SIEE parser, SIEAsia parser, Sheets writer, Integration pipeline, Test suite. Pending: live MCP testing in interactive session + Gmail → Parse → Update automation flow + Xbox parser (blocked on sigh-006). [sigh-000, 2026-06-10]
- Live testing of parsers + pipeline requires interactive Claude Code session with MCP access - autonomous 4am sweep can't directly invoke MCP tools for GDrive fetch/Sheets write. Test harness ready at `test_live_pipeline.py` for when Robert runs an interactive session. [sigh-000, 2026-06-10]

## Steam TOTP / Scraper Authentication

- Steam's TOTP is NOT standard RFC-6238. It uses: (1) base64-encoded shared secret (not base32), (2) HMAC-SHA1 with 30-second intervals, (3) 5-character alphanumeric output from custom alphabet `23456789BCDFGHJKMNPQRTVWXY` (not 6-digit numeric). [sigh-005, 2026-06-06]
- `pyotp.TOTP(secret)` silently produces garbage codes when fed a base64 secret - it expects base32. Always use the custom Steam implementation (stdlib: base64, hmac, hashlib, struct). [sigh-005, 2026-06-06]
- The same secret (`STEAM_TOTP_SECRET` env var, extracted from steamguard-cli maFile) powers both the VPS Death Board endpoint (`/api/steam/totp` in server.js via db-041) and the Steam scraper (`umbrella/sales-insights/steam/scraper_vps.py`). Cross-verify by comparing outputs within the same 30s window. [sigh-005 + db-041, 2026-06-06]

## Console Report Google Sheets Structure

- Sheet `1bwbbgWoAfml-AKvKjVi0IxPxQ62cYAQ-iYLnOrOHPnE` has time-series layout: months as columns (row 2), years as section markers (row 1), platforms as row groups. [sigh-000, 2026-06-07]
- Each platform section (SIEE, SIEA, Xbox, Nintendo, etc.) occupies 4 consecutive rows: (1) Platform name + native currency amounts per month, (2) "FX Date" + FX rate dates, (3) "FX Value" + EUR/USD→SEK exchange rates, (4) "Sum in SEK" + converted amounts (formula-driven, read-only). [sigh-000, 2026-06-07]
- Month names in row 2 are mixed English/Swedish (e.g., "May" / "maj", "February" / "februari"). Normalization required before column lookup. [sigh-000, 2026-06-07]
- Update workflow: parser extracts data → Sheets writer finds platform row + month column → MCP `gsheets_update_cell` updates 3 cells (amount, FX date, FX rate) → SEK formula recalculates automatically. [sigh-000, 2026-06-07]
- Built `umbrella/sales-insights/sheets_writer.py` with month normalization, column/row finders, and update plan generator for MCP execution. [sigh-000, 2026-06-07]

## Revenue-Model Pressure-Testing (game forecasting)

- **EA "1.0 spike" is a myth for most titles.** GameDiscoverCo's 2026 EA-graduates dataset (91 paid titles, gated to >5K copies): only **21% earned more revenue at 1.0 than in their first 30 days of EA** (20% in 2025 - stable). Median EA duration 1y3m. The big EA cash beat is the EA LAUNCH, not the 1.0 launch. Never model "the 1.0 spike lands" as a base-case revenue driver; it's a ~1-in-5 outcome. [Ironcrest/Paradox case, 2026-06-22]
- GDCo explicitly **trends LOW on revenue estimates for "core" genres like strategy** - their own caveat. So strategy-title comps drawn from GDCo/Alinea estimates are conservative, not optimistic. [GameDiscoverCo "EA graduates 2026" email, 2026-06-22]
- **House wishlist-conversion benchmark tiers** (from AP's own Rust Racers financing model, GDrive `1hPqLh9zO_Bd41zB1AvhcnNX-AEO50piBNgz_k12k-30`): Week 1 = 10-30% of wishlists; Month 1 = 15-40% (≈ wk1 ×1.1-1.3); **Year 1 = 30-90% (≈ month1 ×2-3)**. This is the right tool for LIFETIME conversion - far better than bolting the GDCo 0.2x first-week median onto a vague "several times first-week" multiplier. Refund penalty ~10%, refund range 3-17% (avg 10%). Sales/review ratio 20-60 (median 40), not the 30 in our skill. [Ironcrest case, 2026-06-22]
- **Wishlist→sales is NOT linear in wishlist count.** Big wishlist banks (1M+) convert at LOWER % than small ones because large banks accrete low-intent/old wishlists. Manor Lords: 3.2M WL → 1M day-1 (~31% day-1) → **26% LIFETIME** conversion. Cap conversion % as the bank grows; don't apply a small-game 0.2-0.4x to a publisher-inflated bank. [web, gamedeveloper.com / levvvel, 2026-06-22]
- **Comps for grand-strategy unit forecasts:** Manor Lords 2M in <3wk EA, ~3M+ lifetime, 3.2M WL (the broad-accessible outlier). CK3 1M in month 1 (2020) → 2M (Mar'22) → 3M (Sep'23) → **4M (Apr'25)** across PC+console - i.e. the deep end takes ~5 years to reach 4M, only ~1M in year 1. So a 2-year base-game forecast for a between-the-two title should sit well under both year-1 figures. [paradoxinteractive.com press releases, 2026-06-22]
- **DLC attach hard estimates (Alinea):** StarRupture Supporter Pack 55% attach early → settled ~24% as base grew (a $4 pack). Monster Train 2 roguelike DLC 21% attach (the high end for a ~$10 expansion). Chris Z's HTMAG survey gave a "Silver 40%" median but that's small self-selected sample - prefer Alinea's hard estimates. Steam baseline DLC attach is **low single digits** across most genres; engaged strategy/roguelike bases are the exception. [Alinea Analytics + Chris Z HTMAG emails, 2026-06-22]
- **Paradox DLC economics:** lifetime DLC revenue OFTEN EXCEEDS base-game revenue for grand-strategy titles, but that is a 5-10 YEAR figure (CK3 ~EUR 250 DLC library built over years + subscription). Over a 2-year window DLC is a fraction of base, not a multiple - the multiple only shows up in years 3-10. Modelling 2-yr DLC at +30/50/70% of base is defensible-to-generous for the window; the real DLC story is post-window. [web + paradox_publishing_model skill, 2026-06-22]
- **Net-per-unit sanity for a EUR 30-40 premium-strategy title sold heavily on discount over 2yr:** headline price × 0.7 (Steam) × ~0.65-0.70 (blended discount depth + regional + refund over a 2-yr discount-heavy tail) → for a EUR 30-40 title, blended realised net lands ~EUR 13-17. EUR 15 is a fair MIDPOINT. The bear case should use the low end (heavier discounting in a slow-seller scenario pulls realised price down faster - see Rust Racers attenuation curve). [Ironcrest case, 2026-06-22]

## Regional PlayStation Report Discovery

- GDrive contains example reports for building SIEE and SIEAsia parsers: SIEE at `1OMVcoZPNNzNr_JqhacsnZn9m4nFCIKug` (Publisher Statement.XLSX), SIEAsia at `18Pb2azu2MTpTZlfh_fW-QJlzgPruvkpP` (ROYALTY_JAN-2026_6195104501_EUR.xlsx). Both use same base64 → openpyxl flow as existing SIEA parser. [sigh-000, 2026-06-07]
- Built SIEE parser (`parse_siee.py`) and SIEAsia parser (`parse_siee_asia.py`) following SIEA pattern. Both ready for testing and wiring to Sheets writer. Pattern works: base64 XLSX → openpyxl → search for Aurora Punks titles → extract period/vendor/amounts. [sigh-000, 2026-06-08]

## Counterparty Due Diligence (before sharing a data room)

- **Before a financials/cap-table/IP data room goes to an inbound "investor," run a public-source counterparty check** — it's pure CAN-DO research and often the highest-value autonomous contribution when the deal-design items are all Robert/Lawyer-gated. Cross-reference the person's actual career (LinkedIn/RocketReach/press) against the role they're claiming: a career PR/marketing/BD exec framing a $1.5-2M "infusion" is a different risk profile than a fund GP with a cheque-writing track record. [apb-029 Erik Reynolds, 2026-07-07]
- **A signed NDA covers confidentiality only — not source of funds, mandate to represent third-party capital, or deal structure.** Those are separate questions the NDA doesn't answer; flag them before sensitive material ships. [apb-029, 2026-07-07]
- **Watch the exact deal language in the inbound email.** Erik asked to infuse capital "as a fixed contract" — non-standard equity phrasing that hinted at a services/structured-funding or broker arrangement, and it didn't match the Direct-AP-equity frame the corp draft was built on. Frame mismatches between what the counterparty said and what the internal draft assumes are worth surfacing early. [apb-029, 2026-07-07]
- **Red-flag pattern:** a counterparty whose own company/studio is itself actively fundraising while simultaneously offering to deploy 7-figure capital elsewhere. Not disqualifying (separate pots possible) but a flag, not a reassurance. [apb-029 Erik Reynolds / Afrime Studios, 2026-07-07]
- **Gmail MCP:** `gmail_read`/`gmail_thread` take the internal message/thread id but the param is `threadId` (camelCase); `thread_id` errors "Invalid id value." Use `gmail_search` to confirm the threadId first. [apb-029, 2026-07-07]

## Intangible Asset Valuation for Audit (game-on-balance-sheet)

- **Verify the publisher before forecasting - the brief may be wrong.** Vessels of Decay's publisher is **Headup Games GmbH** (Düren), NOT Kinda Brave/Windup. Kinda Brave/Windup publish other AP titles (GFF, Distant Bloom). Always confirm the actual store-page publisher + appid via WebSearch/Steam before building a revenue model. [aurora-punks / vessels-of-decay, 2026-07-15]
- **For an intangible-asset impairment sanity-check, the relevant figure is FUTURE net revenue to the entity, not lifetime gross or already-received advances.** VoD's €108k dev funding was received in 2024 (past); the impairment test needs future royalty PV vs carrying value. Separate the two explicitly for the auditor. [aurora-punks / asset-valuation, 2026-07-15]
- **Read the recoup waterfall to get the entity's actual share.** VoD Headup deal: 20% AP / 80% Headup from day one, flips to 50/50 only when project NET revenue hits €195k (Headup recoups €156k external costs from its 80%, not internal salaries). If projected lifetime net never reaches the flip threshold, the entity stays on the low share the whole horizon - model that, don't assume the 50/50 kicks in. [aurora-punks / vessels-of-decay, 2026-07-15]
- **A launched underperformer is easy to size via Boxleiter:** review-count × 30-50 = units. VoD: 23 Steam reviews (52% Mixed) after 13 months, ~1,800 followers, peak CCU 1, permanent 90% discount → ~700-1,150 Steam units, low-thousands all-platform. That was ~10× BELOW the publisher's own "bad case" (19k units). Publisher pre-launch forecasts (Headup gave bad/med/good = 19k/40k/100k) are a useful upper-bound anchor but realised performance can run an order of magnitude under. [aurora-punks / vessels-of-decay, 2026-07-15]
- **Ownership chain is a gate BEFORE valuation for audit work.** VoD's title chain is not cleanly AP (2022 Överlåtelseavtal CZP↔Blackdrop + Neon Artery buyout clause; canonical doc `aurora_punks/ap_ip_ownership_canonical.md`). Under ÅRL 4:6 an uppskrivning requires the entity to own the asset AND a reliable/lasting value. Flag ownership uncertainty to the auditor separately from the revenue read. [aurora-punks / asset-valuation, 2026-07-15]
  - **CORRECTION (Robert, 2026-07-15):** IP till VoD ägs av **Aurora Punks AB**; ägarkedjefrågan är hanterad och stängd av Lawyer. Återflagga den inte i onödan. Signerat avtal + ägande dokumenterat i [[reference_vessels_of_decay]].
- **Impairment framing that lands with a Swedish auditor:** återvinningsvärde = max(nyttjandevärde = PV of future entity royalties, verkligt värde − försäljningskostnader). State plainly when base-case future net (VoD: ~62k SEK) is a tiny fraction (<3%) of carrying value (2,000,000 SEK) → tydlig indikation på nedskrivningsbehov; recommend formal nedskrivningsprövning + likely reversal of the write-up. Show what units/net would be REQUIRED to support the carrying value (VoD needed ~€875k project net ≈ ~195k units ≈ 2× publisher good-case) to make the gap concrete. [aurora-punks / asset-valuation, 2026-07-15]
- **German withholding tax 15.825%** (15% + 5.5% soli) is withheld by German publishers (Headup) on royalties to foreign partners until an exemption certificate is obtained (~2yr backlog). Creditable but a real liquidity drag - note it in cash-flow forecasts for any German-published title. [aurora-punks / vessels-of-decay, 2026-07-15]

## YouTube Data API v3 as a Research Tool (not just a poller)

- **YouTube Data API v3 answers "does this channel exist / what has it posted" questions that WebFetch/WebSearch can't** — `youtube.com/channel/...` and `youtube.com/watch?v=...` are consent-walled/CAPTCHA'd for the VPS's IP (same block noted in `reference_vps_web_collection_limits` for comment scraping), so WebFetch on a channel or video URL just bounces through a Google consent/sorry redirect. The Data API's `channels.list` (part=snippet,statistics) and `search.list` endpoints are NOT blocked and return authoritative data (real title, description, subscriber/view/video counts, upload dates) for the cost of a couple quota units. Use this whenever a "does X's YouTube exist / is it the real one" question comes up — don't rely on WebSearch snippets alone to confirm identity; cross-check with a direct API call. [db-055, 2026-08-20]
- **This resolved a real open item:** `aurora_punks/community_config.json` had no YouTube channel because `skills/client_channels.md` had carried "Existence unknown" for months (open item in the Phase 0 comms-relaunch audit, apb-040). One `channels.list` call confirmed `@aurorapunks` / `UCN5MWCq05Yj47EELO6Pvo7w` is real (description matches AP's own publisher copy verbatim, uploads include known AP titles KreatureKind/Vessels of Decay/Sir Whoopass) and dormant since 2025-06-27. Existence ≠ access — posting/admin rights are still a separate, unresolved question. [db-055 / apb-040, 2026-08-20]
- **`search.list` for "<game title>" is the fast way to build a `video_ids` watchlist for third-party streamer coverage** — filter results to recent uploads (last few months) and exclude the dev's own channel's videos (those are already covered by `channel_ids` polling, no need to double-list). An actively-posting Let's Play series (multiple episodes within weeks) is a better dev-directed-comment target than a single 2-3 year old video, even a higher-view one — prioritize recency/activity over view count for a comment tracker (as opposed to a KPI/reach report, where view count would matter more). [db-055 Tears of Adria, 2026-08-20]

## Bankruptcy Entity Transitions (Platform Storefronts)

- **Steam/Steamworks entity swap** is a support-channel process, not self-service settings. When a publisher entity enters konkurs (bankruptcy), Valve blocks account mirror-swaps — the old account/assets are property of the konkursbo (bankruptcy estate). The acquiring entity must file a support request asking Valve to either (a) update company-info/payee on the SAME account (legal name → new entity, new bank, new W-8BEN-E), OR (b) transfer apps to a new account. Valve must decide which path. CorpBot pattern: draft a support request + Letter of Consent (mirroring the Microsoft Partner Center precedent) + attach the signed Asset Transfer Agreement from the bankruptcy sale. Robert files via Steamworks → Payments, Banks & Taxes → Contact the Steam Team. [apb-026, 2026-06-25]
- **Platform payment flow during konkurs:** As of late Apr 2026, Valve was still paying revenue to the bankrupt APDS entity months after konkurs filing (12 Dec 2025). Flag payee redirection as URGENT in the support request to ensure post-acquisition revenue flows to the acquirer (CZP), not the konkursbo. [apb-026, 2026-06-25]
- **Sibling platform:** PlayStation (apb-015) is undergoing the same CZP entity swap via PS Partners channel (ticket CS0157316, status TBD). [apb-026, 2026-06-25]


## VoD Headup deal - actual signed terms (correction to prior entry)

- **The SIGNED Headup "License and Publishing Agreement" was located in Drive** (`LicAgr_Vessels_of_Decay_Headup_AP_projectinfo_rev1`, Google Doc; also `..._rev2.docx`). Party on the dev side is **Aurora Punks Development Services AB** (now invoiced via CZP subsidiary), not AP AB. Always find the actual signed agreement before modelling - the "Terms Proposal" email thread was a negotiation draft. [aurora-punks / vessels-of-decay, 2026-07-15]
- **Actual Annex 8 "Share model": Developer gets 20% of all Gross Revenue from day one during recoup, then 50% of Gross Revenue AFTER Headup recoups all "Headup External Costs."** This REFUTES a "recoup-first, 0 to dev until recouped" reading - the dev takes 20% from the first sale. [aurora-punks / vessels-of-decay, 2026-07-15]
- **"Gross Revenue" is defined as "all monies received on Headup's banking accounts relating to the Publishing"** - i.e. post-platform-cut receipts to the publisher, with NO further deduction on the dev's %. It is NOT gross consumer spend and NOT a "net receipts after costs" figure. The dev % is a straight cut of what the publisher banks. [aurora-punks / vessels-of-decay, 2026-07-15]
- **Recoup pool = "Headup External Costs" = external dev+publishing costs PLUS the €108k Development Funding Payment (fully recoupable), ~€156k total.** Under the 20/80 split during recoup, ~€195k cumulative Gross Revenue is needed before the flip to 50/50. Net effect: a weak title never reaches the flip, so the dev is locked at 20% of a small Gross Revenue - the recoup mechanic caps the upside, which STRENGTHENS an impairment case. [aurora-punks / asset-valuation, 2026-07-15]
- **Watch for a downstream developer layer under the AP entity.** For VoD, Neon Artery / Simon Jakobsson (via Bright Gambit "Option C", Oct 2024) gets a 450k SEK licence fee + 30% of net after Headup, reducing AP's retained net by ~30% below its Headup share. When the balance-sheet holder is a middle party, model both the publisher->holder split AND the holder->original-dev split. [aurora-punks / vessels-of-decay, 2026-07-15]
- **Live signal that royalties actually flow:** AP/CZP sent a "Vessels of Decay Revenue invoice" to Headup in March 2026, and the entity change broke Headup's German withholding-tax exemption (filed for AP, must be refiled for the new invoicing entity). Confirms 20%-from-day-one, not zero. [aurora-punks / vessels-of-decay, 2026-07-15]
- **Tooling note:** uploaded .docx in Drive returns "docx_not_extracted" via rag_get_doc (no body); the native Google Doc version reads cleanly. Large native-doc rag_get_doc results (>25KB) persist to a tool-results JSON file - grep it for the contract clauses (Recoup/Revenue Share/Gross Revenue/External Costs) rather than reading the whole thing. [aurora-punks, 2026-07-15]
