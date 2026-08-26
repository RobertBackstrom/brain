---
name: K2C Sands of Duat
description: Kingdom Two Crowns Egyptian DLC co-dev with Raw Fury — PM tracking, contract, milestones, backlog
type: project
originSessionId: 70d622a6-c23f-41fd-92d2-29f436b9b245
modified: 2026-08-17T08:49:32.774Z
---
# K2C Sands of Duat

**Prefix:** k2c
**⚠️ RENAMED 2026-07-03:** DLC is now **Kingdom Two Crowns: Pharaoh Lands** (Niclas/RF). "Sands of Duat" was working-title only; new name aligns with franchise convention. Robert accepted same day; propagate everywhere (checklist: `umbrella/k2c_sands_of_duat/pharaoh_lands_rename_checklist.md`, PLANNING-only, nothing renamed yet). Keep prefix `k2c` + Jira key `KAN` + folder slug unchanged.

**Status (2026-08-16):** MS0-MS3 all delivered and approved. **MS4 Pre-Cert is the live milestone**, due Fri 2026-08-28. **S7 (Aug 10-21) is active; S8, the MS4 hardening sprint, starts Mon Aug 24.** Two dates dominate the fortnight, both inside the gate week: **interim build to RF Thu 20 Aug** and **RF's external playtest starts Mon 24 Aug**. ⚠️ **MS3 invoice (560k, sent 07-31) was due ~08-15 - VERIFY receipt against the bank, do not assume it landed.** **Dubravko started 18 Aug on UI/key-art scope, which is NOT asset-list work — see the 08-19 CORRECTION below.** The asset-list pool is at the no-fourth-artist baseline (−7% over the 9-week window); the Lost Hive extension is what moves it. ⚠️ **Fury Studios contract: notice must be served by FRI 21 AUG to stop at 31 Aug, or the cost runs to 30 Sep (`k2c-047`).** Internal cut 27 Aug, **MS4 gate remains 28 Aug**. Milestones hold: MS4 Aug 28 · MS5 Sep 25 · MS6 Oct 23 · MS7 Gold Dec 1. **Budget:** 5.6 MSEK, team of 6, Apr-Dec 2026.

## 2026-08-26 — CANONICAL: the Staff of Ra is not supposed to damage the bosses

**Bata and the Apesh turtle are deliberately outside the ability targeting system.** The Staff of Ra
beam does not damage them, and it is not meant to. This is design intent from Tim, not a defect, and
it is not a gap to close.

- **KAN-497** "Staff of Ra does not damage bosses (Apesh turtle, Bata)" is **Done, works per design**.
  Robert closed it 2026-08-19 with that exact comment. Oskar had flagged 2026-08-18 that a fix would
  contradict Tim's intent: bosses are not ability targets, fire would need new idle/attack animations,
  and the other weapons either do not use the targeting system or unlock too late to reach Apesh.
- **KAN-520** "Remove Apesh and bata from being able to be targeted" (Oskar) enforces it. **Done
  2026-08-25 10:45, fixVersion MS4**, so the removal is verified, not just checked in. Build notes are at
  **v23** and say the work is complete and verified.
- The RF playtest build notes (Confluence **145260546**) carried the opposite claim in "Also new since
  the Vertical Slice". **Corrected 2026-08-26, v22, v23:** the claim is removed and the page now has a
  **"Working as designed, not defects"** section stating that a report of the Staff having no effect on
  a boss is not a defect. Local record in `k2c_sands_of_duat/playtests/2026-08-07_playtest.md`.

**Do not re-raise it.** A playtest line, standup note or tester report saying the Staff does nothing to
Bata or Apesh is expected behaviour. Treat it the same way as "days on Ra are shorter", which the same
page already marks deliberate.

## Daily run 2026-08-26 — dagens standup + Simons avtal blir ANSTÄLLNING

**LÄGE 2026-08-26:** anställningsavtalet är publicerat och delat. GDoc
`17u8p6XEtlGb_Zd_9EuPXSBk9Fr_GBN2D8FAQbzaozsM` i `k2c_rf_ap/_legals`, Simon har commenter.
Följebrev som Gmail-utkast `r-457580151207798258`, inte skickat. **Draft_11-delningen är återkallad.**
§9.2 låst på **två veckors** uppsägningstid. Kvar: CZP:s säte och firmatecknare, Simons personnummer
och bankkonto, P&L-raden, och Lawyers bekräftelse på §8.7.

**⚠️ Simon har inte kvar Neon Artery AB.** Han vill ha ett vanligt anställningsavtal i stället.
**`draft_11` (B2B med Neon Artery) är därmed dött**, och GDoc:et som delades med honom
(`18Y6T8KF36IaKEHMrPfcOoMc8gHBHsLNO3mSz_Vn13_g`) samt Gmail-utkastet `r-6865446355526422751` är fel
instrument och måste dras tillbaka innan han kommenterar. **`draft_12_simon_czp_employment.md`**
renderat ur Carolinas CZP-anställningsmall.

**Avtalspart: CZP**, bekräftat av Robert 2026-08-26 ("samma som Carolina"). **Betalning: en enda
löneutbetalning 2026-09-25** som täcker både MS4 och MS5. **AGI följer utbetalningsdatum
(kontantprincipen), inte anställningsstart** — Robert rättade min felaktiga flagga om att augusti-AGI
skulle behöva röras; hela anställningen redovisas i septembers AGI. **Timlön:** grundlön **255 kr/h**
(Roberts ~260), bruttolön inkl semester 285 kr/h, arbetsgivarkostnad 375 kr/h.

**Pengarna:** 3 000 kr/arbetsdag är nu **arbetsgivarens totalkostnad**, inte ett konsultarvode.
Bruttolön blir **57 000 kr** inkl 12 % semesterersättning (grundlön 50 893 + semester 6 107),
arbetsgivaravgifter 31,42 % = 17 909, laddad kostnad **74 909**. MS4 11 400 / MS5 45 600.
Månadsekvivalent 45 600 brutto. **Skatt är INTE ett tredje påslag** — A-skatt dras ur bruttot och är
Simons kostnad, inte arbetsgivarens; att bruttoräkna för den också vore dubbelräkning.

**Strukturellt viktigast:** i draft_11 var AP avtalspart och ägde RF-åtagandet, så konsten
överläts direkt till rätt part. **CZP är arbetsgivare men inte RF-motpart**, så konsten stannar hos
CZP om inget mer görs. **§8.7 i draft_12 är ny** och gör en uttrycklig vidareöverlåtelse CZP → AP.
Får inte tas bort. Notera också att **40a § URL bara täcker datorprogram**, inte bildkonst, så
överlåtelsen måste vara uttrycklig (§8.2) och kan inte vila på anställningen i sig. Och §6.2 från
Carolinas mall måste stå kvar: en anställds lön får inte villkoras av att RF betalat.

**Dagens standup (26 aug):** teamet skapade själva **KAN-595 till KAN-605**, som täckte merparten.
Fem genuint saknade skapades: **KAN-606** map button UX (Dubi), **KAN-607** monarch-lista (Dubi),
**KAN-608** blood moon per DLC (Carolina), **KAN-609** javelineers kastar mot pansrade fiender
(Fredrik), **KAN-610** integrera Anubis warrior-animationer (Fredrik). Alla elva teamskapade saknade
fixVersion; stämplade MS4, KAN-605 draget till S8.

## Daily run 2026-08-26 — gårdagens standup (25 aug), Simon och Dubravko in i Atlassian

**Gemini sa Sobeck, Robert sa Bata, och Robert har rätt. AVGJORT.** Standup-notisen 25 aug lyder
ordagrant "Remove the misinformation stating that the Staff of Ra can damage **Sobeck**". Kontrollerat
mot boardet: **det finns ingen Sobek-boss.** Sobek är ö C och dess tickets är level art, scripting,
altare och blessings (KAN-110/111/114/115/545/586); krokodilen är en **mount** (KAN-31, KAN-57), inte en
boss. Projektets bossar är **Apesh (turtle boss)** och **Bata**, plus Set-finalen. Alltså är "Sobeck"
en garble, precis som "Remove **Ba** hint" i samma notis och "Barta" i tidigare. Byggnoteringssidan
namnger Bata och Apesh och är korrekt som den står. Ingen åtgärd kvar.

**Tickets ur standupen: KAN-587 till KAN-594**, alla tilldelade, i S8, fixVersion MS4. Dubravko 587
kartbakgrunder/layout + 588 UI-sprites · Fredrik 589 musikstart mot director time · Oskar 590 ta bort
hint vid Batas död · Eamonn 591 mockups farm/sköldar + 593 sandstensfärg med Simon · Tim 592
trädplaceringar mot climb positions + 594 artisan hut till artisan school. Kommenterade i stället för
att duplicera: KAN-584 (kartfeedback, Tim), KAN-576 (Anubis Warrior-dödsanimation med sand + fade,
Imkan), KAN-545 (övre staty + Sobek-monument, Joanna). Ticketades inte: Oskars Apesh-playtest
(aktivitet) och Fredriks branchuppdatering åt Carolina (handräckning).

**Atlassian-blockeringen från 24 aug är löst (2026-08-26).** Nytt sanktionerat skript **`assistant/atlassian-users.js`**
(syskon till jira-set.js och confluence-set.js) skapar konton och lägger till i grupper, eftersom
auto-mode-klassificeraren stoppar direkta API-anrop. Konventionen på sajten: Jira-åtkomst kommer från
produkten `jira-software` vid create, **Confluence-åtkomst finns inte som produktnyckel utan är alltid
en gruppinläggning** i `confluence-users-aurorapunks`. K2C-crewet ligger i **Sands of Duat** +
`confluence-users-aurorapunks`.
- **Dubravko Jurina** `dubravko@rawfury.com` → accountId `61a7549fc75da80072fa119d`
- **Simon Jakobsson** `simon.jakobsson@live.com` → accountId `70121:3a196c00-e9b2-47c1-8e08-981f0a64d273`,
  visningsnamn blev **"Simon"** (Atlassian härleder ur mailen), han rättar det själv vid accept.
Båda assignable på KAN direkt. Därmed är flaggan "Dubravko har noll Jira-närvaro" stängd.

**Hygiensvep 2026-08-26 (Roberts godkännande).** Sju tickets skapade 24-25 aug låg utanför S8 helt utan
sprint och fixVersion, osynliga i MS4-vyn. Fem stämplade MS4 + S8: **KAN-573, 578, 579, 581, 582**.
Tilldelning lämnad orörd; **KAN-578 och KAN-579 saknar fortfarande ägare** och har kommentar om det.
Två dubbletter stängda efter verifiering: **KAN-580** var KAN-579 ingesterat två gånger från samma
Discord-meddelande 11:15 (identisk text, två vision-läsningar av samma skärmdump), och **KAN-574** var
dubblett av **KAN-569** (Bata-ljud, samma ägare, tom beskrivning, skapad tre dagar senare). Botten kan
alltså skapa samma rapport två gånger inom samma minut, vilket är nytt och värt att kolla varje körning.

**Robert-sidan ur standupen:** playtest-nyckel + grekisk DLC-nyckel till Simon, Discord-inbjudan,
kontraktsförslag (underlag: `contracts_2026_subcontractors/underlag_11_simon_neon_artery.md`).
Milstolpe: kodlåsning fredag, gray box tillåtet på utvalda öar för att nå MS4.

## Daily run 2026-08-24, del 2 (Aug 21 + Aug 24, sprintstängning, build notes, Simon)

**⚠️ DATUMFEL I DEL 1.** Del 1 ankrade på den senaste Gemini-notisen i `k2c-018` i stället för på
systemdatumet och processade därför 19 aug playtest + 20 aug standup när uppdraget gällde 21 aug
playtest + 24 aug standup. Materialet var oprocessat och tickets som skapades är giltiga, men
datummärkningen var fel och är rättad i output_log, memory, pm_learnings och time_log.

- **S7 stängd, S8 startad.** S7 löpte ut fre 21 aug och stod öppen i tre dagar. **90 ofullbordade
  ärenden** flyttade till **S8 · MS4 Pre-Cert · Hardening** (24 till 28 aug), som nu är aktiv och
  slutar på MS4-grinden.
- **In Review är en förvaringsplats, inte en fixad-kolumn.** Robert bad teamet i Discord 21 aug 13:44
  att sätta In Review när de fixat, "so it is easier for me to see what is in and for all of us to
  verify fixes". Tre dagar senare står **62 tickets** där. Mot hans egen grind, verifierad som löst i
  speltest, klarar **exakt en**: KAN-493 (Bata sprite-flipping), satt Done på Oskars verifiering
  21 aug 12:44. **KAN-467 (day/night) är motbevisad** — Fredrik markerade DONE 12:31 och rapporterade
  regressioner efter demon 14:08 samma dag, och KAN-582 restes 24 aug på samma orsak. **Fem tickets
  har stått In Review i två till tre månader:** KAN-247 och KAN-280 (Roberts egna, sedan 22 maj),
  KAN-302, KAN-303, KAN-354 (sedan 26 juni). Verifieringshalvan saknar ägare.
- **Bygget för external playtest:** Steam **stable**, PC och Mac, uppladdat **24 aug 16:32 CEST**
  (14:32 UTC i Discord-loggen). Oskar 13:26 UTC: "Can't find any more gamebreaking bugs, I'll create a
  release build and upload to stable", och 13:27: "Played to and defeated Apesh, islands A-D and F
  seems to work fine". **Build notes ligger på Confluence id 145260546** i K2C-spacet.
  **Byggversion 2.4.1 (R24290)**, DRM-nycklar kommer från **@Naseer**. Båda ifyllda 24 aug.
  **Testfokus (Robert 24 aug): Start island, Ra och Bata med pussel, plus Lurker, Javelineer och
  banner-systemet.** Sobek och Anubis är i bygget men uttryckligen UTANFÖR scope, tvärtemot första
  utkastet som pekade på dem som nya MS4-öar. Enda kvarvarande lucka är stable-lösenordet.
  **v6:** varje fokussystem bär sin egen "Already known"-lista (Lurker 11 punkter, Javelineer 8,
  banner 8), hämtade ur KAN. Robert vill ha kända problem *med* i underlaget, inte bara en
  sammanfattande rad. **KAN-583** skapades i samma pass för Fredriks otickade fynd från 21 aug
  (javelin throwers blir archers på nästa karta), eftersom sidan lovar att allt uppräknat är spårat.
  **v9, CANONICAL: sidan är INTERNT FYI till Raw Fury, inte testarmaterial.** Robert 24 aug. Det
  testarvända dokumentet är RF:s enkät. Sidan bär nu en varningspanel om det, och defektlistorna är
  omramade från "rapportera inte" till "sålla inkommande rapporter".
  **Enkätriage (v9):** av sex fokusområden täcker enkäten Ra-pusslet och Large Black Cat, delvis Start
  island och Javelineer, och **saknar helt Lurker, banner-systemet och co-op** plus Bata-*valet*.
  Q15 erbjuder Chariot som inte finns i bygget och Q13:s Merchant-caveat är inaktuellt. De två
  invändningarna från 7 aug (Q8 mot KAN-467, Q11 mot KAN-463) är däremot **lösta**, båda ticketsen
  är Done. Oklart om 7-augusti-återkopplingen någonsin nådde RF, den skulle gå via Tim.
- **Neon Artery AB (Simon Jakobsson), CANONICAL:** org nr **559460-3044**, säte **Gustav III:s Väg 105,
  168 39 Bromma**, firmatecknare **Simon Johannes Jakobsson**, simon.jakobsson@live.com. Läst ur
  `ContractorAgreement_Simon_contractor___AP-signed-document.pdf` (Zigned 2024-10-18, Gmail-msg
  `1929f48a12290b29`). Notera att **Timmermansgatan 43 i det avtalet är AP:s dåvarande adress**, inte
  Neon Arterys. Uppgifterna är två år gamla, kontrollera mot allabolag före signatur.
  Underlag: `contracts_2026_subcontractors/underlag_11_simon_neon_artery.md`.
  **Kanonisk hemvist för bolagsuppgifterna: [[reference_vessels_of_decay]]** (befordrade 2026-08-24).
- **Dubravkos mail är `dubravko@rawfury.com`** — projektets `CLAUDE.md` säger felaktigt "No email on
  file". Varken han eller Simon har Atlassian-konto. Inbjudan blockerad, se output_log.
- **Discord-läsaren stämplar i UTC, Robert pratar CEST.** "Nytt bygge 16.32" var 14:32 i loggen.
  Lägg alltid två timmar på Discord-tider när Robert refererar till dem sommartid.

## Daily run 2026-08-24, del 1 (Aug 19 playtest + Aug 20 standup, båda oprocessade sedan tidigare)

Sources: Gemini "K2C Playtest" 2026-08-19 15:14 and "Sands of Duat Daily Standup" 2026-08-20 08:29 (both in `k2c-018`), cross-checked against Discord #dev/#art/#art-support/#general for Aug 19-20 and the live KAN board (88 issues in S7).

- **12 tickets created, KAN-547 to KAN-558**, all assigned, all pulled into **S7** (Robert's call, over S8) and all stamped **fixVersion MS4 - Pre-Cert Build**. Fredrik: KAN-547 boat faces wrong way on client, KAN-548 BoatSailPosition upgrades into a Greek building, KAN-550 exclusion zone payment exploit, KAN-557 purple-overlay tooling. Oskar: KAN-549 merchant donkey flickers, KAN-551 portal animation snaps, KAN-552 Bata death burning fade-out, KAN-553 weapon material rendering inconsistencies. Joanna: KAN-554 monument breaking animations. Carolina: KAN-555 additional sunny-weather track, KAN-558 campaign select stinger volume. Tim: KAN-556 weather balance (rain frequency + snow trigger), set **In Review** because he checked the fix in at 14:38.
- **KAN-421 was the dedup win.** The playtest item "javelin turns into civilians / demotes" was already ticketed as "Javelin units become civilians after throwing spears", sitting **unassigned and parked in S8** while Fredrik carried it on his own list that morning. Assigned Fredrik, pulled to S7. This is the third time on this project that active work turned out to be already-ticketed-but-parked. Search before creating pays every single run.
- **Bot-created tickets are a standing hygiene leak.** KAN-533/534/535/536/540/541/542, all created Aug 18-20 by the Death Board Discord bot, sat in the **backlog with no sprint and no fixVersion**, and three were **unassigned even though the requester named an owner in the same Discord message** (Tim, #qa 2026-08-18: "create a jira and assign to @Fredrik" produced KAN-533 unassigned). All 7 moved to S7; fixVersion MS4 set across the whole KAN-531 to KAN-546 range (16 tickets, incl. subtask KAN-532, which accepted fixVersion fine even though sprint is parent-inherited).
- **Purple was two things, not one.** The Aug 19 note's "automate asset identification with purple texture overlay for Greek assets" reads as tooling; KAN-504 (Aug 7, Tim) treats purple tint as a rendering bug; the Aug 20 standup says "resolve unit purple tinting". Robert's call: **separate**. KAN-504 stays a bug, KAN-557 is the tooling, both cross-referenced in comments.
- **KAN-505 moved to In Review** (Joanna pushed tree-scatter off the 3 blocks under the hermit houses, #art-support 08:15).
- **Comments added** to KAN-459 (knights-isolation test, plus Fredrik's finding that with a knight everything boards, without knights it is capped at the 3 archer positions), KAN-528 (Tim settled on **50 boat pieces**), KAN-546 (croc rebased on the wolf attack/prefab; cleanup rename crocodile2 to crocodile and eat-at-any-time still open), KAN-544 (suspected duplicate of KAN-412), KAN-504 (the purple split).
- **⚠️ Dubravko has zero Jira presence** despite shipping title-screen art Aug 18-20 in #art. Three days of visible work, no ticket. Needs a UI/key-art ticket set before the MS4 gate.
- **⚠️ KAN-412 vs KAN-544** are both "Staff of Ra SFX", both In Review on Carolina. Duplicate, needs a call.
- **Robert-side, not Jira:** Stockholm artist meeting (**verified 2026-08-20: nothing on the calendar, still needs scheduling**) and the dev-team apparel budget evaluation.

### Discord handle to Jira display name (verified 2026-08-20)
`N1tch` = Tim Browne (Discord id 163064870227410944) · `Arlenti` = Joanna Supska (190900589683539968) · `BlazeByrne` = Eamonn Byrne · `Imi` = Imkan Hayati (869956457368547338) · `Fredrik` (381813205724561411) · `Oskar` · `Carolina ˖✧` = Carolina Foghammar · `Dubi` = Dubravko Jurina. Needed on every run, because Gemini notes use real names and Discord uses handles.


## 2026-08-17 — CANONICAL: the RF LTC says NOTHING about credit, and §5.1 is what actually binds AP's mouth

**Verified by reading all 12 pages of the signed contract** (`SoD_LTC_Contract_Aurora_Punks_2026-04-15_signed.pdf`, Drive `1rBBGu-2uEKLKs497JLz-go-yxz6w5Fpt`, DocuSign 1DD23F7B, effective 24 Apr 2026, signed 27 Apr by Andreea + Robert / 29 Apr by Pim Holfve) plus Schedule C (Proposal v2). Do not re-derive this.

1. **There is no credit clause.** No attribution, splash, logo, developer-branding, press or announcement provision anywhere in §§1-9 or Schedules A/B/C. The only occurrence of "marketing" is MS7's deliverable line "launch coordination with RF marketing", which is an obligation *on* AP. Schedule C's cover line "Developer: Aurora Punks" and Schedule A special condition 2 (Tim Browne as Creative Director, a material condition) are descriptive only, even though schedule content takes precedence per §1.1.
2. **AP reserved nothing.** §4.3 assigns all rights in the Work to RF; §4.2 gives RF a perpetual sublicensable licence over AP's pre-existing tools. No portfolio or marketing-use carve-out.
3. **The real constraint on AP speaking publicly is §5.1**, not the missing credit clause. It deems "the Work and the Customer Properties" Confidential Information and bars publication to third parties without RF's **prior written approval**. §6.1 attaches an indemnity to a section 5 breach and the obligation survives termination. §5.2(a) releases only what RF has itself made public, and only after it does — so if RF announces without naming AP, **AP still cannot name itself**.
4. **Load-bearing consequence for the Oct 8 relaunch (apb-040):** permission to speak needs **no amendment**. A written OK from Niclas/Pontus in the mail thread *is* the §5.1 mechanism. Only an in-game splash, being an obligation on RF, would need a signed instrument — §9.1 makes this the complete agreement, modifiable only by written instrument executed by authorised representatives, so verbal commitments move nothing.
5. **Fallback arguments are weak, present them as weak.** `URL (1960:729) 3 §` namngivningsrätt survives the assignment and cannot be blanket-waived, but belongs to the individual creators (Tim, Fredrik, Imi), never to Aurora Punks AB — a company is not *upphovsman*. It yields a credits-list line, not a splash. `VmL (2010:1877) 1 kap. 11 § p 3` permits a truthful "Aurora Punks developed Pharaoh Lands for Raw Fury" as referential use, but carries no screenshots, key art or trailers (RF copyright).
6. **Downstream gap:** all six K2C subcontracts carry §3.9 granting contractors portfolio/showreel rights including screenshots and video clips of the released build, plus a reference to "the credits delivered in the final build". AP does not hold those rights upstream. Saved for now by the clause's own "subject to any publicity rules notified by ... the upstream publisher", so no breach — but six counterparties' expectations are set against an uncontracted credit.
7. **State of play:** Robert put the credit question to Niclas on the **4 Aug RF sync** ("noted, to be settled with Pontus"); still unsettled as of 17 Aug. Robert's steer 2026-08-17: he is in touch with Niclas and **not concerned**, so no mail was drafted and this was not raised as a blocker. Full analysis in `wiki/legal/sv_ip.md` § "Credit / attribution in co-dev and outsourcing agreements".

### ⛔ 2026-08-19 CORRECTION — the fourth artist is NOT asset-list capacity

**Every padding figure in this file that counts Dubravko toward the ~1 009 h asset-list
pool is WRONG.** The 2026-08-17 art onboarding meeting scoped him to **UI and key art:
game map, title logo, menu shield progression**. That work is not on the 2 872-row asset
list, so his hours do **not** reduce the ~1 009 h remaining on it.

- The **+28% / −2.5% / −7% figures below were computed for a production artist** burning
  down the asset list. They do not describe the artist we actually hired. Do not quote them
  for Dubravko.
- The asset-list pool therefore sits at the **no-fourth-artist baseline** (936 h over the
  9-week window, i.e. **−7%**), and the Lost Hive extension remains the only thing that
  moves it.
- The indirect benefit is freeing **Imi** from UI work, but only **three open UI tickets
  exist project-wide** (KAN-399, KAN-407, KAN-426), so the offset is small.
- **Hiring him may still be right** — a world map and title logo are launch-critical and
  nobody was on them. But it is a **different decision** from the one the 08-10 budget memo
  argued, and it left him starting **18 Aug on work with no tickets**: no ticket for the
  game map, none for the menu shield progression, and the title logo exists only as
  KAN-407, a typo fix in Icebox.

**MS4 gate is 2026-08-28, unchanged** (Robert, 08-19). The "August 27th" in the 08-17
standup notes was an **internal cut date**, not a milestone move. Gemini garble risk
confirmed again.

## 2026-08-15 — Fourth artist RESOLVED AND BOOKED (Dubravko Jurina), Gmail outage recovered

**The artist is Dubravko Jurina** (Fury Studios). Gemini's "Bravu Jurina" was a garble.
Discord **`dubi2583`**. Broker is **Tom Gojevic, "Dungeon Keeper, Fury Studios"**,
+385 Croatia, mailing from `tom@rawfury.com`.

**⚠️ Entity question from 08-13 is ANSWERED: Fury Studios, not Raw Fury.** So this is a
new subcontract AP books and pays, NOT a Raw Fury secondment absorbed by the LTC. The
zero-margin-impact case is dead.

**Rate: 32 EUR/h = 352 SEK/h** at EUR/SEK **11.00** (frankfurter 10.999 + er-api 11.014,
2026-08-14/15). Monthly-equivalent 60 966 SEK against the 60 000 assumed on 08-10, so
**the entire 08-10 capacity and budget analysis stands unrevised** (346 SEK/h modelled,
352 actual, 1.7% out).

**🔴 The real constraint is duration, not rate.** Tom committed only to "at least until
end of month" (= 31 Aug), "might be more". The +28% padding case needs Dubravko through
23 Oct. **Robert's decision: book the confirmed floor only.** Start **Tue 18 Aug**, so
**10 working days, 80 h, 28 160 SEK**. ~~That leaves art capacity at roughly −2.5% against ~1 009 h remaining.~~ **STRUCK 08-19: he does UI, not asset-list work, so his hours never applied to that pool. See the 08-19 CORRECTION.** **The padding problem is NOT solved**, only deferred to
whether Tom extends. Scenario B (to 30 Sep, 264 h, 92 928) and C (to 23 Oct, 400 h,
140 800) are pre-costed in `k2c-041` ready to book.

**P&L written** — workbook `1ml7BaJaVDTZwDp-CKFd6LPPaJ0HzaQsLQm96rt0-yiU` tab
`k2c_pnl_2026`, row 15: A15 label with the caveat, B15 60 966, C15 1, **G15/H15 zeroed**,
**I15 25 344** (72 h in MS4 window), **J15 2 816** (Mon 31 Aug, past the MS4 gate into
MS5). Chain verified to `ap_pnl_2026` row 10: **P&L 946 849 → 915 873** (−30 976 =
28 160 × 1.1), margin **16.9% → 16.4%**. AP master updated automatically.

**⚠️ TWO SHEET-ID TRAPS, both cost time today:**
1. `output_log.md:882` points at `1YAP1gbvxaf0Drnky2AoBMGCrGbaJYmo2uY0BxVXS8jI` which is
   **404, dead**.
2. The standalone `k2c_pnl_2026` sheet `1xlHrzOLXBrGWZj7cFQKw53ovqA6nDkrjU8ilqkW2NnM`
   still opens and still shows plausible numbers, but carries a **LEGACY banner** and was
   superseded 2026-06-23. **Writing there would have silently done nothing.** The only
   live P&L is the AP workbook tab.
3. **Row 15's G15:J15 were live MS-ratio formulas.** Setting B15 without clearing them
   would have booked **274 346 SEK for an 80-hour engagement** (ratios MS2 1.35, MS3 0.9,
   MS4 0.9, MS5 1.35). Row 14's hardcoded-per-milestone pattern is the correct one.

**Contract: Robert overrode the recommendation.** Advice was to decline Tom's Croatian
template and send AP's `_TEMPLATE_MASTER_CZP_subcontractor.md` (IP vests in AP and feeds
the RF LTC chain; Swedish law like the other ten; available today vs "next week").
**Robert chose to take Tom's rough translation.** Agreed mitigation: **Assistant reads
the IP and governing-law clauses before signature.** Still open: whether the counterparty
is AP↔Fury Studios or AP↔Dubravko personally (changes VAT reverse charge and the IP
chain), and hours/week (40 assumed, never stated).

**Reply to Tom drafted, NOT sent** — Gmail draft `r2833583466992018013`, in-thread on
`1a0006e8708f7885`: rough translation fine, Robert will reach out on Discord and set a
meeting asap, asks Tom to confirm a **Tuesday 18 Aug** start.

### Gmail was dark for 28 hours (db-181, now closed)

Work Gmail OAuth grant **revoked by Robert's Google password change**. Broke
**2026-08-14 12:18 UTC**, 343 logged failures, re-authorised 2026-08-15 ~16:45 UTC.
Personal Gmail and GDrive were unaffected, so grants die *selectively* — "one thing
works" is not evidence the others do. Dead meanwhile: the 15-min inbox scan, the 06:30
sweep, Gemini notes ingestion, RAG gmail, `gmail-draft.js`.

**One k2c meeting fell in the hole: "K2C Playtest" Fri 14 Aug (13:26 UTC).** Recovered
by `post-meeting-sweep.js` (ticket `db-146`), captured to
`playtests/2026-08-14_playtest.md`, **not yet ticketed**. Findings: tree/Z-index sorting
obstructing quest items; players can target bosses with special abilities; boss death
animation + item removal desync **on client**; no mirror-placement SFX; connectivity
fixed by standardising Steam friend codes. The two boss items look like the same
**boss-registration** root cause Fredrik traced for KAN-497. Decisions: testers guided by
**written instruction, not technical restriction** (so the interim build needs no island
gating); formal asset checklist for the new artist.

**⚠️ Monday 17 Aug: Tim + Imi + Robert meet to populate the asset-list checklist for the
new artist** — one day before Dubravko starts. That is also the moment to price the ~12
"re-use" items carrying the whole ±200 h uncertainty in the capacity model.

**🐛 DevOps:** `post-meeting-sweep.js` throws `Cannot read properties of null (reading
'slice')` when an event resolves via the **Drive** branch instead of Gmail, so
Drive-sourced meeting notes are silently dropped. Reproduced on the 08-12 timeline review.


## Authorization Letter Carolina — TVÅ FEL I JULIETTES UTKAST (upptäckt 2026-08-05)
Juliette (juliette@combinedeffect.com, "Master of Rules, Combined Effect AB", RF:s utlagda juridik) skickade utkastet 2026-07-03 och **påminde Carolina direkt 2026-08-04 13:41**: "Jag kan se att du fortfarande inte har signerat avtalet." Dokument: `Carolina Foghammar_Authorization letter_KTC DLC_2026-07-01.docx`, tråd `19efa4a445c93449`. Robert svarade 2026-07-08 "ser bra ut, lägg till Carolina som composer" **utan att någon läst utkastet mot hans egna instruktioner från 2026-06-24**. Två av dem är inte implementerade:
1. **"Independent artist" står kvar.** Andra WHEREAS: *"composed and implemented by the Composer, an **independent artist employed and remunerated by Developer**"*. Robert bad uttryckligen: *"hon är inte en independent contractor i skatte- och försäkringshänseende. Bra om Juliette kan anpassa de skrivningarna så att avtalet blir en ren rättighetsöverlåtelse snarare än ett konsultuppdrag."* Formuleringen är dessutom självmotsägande.
2. **⚠️ FEL ARBETSGIVARE — sakfel i avtalstext.** Brevet anger **Aurora Punks, 559256-9718** som "Developer" och säger att Carolina är *"employed and remunerated by Developer"*. Hon är **visstidsanställd i CZP**, inte AP (OpenSign `wq8WdASeej`). Memory hade redan en stående instruktion om exakt detta ("Lawyer to ensure Juliette's draft doesn't mis-state her employer") och den föll mellan stolarna. **Konflikt att lösa innan man rättar:** Robert presenterade medvetet AP som engagerande bolag mot RF, så en rättelse exponerar CZP-strukturen. Roberts beslut, inte PM:ens.
- **✅ BEKRÄFTAT 2026-08-05 (Robert): Carolina avvaktar några saker från STIM.** Det är alltså STIM-klausulen som håller signaturen, inte rättighetsöverlåtelsen. Roberts källa: *"Carolina nämnde idag..."*.
- **✅ SVAR SKICKAT AV ROBERT SJÄLV 2026-08-05 22:37 CEST**, i tråden `19efa4a445c93449` till Juliette: *"Hoppar in med svar, Carolina nämnde idag att hon väntar på input från STIM på några punkter, återkommer så snart det är klart. Sommartider gör att det tar lite längre tid."* Han sa först att han skulle ta det på Slack ("jag och Juliette är tajta"), men mailade i praktiken. **Fångat av /close steg 0**, inte av sessionsminnet.
- **⚠️ DE TVÅ FELEN ÄR FORTFARANDE INTE FRAMFÖRDA TILL JULIETTE.** Roberts mail rör bara STIM-fördröjningen. Varken "independent artist"-formuleringen eller fel arbetsgivare (AP i stället för CZP) har tagits upp med henne i skrift. Nästa naturliga tillfälle är när hon återkommer efter STIM-beskedet, och rättelsen måste in i själva dokumentet innan Carolina signerar.
- **Kanalval:** etablerad relation, informell väg är rätt här och ska inte ifrågasättas igen. RF:s workspace är läsbar via `mcp__slack-rawfury__*` om något av detta ändå avhandlas där.
- **Trolig orsak till att Carolina inte signerat: STIM-klausulen.** Hon garanterar att skriva under sådant som säkerställer att RF *"shall not have to pay any royalties or other fees to STIM"*. För en svensk kompositör är STIM hela uppbördsvägen för framförandeersättning, och det är den klausul som biter hårdast personligen. Övrigt i brevet matchar Roberts 24 juni-linje: full överlåtelse i evighet inkl. källmaterial, intäkter från Spotify/Bandcamp/vinyl/egen YouTube behålls, ingen distribution på spelplattformar (alltså ingen Steam-OST), sex månaders släppfönsterkontroll plus en "materially detrimental"-klausul med 14 dagars rättelsefrist, och kvitto på att hon är fullt kompenserad utan royalty.
- **Lawyer aldrig inkopplad.** Robert sköt upp det i juni i väntan på Juliettes riktiga utkast. Utkastet har funnits sedan 3 juli och ingen har granskat det. **k2c-030, k2c-031 och k2c-034 ligger alla kvar som critical sedan 2026-07-07** med deadline 9 juli.

## Daily runs 2026-08-04 till 2026-08-13 — ROTERADE

Fem daily-run-block flyttade 2026-08-24 till `archive/project_k2c_sands_of_duat_daily-runs_2026-08.md`
för att hålla den här filen läsbar. Inget raderat, allt sökbart via `rag_search(source="memory")`.
Innehåller körningarna 08-13 (P&L-kedjeaudit), 08-10 (sprintplanering och art-tidslinje),
08-07 (playtest + RF-enkätgranskning), 08-05 och 08-04.

## Current state 2026-08-02 (MS3 approved, MS4 redefined, backlog triaged)
- **✅ MS3 APPROVED IN WRITING by Ishani 2026-07-30 17:55 CEST** (thread `19f95d5a93d1e245`): "we are approving this most recent milestone, please go ahead and send the invoice to finance!" **Invoice = 560 000 SEK ex VAT to moneymoney@rawfury.com, due 15 calendar days** per Schedule A. Followup **k2c-039** raised for CorpBot; k2c-037 (Eamonn go-ahead) is unblocked. Also on that mail: Ishani + Pontus played through and **small notes are coming ~Jul 31/Aug 1**; **small external playtest planned for August**; **Niclas back from PTO next week** and may add feedback.
- **⚠️ MS4 REDEFINED on the Ishani sync 2026-07-28** — **Switch only, and the bar is "ready for Compliance / Cert QA" rather than submitted for cert.** Missing localisation is acceptable if documented as a known issue. **Cert is now staged: Switch = MS4 · PlayStation = MS5 · Steam = MS6** (Robert, 2026-07-31). Platform build tickets re-milestoned to match (KAN-190/191 → MS6, KAN-192/193 Xbox + KAN-194/195 PlayStation → MS5). Schedule A says "submitted for cert on Steam / Switch / PlayStation for Rapid Patching approval", so this is a **verbal variation of a signed term**; **Robert's call 2026-07-31: no written confirmation needed, "we are close enough to RF to handle this without going legal."** Knock-on: **trophies are no longer an MS4 gate** because Switch is the only non-PC platform in scope — trophy design from Tim stays parked until he is back.
- **Confluence Milestones page 42303512 now v4** carrying the revised MS4 row, the three-milestone cert staging and a dated info panel explaining the variation.
- **MS4 gate ticket = KAN-482** (Oskar): Switch build ready for Compliance / Cert QA, lotcheck requirements, stable external-test build, loc documented as known issues, trophies out of scope. Supersedes KAN-87, which is stranded as a subtask under the closed MS1 porting risk log and cannot be sprinted.
- **BACKLOG TRIAGE 2026-07-31/08-02 (Robert, item by item): MS4 open 197 → 88.** 80 closed, 7 iceboxed, rest re-milestoned. Closed: 36 spec subtasks under already-Done parents · 28 MS1 pre-prod items (KAN-25/27/36/44/47/68/84 + subtasks, incl. KAN-72) · island epics KAN-5 (Ra) + KAN-6 (Bata), since further work on a delivered island is a bug and outside epic scope · epics KAN-2, KAN-4, KAN-253 (banner), KAN-261 (lurker greed), KAN-355 (Merchant — **delivered, not cut**; all three children were Done) · Ra's mounts KAN-148/150 · RF-owned KAN-244 + KAN-271. **Iceboxed** (out of scope, reversible): KAN-176 per-island greed variants, KAN-182 War Room, KAN-184 Bulk Buy + subtasks, and **KAN-218 "Greed Mask upgrades" which is an artefact of an early Death Board bot test** (its description is the raw test message; real greed-mask work is elsewhere). Kept: Monarch rework KAN-248, Demolisher hermit KAN-266.
- **Content items are milestoned BY THEIR ISLAND** (Robert's rule) — full table in [[project_k2c_epic_structure]]. Not island-connected and therefore parked: greed variants, greed mask, War Room, Bulk Buy.
- **S6 mid-sprint: 71 issues, 40 open.** Load is lopsided: **Fredrik ~11 open, Tim ~11 open** (Tim was away the first week), everyone else 1–4. **Only 2 open Critical bugs: KAN-463, KAN-459.** S6 was reconciled against the sprint-planning notes on 07-27: the 8 MS4 island tickets pulled in (Sobek KAN-110/112/114/289, Anubis KAN-134/136/138/292) plus **KAN-471** art asset audit (Eamonn+Joanna), **KAN-472** Apesh boss prototype (Fredrik+Oskar), **KAN-473** Apesh placeholder sprites then animation pass (Imi).
- **⚠️ OPEN AS OF 2026-08-02:** Ishani promised her + Pontus's playthrough notes "in a day or so" on 07-30 — **nothing from any @rawfury.com address since 07-31**, now 3 days. RF also want a **small external playtest in August**, and **Niclas is back from PTO** and may add feedback. **87 open issues still carry no fixVersion** and are invisible on every release view — unswept. Tracked on **k2c-039**.
- **Bot half-tickets triaged (Jul 27–31):** KAN-475→Joanna (Bug), KAN-476→Tim (Bug), KAN-480→Carolina, and KAN-470/474 tagged MS4 but **still unassigned** (no owner evidence in Discord). KAN-477/478/479 were created properly by the team.
- **KAN-481 created manually** — Robert's 2026-07-27 19:53 #qa report ("Lurker z is off, the stable hermit obscures it") never became a ticket because he typed **"assign a big to Fredrik"** and the typo stopped the bot parsing. Assigned Fredrik, MS4, S6, Severity Minor. **Bot gap worth handing to DevOps: accept "big"/near-miss verbs, or reply when a create-intent message fails to parse.**
- **Apesh boss art effectively delivered early** — Imi checked in 12 Apesh sprites 2026-07-28 (Idle/Stand/Defend/ChargeUp/Attack/Death/WalkF+B) and is making single-frame animation clips; Oskar + Fredrik both agreed to that shape in Discord. KAN-473 is the tracking ticket.
- **The 2026-07-31 standup DERAILED INTO TEEF partway through** (Robert, 2026-07-31 — I had first mis-called the note confabulated; it is accurate, the meeting just covered two projects). Split: **Teef** = October soft launch, mobile experience, soft-launch sync/polish. **K2C** = code rebasing challenges · **platform content requirements** (the Switch compliance push for MS4) · colour schemes / interface adjustments · team playtest validated functional consistency · kingdom management system needs refinement off recent session feedback · group action to test multiplayer. **KAN-87** (Platform-specific gotchas / cert requirements, Oskar) is the existing home for the platform-content-requirements strand and is now MS4 critical path. Teef half belongs in that project's record.

## Fury Studios doo — the entity behind Dubravko (recorded 2026-08-19)

**`tom@rawfury.com` is NOT Raw Fury the publisher.** Tom Gojević signs as "Dungeon Keeper,
**Fury Studios**" and Dubravko's address is `dubravko@rawfury.com`. Fury Studios people sit
on the `rawfury.com` mail domain, so **the domain tells you nothing about the entity**. This
cost real time on 08-13 to 08-15.

| Field | Value |
|---|---|
| Legal name | **Fury Studios doo** |
| Address | Radnička 37A, 10000 Zagreb, Croatia |
| OIB (org/VAT no.) | **60629627249** (VAT: `HR60629627249`, verify in VIES) |
| Signatory | Tomislav Gojević, **procurator** |
| Role | KTC base-game dev studio (distinct from Raw Fury, the publisher) |
| Relationship | **B2B services**. Dubravko is Fury Studios' *personnel*, not a freelancer and not AP's worker (Agreement Art 3) |
| Rate | **32 EUR/h** = 352 SEK/h at EUR/SEK 11.00 |
| Contract | Business Cooperation Agreement (indefinite) + per-project Addendum, **Croatian law, exclusive jurisdiction Zagreb** |
| VAT treatment | EU B2B **reverse charge** |

**Also known:** David owns Fury Studios' GitHub, Naseer owns Steam, and "Haglet" is the
team's spelling. Full contract review and defects in **`k2c-047`**.

**Client-entity trap:** Tom's draft named **Aurora Punks AB** while Robert directed invoicing
to **Creation Zero Point AB (559182-7471)**. Art 6(2) vests IP in "the Client", and every
other k2c sub vests in CZP, so signing with AP AB named would route this one artist's IP
through the wrong entity. See [[project_rlr_ip_dispute]] for why that class of mistake is
expensive here.

## Contract: the binding milestone definitions
**Binding milestone definitions = the signed Outsourcing Agreement, Schedule A** (eff. 2026-04-24, DocuSign 2026-04-29, Pim Holfve/RF + Robert/AP), PDF `gdrive:1rBBGu-2uEKLKs497JLz-go-yxz6w5Fpt` (RAG-indexed, full text searchable). **MS4 Pre-Cert Build, Aug 28, 560 000 SEK: "Feature complete build with placeholder art (greybox ok), submitted for cert on Steam/Switch/PlayStation for Rapid Patching approval, no new features, known bugs documented."** Note **Switch is an MS4 cert platform and Xbox is MS5** — the Confluence page had these swapped. Acceptance mechanics: RF has **5 business days** to approve/reject in good faith, AP resubmits within **10 business days**, and **every delivery except MS0/MS1 must include the build AND the source code of the Work** (worth auditing whether MS2/MS3 actually shipped source). Schedule A also makes **Tim Browne as Creative Director a material condition**.
- **The client-facing mirror of this is the Confluence Milestones page `42303512`** (K2C space, RF has access), now **v4**. It had drifted from Schedule A on two counts before 2026-07-27: Switch and Xbox were swapped between MS4 and MS5, and MS3 scope was listed as "BATA + Anubis/Apesh" when the contract's "two islands playable end-to-end" was satisfied by **Ra (A) + Bata (B)**. Both corrected, and the page now carries the cert staging plus a delivery/acceptance section quoting Schedule A. When the page and the contract disagree, **the contract wins** — re-derive from the PDF, not from the page.
- ⚠️ **UNRESOLVED SCOPE TENSION (still open 2026-08-02).** Schedule A defines MS4 as a **feature complete build**, which reads as all seven islands. The board has D (Sphinx), E (Osiris) and G (Set) at MS5. The 07-28 sync changed the *cert* bar to Switch-only Compliance/Cert QA but never addressed the *feature-complete* bar, so this is genuinely still open. It is a 560 000 SEK acceptance question — worth settling with Ishani before the Aug 28 delivery rather than at it.

## Lost Hive Amendment No. 1 — MS3 80h uplift (CorpBot, 2026-07-22)
Eamonn asked on Discord which period to invoice now that MS3 moved to Fri Jul 24, and what the amount should be after they went to 80h/week. **Two separate items, do not conflate:**
- **MS2 = 67,500 ex VAT, UNCHANGED and invoiceable now.** RF accepted the Alpha Jul 2 and funds have landed. The MS2 period closed Jun 26, *before* the 80h change on Jul 6. Lost Hive had only ever invoiced MS1 (Fortnox faktura 22, 13,500 + VAT, Jun 10) — no MS2 invoice had been raised.
- **MS3 = 86,400 → 102,600 ex VAT.** Lost Hive ran a combined 80h/week from 2026-07-06 = +25% over the contracted 64h, covering 3 of the 4 weeks in the MS3 window (Jun 29 – Jul 24). `86,400 × (0.25 × 1.00 + 0.75 × 1.25) = 102,600`. Robert picked this over the hours-recompute (304h × 346 = 105,231) — scale the signed lump sum, don't reopen how it was derived.
**Total Fee 300,000 → 316,200.** Exhibit A capped at 300k, so the uplift needed a written amendment. **MS4 + MS5 unchanged** (86,400 / 46,200) — Robert agreed they revert to a 64h week from MS4 ("we can do that"), written into the amendment. Clause 5 states the uplift is one-off, sets no new rate and no precedent — §5.1 keeps hours as "a performance expectation, not a minimum-hours guarantee", so this is goodwill, not entitlement.
- Source `contracts_2026_subcontractors/amendment_01_losthive_ms3_uplift.md` → PDF in `_build_amendments/`. **OpenSign `G6yBKo1OtA`**, ordered Mattias → Andreea → Eamonn, placement `sub`. Mattias emailed + watcher-seeded 2026-07-22 14:01; auto-advance handles signers 2-3.
- Gmail draft to Eamonn `r1838279017090029127` (voice pass by The Author) — awaiting Robert's send.
- ✅ **P&L RECONCILED 2026-07-22.** The standing "row 14 still 270,000" warning was **STALE and wrong** — the live sheet was already on the 300,000 split; 270k lived only in the frozen local CSV + a tracker note. One cell written: `k2c_pnl_2026!H14` 86,400 → **102,600** via `gsheet-set-cell.js`. Everything above it is formulas and recomputed: N14 → 316,200, H17 → 550,170, H24 → -45,187, **N24 K2C profit 964,669 → 946,849**. **AP P&L needed no edit** — its row 10 is `=k2c_pnl_2026!F24…L24`, so O10 followed to **946,848.86 kr** on its own (verified by read-back).
- **80h window CONFIRMED by Robert 2026-07-22:** 3 weeks at 80h (Jul 6–24, incl. the current week), back to 64h from **Mon Jul 27**. 102,600 stands. Mattias + Andreea had already signed `G6yBKo1OtA` by the time the question came up — no void/resend needed. Amendment Clause 4 ("reverts from the start of the MS4 window") lines up exactly with Jul 27.

## Milestone island deliverables — AUTHORITATIVE island → MS map
**Finalized 2026-07-08 by Robert + Tim over 3 rounds. Verify live before acting; these fixVersions have drifted twice.**

**A (Ra, KAN-5) = MS2 · B (Bata, KAN-6) = MS3 · C (Sobek, KAN-7) = MS4 · D (Sphinx, KAN-8) = MS5 · E (Osiris, KAN-9) = MS5 · F (Anubis/Apesh, KAN-10) = MS4 · G (Set, KAN-11) = MS5.**

Drivers (Tim): MS3 VS = Bata. **Ra shipped in the MS2 Alpha so it stays MS2** (Robert: "keep RA in MS2") — don't retag delivered work to a later milestone just to match a re-homed epic. **Bata (B) and Anubis (F) are choice-LINKED** (the Bata choice pays off on Anubis), so F was pulled forward to MS4 alongside Sobek (C, easy scripting-wise), and Sphinx (D) pushed back to MS5 with Osiris (E) and the Set (G) finale. Future-island tasks stay in BACKLOG per rolling-wave and get pulled at MS planning.

**KAN-5 and KAN-6 were closed 2026-07-31** — both islands are delivered, and per Robert any further work on a delivered island is a bug, which sits outside epic scope.

Framing islands: **Start island + Final Boss island = MS2**. **Deferred:** the final cave boss battle, slot TBD post-MS2.

Content items (mounts, items of power, blessings, bosses) are milestoned **by the island that unlocks them** — full table in [[project_k2c_epic_structure]].

**Project folder:** `umbrella/k2c_sands_of_duat/` · **Epic:** `assistant/followups/k2c-000-epic.md`

## Key Contacts
- Niclas Lagerlof (niclas@rawfury.com) — RF producer
- Ishani Birch (ishani@rawfury.com) — RF Sr Publishing Producer
- Alan Kertz (alan@rawfury.com) — RF design lead
- Pontus (RF) — Brand Manager (key art / store assets / naming)
- **Mia Došen (RF) — covering for Ishani while she is away** (from 2026-08-05). Owns the external playtest thread in Slack.
- **Timothy (RF) — UX Manager, runs RF's testing teams.** Confirmed by Robert 2026-08-07. He organises the external playtests, so playtest/survey feedback is addressed to him alongside Mia. **NOT Tim Browne** — different person, easy to conflate in the shared Slack channel.
- Naseer (naseer@rawfury.com) — RF Release Manager (added 2026-05-14; Steam ID + console product config; connect with Oskar)
- Tim Browne (tim@brightgambit.com) — Designer, Bright Gambit
- Fredrik Laurent (fredrik.laurent@gmail.com) — Lead Programmer (Ark Island)
- Imi (imi@redmarmosetstudios.com) — Art Lead (Red Marmoset Studios)
- Oskar Hansen (oskar@aurorapunks.com) — Porting Lead (Skokloster)
- Eamonn Byrne, Joanna "Ash" Supska — Lost Hive (additional art, May 7 – Aug 31, 270k initial cap, attending standups)

## Infrastructure
- Confluence: aurorapunks.atlassian.net/wiki/spaces/K2C (populated Apr 8 with full GDD; spaceId 557058)
  - Home page (id 557165) rewritten 2026-05-15 — proper welcome + Legend frontdoor (no more default template)
  - **MS1 Delivery — Legend** (id 41648145, child of Home) — front-door for RF MS1 review, maps plan deliverables → pages
  - **Gameplay Code Risk Assessment** (id 917521) — Fredrik-side risks; augmented 2026-05-15 with Haglit (HIGH) + Git/merge strategy (OPEN)
  - **Porting Risk Assessment** (id 32407556, was "Porting Risk Assesment" typo) — Oskar-side risks, includes NX Addon 20.x.x deadline Jun 30, 2026 (CRITICAL: forces Unity bump on Switch which may re-trip Haglit)
- GitHub: RawFury/kingdom-two-crowns, DLC branch **`egypt/dlc-setup`** (NOT `twocrowns/next-dlc` — that branch does not exist; corrected 2026-05-21). Branch had only 4 DLC commits, all 2026-04-17 (Fredrik: egyptian map, blocks_egyptian scene, DLC bootstrap, gender animator fix). **No commits since 2026-04-17** — MS2 engineering work is not landing in version control. Diverged from active dev branches; merge/branch strategy still open (owned by Fury Studios). `gh` CLI authed as RobertBackstrom with full repo scope.
- Tim's GDD docs: Shared via Google Drive Apr 6 (spreadsheet + wiki transfer doc)

## Payment Terms (agreed Apr 8, updated Apr 14)
- RF: max 5 business days to approve delivery
- AP: 10 business days to redeliver if rejected
- Invoice on standard 30-day terms
- Schedule history: AP original 15/18/20/17/15/10/5 → Niclas rebalanced to 0/15/15/20/15/20/15 (fixed front-loading) → 2026-04-14 expanded to 0/15/15/**10/10**/15/20/15 across MS0–MS7 (new MS3 Vertical Slice Jul 20 added to smooth Jul-Sep gap)
- 8 milestones now: MS0 Contract, MS1 Pre-Prod, MS2 Alpha, MS3 Vertical Slice, MS4 Pre-Cert, MS5 Content Complete, MS6 RC, MS7 Gold

## Atlassian
- Jira: aurorapunks.atlassian.net, project key KAN, team-managed, ~302 issues (26 epics)
- **Native Sprints enabled 2026-05-22** (was simple Kanban). Board 1 now has 15 sprints S1-S15 (ids 1-9, 15-20) mapping the sprint plan MS2->release. S1 active. Sprint membership: JQL `sprint = {id}`.
- **Bug `Severity` field LIVE 2026-07-26** — `customfield_10170`, single-select **MF / Critical / Major / Minor**, scoped to the Bug work type. Set it via `jira-set.js update <KEY> <file>` with `{"customfield_10170":{"value":"Critical"}}`; filter with `project = KAN AND Severity = Critical`. Created through `assistant/atlassian-team-field.js --commit` (db-257). **`Repro` (5/5…0/5) still NOT created** — the commit run was classifier-blocked, Robert to run the one-liner in db-257. `Priority` does not exist on the Bug work type (it sits unused in the settings System-fields rail), so Severity is the only criticality signal.
- API access via token at `~/.claude/.atlassian-credentials.json` (expires Dec 31 2026)
- Rovo MCP only connects to badass-studios site, not aurorapunks — use API token for K2C
- Notifications: turned off on both Jira and Confluence by Robert manually
- Plan: currently on paid trial, can downgrade to Free (only 2 real users)
- Legacy status column "To Do This Sprint" is redundant post-sprints — pending rename to "To Do"

## GDrive
- K2C folder (k2c_rf_ap): 1l06e7S7finV0wneJbWBtOgMGTGA_R3Iu — upload deliverables here via gdrive-upload.js. (Old id 1OnxfhtbjHF_ua4PXfcdEb6VzAEpmd4I7 is DEAD — "File not found"; corrected 2026-07-08.)
- **K2C P&L — MIGRATED 2026-06-23 into the AP P&L workbook** as tab `k2c_pnl_2026` (gid 1170637760) inside `1ml7BaJaVDTZwDp-CKFd6LPPaJ0HzaQsLQm96rt0-yiU`. **Edit there** — the AP K2C line is a live formula off this tab. The old standalone sheet `1xlHrzOLXBrGWZj7cFQKw53ovqA6nDkrjU8ilqkW2NnM` is **LEGACY/frozen** (A1 banner). Sanctioned numeric-cell writer = `assistant/gsheet-set-cell.js` (USER_ENTERED; `gsheets_update_cell` MCP writes TEXT and breaks SUMs).
- Project plan (Google Doc): 1mCsBnWiRByqfxkGbhURH6J2p3Gw5N6WEOf6Uyepnf3k
- Feedback response (Google Doc): 1qv9HjYvGTr5PQ2fXos3bc-VucNTUtLo8EZ1JzhcyeGg

## Discord
- K2C server: **"K2C Sands of Duat Dev"**, guild id `1492150019833467010` (env `DISCORD_K2C_GUILD_ID`). Invite: discord.gg/vN9phwUg
- **Death Board bot IS in the server** (corrected 2026-05-21 — the earlier "not added" note was stale). Bot has admin; can post + pin in any channel.
- Channels: #general, #dev, #art, #questions, #links, **#brief** (`1493262512693575750` — Death Board auto-posts here), **#production** (`1495683271940505680` — milestone/sprint announcements; sprint plan pinned here 2026-05-21).
- Posting: assistant/discord-bot.js uses discord.js; bot token in `.env` as `DISCORD_BOT_TOKEN`. assistant/ has no `dotenv` dep — parse `.env` manually in one-off scripts.

## Carolina — payroll parameters (canonical, verified 2026-07-24)
CZP visstidsanställd 2026-06-22 → 2026-10-13, milstolpebetald. Underlaget för varje återstående utbetalning, så ingen behöver räkna om:
- **Skattetabell 29, kolumn 1.** Adress Åkersberga = **Österåkers kommun 28,93%** (16,60 kommun + 12,33 region, lägst i landet) + **begravningsavgift 0,292%** (enhetlig nationell, Kammarkollegiet 2026) = 29,22 → tabell 29. Född 2000-03-31 → kolumn 1 (under 66 vid årets ingång).
- **Preliminärskatt per utbetalning:** MS2 11 700 brutto → **1 371** (netto 10 329, betald manuellt 2026-07-24). **MS3/MS4/MS5 22 500 brutto → 3 543** (netto 18 957), tabell 29 kol 1 intervall 22 401–22 600.
- **Arbetsgivaravgift 31,42%** (full sats, ålder 26). Kontrollräkning: brutto × 1,3142 ska matcha den laddade kostnaden i P&L rad 16.
- **Antaganden Henrik inte invände mot** (2026-07-24): CZP är huvudarbetsgivare (annars 30% platt) och hon är inte med i Svenska kyrkan (annars tabell 30). Håller tills Sifferrådet säger annat.
- **Flöde:** Sifferrådet bokför + attesterar lönen och skickar lönebesked till cfoghammar@gmail.com; **Robert betalar från SEB**. Skattekonto (avdragen skatt + arbetsgivaravgift) senast den 12:e månaden efter. Bank: Nordea 32682231896. Se [[reference_entity_accountants]].

## Historical — June–July 2026 (superseded, condensed 2026-08-02)
Per-day detail lives in `umbrella/k2c_sands_of_duat/standups/` + output_log, and every run is searchable via `rag_search(source="agents")` against pm_learnings. The durable facts:
- **Deliveries:** MS1 2026-05-15 · **MS2 (Alpha) 2026-06-26**, approved by Niclas 07-02 ("all good, it's approved"), invoice sent 07-03, 7 In-Review deliverables closed on approval (KAN-78/94/96/98/170/309/351) · **MS3 (Vertical Slice) 2026-07-24**, build **24074** on the Steam Stable branch, approved by Ishani 07-30, invoice sent 07-31. MS3 slipped 4 days from Jul 20 (the Jul 6 Gemini "late August" was a transcription error).
- **Delivery-package pattern, reuse it for MS4:** Confluence Legend pages — MS1 `41648145`, MS2 `89063426`, **MS3 `125566978`** ("Delivery - Legend & Build Notes", 13 known issues ticket-linked, 7 deferrals, 5 RF asks). Build each from a **single-source renderer** (`assistant/k2c_ms3_legend_build_2026-07-24.js`) that emits the Confluence XHTML and the local markdown mirror together so they cannot drift. Pull the previous Legend's storage XHTML to reuse its heading skeleton, then re-derive every fact from the live board.
- **Playtest checklist pattern:** Confluence `118063106` is master (real `<ac:task-list>` checkboxes, Tim can extend it in place), mirrored read-only into **KAN-444**. Confluence beat a GDoc because the external collaborator already had space access.
- **Sprint cadence (still live):** 2-week production sprints, a flexing 1–2 week hardening sprint ending exactly on each milestone date, retro last Friday, planning the following Monday. Ladder S1–S15 runs to Gold. Re-laid 2026-07-08 for the MS3 slip: S5 Jul13-24, S6 Jul27-Aug7, S7 Aug10-21, S8 Aug24-28.
- **Bug workflow:** KAN is team-managed; **Bug type id 10006**. Six tickets converted Task→Bug on 2026-07-08 (KAN-417/397/408/409/400/365). The Severity + Repro fields Robert asked for then were UI-only at the time; **Severity shipped 2026-07-26** (see the Atlassian section), Repro still not created.
- **Tools built for this project:** `assistant/jira-set.js` (sanctioned KAN writer — curl writes get classifier-denied) and `assistant/confluence-set.js` (file-based page bodies, auto version bump). Both allow-listed in `.claude/settings.local.json`.
- **Recurring defect:** the Death Board Discord bot creates **half-tickets** from #qa — it now resolves @-mention assignees but still leaves issue type, fixVersion and sprint empty, and it fails silently on a mistyped verb. Sweep `created >= last run` every run; NO-SPRINT is the tell.
- **Deferred out of MS3:** the Ra shorter-days mechanic (Robert 07-24: "I would prefer we do it in next MS") → now **KAN-467**, MS4. Seasonal mechanics cut to hold the VS date.
- **Grafted to MS5 on 2026-07-10:** **KAN-422 ACHIEVEMENTS / TROPHIES** (tasks 424–428) and **KAN-423 DROUGHT — Seasonal Art Pass** (tasks 429–433), all in backlog per rolling-wave.
- **Still unanswered by RF:** the **cultural-sensitivity / Egyptian-iconography mail sent 2026-07-10** (thread `19f4b3b867bdd91f`, to Niclas + Ishani + Pontus) — a transparency flag, publisher domain, not a proposal. Also open from the MS3 delivery mail: the **Pharaoh Lands wordmark** for title art, and a build/version numbering convention with Fury.
- **Conventions set in this window:** per-asset production tracking lives on the **K2C New Asset List, Confluence page 98338** (tickets link to it rather than enumerating assets); Javelinist is a FEATURE epic **KAN-349**; Egyptian unit reskins are one Task **KAN-354**.
- **Caveats proven repeatedly here:** Gemini notes garble dates, numbers, owners and occasionally whole topics — cross-check every hard value against Discord, which is verbatim. Never set Done or In-Review off a standup note; the gate is the client's written approval or a team poll.

## Historical — May 2026 (superseded, condensed 2026-07-24)
Per-day detail lives in `umbrella/k2c_sands_of_duat/standups/` + output_log; the durable facts:
- **MS1 delivered 2026-05-15** (Gmail thread `19e2cce92e33f047`, Niclas + Ishani). Confluence Legend id 41648145 was the delivery front-door; Milestones page id 42303512. RF's MS1 review came as **Confluence inline comments, never a formal approval email** (Alan Kertz + Niclas, May 19-21, collaborative) - the first RF payment gated on that sign-off.
- **Native Sprints enabled on KAN 2026-05-22** (was simple Kanban; the UI toggle is the only way on team-managed - REST can't do it). **15 sprints S1-S15** created from `drafts/k2c_sprint_plan_2026.md`: 2-wk production sprints + a flexing 1-2 wk hardening sprint landing on each MS date, retro last Friday / planning next Monday. Plan pinned in Discord #production. That ladder is still the live structure.
- **Fury Studios tech sync 2026-05-13** (notes in `standups/2026-05-13_fury-tech-meeting.md`). Durable outcomes: **Haglet** (team's spelling, not Haglit) is being removed class-by-class by Fury and will NOT be done pre-DLC - worker + night code is the highest overlap risk with the banner rewrite, so ping Fury before touching Haglet-coupled classes. Sprite-swap for visual-only changes, prefab variants for substantial; minimise prefab/scene churn to ease merges. No shared build server; David owns GitHub access, Naseer owns Steam.
- **Design decisions locked in May:** wall-phasing Set-Touched Greed **deprecated** in favour of Lurker greed; banner system rewrite a keeper; "Hollywood-authentic" Egyptian aesthetic (Civilization-like reference); Greed mask Set-inspired.
- **Contracts:** RF LTC signed 2026-04-29 (GDrive `1rBBGu-2uEKLKs497JLz-go-yxz6w5Fpt`). The 6 subs went through a May flow-down pass (10-day cure mutual, 30-day convenience client-only, no-AI rep 3.10, RF Schedule A item 3 support terms verbatim). Lost Hive was scrapped and redrafted from scratch. **Side-finding for AP board minutes: Robert is co-Director of Red Marmoset Studios Limited alongside Imi** - disclose as related-party next to Robert/CZP. Risk memo: `Legal/RISK_MEMO_K2C_subcontracts_2026-05-06.md`.
- Superseded by later blocks: all sprint/issue counts, the 337,500 Lost Hive forecast (now 316,200), the 1,019,626 profit figure (now 946,849), and the `1xlHrzOLXBrGWZj7cFQKw53ovqA6nDkrjU8ilqkW2NnM` sheet id (K2C P&L migrated into the AP workbook 2026-06-23).

## Historical — Apr 2026 (superseded, condensed 2026-06-22)
- Deal confirmed Apr 1; full team assembled by Apr 13 (Robert/Tim/Oskar/Fredrik/Imi); MS0 contract signed Apr 29 (was due Apr 15, RF Legal drove the draft). Launch moved Dec 3→Dec 1 (Ishani, Apr 14). Payment schedule, 8-milestone structure, Jira/Confluence/GitHub access, and full GDD all set up in April. "Sands of Duat" flagged as working-title-only (cultural check). Per-day detail lives in `umbrella/k2c_sands_of_duat/standups/` + output_log.

## Sound designer: Carolina Foghammar Nömtak (CURRENT = PIVOT 5, 2026-06-22; was decided 2026-06-15)
> Live state lives in `umbrella/k2c_sands_of_duat/k2c_contracts_tracker.md` (section 7, PIVOT 5 banner). This block updated 2026-06-22.
- **Carolina Foghammar Nömtak** (full legal name; cfoghammar@gmail.com), pnr 000331-2162, Västra Banvägen 8 B, 184 50 Åkersberga. K2C sound designer/composer; also ToA + Knives & Gutters. Came to AP as an AP Academy LIA intern (Game Audio Producer & Sound Designer; Robert was her mentor) — junior, no own company.
- **Scope:** 12 music tracks (classical-Egyptian + minimalist electronica) + ~25 SFX/stings + implementation. Source docs: "Sands of Duat - Audio needs" sheet `1PvIqCvTHADxEptKYCRnFkoInxeEGNE3UcO1fJqFaOHM`; "Soundscape / Composer brief" `1889cDCpRDwmamKwai9Wo6JzG4oqJ1AGmFo_ZN-eQ3I0`.
- **Structure = CZP EMPLOYEE (visstid), DECOUPLED.** Hired as a fixed-term CZP employee (NOT a sub), 2026-06-22 → **2026-10-13** (extended 2026-06-23 from 2026-09-25 in calendar time for her 6–22 Jul absence; audio still locks at MS5). **Comp (negotiated 2026-06-23): 180 SEK/h × 440h = 79,200 SEK GROSS / ~104,086 LOADED** (was 152/h → 66,962/88,000; she opened 220, CZP capped 172, met 180), milestone-paid MS2-MS5 (11,700/22,500/22,500/22,500 gross), ~15 days after each delivery. **Implementation scope clarified** — she assists/ensures audio integrates + adapts, not direct code work. K2C P&L row 16 → 15,376/29,570/29,570/29,570 loaded; **margin 1,010,826 → 993,131**.
- **IP — Carolina RETAINS her music** incl. streaming (YouTube, Spotify) + publishing. AP/RF get only in-game + marketing + OST/vinyl, granted via a **separate Raw Fury-template music-rights agreement** (RF sends ~2026-06-23), NOT via the employment contract. "Same setup as a previous Kingdom DLC" (agreed with Niclas). The RF music fee = 0 (within the 5.6M dev budget).
- **Docs:** employment = `contracts_2026_subcontractors/draft_08_carolina_czp_employment.md` (Enclosure 1 synced 2026-06-23 to the negotiated terms); review Gdoc `1MjarjK5A8X...` updated **in place 2026-06-23** (same fileId/share/link — Carolina still commenter). **MUSIC AGREEMENT (Carolina↔RF) — RF templates received 2026-06-24** (Niclas, thread 19efa4a445c93449): "Raw Fury_Content Creation.docx" (master) + "Special conditions - composer.docx" (license-back). Saved + extracted to `contracts_2026_subcontractors/_rf_music_templates/` (RAG). **Robert decision 2026-06-24: ACCEPT RF's model as-is** = Carolina ASSIGNS all music rights (incl. publishing/master) to Raw Fury, retains only a license-back to live-perform + sell soundtrack on DSP (Spotify/YouTube) + vinyl POST-release (15 b.d. notice + credit, revenue hers). ⚠️ This **overrides the §8.4 "reservation/she-keeps-publishing" framing** and walks back the 2026-06-22 employment cover-mail promise ("du behåller din upphovsrätt/publishing") — re-explained to Carolina. **RF's Juliette drafts the real agreement** from the template + Carolina's details (she's a private individual, not a contractor; RF music fee = 0, within dev budget). **Lawyer NOT looped yet** (Robert deferred — review Juliette's real draft before signing). **Both Gmail SENT 2026-06-24** (Robert): Niclas reply (accept + Carolina's details + pnr + fee=0) — Robert presented the engaging entity to RF as **Aurora Punks**, NOT CZP (his RF-facing framing; she's legally CZP-employed but the music deal is Carolina-as-private-individual↔RF, so unaffected — Lawyer to ensure Juliette's draft doesn't mis-state her employer). Carolina re-explanation sent (Robert trimmed the explicit walk-back paragraph, kept the positive structure). **RETIRED:** draft_07/07b/09/10. **✅ EXECUTED 2026-06-24** — OpenSign doc **`wq8WdASeej`** fully signed by both (Robert/CZP + Carolina), isCompleted=true. Executed PDF in K2C `_legals` (id 1JNNzcygQGnVRfu09jEni02HB6mHlWfzA); source GDoc in `_legals/_working`. **NEXT = payroll:** Carolina is now a CZP employee — **CZP payroll is handled by Sifferrådet (Henrik Franzén, henrik@sifferradet.se)**, NOT Amer (Amer/book-it = Aurora Punks bokslut). Payroll email **SENT to Henrik 2026-06-24** with the milestone payment plan + Carolina's bank (**Nordea 32682231896**). Emilie (Henrik's assistant, Sifferrådet address unknown) to be looped in separately by Robert. Workflow: Sifferrådet books+attests the lön, Robert sends to SEB. MS2 installment 11,700 gross targets ~2026-07-11. Jira: KAN-368, KAN-311 AUDIO epic, KAN-364 Lurker SFX.
