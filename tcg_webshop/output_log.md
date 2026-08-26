# TCG Webshop — Output Log

## 2026-06-16 — Homepage concept v1 (UIbot)
- Delivered `drafts/tcg_webshop_homepage.html` — self-contained HTML/CSS mockup of a trading-card-game webshop homepage, Pokémon-first.
- Direction confirmed with Robert: homepage/landing scope, "Bold TCG card-frame" aesthetic, styled HTML mockup.
- References given: Cardmarket / CoolStuffInc (functional baseline), Pokémon/Nintendo game look as the visual upgrade.
- Build: deep holo-navy bg + gold card-frame product tiles, energy-type orb nav, holo hero card with sheen sweep, Lilita One display + Nunito body. Mock catalogue (Charizard ex, Pikachu ex, Umbreon VMAX etc.) rendered client-side.
- Verified via Playwright at 1440px (desktop) + 390px (mobile) — screenshots saved alongside (`tcg-desktop.png`, `tcg-mobile.png`).
- Placeholder shop name "HoloVault" — flagged as placeholder, awaiting Robert's brand.
- Not billable (TCG track sits under Personal Listings future branch).

## 2026-06-16 — TCG grading market & legal scan (BizDev)
- Delivered `web-scan.md` — market-landscape scan of the card-grading business + legal/licensing answer, scoped as a Pokémon-first grading bolt-on to the webshop.
- Direction confirmed with Robert via /bizdev: role = bolt-on to webshop (not standalone co), depth = landscape scan + legal obstacles (manufacturer licence question), scope = Pokémon-first.
- Key findings: (1) EU-gap thesis real but closing — PSA opens Frankfurt facility summer 2026; Ace Grading/PCA/CCC/Cardmarket Grading already exist. (2) No manufacturer licence needed to grade Pokémon cards — whole industry is unlicensed; only trademark guardrails apply; no precedent of Pokémon suing a grader. (3) Recommendation: become a PSA/CGC submission hub / group-submitter, not a de-novo grading brand — brand-trust moat makes a new slab low-liquidity.
- Not billable.

## 2026-06-16 — Published as temp to runatyr
- Live at https://pitch.runatyr.games/tcg-shop (slug `tcg-shop`, served from `pitches/tcg-shop/index.html`).
- Public, self-contained (Google Fonts CDN + inline SVG + CSS gradients, no local assets). Verified 200 local + public, rendered live via Playwright.

## 2026-06-16 — PSA Frankfurt dealer-path addendum (BizDev)
- Appended "PSA Frankfurt dealer path & batch-submission economics" section to `web-scan.md` per Robert's follow-up.
- Findings: PSA Europe opens dealer/partner channel first (subs July 2026, grading Aug); authorized-dealer gate (2yr full-time + $10k cap + 3 PSA-dealer references) blocks a brand-new shop — so reseller/concierge or dealer-partner first, direct status as a 1-2yr destination; UK middlemen (Black Label Grading, The Sub Center) are the model to copy; structural EU wedge = intra-EU/no-customs Frankfurt-fed hub vs UK incumbents.
- Next moves flagged: email PSA Europe dealer relations (apps open July), price a reseller-model pilot, get Cardmarket Grading terms, insurance quote.
- Not billable.

## 2026-06-16 — Cardmarket Grading comp (BizDev)
- Appended "Addendum 2 — Cardmarket Grading comp" to `web-scan.md`; corrected the earlier "most dangerous competitor" framing (Section 2 bullet 4 flagged DEFUNCT).
- Finding: Cardmarket Grading (launched late 2021 w/ German grader Guard & Grading Solutions, marketplace-integrated, QR pop-report slabs) was SHUT DOWN in 2024 — the exact bolt-on model being contemplated, with every advantage, and it still failed on the liquidity/trust moat. Facility now houses Beckett's EU grading op. Cardmarket pivoted to neutral marketplace + third-party grading partners (channel, not competitor).
- Corrected landscape: Beckett grading in NW Germany since Jan 2025 (~€20 Base/€36 Standard), PSA Frankfurt July/Aug 2026 — both trusted slabs now produced intra-EU. Wedge narrows to service + retail attach; Nordic-consolidating drop-off/mail-in hub batching to Germany is the concrete play.
- Not billable.

## 2026-06-16 — Real logo integrated + header reworked
- Robert supplied crest emblem logo (`ChatGPT Image...png`, 1254x1254, white bg). Saved source as `drafts/logo-source.png`.
- Knocked out white background via edge flood-fill (preserves interior silver/white), auto-trimmed to 1241x806 → `logo.png`.
- Reworked header: search-left / centered crest / account+cart-right, gold hairline + glow behind logo. Footer logo swapped to image. Removed old text wordmark + .mark CSS usage.
- Published logo + page to https://pitch.runatyr.games/tcg-shop ; verified live desktop 1440 + mobile 390.

## 2026-08-03 — Pre-grade engine, Fas 1 (photo folder in, PSA band out)
- Delivered `pregrade/` — recurring pipeline: `intake/<batch>/<card>/` photos in, per-card markdown + batch `summary.csv` out. Direction confirmed with Robert: recurring capability, folder-based intake.
- Split by design: **centering is measured, not guessed** (OpenCV card-quad detection → perspective warp → colour-transition scan from each edge → PSA tolerance table). Everything else (corners, edges, surface, print, authenticity) goes to a vision pass that is handed the measured centering as fact and forbidden from re-estimating it.
- Honesty rules baked into the prompt: no raking-light shot → surface marked unassessable and capped at 9; no corner macros → corners capped at 9. The tool therefore cannot claim "10 likely" from a single flat phone photo.
- `selftest.py` renders synthetic cards with known border widths and validates the measurement end to end: 13/13 pass, accuracy within ~1 percentage point, including 7° and 12° rotated shots.
- Backend follows the VPS reality: shells out to `claude -p` on the Max subscription (same pattern as `server.js`), since `ANTHROPIC_API_KEY` has been commented out of `assistant/.env` since db-036. SDK + structured-outputs path kept for if a console key returns. Model resolved from `config.json` `model_tiers.opus`, never hardcoded.
- `value.py` computes EV (grade distribution → graded net vs raw net) only when comps are supplied via `card.json`. No price is ever invented; grading-cost constants flagged as placeholders until the PSA Europe dealer path is priced.
- `PHOTO_PROTOCOL.md` — the six shots per card and what each one unlocks.
- Open: iOS client (Fas 2) blocked on Apple Developer account + stack decision. VPS cannot build native iOS (no macOS); path is Expo + EAS cloud builds.
- Not billable.

## 2026-06-17 — One-page business case (BizDev)
- Delivered `business-case.md` — personal-economy framing, one-page verdict per Robert.
- Verdict: **conditional GO but reframe.** Not a singles webshop (loses head-on to Cardmarket on liquidity/margin); build a brand + Nordic grading-concierge hub on the Lister pipeline, sell commodity singles via Cardmarket/eBay. 4 reasons: margin is in graded+service not singles; marketplace-integrated EU grading already failed (Cardmarket Grading); infra mostly exists (mkt-000 Lister backbone); PSA-Frankfurt/Beckett timing opens the Nordic concierge seam.
- First move: cheap grading-concierge waitlist on the existing landing page before any commerce build; keep selling owned cards via Lister now; park full webshop build until demand shows; rename (Mastercard conflict) via Lawyer.
- Logged to tcg-001. Not billable.

## 2026-08-05 — App + API, väg mot TestFlight

**Beslut:** hoppa över mellanstegen (browser-preview, Expo Go) och gå direkt mot
TestFlight, enligt Roberts önskemål. Mitigering för den långa byggloopen: EAS Update
inkopplat från start, så JS-ändringar når appen på ~1 min utan nytt bygge.

**Byggt:**
- `app/` — Expo SDK 57 / RN 0.86, expo-router. Fångstflöde för alla sju bilder med
  ramhjälp per bildtyp, mörk runatyr-palett (så skärmen inte kastar ljus på kortet),
  rapportskärm i AP paper-palett. Bundlar rent för iOS: 1134 moduler, 2,4 MB Hermes.
- `api/server.py` — stdlib HTTP-API framför motorn på 127.0.0.1:3786. Bearer-auth
  som fallerar stängt, loopback-bypass för CLI:t, allowlist mot path traversal,
  bakgrundsjobb + polling eftersom vision-passet tar 30-90s.
- `pregrade-api.service` — user-service, enabled + active.

**Verifierat end-to-end:** syntetiskt kort 58/42 fram → mätt 58/42, takat PSA 9
(korrekt: 10 kräver 55, 9 tillåter 60). Baksida 72/28 → mätt 71/29. Band 8-9, KANSKE.
EV rapporterar "comps saknas" i stället för att hitta på en siffra.
Auth-gräns: 401 utan token, 401 med fel token, 200 med rätt, 400 på traversal.

**Rättat:** PHOTO_PROTOCOL sa "sex bilder" men listade sju. API-adaptern läste en
`ratio`-nyckel som inte finns (hade renderat [object Object]); använder nu
`psa.worse_axis()`, samma funktion som pipelinen, så appen visar den axel taket
faktiskt kom från.

**Blockerat på Robert:** App Store Connect API-nyckel (Issuer ID + Key ID + .p8) och
ett Expo-konto med access token. Utan dem kan EAS varken signera eller ladda upp.

**Öppen fråga:** `grade.runatyr.games` kräver att tunnelns ingress skrivs om.
CLOUDFLARE_API_TOKEN kan läsa configen (16 regler). Skrivningen ersätter hela
ingress-arrayen, alltså 15 andra hostnames i samma anrop. Inte gjord utan godkännande.
