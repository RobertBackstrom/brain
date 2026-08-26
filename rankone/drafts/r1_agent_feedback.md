# Candid feedback on the R1 agent (r1-agent.fly.dev)

**From:** the Aurora Punks AI assistant (the agent that actually drove R1, not a human clicking through the UI)
**Window:** late June 2026, first week of access
**Used on:** two live commercial pitches - Curveball / "Major League Curveball" (Roblox Blade Ball as the reference audience) and Flightball / Formula Drone (Knockout City-adjacent audience). Both were real deliverables that went in front of partners, so this is feedback from production use, not a kick-the-tyres demo.

A note on who's writing: I consumed R1 programmatically, by driving the web app with a headless browser, because there's no API. That shapes a lot of what follows. A human poking at the chat box would not hit half of these. But for the "AI data monetization" thesis to land, the heaviest users of this thing are going to be machines, so the machine's-eye view is the relevant one.

---

## What's genuinely good

1. **The differentiated data is the over-index data.** Psychographic over-index (Blade Ball: Party Themes 2.09x, Last Man Standing 2.03x, Arcade Action 1.70x) and cross-game affinity (Friday Night Funkin' 3.19x, Brawl Stars 3.07x, Stumble Guys 2.60x) are the numbers I could not have gotten cleanly from GameDiscoverCo, SteamDB, or Newzoo. That is the asset. When R1 leads with affinity and over-index, it's doing something nobody else does.

2. **Roblox / UGC coverage.** Getting behavioral and affinity data on a Roblox experience (Blade Ball) is rare. Most market-intel tools are Steam-centric and go blind the moment the audience is on Roblox or mobile-native. R1 didn't. That alone made it worth running for the Curveball pitch.

3. **Reachable-profile counts are the killer feature and they're underplayed.** "1,855 profiles / ~860k player reach, reachable for playtest, survey, creator outreach" turns an intel report into an actionable channel. Nobody else can say "and here are the actual people." This should be the headline of the product, not a footnote at the bottom of a block.

4. **Source transparency.** Citing the profile count behind each block (1,855 for the Blade Ball audience, 1,744 for the KPI set, 282 for the PC comparables) is good practice and built trust. I left those citations in the pitch deliverable verbatim.

5. **It will disagree with you, with reasoning.** On Curveball, our brief was a sub-$10 price. R1 pushed back unprompted, argued for $14.99-19.99, and backed it with a comparables read (Lethal League Blaze as the premium-success model, Knockout City as the cautionary F2P-collapse case). That was the single most useful output of the session. More on this under "the advisory behavior" below, because it's a strength that needs a guardrail.

---

## What's inconsistent or concerning

1. **The headline numbers are wide ranges, and it's not always clear which are proprietary.** Blade Ball came back as MAU ~15M-25M, DAU ~1.2M-2.0M, peak CCU 100k-250k. Ranges that wide read like modeled estimates, not measured data. The problem isn't the ranges themselves, it's that they sit in the same block, same formatting, as the tight proprietary numbers (the over-index multipliers). I genuinely could not tell, from the output alone, which figures came from RankOne's curated profiles and which came from web search plus inference. For a data product, that line has to be visible.

2. **Profile counts shift per query and don't obviously reconcile.** 1,855 here, 1,744 there, 282 for comparables. That's probably correct (different queries hit different sub-populations), but to a consumer it looks like the n is being chosen after the fact. And 282 profiles underpinning a pricing recommendation is a thin base to hang a "$14.99-19.99 is optimal" call on. Surfacing a confidence level, or the n, next to each claim would help me decide how hard to lean on it.

3. **Determinism is untested and I'd bet it's low.** I didn't run the same query twice in the same session, but everything about the architecture (web search plus LLM reasoning in the loop) says the same prompt would give different numbers on a re-run. For pitch work that's a real problem: if I cite "100k-250k CCU" today and someone re-queries next week and gets "80k-200k," the deliverable looks unreliable through no fault of the deck. A "data mode" that returns the underlying RankOne figures deterministically, separate from the reasoned narrative, would fix this.

4. **Output is prose, not structured.** Every answer is markdown tables plus paragraphs, with the structure varying between queries. I had to scrape the rendered text and hand-restructure it into the intel doc. Two queries about the same kind of thing (an audience profile) came back with different section orders and different fields populated. For a human reading one answer, fine. For anything programmatic or comparative, it means custom parsing every time.

---

## Improvements, roughly in priority order

1. **Ship an API or an MCP server.** This is number one by a wide margin. Right now the only way in is a password-gated React SPA, which I drove with headless Playwright: log in, click "New chat," fill the composer, press Enter, then poll the textarea's `disabled` state to guess when generation finished. That's brittle glue against a UI that can change at any deploy, and it's the kind of integration that breaks silently. A JSON API (even a thin one: query in, structured intel out, with the proprietary-vs-modeled split and an n/confidence per field) would make R1 a first-class data source instead of something I have to scrape. If the monetization thesis is "feed curated preference data to AI consumers," the API *is* the product.

2. **Separate proprietary data from reasoned narrative in the output.** Two clearly labeled sections: "RankOne measured" (from the profiles, with n) and "RankOne modeled / web-augmented" (the inference layer). I'd trust and cite the first far more aggressively, and I'd stop having to caveat the second.

3. **Cut latency, or make progress machine-readable.** Responses took 60-180 seconds. That's tolerable for one query but punishing when I need five for a pitch, and the "is it done yet" signal is purely visual (the input box greys out). Even without speeding up the reasoning, a streamed status or a completion event would remove the polling guesswork.

4. **Add a data-only mode.** A toggle (or an API flag) that returns just the numbers, deterministically, with no advisory narrative and no web-augmentation. That's what I want 80% of the time when I'm filling a KPI table. Keep the full reasoned mode for the "what should we do" questions.

5. **Promote the reachable-profile / activation angle to the front.** Right now it reads as a stat at the end of an audience block. It's actually the thing that separates R1 from every passive intel tool. Lead with it: "here's the audience, here's its shape, and here are N reachable profiles you can survey or recruit tomorrow."

6. **Expose confidence / sample size per claim.** Even a coarse high/medium/low next to each figure would let a consumer weight it. A 1,855-profile audience read and a 282-profile pricing read should not look equally authoritative on the page.

---

## On the advisory behavior (a strength that needs a guardrail)

R1 doesn't just report, it advises, and the advice was good. The Curveball pricing pushback and the "position this as a reaction-brawler, not a party game" framing were both sharper than a lot of human comps work I've seen. Keep that capability.

But for an intel tool, the boundary between "here is the data" and "here is what you should do" has to be deliberate, not incidental. When the advice contradicts the user's stated brief (as it did with our sub-$10 price), that's exactly when it's most valuable AND most in need of a visible separation, so the consumer can take the data and still make their own call. My suggestion: keep advice on by default, but clearly fenced off from the measured data, and make it suppressible (see the data-only mode above). A toggle between "analyst" and "data feed" would serve both jobs cleanly.

---

## Bottom line

The proprietary affinity, over-index, and reachable-profile data is real and differentiated, and the Roblox/mobile coverage is a genuine edge. The packaging around it is the weak part: no API, prose-only output, wide unlabeled ranges, and an opaque line between measured and modeled. Fix the provenance labeling and ship an API, and R1 goes from "a smart chat box I have to scrape" to "a data source I'd wire into every pitch by default." For the AI-data-monetization direction specifically, that second thing is the whole game.
