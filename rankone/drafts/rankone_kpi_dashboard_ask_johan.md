# The KPI dashboard we need from Johan

Draft v1 - prepared for the Robert + Peter sync (Wed Jun 17, 10:00). Refine live, then hand to Johan.

## Why this exists
RankOne reports the wrong scoreboard. The shareholder updates lead with cumulative users (101,155) and Twitch reach (77.8M) - both top-of-funnel vanity numbers. A growth investor or an acquirer underwrites a different set: the rate of new growth, how well the product holds people, and whether the B2B Insights line turns the data asset into revenue. Right now those numbers are either buried or absent.

The ask to Johan is simple: one monthly dashboard, same cadence as State of RankOne, built around what a buyer or a lead investor actually diligences. Not more reporting work - a sharper scoreboard that also tells the team where to push.

## The dashboard - 7 metrics in 4 groups

### A. Growth (is the curve bending?)
1. **New-user growth RATE, monthly** - net new signups / prior-month base, as a %. Not the cumulative count. We already estimate this at ~1.7-1.9%/mo (roughly flat ~1.5-1.8k net adds for years). We need Johan's exact monthly series so we stop guessing.
   - *Why:* a growth VC needs to see this accelerating. Flat/decelerating % is the single fact that has held the raise back for 5 years.
2. **Acquisition channel mix + CAC** - where the new users come from (streamer-driven, organic, paid, Steam import) and blended cost per acquired user. Historically cited at ~10 SEK/user via streamers.
   - *Why:* tells us whether growth is repeatable and whether it scales with spend, or whether it is a fixed organic trickle.

### B. Engagement and retention (does it hold people?)
3. **Retention cohorts** - D1 / D7 / D30 (or month-N) curves by signup cohort, last 6-12 months. The deck shows 1-day 42.8%, 7-day 36.3% (up from 32.8% YoY), 30-day 26.7% - genuinely the strongest number RankOne has. We need it as a living cohort table, not a single snapshot.
   - *Why:* for a data/social product this is THE number. It is also the asset's best story - it is improving while the base grows.
4. **Activation rate** - % of new signups who build a real profile (e.g. add N games / write 1 review) within 7 days.
   - *Why:* separates the ~18.8k engaged MAU from the 80% who bounced. Shows whether the funnel converts a signup into a user.
5. **Engagement depth per active user** - games logged + reviews written per MAU. The aggregate (2.6M relations +51%, 413k reviews +60%) is strong; we need it per-active to prove the core is deepening, not just accumulating.
   - *Why:* depth per user is what makes the taste-graph defensible and the data sellable.

### C. Monetization / B2B (is there a revenue engine?)
6. **B2B Insights traction** - number of paying dev customers, named pipeline, ACV / ARR. This is the money metric and it is essentially absent from every update.
   - *Why:* this is the entire profitability case and half the acquisition case. If there is an ARR line, even small, it changes the conversation. If there is not, we need to know that today.
   - *Also capture, separately:* the consumer subscription tiers (Rankone+ $5, Create $39, Pro $295) - paying-subscriber count + conversion % vs the 1-1.5% plan assumption, once they are actually live.

### D. The data asset (what an acquirer is really buying)
7. **Data coverage / uniqueness** - size and growth of the curated relation graph, plus a coverage/uniqueness read vs comparable datasets (what does RankOne have that Newzoo / Sensor Tower / VGI / Steam do not).
   - *Why:* an acquirer underwrites the dataset, not the app. Peter (Newzoo) is the right person to define what "valuable and defensible" looks like here.

## First cut - keep it light
If asking for all 7 at once stalls it, the non-negotiable first five are **1 (growth rate), 3 (retention cohorts), 4 (activation), 6 (B2B ARR/pipeline)** and a single honest line on **2 (CAC)**. Those four-plus tell us, within a month, which fork RankOne can actually fund. The rest can follow.

## Format and cadence
- One slide or one sheet, refreshed monthly alongside State of RankOne.
- Trends over time, not point-in-time snapshots - every metric as a 6-12 month series.
- Honest is better than flattering. A weak retention curve we can act on beats a vanity number we cannot.

## The framing for Johan (Robert to voice)
Not "your reporting is wrong." More: "if we are going to take the commercial side seriously - whether that is a real raise or a profitability push - we need to be looking at the same scoreboard a buyer looks at. Here is the dashboard. Most of it you already have; some of it (B2B ARR, cohorts) we just need surfaced. Can we build this together this month?"

---
*Sourced from: rankone_peter_sync_prep.md, wiki/company/rankone.md, State of RankOne 2026-05-18, Future of Creation v2.1 deck. Numbers to be replaced with Johan's actuals once the dashboard exists.*
