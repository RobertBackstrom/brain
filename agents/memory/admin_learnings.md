# Admin Agent Learnings

<!-- ROTATION-NOTE -->
> **This file holds the most recent entries only** (rotated by `assistant/rotate-learnings.js`, ~100 KB budget).
> Older entries live in `archive/admin/` and are listed in the archive index at the bottom of this file.
> Nothing is deleted and everything stays searchable via `rag_search(query, source="agents")`.
>
> **Still append new learnings to the TOP of this file** — rotation moves the tail out on its own.

>

<!-- Append new learnings with: learning, source project, date, category -->

## 2026-09-01, ett "enkelt" avtal blir enkelt genom att ta bort penningflöden, inte genom att korta meningar [cvb]

**Project:** Curveball (The Gang Studio) | **Category:** avtalsskrivning, mallhantering, firmateckning

**Uppgiften:** Joel Edström bad om "något enklare avtal på plats oss emellan iaf". Förlagan,
AP:s publishing-mall, är 28 sidor. Resultatet blev fyra. **Det som gjorde skillnaden var inte
språket utan att räkna penningflöden.** Förlagan har fem separata flöden (QA-tak, lokaliseringstak,
portingtak på 50 000 USD, 15 procents påslag på marknadsföring, plus vinstdelningen), och varje
flöde drar med sig en definition, en rapporteringsplikt och en tvistyta. Vår affär har **ett**
flöde, en recoup-siffra och en split, eftersom AP inte tar någon köpt media. Då försvinner
Exhibit A och Exhibit B av sig själva. **Generell regel: när en motpart ber om något enkelt, räkna
antalet belopp som kan diskuteras i efterhand och kapa dem, i stället för att korta klausulerna.**

**Mallar som är märkta "tomställda" är det ofta inte.** `Publishing_Agreement_Client_AuroraPunk_Template`
(`1SCNUNc9jf2eXC7-kaaJhes0iQP2i4H96Xal6lrsYPt4`) har rubriken "Aurora Punks and Kinda Brave",
Distant Bloom i preambeln, **Sir Whoopass i Exhibit A**, och signaturblock med Niklas Karlsson,
Atomic Elbow AB samt Scrive-transaktionsstämplar på var femte sida. Tre olika kunder i ett
dokument som beskrivs som en blank mall. **Greppa alltid efter motpartsnamn, org.nr och
signaturstämplar i en mall innan text ur den går till en klient**, annars bryts
[[feedback_no_client_cross_reference]] av mallen och inte av skribenten.

**Riktningen på pengaflödet vänder halva avtalet, inte bara betalningsklausulen.** När AP gick från
att få en andel av utvecklarens intäkt till att ta emot pengarna från plattformen flyttade
rapporteringsplikten, betalningsplikten **och granskningsrätten** över till AP. Förlagornas
dubbelriktade audit-klausul, som är skriven för att båda parter säljer på olika butiker, blir då
fel i båda riktningarna och ska ersättas av en enkelriktad. **Kolla vilken part som är säljande
part innan du återanvänder rapporterings- och auditsektioner. Det är den frågan som avgör deras
riktning, inte vem som är utgivare.**

**Klausulmönstret som är värt att återanvända: co-publisher ur egen andel.** WMAY-mallen säger bara
att part får anlita partner och ska notifiera motparten. Det räcker inte när AP vill kunna ta in en
finansiär senare. Formuleringen som löser det säger fyra saker på en gång: partnern betalas **ur
AP:s egen andel**, motpartens andel påverkas inte, **recoup-beloppet höjs inte**, och ingen
omförhandling krävs. Den tredje punkten är den som brukar glömmas och är precis där en motpart
annars kan tappa pengar. Finansiären namnges inte i avtalet, vilket dessutom håller
[[feedback_no_client_cross_reference]].

**Faktapost med bred räckvidd: AP:s firma tecknas två i förening, alltså har varje AP-avtal två
signaturrader.** Signaturblocket ska bygga för Robert plus ytterligare en ledamot, och en
OpenSign-flow för ett AP-avtal med en motpart har därmed **tre** undertecknare, inte två. Det är
lätt att skicka ut ett avtal som inte kan bli giltigt undertecknat. Samma sak gäller motparten:
fråga efter firmateckningssätt samtidigt som du frågar efter org.nr, inte efteråt.

**Tags:** publishing-avtal, mallhygien, tomställd-mall-som-inte-är-tom, penningflöden,
audit-riktning, co-publisher-ur-egen-andel, firmateckning-i-förening, OpenSign-tre-signatärer,
the-gang-studio, cvb

---

## 2026-07-15 — Necrotic Dominion: Elias Strandberg timavtal — rate/volume/start bump before signature

**Task:** update Elias' hourly contract 188→220 kr/h, 60→45 h/mån. Executed end-to-end.

**Learnings (reusable):**
- **`gdoc-replace.js` is the right tool to amend a native Google Doc contract in place.** `node assistant/gdoc-replace.js <fileId> "old" "new" ["old2" "new2" …]` does surgical `replaceAllText` via the Docs API — preserves clause numbering, bold, layout (unlike `gdrive-update-doc.js` which re-imports a whole HTML body). It reports occurrences replaced per pair, which doubles as verification (I got 1/1 on each of 7 pairs). Use the **smallest reliably-unique** find string; watch out that spacing/format variants are distinct strings ("60 h/month" ≠ "60h/month" ≠ "60 hours per month" — the ND contract had all three).
- **Contract-edit-vs-amendment gate:** before touching a rate, establish whether the contract is signed and whether the start date has passed. Here: unsigned (never sent to OpenSign) + engagement not yet begun → edit-in-place + move start date (07-01→07-17), no retroactivity, no addendum needed. If it had been signed/started, it's an addendum, not an edit. Always ask Robert this before assuming.
- **"inclusive of 12% semesterersättning" must be confirmed on any rate change.** 188 was semester-inclusive; Robert confirmed 220 keeps the same structure. Loaded CZP cost = timlön × 1.3142 (arb.giv.avg only, since semester is already inside the rate): 220 × 1.3142 = **289.12 kr/h**. (Contrast the *on-top* case: ×1.12×1.3142.)
- **ND budget `nd_budget_v3` (`15G3O-9EnR-…`) IS formula-driven** despite the `.csv` tab name — updating input cells B4 (timlön) + B6 (volym) recomputed loaded cost, per-workstream cost, run-rate and calendar automatically. Confirmed the preserve-formulas rule by re-reading after the input write. The formula-Sheet ID cited in `scope_plan.md` (`1V1UjzxD…`) is **dead (404)** — v3 is the live budget; the ND Drive folder `1Ire43dVh7Pin…` holds exactly two files (contract Doc + budget Sheet).
- **Sync every artifact, not just the client doc:** contract Doc + budget Sheet + local `drafts/*.md` (source) + project memory + project CLAUDE.md + output_log. A rate lives in ~6 places here.
- **Data-quality flag surfaced:** the live contract Doc heading had a garbled/concatenated Employee address (two addresses run together) that the local draft did not — a stray manual edit on the Doc. Flagged to Robert rather than guessing which is current. Lesson: diff the live signature-bound Doc against the local source draft when editing; they can drift.

- **Sending this timavtal via OpenSign needs MANUAL placement — the built-ins don't fit.** `--placement nda` anchors to NDA-only text ("For and on behalf of", "Name: Robert/Octavio") the timavtal lacks → returns null → falls back to `last`, which drops signature widgets on the **last page**. But this contract's signature block sits on **page 2, before Annex A** (Annex is the last pages), so `last`/`nda` would put fields inside the Annex tables. Fix: export the Doc to PDF, run `node opensign.js anchors <pdf>`, then call `os.createSignatureRequest({ placement: 'manual', signerWidgets })` programmatically (the CLI can't pass manual coords). For the ND timavtal the block is page 2 (w=596 h=842): Company col x≈72, Employee col x≈268, "Place and date" line yTop≈493, printed party name yTop≈513 — put the signature widget (W140 H16) at yPosition≈498 (on the line, just above the name) and a `type:'date'` widget (auto-fills 'today') at yPosition≈489 on the "Place and date" underscores. Signers: idx0 = Robert for CZP `robert@aurorapunks.com`, idx1 = Elias `elias.h.strandberg@gmail.com` (his personal Gmail. **CORRECTED 2026-08-31 (sbz-001): `elias.strandberg@aurorapunks.com` is NO LONGER defunct** — it was recreated as a Google Group forwarding to that same personal Gmail. Either address reaches him; see [[reference_ap_contractor_mail]]). Sent unordered, both emailed. Doc `ZiR26oSoI2`, 2026-07-15.
- **Always `parseQuery('contracts_Document', …)` before creating a signature request** (admin.md rule) — there's no `list` CLI subcommand, but `os.parseQuery` is exported. Filter Name client-side for the counterparty. Confirmed 0 prior Elias/timavtal docs before sending.
- **Verify the exported PDF text before an external send** — grep for the new values present AND the stale ones absent (here: 220/45/07-17/Bandhagen present; 188/60/07-01/Lovisedalsvägen absent). Cheap insurance against a Doc edit that didn't land or a stale export.

**Source:** Necrotic Dominion (nd-001, Elias hourly engagement; nd-002 address+signing)
**Tags:** necrotic-dominion, elias-strandberg, timavtal, gdoc-replace, contract-amendment, semesterersättning, loaded-cost, formula-sheet, czp, opensign, manual-placement, signature-widgets, parseQuery-precheck, pdf-verify, address-drift

---

## 2026-08-31 - Ett "empiriskt test" av en plattformsbanner måste köras till submit (swa/apb, Xbox)

Beslutet 2026-08-27 var att låta Partner Centers ogodkända App Developer Agreement stå och i
stället testa empiriskt om den faktiskt blockerar. Testet definierades som "låt partnern skapa en
add-on". **Det var för kort.** Skapandet gick igenom, och i två dagar såg det ut som att bannern
var kosmetisk. Först vid submit slog den till. **Definiera plattformstest efter den handling som
faktiskt är i fråga**, alltså publicering, inte det närmaste steget som råkar vara lätt att prova.
Ett halvt test ger falskt lugn och kostade här fyra dagar av en blockerad klient.

**Kolla vilken entitetssträng som sitter på vilket lager innan du bygger ett argument på den.**
Robert utgick från att Xbox-avtalet skulle godkännas "för APDS AB". Partner Center-kontot står i
White Lines Black Spaces AB:s namn; APDS är SupplierWeb- och payee-profilen (vendor 0003066327).
Fyra entitetssträngar i tre Microsoft-system, och de är inte överens. Samma fråga ("vilket lager
menar vi") gäller Nintendo och PlayStation.

**Rättighetsägande är inte firmateckningsrätt.** CZP förvärvade rörelsen med publicerings- och
distributionsrättigheter, inte bolagen. Det ger ingen behörighet att godkänna nya avtal i APDS
eller WLBS namn; konkursbona företräds av sina förvaltare. När Robert ändå väljer den vägen är
det hans beslut att fatta, men det ska ligga i klartext i ticketen med skälen emot, inte
tystas ner. Se [[project_apds_czp_rights_chain]] för den stående formuleringsregeln.

**Faktapost:** `finance@aurorapunks.com` är ett **ägarkonto** på AP:s Partner Center, inte bara
Manager. Hektors `andreassonhektor@gmail.com` är alltså inte enda vägen till Account settings och
Legal Info, och ett ägarbyte behöver inte vara första draget vid entitetsändringen.

**Kanonisk hemvist:** Microsoft-kontotopologin (vilket konto som fungerar mot Partner Center,
royaltyportalen och SupplierWeb, vendornumren, de fem entitetssträngarna) ligger nu i
[[reference_microsoft_accounts]], inte utspridd i den här loggboken och i `secrets_registry.md`.
Läs den innan nästa Microsoft-ärende.

## 2026-08-28 — Plattformens payee-byte har oftast en namngiven blankett med ett eget mottagarfält, och den ligger redan ifylld i vår egen Drive [apb / apb-057]

**Project:** Aurora Punks (PS Partners-onboarding av CZP) | **Category:** plattformsadministration, payee, verifieringsmetod, entitetsbyte

**Huvudlärdomen, och den generaliserar till varje plattform:** när en plan skriver "payee-bytet är
ett eget ärende med egen ledtid", stanna och leta efter **instrumentet** innan du planerar runt
ärendet. Hos Sony visade det sig vara en namngiven blankett, `SIE Company Setup Form` (v20210315,
tre avsnitt, avsnitt 1 fylls internt av SIE), och **förra entitetsbytets ifyllda, DocuSign-signerade
exemplar låg redan i vår Drive**. En `rag_search` på plattformsnamn plus "company setup form payee
bank" tog två minuter och förvandlade ett formlöst supportärende till en transkribering.

**Det som satt i det gamla exemplaret var själva lösningen på entitetsproblemet.** WLBS-blanketten
angav `Company/Indiv. Name: White Lines Black Spaces AB` men
`Payee Name (if different from above): Aurora Punks Development Services AB`, med APDS eget
SEB-konto. Sony har alltså **ett eget fält för att skilja avtalspart från betalningsmottagare**, och
förra entitetsbytet gick igenom den vägen, inte genom nytt avtal och inte genom kontoflytt.
**Generell regel: innan du föreslår en kontoflytt eller en avtalsnovation hos en plattform, kontrollera
om deras finansblankett redan har ett payee-fält.** Det är den billiga vägen och den har prejudikat.

**Kontrollera vad blanketten gör obligatoriskt, för där ligger den enda riktiga ledtiden.** SIE:s
kontoändring kräver fyra saker: telefonnummer till ekonomikontakt för uppringd verifiering, färsk
W-9/W-8, uppdaterad setup-blankett, och **utanför USA och Kanada kontoinstruktioner på bankens
brevpapper**. Den sista är en beställning hos banken och den enda posten vi inte kan producera
själva. Den ska beställas först, inte sist. Övrigt att räkna med: **betalningsvillkor netto 60** och
**en blankett per valuta**.

**Namnkedjan Payee Name -> W-8 -> kontohavare måste vara identisk, annars tystnar utbetalningarna
utan notis.** Det är samma mekanik som stoppade Microsofts royalty i fem månader (`apb-055`).
Verifiera kontohavarens exakta lydelse mot ett kontoutdrag innan du skriver Payee Name, inte mot
minnet. Här var den `CREATION ZERO POINT HOLDING AB`, alltså ska handelsnamnet "Aurora Punks" bara
stå i DBA-fältet. **Handelsnamn i ett payee-fält är en tickande betalningsstopp.**

**W-8BEN-E: skriv aldrig av den från grunden, kopiera den föregående entitetens.** APDS signerade
exemplar gav hela uppsättningen: chapter 3 = **Corporation**, LOB-grund = **ownership and base
erosion test**, artikel **12 §1**, **0 %** på **Royalties**, och Foreign TIN-fältet tar **momsnumret**
(`SE` + org.nr utan bindestreck + `01`), inte org.nr. Noll procent är rätt för svenskt bolag enligt
skatteavtalet med USA. AP fyllde en gång i 30 % mot Robot Cache och fick det påpekat av motparten.
**Men kopiera inte chapter 4-statusen (FATCA) blint mellan entiteter av olika slag:** ett
verksamhetsdrivande bolag är normalt Active NFFE, ett **holdingbolag kan vara Passive NFFE**, vilket
dessutom utlöser ett ställningstagande om substantiella amerikanska ägare. Den posten ska revisorn
avgöra. Och läs originalPDF:ens kryss som bild när textextraheringen placerar en markering i en
del av blanketten som inte kan stämma, checkbox-glyfer extraheras som "4" och hamnar fel.

**Tags:** Sony, SIE, PlayStation, payee, W-8BEN-E, Active-NFFE, Passive-NFFE, artikel-12,
company-setup-form, kontobekräftelse-på-brevpapper, netto-60, namnmatchning, entitetsbyte, apb-057

---

## 2026-08-28 — Plattformarnas egna nyhetsbrev är driftinformation, inte reklam, och de kommer HTML-only så våra mailverktyg visar dem som tomma [apb / apb-057]

**Project:** Aurora Punks | **Category:** verktygsfällor, ärendebevakning, plattformsadministration

**Fällan:** `gmail_read` och `gmail_thread` returnerar `"(no plain text body)"` för
plattformsutskick som saknar text/plain-del. Två utskick från
`noreply-comms@partners.playstation.net` (26 och 27 aug) såg därför tomma ut i verktyget, och
snippet-raden gav bara en marknadsföringsaktig ingress. **Innehållet var driftkritiskt.**
Lösningen är fem rader: hämta `format:'full'` via `assistant/gmail-api.js`, rekursera genom
`payload.parts` efter `text/html`, base64url-avkoda och strippa taggar med länkarna bevarade som
`text [url]`. Skriptet ligger som mönster i den här ärendeloggen. **Läs aldrig av ett
plattformsutskick på snippet-raden, och tolka aldrig "(no plain text body)" som "inget innehåll".**

**Vad som faktiskt låg där, som exempel på varför det är värt besväret:** Sony flyttade
DevNet-användarhantering in i PlayStation Partners 26 aug (träffar Collaborator-steget i en pågående
title transfer), omdefinierade Team Admin till en delegerad roll under **Global Account Admin**
(vår öppna post var ställd på fel roll och frågan till motparten hade blivit fel ställd), lanserade
en ny dokumentationssajt med en onboardingsida som täcker exakt den sekvens vi höll på att
rekonstruera själva, och annonserade två underhållsfönster i Content Pipeline. Fyra saker som alla
påverkar ett kritiskt ärende, i två mail som såg ut som nyhetsbrev.

**Generell regel:** när ett ärende hänger på en plattform, läs plattformens egna utskick från de
senaste två veckorna som **primärkälla** innan du reviderar planen. Rollmodeller och portalgränser
ändras mellan att en plan skrivs och att den utförs.

**Tags:** gmail-html-only, format-full, multipart, PlayStation-Partners, GAA-vs-Team-Admin,
DevNet-user-management, plattformsutskick-som-primärkälla, apb-057

---

## 2026-08-28 — En misslyckad obevakad inloggning ska inte köras om: utelåsningsrisken är dyrare än läsningen [apb / apb-057]

**Project:** Aurora Punks | **Category:** autonomt omdöme, Playwright, säkerhet

**Situationen:** `devnet-ip-allowlist.js --login` fyllde Sonys Okta-formulär korrekt (bekräftat på
skärmdumpen `login-1b-filled.png`, e-post i mörk text alltså verkligt värde, lösenordsfältet fyllt),
men efter Sign in visade `login-2-post-password.png` **samma inloggningsruta med tomt e-postfält**.
Ingen MFA-kod skickades, och mailpollningen timeoutade på 180 s med diagnosen "no MFA mail" som
pekar åt fel håll. Rätt diagnos: **submit avvisades och widgeten återrenderades**, sannolikt
utgånget DEVNET_PASS.

**Beslutet, som är själva lärdomen:** jag körde **inte** om den. Upprepade misslyckade
inloggningar mot Okta låser kontot, och det var samma konto Robert behövde för att kunna skicka in
en kritisk plattformsansökan inom dagar. **En läsning som kan vänta är aldrig värd en utelåsning av
ett konto på den kritiska vägen.** Regel för obevakade körningar: en misslyckad inloggning mot ett
MFA-skyddat konto är en rapportpunkt, inte något att försöka igen. Fortsätt med den del av ärendet
som inte är gated på inloggningen, och det finns nästan alltid en sådan del (samma ordningsläxa som
i `apb-055`, där pengarna låg i den ogatade halvan).

**Två diagnostiska detaljer att återanvända.** (1) `login-2-post-password.png` skiljer på
avvisad inloggning och trasig mailpollning på en sekund, jämför om e-postfältet är ifyllt eller
tillbaka på platshållartext. Kolla den skärmdumpen **före** du felsöker mailpollaren.
(2) `.check().catch(() => {})` på "do not challenge me"-rutan loggade "ticked" fast rutan förblev
omarkerad på skärmdumpen. Tyst svald sidoeffekt, samma antimönster som redan är noterat för
sentinels: **ett steg som inte kunde utföras ska larma lika högt som ett steg som utfördes fel.**
(3) En sparad `storageState` som bara innehåller Akamai- och Adobe-cookies är **inte** en session.
Kontrollera att det finns en identitetscookie från SSO-domänen innan du kallar en state-fil
autentiserad.

**Tags:** Okta, utelåsningsrisk, obevakad-körning, devnet-ip-allowlist, tyst-swallad-catch,
storageState-utan-identitetscookie, apb-057

---

## 2026-08-28 — plattformarnas avräkningar ligger i mailen, i maskinläsbart skick

Uppföljning på posten om Steams "Life to date". När ett bolag är i konkurs och huvudboken är borta
går titelnivå ändå att rekonstruera, för plattformarna mailar sina avräkningar och gör det i
strukturerade format.

**Sony.** `NO-REPLY-BI@sony.com` skickar varje månad "Purchase Order ... SALES <månad>" med
`Publisher Statement.XLSX` bifogad. Ark 2 har en rad per SKU, land och månad med **No Units Sold**,
WSP i lokal valuta och Total WSP i settlement-valutan. Tre separata flöden: SIE Europe
(Publisher Statement), SIE America ("Digital Third Party Royalty Report for UB<kod>") och
Japan/Asien ("PlayStation Store ROYALTY_<MON>-<år>_<vendor>_EUR"). Sök `from:sony.com has:attachment`.
Statements fortsätter komma till ett konkursat bolag.

**Beep Japan.** Månatliga "REV REPORT"-PDF:er per plattform och format, med SRP, pris efter
plattformsandel, **Units Sold** och Revenue i JPY. Hela historiken låg dessutom som en zip på 2,8 MB
i en enda tråd. Leta efter zip-bilagor innan du parsar hundra lösa filer.

**Nintendo.** Skickar bara notiser, ingen data. Rapporterna finns enbart i Developer Portal och
kräver inloggning. Räkna inte med mailen där.

**Verktygen.** `assistant/gmail-attachments.js search "<query>" --download --output-dir <dir>`
gör bulkhämtning, men **filnamn krockar** eftersom Sony kallar varje bilaga "Publisher
Statement.XLSX". Ladda ner per meddelande till en egen mapp döpt efter ämne plus message-id.
CLI:ts `list` trunkerar attachment-id med "..." så det går inte att kedja, medan MCP-verktyget ger
hela id:t. Gmail-sökningen returnerar högst tio meddelanden per anrop, så historik måste hämtas i
månadsfönster med `after:`/`before:`.

**XLSX utan bibliotek.** openpyxl finns inte på VPS:en. Packa upp med `zipfile`, läs
`xl/sharedStrings.xml` och `xl/worksheets/sheet*.xml` med ElementTree, slå upp `t="s"`-celler i
strängtabellen. Räcker gott för avräkningsfiler.

**PDF-parsning:** `pdftotext -layout` finns installerat. Validera alltid utvunna enhetstal mot
priset, `abs(revenue - units*price) < 5 %`, annars plockar regexen upp SRP-tal som antal och du får
tolvtusen sålda exemplar av ett spel som sålt trettio.

## 2026-08-28 (addendum 2) — Fråga om verktyget redan finns innan du lägger en uppgift på Robert [project: czp, 1993]

**Kategori:** verktygsinventering, plattformsdata · **Taggar:** ndp, nintendo, playwright-session, followup-hygien, avstämning-som-bevis, czp-032, czp-033

Jag skrev czp-032 och lade den på Robert med motiveringen att Nintendos säljrapporter "bara går
att läsa inne i portalen". Det stämde. Slutsatsen att det därför var hans uppgift gjorde det inte.
`assistant/ndp-session.js` fanns redan sedan devkit-arbetet tre dagar tidigare: lösenord ur `.env`,
MFA-koden hämtad ur Gmail, 30 dagars enhetstrust i en persistent Playwright-profil. Robert behövde
påminna mig om ett verktyg jag själv hade i repot.

**Regeln:** innan en uppgift skrivs som "Robert måste logga in någonstans", `grep` efter tjänstens
namn i `assistant/*.js` och i agent-learnings. En inloggning som någon annan agent redan har
automatiserat är inte ett hinder. Det gäller särskilt portaler bakom MFA, eftersom det är precis
dem någon redan har lagt en dags arbete på att komma in i.

**Var Nintendos siffror ligger.** Admin > **Payments and Financial Reports**, inte under
produkterna. Sidan renderar hela historiken som Liferay-dokumentlänkar (`/documents/23933/...`) i
DOM:en. JSON-API:t `/o/payments/list/23933` syns i nätverksloggen men svarar **500 vid refetch** i
sidkontexten, så DOM-länkarna är den hållbara vägen. Tre filtyper per månad:
`DigitalSalesReport` (pdf, sammanställning och provisionsfaktura), `DigitalSalesDetail` (csv, en
rad per titel, land och månad med `Sales Units` och `Final Payable Amount` i utbetalningsvalutan)
och `DigitalSalesDetailByState` (csv, US och CA per delstat). Verktyg byggda:
`assistant/ndp-sales-reports.js` och `assistant/ndp-aggregate.js`.

**Praktiskt:** en Playwright-`launchPersistentContext` låser profilkatalogen, så två skript mot
NDP kan inte köra samtidigt. Kör dem i serie. Nedladdning av 190 dokument tar drygt fem minuter,
alltså längre än Bash-verktygets tvåminutersgräns; kör i bakgrunden och vänta på processen, inte
på en `sleep`.

**Avstämningen är det som gör siffran användbar.** Detaljraderna för alla titlar summerade till
89 513,94 SEK. Utbetalningsbeskeden visade 89 138,70 remitterat plus 375,24 innehållet under
minimibeloppet. Exakt samma summa. Sex månader saknade detalj-csv, och deras pdf visade
Sales Amount 0,00, alltså inga sålda enheter och inte en lucka. **Innan ett plattformsvärde skrivs
in i ett kundunderlag: hitta plattformens egen kontrollsumma och stäm av mot den.** Utan den kan
man inte skilja "det såldes inget" från "filen saknas", och det är skillnaden mellan en korrekt
rapport och en som underskattar utvecklarens andel.

**Bifynd som var värt mer än siffrorna.** Utbetalningsbeskeden bär betalningsmottagare och
bankkonto. Mottagaren byttes i januari 2024 från White Lines Black Spaces AB till "Stockholm Core
Office", och bankkontot byttes i februari 2025, alltså fem månader efter WLBS-konkursen. Det syns
bara om man läser pdf-huvudena, inte i csv-datan. **Läs metadata i avräkningar från en motpart,
inte bara beloppen** — vid en konkurs är mottagarraden ofta det enda spåret av att någon har
dirigerat om ett penningflöde. Ligger som czp-033.

**Utfallseffekt på 1993:** Nintendo utanför Japan gav 2 091 enheter och 51 664 SEK netto, mot
10 000 uppskattat. Mottagen Gross Revenue gick från 202 916 till 244 580 och återvinningen av
Service Spend från 74,9 till 90,2 procent. Slutsatsen står sig men marginalen är tunn, och det
är den sortens ändring som avgör om nästa kvartalsrapport utlöser en utvecklarandel.

**Kanonisk hemvist:** rättighetskedjan för 1993 (Krister som ägare, Gunnars och Mattias 20 procent,
Limit Breaks 8 procent, WLBS-avtalets saknade sektion 12) ligger nu i
[[project_1993_space_machine]], inte bara i den här loggboken. Läs den innan nästa kvartalsrapport.

## 2026-08-27 — Registreringsstatus (F-skatt/moms) hämtas utan BankID via Skatteverkets öppna e-tjänst — allabolag ljuger [apb / apb-056]

**Project:** Aurora Punks | **Category:** skatt, playwright, verifieringsmetod, öppna-källor

**Lärdomen som sparar en BankID-runda:** Skatteverkets e-tjänst **"Hämta företagsinformation"**
svarar på om ett bolag är godkänt för F-skatt, registrerat för moms och registrerat som
arbetsgivare — **öppen för alla, ingen e-legitimation**. Svaret kommer per mail, alltså läsbart
med Gmail-MCP direkt efteråt. Det gör hela frågan "har bolag X F-skatt?" autonom. Ingen anledning
att be Robert logga in på verksamt för den frågan.

**Sidan:** `https://skatteverket.se/privat/sjalvservice/allaetjanster/tjanster/hamtaforetagsinformation.4.3810a01c150939e893f3e69.html`.
Formuläret ligger **inbäddat på sidan**, inte bakom någon "Starta tjänsten"-länk, och är byggt av
**web components med shadow DOM** (`hamtaforetagsinformation-skv-wizard`). Konsekvenser för
Playwright:
1. `$$eval('input,button')` på light DOM hittar **ingenting** — bara sidans sök- och menyfält.
   Man måste rekursera genom `el.shadowRoot`.
2. Fälten har stabila id:n: `input#PERSONORGNUMMER_FIELD_NAME_ID`, `input#EPOST_FIELD_NAME_ID`.
   `page.fill()` med de selektorerna funkar (Playwright piercar öppna shadow roots).
   Obs: id:t sitter på **både** custom-elementet och inner-inputen, så prefixa med `input#`.
3. Samtyckesrutan har genererat id (`skv-selection-control__XXXX`) — matcha på regex, inte exakt.
4. **Knapparnas text ligger i en slot, så `innerText` är tom.** Klicka på klassen i stället:
   `button[class*="--primary"]` som är `offsetParent != null`. Wizarden är tre steg
   (Gör en beställning → Granska och skicka in → Kvittens) och samma primary-klick tar dig genom
   alla. Kvittensen säger "Vi har tagit emot din förfrågan".
5. Cookie-bannern måste bort först: `#accept-all_button`.
6. `sjalvservice.skatteverket.se` finns inte som värdnamn (`ERR_NAME_NOT_RESOLVED`), och den
   gamla `/foretag/etjansterochblanketter/...hamtaforetagsinformation`-URL:en är **404**. Rätt väg
   är `/privat/sjalvservice/...`.
7. Nod-tips: `require('playwright')` löses relativt **skriptets** katalog, inte cwd. Ett skript i
   `/tmp` hittar inte modulen även om du `cd`:at till `assistant/`. Kör med
   `NODE_PATH=/home/assistant/projects/assistant/node_modules`.

**Fyndet i sak:** Aurora Punks AB, 559256-9718 — **Godkänd för F-skatt: NEJ. Registrerad för moms:
NEJ** (svar 2026-08-27 13:40 från `foretagsuppgifter@skatteverket.se`). Det bekräftar premissen i
Lawyer-PM:et 2026-07-17 ("CZP fakturerar bara för att AP nekats F-skatt") och att hela
paying-agent-strukturen i K2C-memot 2026-05-04 fortfarande vilar på ett öppet ärende.

**Varningen:** **allabolag.se listade AP som "Registrerad för: Moms, F-skatt, Arbetsgivaravgift"**
och angav Skatteverket som källa. Det är fel. allabolags registreringsblock släpar eller speglar
nyregistreringen från 2020 — använd det aldrig som underlag för om en motpart har F-skatt. Det
ligger i linje med den äldre lärdomen att allabolag släpar efter Bolagsverket på styrelsedata.
Gå alltid till Skatteverkets egen e-tjänst.

**Kvar bakom BankID:** själva **ärendestatusen** för ansökan (avslagsdatum, motivering, ev.
överklagandehänvisning) ligger på Skatteverket Mina sidor / verksamt.se och kräver
e-legitimation. Playwright kan inte signera med BankID — den delen måste Robert hämta, eller så
ringer man Skatteverkets företagsskattelinje.

**Tags:** F-skatt, moms, Skatteverket, hämta-företagsinformation, shadow-DOM, web-components, Playwright, allabolag-opålitlig, BankID-gräns, konkurssmitta, APDS, paying-agent, apb-056

**Tillägg samma dag — firmateckning i förening styr HELA kanalvalet mot Skatteverket, inte bara
signaturen.** Robert påpekade att AP:s firma tecknas i förening. Det är rätt, och det har tre
följder som är lätta att missa och som gäller varje bolag med föreningsteckning:
1. **Samtliga som tecknar i förening måste underteckna ansökan.** En ledamot ensam kan inte skicka
   in skatte- och avgiftsanmälan, oavsett om det sker via verksamt.se eller på papper.
2. **Personer som tecknar i förening kan inte registreras för e-tjänsten** för moms- och
   arbetsgivardeklarationer. De måste i stället utses till **deklarationsombud (SKV 4809)**.
   Behörigheten firmatecknare/ombud i e-tjänsterna styrs av **SKV 4801**.
3. **Pappersvägen är den rena vägen vid föreningsteckning:** **SKV 4620** (Företagsregistrering,
   skatte- och avgiftsanmälan), undertecknad av två ledamöter. Ändringar går på **SKV 4639**.

**Gränsdragningen som håller arbetet igång:** att *ringa* Skatteverket och fråga vad avslagsgrunden
var är ingen rättshandling och kräver ingen medtecknare. Blockeringen träffar inlämnandet, inte
informationsinhämtningen. Fråga alltid "är detta en rättshandling eller en fråga?" innan du parkerar
ett ärende på firmateckning.

**AP:s lydelse (registreringsbevis, senaste registrering 2026-04-21):** *"firman tecknas av
styrelsen; firman tecknas två i förening av ledamöterna; dessutom har verkställande direktören rätt
att teckna firman beträffande löpande förvaltningsåtgärder."* Robert är ledamot, varken VD eller
ensam firmatecknare. Varning: registret listar Andreea Chifu som VD medan masterbrain säger att hon
avgick som VD under 2025 — om avgången aldrig anmäldes till Bolagsverket står hon kvar. **Luta dig
aldrig mot VD-spåret utan färskt registreringsbevis.**

**Tags (tillägg):** firmateckning-i-förening, SKV-4620, SKV-4639, SKV-4801, SKV-4809,
deklarationsombud, rättshandling-vs-fråga, VD-i-registret-vs-verkligheten

## 2026-08-27 — Plattformens entitetsnamn bor i flera system som tystnar var för sig, och "statements kommer" betyder inte "pengar kommer" [apb / apb-055]

**Project:** Aurora Punks (Xbox-entitetsflytten) | **Category:** plattformsadministration, payee, verifieringsmetod

**Huvudlärdomen, generell för varje plattform:** ett bolagsnamn hos en plattform är inte **ett**
fält, det är tre till fyra fält i tre olika system som uppdateras var för sig och tystnar var för
sig. På Microsoft ligger de så här, och de var alla oense med varandra:

| Lager | System | Vad som stod där |
|---|---|---|
| Company account | partner.microsoft.com | White Lines Black Spaces AB |
| Avtalen | Adobe Sign (TLA, GDK-addendum) | WLBS AB dba Aurora Punks |
| Supplier/payee | SupplierWeb + royalty.microsoft.com | APDS AB, vendor 0003066327 |
| Legacy vendor | SupplierWeb | WLBS AB, vendor 0003039381 |

**Att fråga "vilket bolag står kontot i" utan att säga vilket lager man menar ger fel svar.** Fråga
per lager. Och notera att vendorposten aldrig döptes om: MS skapade en **ny** supplier-profil vid
förra entitetsbytet och lät den gamla ligga kvar. Räkna alltså inte med att en namnändring är den
mekanism plattformen använder, även när det är den man ber om.

**Den dyra lärdomen: kontrollera betalningsflödet, inte rapportflödet.** Royalty-*statements* från
Microsoft fortsatte komma varje månad hela vägen till 17 aug 2026, så allt såg friskt ut. Men
`Microsoft Payment Advice` (avsändare `MSSADM@microsoft.com`) upphörde efter **13 mar 2026**. Fem
månaders utbetalningsstopp, helt tyst, ingen avvisningsnotis. Nintendo skrek `RSN REGULATORY
REASON`, Microsoft sa ingenting alls. **Metod som avslöjar det på en minut:** sök på
`subject:"Microsoft Payment Advice"` (eller plattformens motsvarande betalningsavi) och jämför
serien mot statement-serien. Två serier, inte en. Ett glapp mellan dem är ett betalningsstopp.
Gör den kontrollen på varje plattform vid varje entitetsärende, den är gratis.

**Plattformens egen förklaring låg i en två år gammal tråd.** Reed Hunt, 2024-08-14: *"Whenever
there's a legal name or business address mismatch in those two places on our side [SupplierWeb
och avtalen], the team is unable to send royalty payments."* Åtgärden Microsoft då accepterade var
**ett signerat dokument på företagets brevpapper som anger gammalt och nytt värde explicit**, inte
en kontoflytt och inte en produktmigrering. Det är ett billigt instrument som löser en dyr
blockering, och det är värt att erbjuda proaktivt. **Generellt: sök i den egna mailhistoriken
efter förra gången samma plattform löste samma klass av problem innan du ber dem beskriva
processen.** Motparten har ofta redan skrivit ned svaret åt oss.

**Tredje mönstret, och det är ett återfall:** RoyCare gav 2026-05-01 en rak hänvisning
(`p2pvisup@microsoft.com` för byte av juridisk person, DUNS och bank) och stängde ärendet.
Ingenting skickades dit på fyra månader. **En hänvisning till ett annat team är inte ett svar,
det är en öppen åtgärd.** När en supportkedja slutar med "kontakta X", ticketisera X samma dag,
annars dör spåret när ärendenumret stängs. Samma form som Reeds direkt-invite-förslag i `swa-002`
som låg orört från 2026-06-25 till 2026-08-17.

**Fjärde: utbetalningar som gick till ett konkursbolag efter konkursdagen ska återvinnas i en
befintlig avstämning, inte i ett eget ärende.** Fyra MS-advices (15 dec 2025, 13 jan, 13 feb,
13 mar 2026) landade hos APDS bo. Atomic Elbow körde redan en post-för-post-avstämning mot samma
förvaltare för samma period för sin andel. Att öppna ett parallellt spår mot en förvaltare som
redan sitter med underlaget är dubbelarbete och sämre position. **Kolla alltid om en annan part
redan driver samma återvinning mot samma bo.**

**Ordningsläxa:** planen hade satt "läs portalen först" och gjort allt annat beroende av
inloggningen, som var blockerad på creds. Men payee-halvan krävde ingen inloggning alls. **När ett
spår är gated på en credential, leta efter den del av spåret som inte är det innan du parkerar
hela ärendet.** Här låg pengarna i den ogatade halvan.

**Tags:** Microsoft, Xbox, Partner Center, SupplierWeb, RoyCare, p2pvisup, payee, vendor,
entity-transfer, APDS, WLBS, CZP, konkurs, betalningsstopp, verifieringsmetod

## 2026-08-27 - Att en bilaga finns är inte samma sak som att den håller, och en rutinbegäran har ett datum den inte får skickas före [apb / apb-054, apb-051]

**Project:** Aurora Punks (Nintendo-entitetsflytten APDS till CZP) | **Category:** process, avtalsgranskning, motpartstaktik, verktygsfällor

**Kärnan: sändchecklistan kontrollerade att avtalen fanns i Drive, inte vad de säger när motparten läser dem.** Ett mail till Nintendo licensing låg klart att skickas med två signerade avtal bifogade och en checklista som var avbockad på "handlingarna finns". Att extrahera båda PDF:erna och läsa dem som en granskare hos motparten tog tio minuter och hittade fyra saker, varav en hade kunnat skapa en ny fordran åt en pågående processmotpart. **Regel: innan en handling bifogas en extern begäran, läs den utskriven och kontrollera fyra saker.** (1) **Identifierare mot det mailet påstår.** Boavtalet skriver säljarens org.nr fel på två ställen i den operativa texten, preambeln och den punkt som definierar "Bolaget", medan rätt nummer förekommer en enda gång i en bilaga sammanställd av en utomstående. Vår motpart matchar mot kontots registrerade nummer. (2) **Hänvisningar till bilagor som inte ligger med.** Det andra avtalets punkt 1 överlåter "the assets mentioned in the enclosed addendum" och något addendum finns inte i handlingen, i just det led som ska belägga köparens fång. Motargumentet låg i punkt 2 i samma avtal, men det måste skrivas ut, annars är standardsvaret "please send the addendum" och tre veckor är borta. (3) **Villkor som inte är uppfyllda.** Äganderättsförbehåll plus "all rights are transferred once proof of payment is done", med en obetald slutrat. Volontera aldrig det, men vet att det står där. (4) **Adresser och datum som skiljer sig** från det mailet anger. Föregrip varje avvikelse i en mening. Att själv peka ut ett fel läses som noggrannhet, att bli påkommen med det läses som en diskrepans i anspråket.

**En konkursköpares fordringar följde inte med, och det styr hur payee-frågan får formuleras mot varje plattform.** Rörelseöverlåtelseavtalet undantar uttryckligen "likvida medel och fordringar" och tillträdesdagen är en bestämd dag. Plattformsintäkt upplupen före tillträdet är därmed en fordran som stannade i konkursboet. Utkastet skrev "there is an outstanding balance on the account" som vi vill ha löst, alltså ett skriftligt anspråk, fyra dagar före ett förlikningssammanträde där samma bo driver återvinning mot köparbolaget. **Fråga aldrig efter "the outstanding balance" i ett entitetsbyte. Fråga från vilket datum utbetalningar går till den nya entiteten och låt plattformen sätta brytpunkten.** Samma svar löser payee-frågan, ger det datum vi faktiskt behöver, och skriver inte ihop en ny post åt motparten. Gäller varje plattform i en konkursköpt portfölj.

**En rutinåtgärd som "kostar ett mail" kan ändå ha ett datum den inte får skickas före.** Åtgärdslistan bar "be förvaltaren om skriftlig rättelse av org.nr". Förvaltaren är motpart vid ett sammanträde fyra dagar senare. En begäran om ett intyg som stärker vårt fång, inkommen då, talar om för honom att hela plattformsspåret hänger på hans medverkan, alltså en hävstång han inte hade. **Stäm av varje begäran om intyg, bekräftelse eller rättelse mot processkalendern innan den går, även när den är ren administration.** Rättelsen behövdes dessutom inte för att kunna skicka.

**Verktygsfälla: skapa aldrig om en Gmail-draft som bär headers verktyget inte kan skriva.** Draften hade `Cc` satt, och `gmail_create_draft` har inget CC-fält samtidigt som den raderar befintliga drafter på samma tråd. Att "förbättra" draften genom att skapa om den hade tyst tappat CC:n till den namngivna handläggaren. **Läs headern innan du rör en färdig draft. Leverera textändringar som klipp-och-klistra-block i memot i stället för att bygga om draften.** Samma sak gäller bilagor, inReplyTo och trådtillhörighet. Och en avbockad checklistpunkt är värd att verifiera mot verkligheten, inte mot listan: punkten "CC saknas" var redan åtgärdad och hade annars gett dubbel CC.

---

## 2026-08-26 — En domstolskallelse kan ligga i Drive utan att någon vet om den, och "ingen anmärkning registrerad" har ett bäst-före-datum [apb / apb-051, apb-053]

**Project:** Aurora Punks (APDS-konkursen K 4429-25) | **Category:** process, ärendebevakning, självrättelse

**Learning (en negativ statuskontroll är färskvara, och Säker e-post bryter hela vår normala mailkedja):** Ett 4am-svep på en ticket om rättighetskedjan APDS -> Bright Gambit -> CZP hittade i stället att förvaltaren gett in **anmärkningsskrift 2026-08-11** mot CZP:s bevakning om 512 500 kr och att Umeå TR **kallat till förlikningssammanträde 1 september kl. 09:30**. Kallelsen kom 2026-08-12, PDF:en låg i Drive och var RAG-indexerad, men ingen ticket, inget memo och ingen aktivitetspost fanns. Två saker gjorde att den föll mellan stolarna. **(1) Den senaste noteringen i materialet var "Ingen anmärkning har registrerats per 2026-08-06"** och den lästes vidare som ett tillstånd. Anmärkningen kom fem dagar senare, på fristens sista dag, vilket är exakt när motparter ger in. En negativ kontroll mot en löpande frist ska alltid skrivas med **både datum och fristens utgång** ("ingen anmärkning per X, fristen går ut Y"), annars läser nästa agent den som ett svar i stället för en ögonblicksbild. **(2) Sveriges Domstolars "Säker e-post" levererar bara en avisering med en engångslänk**, ingen bilaga och inget innehåll. Vår vanliga kedja (gmail_search -> läs tråd -> extrahera bilaga -> ticketisera) ser därför ingenting att ticketisera, och `gmail_search` på "Umeå tingsrätt" ger en tom notis. Innehållet finns bara om någon manuellt öppnat länken och laddat ned. **Meddelandena raderas ur tjänsten efter 30 dagar.** Praktisk regel: en avisering från `umea.tingsratt.allmanna@dom.se` eller `securemail.domstol.se` ska alltid bli en ticket direkt på aviseringen, innan innehållet är känt, och nedladdningen ska arkiveras med målnummer i filnamnet. Kom också ihåg att **räkna aviseringarna** - här kom två (15:10 och 15:11) och bara en laddades ned, vilket gör att en möjlig andra anmärkning mot Roberts privata bevakning fortfarande är okänd.

**Sidofynd med bäring på allt underlagsarbete:** när en förvaltare skriver att "något underlag till stöd för betalningarna har inte påträffats", stäm av påståendet mot **hans eget utlämnade material** innan det tas för givet. De 192 000 kr som här angreps enligt KonkL 4:10 delade sig vid avstämning mot huvudbok 1675/2440 i 107 000 kr låneåterbetalningar med daterade motposter i samma huvudbok och 85 000 kr faktiska delbetalningar av en förfallen faktura. Bara den andra halvan matchade förvaltarens beskrivning. Anmärkningsskriften innehöll dessutom ett räknefel ("fem betalningar", listar sex). Motpartsskrifter är inte avstämda källor.

---

## 2026-08-26 — tesseract finns INTE på den här maskinen längre, läs skannade PDF:er som bilder i stället [apb / apb-051]

**Project:** Aurora Punks | **Category:** tooling, självrättelse

**Learning:** En tidigare learning (2026-06-10, DevOps) säger att poppler-utils **och** tesseract-ocr installerades på VPS:en för agent-PDF-läsning. Per 2026-08-26 gäller bara halva: `pdftotext` och `pdftoppm` finns i `/usr/bin`, **`tesseract` saknas helt** (exit 127). Sannolikt en följd av bare-metal-migreringen. Konsekvensen är att en inskannad PDF utan textlager ser tom ut - `pdftotext` på det signerade APDS/CZP-konsultavtalet gav bara en av sex sidor, och just den sidan saknade avtalets bärande villkor. **Arbetssättet som fungerar:** `pdftoppm -r 200 -png fil.pdf /tmp/ut/p` och läs sedan varje `p-N.png` med Read-verktyget, som ser bilden. Det tog fram punkt 1 (uppdraget beskrivet som "approximately 40 hours per week", flexibelt schemalagt) och punkt 2 (fast arvode "100 000 SEK + VAT per month", månadsvis fakturering "specifying the work performed") - allihop avgörande för att kunna svara på en begäran om tidredovisning. Kontrollera alltid `which tesseract` innan du planerar ett OCR-steg, och hoppa direkt till bild-läsning när sidantalet i `pdfinfo` inte matchar mängden text `pdftotext` ger.

---

## 2026-08-26 — Ett mellanled i en förvärvskedja ger bättre rättsläge, men bara om mellanledets egen förvärvshandling finns [apb / apb-051]

**Project:** Aurora Punks / CZP | **Category:** avtal, bokföring, M&A-hygien

**Learning:** Kedjan APDS-konkursbo -> Bright Gambit -> CZP är starkare än en direkt närståendeöverföring, eftersom ett mellanled med eget förvärv ur boet bryter den raka linjen från konkursbolaget till ägarens holdingbolag. Men styrkan sitter helt i mellanledets **egen** förvärvshandling, och den saknades hos oss: bred Drive-sökning gav 19 Bright Gambit-träffar utan att avtalet APDS-konkursbo -> BG fanns bland dem. Det man ska göra då är inte att fortsätta leta internt. **Motparten skrev redan svaret i klartext:** Andreea 2026-06-10, "We have an agreement for the assets with the contract as an appendix". Konkursboavtalet finns alltså som bilaga till hennes exemplar och ska begäras därifrån. Läs motpartens formuleringar som ett arkivindex, inte bara som ett svar.

**Två saker att kontrollera i varje sådan kedja, båda missade här tills nu.** (1) **Återtagandeförbehåll mot faktisk fakturering.** Avtalets punkt 4 håller äganderätten hos säljaren tills full betalning skett, och slutraten var obetald. Orsaken visade sig dock vara att **säljaren aldrig fakturerat** (CZP:s SIE4 och Gmail visar bara rat 1 och 2, 36 000 + moms vardera), inte att köparen låtit bli att betala. Det är en helt annan förhandlingsposition, och åtgärden är att be säljaren fakturera, inte att be om ursäkt. (2) **Kontering mot påstådd ägarposition.** Båda betalda raterna är konterade på **6991 "Övriga externa kostnader, avdragsgilla"**, inte aktiverade som anläggningstillgång. CZP har alltså kostnadsfört förvärvet av source code, varumärken, domäner och publishing-rättigheter som en löpande kostnad, samtidigt som samma 110 000 kr ska stå som återköpsankare i IP-tillgångslistan och samma avtal åberopas för att CZP innehar rättigheterna mot en plattformsinnehavare. Den motsägelsen syns för var och en som läser både boken och avtalet. Stäm av konteringen med redovisningskonsulten så snart ett förvärv ska bära en rättighetsposition utåt.

---

## 2026-08-26 — Fortnox-åtkomst per bolag skiljer sig, och gamla förlagsavtal har hål

**Sök i mailen efter SIE-bilagor INNAN du säger att bokföringen är otillgänglig.** Det var mitt
misstag 2026-08-26: jag rapporterade WLBS som förlorat eftersom Fortnox svarade `NO_YEARS`, men
redovisningskonsulten hade mailat hela SIE-filen till revisorn två år tidigare. Sökningen som
fungerar är `from:<konsult> filename:se` och `(huvudbok OR SIE OR bokslut OR årsredovisning)
filename:se` i Gmail. För konkursade bolag: sök också på konkursförvaltaren, bouppteckningen
innehåller balansräkningen per konkursdagen. Regel: ett bolags bokföring är otillgänglig först
när både Fortnox, mailen till och från redovisningskonsulten och förvaltarkorrespondensen är
genomsökta.

**WLBS och APDS projektmärkte på dimension 6, per titel.** Det gör titelnivå-P&L möjlig rakt ur
SIE:n för bolag som inte längre finns. WLBS-objekt: 16 "Internal - 1993", 53 "INTERNAL - Vessels
Of Decay", 115 "CO-DEV Sir Whoopass", 110 "Robot Lord Rising Ext IP Dev". Kolla alltid
`#OBJEKT 6` innan du säger att en gammal titel inte går att räkna på.

**Fortnox gatekeepar per bolag, inte per session.** Samma inloggade session kan ha full åtkomst i
ett bolag och vara helt blockerad i ett annat. Aurora Punks Development Services AB listar sina
sju räkenskapsår men svarar *"Bekräfta din identitet för att se dina siffror. Logga in med
e-legitimation"* på varje exportförsök, medan CZP och Runatyr fungerar med lösenordssession.
White Lines Black Spaces AB svarar `NO_YEARS`, alltså inga räkenskapsår kvar alls efter konkursen.
Slutsats: innan du lovar en rapport som bygger på ett annat bolags huvudbok, testa åtkomsten
först. `fortnox-sie-pull-all.js --tenant "<namn>"` ger svaret på en minut, och felkoderna
`no_export_button` respektive `NO_YEARS` skiljer BankID-spärr från raderad data.

**Fortnox-sessioner dör snabbt.** Två pull-körningar i rad kräver `fortnox-login2.js` mellan sig.
Kedja alltid login, pull, login, pull i bakgrundsjobbet.

**Läs mallanpassade förlagsavtal efter dinglande korsreferenser.** WLBS-avtalet med Krister
Karlsson (2019-09-20) refererar "Section 12 Developer Funding Repayment", "Initial Advance",
"Additional Advances", "Total Principal Amount" och "Markup" på sju ställen. Ingen av dem finns
i det undertecknade dokumentet. Finansieringssektionen togs bort när mallen anpassades och
korsreferenserna städades aldrig. Effekten är att inget förskott är recoupbart, bara Service
Spend. Metod: extrahera sektionsrubrikerna med `grep -nE "^[A-Z][A-Z ]{4,}$"` på den utvunna
texten och stäm av mot varje "as described in Section N".

**Sök dubbelbokning på beloppen, inte på namnen.** Gäller vidarefakturerade utlägg och
koncerninterna affärer. Se posten 2026-08-25 om A76.

**docx från gdrive MCP kommer som base64.** `gdrive_read_file` returnerar hela zip-filen
base64-kodad efter en rubrikrad. Avkoda, packa upp `word/document.xml`, ersätt `</w:p>` med
radbrytning och strippa taggar. Det ger läsbar avtalstext på ett par sekunder.

**Projekttaggning i CZP började 2026.** Dimension 6 "Projekt" har objekt per titel, till exempel
10 = 1993 Space MAchine, 11 = Vessels of Decay, 19 = Sands of Duat. Före 2026 finns inga taggar,
så äldre år måste sökas på motpartsnamn i verifikationstexten i stället.

## 2026-08-26 — Kontrollera underlagens innehåll, inte filnamnet, innan de går till revisor [AP bokslut 2025, apb-052]

Två träffar i samma revision, båda av samma sort: dokumentet var inte vad etiketten sa.

1. `Revers_DekoDu_Aurora_Punks_AB.pdf` i revisionsmappen var i själva verket reversen till **Loot Spawn AB**
   (50 tkr, 2 %, 2025-11-11). Revisorn upptäckte det, inte vi, och det kostade en runda i tråden. Rätt
   DekoDu-revers låg i en helt annan mapp.
2. Det BankID-signerade dokumentet från Almi som såg ut som ett tomt engagemangsbesked var **beställningen**
   av engagemangsspecifikationen. Rubrik "Beställning av...", Robert som signerare, ifylld på 51 sekunder
   enligt verifikatet. Se [[reference_almi_engagemangsspecifikation]].

**Regel:** öppna varje PDF och läs första sidan innan den går till revisor, bank eller motpart, även när
filnamnet ser rätt ut och särskilt när filen ärvts från en tidigare mapp eller ett tidigare år. `pdftotext
-layout fil.pdf | head -40` räcker för textbaserade PDF:er; är den bildbaserad, öppna PNG:en och titta.
Kostnaden är sekunder, alternativet är att revisorn hittar felet åt dig.

**Följdregel för långivarbesked:** ett dokument som kräver *din* signatur är nästan alltid en beställning
eller ett avtal, inte ett besked. Ett besked signeras av utfärdaren, inte av mottagaren.

## 2026-08-26 — Steams "Life to date" gör historisk royalty räknebar utan huvudbok

När ett bolag är i konkurs och huvudboken är borta finns royaltyhistoriken ändå, hos plattformen.
**Steams månadsrapport i PDF har en sektion "Steam Sales Report: Life to date"** med ackumulerade
enheter, Net Steam Sales och Revenue per produkt sedan kontot startade, plus en Payment
History-tabell per månad. Två sparade månadsrapporter från olika tidpunkter ger periodens intäkt
som en ren differens, utan att någon bokföring behövs. För 1993 gav 2021-10 och 2023-03 hela
Steam-historiken på två tal.

Metod: `gdrive_read_file` returnerar PDF:en base64-kodad efter en rubrikrad. Avkoda, skriv till
fil, kör `pdftotext -layout` och läs sektionen mellan "Life to date" och "Payment History".
Relationen mellan kolumnerna är Revenue = 0,70 × Net Steam Sales, alltså efter Valves 30 procent.

Samma logik gäller andra plattformar: Sonys och Nintendos avräkningar och förläggarens
kvartalsrapporter ligger hos motparten, inte hos det konkursade bolaget. **Innan du säger att en
historisk royaltyfråga inte går att räkna på, fråga var pengarna kom ifrån och hämta det därifrån.**

Vid uppskattning: särskilj alltid i tabellen vad som är bokfört och vad som är uppskattat, ange
grunden per rad, och känslighetstesta slutsatsen i minst tre scenarier. Robert accepterar en
uppskattning men inte en siffra utan ursprung.

## 2026-08-19 — Fortnox via Playwright: bokföring, behörigheter, bankfeed (CZP)

**Fortnox rättigheter läses ur `/api/user/users-v2/me/rights`.** Returnerar en platt lista med
strängar (`bf.bookvoucher`, `kf.bookinvoice`, ...). Detta är den auktoritativa källan. Gissa
aldrig utifrån om modulchippet i Administrera användare är grönt: chippet betyder bara att
användaren har *programmet*, inte att hen får skapa bokföring. Fånga svaret genom att lyssna på
`ctx.on('response')` i Playwright; en `fetch()` inifrån sidan ger `unauthorized`.

De sex rättigheter som styr faktisk bokföring: `bf.bookvoucher`, `bf.booksinvoice`,
`bf.booksinvoicepay`, `bf.authorizebookkeep`, `kf.bookinvoice`, `kf.bookinvoicepay`. Saknas
`bf.bookvoucher` renderar `/bf/voucher/new` noll fält och bankfeeden svarar "Du saknar behörighet
för att skapa och koppla verifikat".

**Leverantörsfakturor bokförs INTE genom att spara fakturan.** Markera raden i `/lf/sinvoicelist`,
klicka **Bokför** i listfoten, bekräfta OK. Fakturan kan ha `authorizeFlowIsDone=true` men
`authorizeBookKeep=false`, alltså attesterad men inte bokföringsattesterad, och då står den kvar
som "Ej bokförd" med asterisk på ver.nr hur mycket man än sparar.

**Bankfeeden är rätt källa för motpart.** SEB:s CSV-export kapar textfältet vid 12 tecken och tar
bara med mottagarkonto ibland, så "KORTFRIST LÅ" och "ÄGARLÅN, KOR" ser anonyma ut i kontoutdraget.
Fortnox `/transactions` visar full motpart, referenssträng och valutabelopp. Där framgick att
4 303,72 var Yaozuo 450 USD och att de två lånen gick till Runatyr respektive Aurora Punks.

**Bankfeedens "Skapa verifikat" förifyller motkontot.** Formuläret ger 1930-raden färdig och lämnar
`#account1` tom. Fyll bara i motkontot och klicka Bokför. Automatbokföring uteblir när flera
regelverk matchar samma transaktion (CZP hade både "ÄGAR" och "ÄGARLÅN UT").

**Kundfakturor bokförs vid utskrift eller utskick, men det kan gå sönder.** På CZP returnerar
`POST /api/kf/invoice/sendv2` med `sendType: "print"` 201 utan att skapa verifikat, och
`"dontSend"` ger 500. Kundfakturalistan saknar Bokför-knapp. Fältet `bookKeep` speglar status
(1 = bokförd), det är inte en inställning man kan slå på. Olöst per 2026-08-19.

**Nyttiga rutter:** `/lf/sinvoicelist`, `/lf/supplierinvoice/<nr>`, `/kf/invoicelist?filterby=unposted`,
`/kf/invoice/<nr>`, `/transactions`, `/transactions/history`, `/common/accountlist`,
`/common/account/new`, `/common/account/<nr>`, `/bf/voucher/new`, `/common/settings/financialyear`.
Hash-rutter som `#/common/account/new` tappas vid direkt goto; klicka ankaret via JS i stället.
Verktyget ligger i `assistant/fx.js` (goto/click/sel/js/fill/btn/key/links/wait, FX_NET för
nätloggning). Sessionen dör med INVALID_SESSION efter en stunds körande; kör om `fortnox-login2.js`.

### 2026-08-25 — En fallerad plattformsbetalning till ett konkursbolag är aldrig ett payee-fel [project: apb / apb-042, apb-013]
Nintendo of Europe rapporterade `RSN REGULATORY REASON` på PID 291215956 (Aurora Punks Development Services AB, konkurs 2025-12-12). Ticketen hette "fix payee settings" och det var fel diagnos i två led.
- **Bankledet:** `RSN REGULATORY REASON` är en compliance-avvisning på mottagarsidan, inte ett formatfel i IBAN. Mot ett bolag i konkurs är det förväntat beteende. Ingen redigering av payee-fältet kan få betalningen att gå igenom, så varje timme lagd på fältet är bortkastad.
- **Avtalsledet, det farligare:** att peka payee mot förvärvarens bankkonto medan publisher-avtalet fortfarande står på konkursbolaget innebär att förvärvaren tar emot pengar under ett avtal den inte är part i. Det ger konkursförvaltaren en rak invändning mot medlen. Betalningsvägen måste följa ett avtal den mottagande entiteten faktiskt håller.
**Generell regel:** när en plattform (Nintendo, Sony, Valve, MS) rapporterar en fallerad utbetalning och kontot står på ett bolag i konkurs, är payee-ärendet alltid *nedströms* entitetsöverföringen. Sortera om ticketen, gör den till ett barn, och rör inte payee-fältet förrän licensee-bytet är klart.
**Andra fyndet:** signera aldrig mot en licensor i ett ärende med fel koncernbolag. Roberts svar 2026-08-11 var signerat "Aurora Punks AB", ett tredje bolag som varken äger kontot (APDS) eller rättigheterna (CZP). Tre entiteter i en tråd är hur ett licensing-team tappar bort ärendet. Namnge alla tre explicit och säg vilken som är vilken.
**Tags:** Nintendo, NDP, konkurs, entity-transfer, payee, APDS, CZP, plattformsutbetalning, RSN

### 2026-08-25 — Nintendo har tre separata processer, och licensee-avtalet grindar verktygen [project: apb]
Steam och PlayStation lärde oss att skilja på processer, Nintendo har samma delning men med en konsekvens de andra saknar:
- **(a) licensee/publisher-avtalet** grindar rätten att ladda ned SDK och Nintendo Dev Interface överhuvudtaget,
- **(b) devkit-registrering** knyter hårdvaruserienummer till licensee,
- **(c) titelägande + payee**.
Att (a) grindar verktygen betyder att entitetsfrågan inte är administrativ städning, den är en teknisk blockerare för cert och release. Gränsen som går att dra i praktiken: **testning** på ett konkursbolags access förbrukar ingen submission-slot och skapar ingen ny förpliktelse, alltså acceptabelt kortsiktigt. **Submission till Lotcheck** gör bådadera, alltså inte acceptabelt oavsett vems inlogg som används. Dra linjen där, inte tidigare, annars stoppar man testning i onödan.
**Tags:** Nintendo, licensee, SDK, NDI, Lotcheck, cert, devkit, entity-transfer

## 2026-08-25 — Fortnox leverantörsfakturor: bokföring, projekttagg, dubbelbokningsfälla (CZP)

**Bokför-knappen på en leverantörsfaktura är inte en button-roll.** Den ligger som
`span.js-supplierinvoice-split-action-label` i sidfoten, ett split-action-element. Tolv
Bokför-kandidater finns i DOM:en och elva är osynliga (`offsetParent === null`) eftersom de hör
till andra moduler i samma ram. Filtrera alltid på synlighet innan du klickar. Verktyget är
`assistant/fx-levfaktura.js`.

**Konteringsraderna är delvis inputs, delvis genererade.** Raderna 2440 och 2641 skapas ur
headerfälten `form-supplierinvoice-total` och `form-supplierinvoice-vat`, de går inte att skriva
direkt. Kostnadsraderna är fria inputs utan id eller name, bara `class="text"`, så de måste
adresseras på index bland de **synliga** inputarna. Projektfältet
`#form-supplierinvoice-projectField` är en autocomplete som tar koden som text, "19" räcker,
och löser upp sig till "19 - Sands of Duat".

**Fortnox automatik konterar levfakturor rätt men tappar projekttaggen.** Fyra av fyra fakturor
låg korrekt konterade mot samma konton som föregående faktura från samma leverantör, men den nya
Lost Hive-fakturan saknade objekt 6 "19" som föregångaren hade. Kontrollera alltid projekttaggen
mot förra verifikatet från leverantören innan bokföring, annars läcker projektredovisningen.

**Dubbelbokningsfällan vid vidarefakturerade utlägg.** Innan en levfaktura som avser utlägg
bokförs: sök i SIE:n efter ett manuellt verifikat som redan tagit samma kostnader. I CZP hade
A76 "Utlägg Robert Q1 2026" bokfört exakt samma poster mot 2820 tre månader innan Runatyr
fakturerade dem. Fem radsummor matchade till öret. Rätt hantering är att bokföra fakturan som ren
motpartsväxling, 2440 mot 2820, utan moms- eller kostnadsrad, eftersom kostnaden och momsen redan
ligger i det första verifikatet. Sök på de karaktäristiska beloppen, inte på leverantörsnamnet,
eftersom det manuella verifikatet heter något helt annat.

**Fortnox utbetalningsvy har egna betalsätt för koncerninterna konton.** CZP har "Runtyr (1713)"
vid sidan av Bankgiro (1930) och Plusgiro (1920). En koncernintern faktura kan alltså slutbetalas
mot fordringskontot direkt i Fortnox, ingen manuell kvittningsverifikation behövs.

**Lobbyns kontosaldon har tidsstämpel, skärmbilder har inte.** Läs alltid saldot ur lobbyn med
"Hämtades" -raden i stället för att lita på ett tal från en tidigare skärmbild. Jag citerade
806 016 från en gammal bild när kontot i verkligheten hade 387 895,10.

## 2026-08-25 — När revisorn säger sig sakna underlag: kolla behörigheten, inte tråden [AP bokslut 2025, apb-052]

Christine (Parameter Revision) efterlyste underlag i tre omgångar och bad till slut om att få "driven"
delad med sig. Mailtråden gav inget svar på om hon faktiskt hade åtkomst. Drive-API:t gjorde det på en
minut: hon låg redan som **reader** på `Aurora Punks Board/_deliverables_working`
(`1TmSqmdwPY115LXwlFHNDyCniQkEzxGCh`), med allt hon bett om i mappen. Luckan var kommunikativ, inte
teknisk: mapplänken hade aldrig mailats till henne, så delningen fanns bara som en automatisk
Google-notis i hennes inkorg.

**Regel:** vid "jag har inte fått X", verifiera i tre steg innan du skickar om något. 1) Ligger personen
på mappen (Drive-API, se [[devops_learnings]] 2026-08-25 för anropen)? 2) Finns filen i mappen? 3) Har
länken någonsin lämnat vår sida i ett mail (`gmail_search` på mapp-ID:t)? Steg 3 är den som brukar fallera.

**Gotcha värd att minnas:** Amer Alsaleks Drive-åtkomst sitter på **`amersalek@gmail.com`**, inte på
`amer@book-it.se` som han mailar från. En sökning på arbetsadressen får det att se ut som att han saknar
åtkomst till AP-materialet. Kolla båda adresserna innan du drar slutsatsen att en delning saknas.

Kanonisk plats för mapp-ID + behörighetsläge: [[reference_drive_folders]]. Engagemangsbeskedets väg:
[[reference_seb_engagemangsbesked]].

### 2026-08-25 — Läs SIE-filen i stället för att driva Fortnox-webben, och matcha Levfakt mot Levbet [project: apb / apb-051]
Frågan var om alla Bright Gambit-fakturor var betalda. Snabbaste vägen var **inte** browser-automation: `uploads/CZP_2026_SIE4_*.se` dras redan regelbundet, så en färsk SIE fanns på disk. SIE är CP437-kodad, `iconv -f CP437` först.
**Metoden som ger svaret på en rad:** varje leverantörsfaktura bokförs som `#VER ... "Levfakt <leverantör> (<fakturanr>)"` och varje betalning som `#VER ... "Levbet <leverantör> (<fakturanr>)"`. En faktura utan matchande Levbet är obetald. Räkna par per fakturanummer i stället för att titta på saldon, då syns exakt vilken post som saknas.
**Fyndet:** fem av sex BG-fakturor betalda, faktura 906 om 110 000 + moms bokförd 2026-08-18 obetald. Och viktigare, den var på **hela** avtalsbeloppet trots att 72 000 redan betalats via två tidigare rater, alltså en trolig dubbeldebitering på 72 000 netto. Ingen kreditfaktura fanns.
**Generell lärdom:** när någon säger "allt är betalt", verifiera per faktura och jämför summan mot avtalets totalbelopp, inte bara mot att betalningar existerar. Det var beloppsjämförelsen mot avtalet som avslöjade problemet, inte betalningsmatchningen.
**Tags:** Fortnox, SIE, leverantörsreskontra, Levfakt, Levbet, dubbeldebitering, Bright Gambit, verifieringsmetod

## 2026-08-21 — Två likanamnade OpenSign-watchers, och arkiveringsjobbet är inte ticket-medvetet [apb / apb-047]

**Project:** Aurora Punks (apb-047, augustireversen) | **Category:** tooling, ticket-hygien, självrättelse

**Learning (`opensign-watch.js` ≠ `opensign-watcher.js` — namnen skiljer sig med en bokstav, jobben är helt olika):** Repot kör **två** separata OpenSign-bevakare med nästan identiska namn och nästan identiska loggfiler: **`opensign-watch.js`** (körs via **crontab, en gång/dygn kl 08:15**, egen registry `assistant/opensign-watch.json`, loggar till `logs/opensign-watch.log`) gör **slutförande + arkivering** — laddar ner signerad PDF, mailar Robert, filar till rätt Drive-mapp. **`opensign-watcher.js`** (körs via **systemd-timer var ~61:e minut**, egen state `assistant/state/opensign-watcher.json`, loggar till `logs/opensign-watcher.log`) är en **nudge-bot** som bara påminner obesvarade signatärer, med ett nudge-tak. Jag såg först att `opensign-watch.log` inte hade en enda ny rad sedan gårdagens 08:15 och drog slutsatsen att arkiveringsjobbet kanske hade slutat köra — fel spår. Kontrollera **crontab -l** för schemat (dagligt, inte kontinuerligt) innan du tolkar en tyst logg som ett trasigt jobb, och håll aldrig de två skripten/loggarna isär av minnet, kolla filnamnet tecken för tecken.

**Learning (arkiveringsjobbet uppdaterar aldrig followup-ticketen — den kan bli "klar i tysthet" i upp till ett dygn):** `opensign-watch.js` slutförde och arkiverade augustireversen redan **2026-08-20 08:15** (några timmar efter att föregående sessions 04:20-check såg "KM väntar"), men skrev bara till sin egen registry + mailade Robert. **Ingen process synkade followup-ticketens `status`**, så apb-047 låg kvar `in_progress` ända till nästa dags 4am-sweep upptäckte det av en slump. **Regel: när ett ärende väntar på en extern automatiserad vakt (signering, betalning, godkännande), lita inte på ticketstatusen som sanning om vaktens jobb — slå alltid upp vaktens EGEN registry/state-fil (här `assistant/opensign-watch.json`, `_state`/`completedAt`-fälten) live, den kan redan ha gjort klart utan att någon flaggat det uppåt.** Samma disciplin som redan gäller Steamworks-grindar (se 2026-08-04-noten) — poll källan, aldrig ticketens senaste snapshot.

**Tags:** apb-047, opensign-watch-vs-watcher, cron-vs-systemd-timer, arkivering-ej-ticket-medveten, tyst-klar, poll-inte-snapshot

## 2026-08-20 — En "ägarlån"-etikett räcker inte som sökväg till rätt minnesfil; och `opensign.js status` är den billiga sanningskällan för signeringsläge [apb / apb-047]

**Project:** Aurora Punks (apb-047, augustireversen CZP→AP) | **Category:** memory-hygiene, tooling, self-correction

**Learning (namnlikhet ≠ samma facilitet — verifiera beloppet, inte bara ordet "ägarlån"):** DevOps routade ärendet med förslaget att skriva in villkoren i `project_ap_ek_2025_almi_agarlan`, "den handlar om AP:s eget kapital och ägarlån". Rimligt på ytan, men den filen dokumenterar en helt annan facilitet — ett ~1,25M-lån som ersatte Almi-lånet i KBR-uppgörelsen. De två kortfristiga 50 000-reverserna (juli + augusti 2026) är separata, mindre lån med eget syfte (löpande utgifter/revisor). Att skriva in dem i Almi-filen hade skapat tre liknande belopp i samma dokument utan tydlig avgränsning — precis den sortens sammanblandning en revisor snubblar på vid nästa bokslut. **Regel: innan du skriver ett kanoniskt finansiellt faktum i en föreslagen minnesfil, läs filen och kontrollera att ämnet faktiskt är samma facilitet/avtal, inte bara samma etikett ("ägarlån", "revers", "lån"). Skapa hellre en ny sektion i den mest topikmässigt korrekta filen (här: `project_aurora_punks.md`, AP-governance) och lägg en tvärreferens åt båda hållen.**

**Learning (`node assistant/opensign.js status <documentId>` är en läsning, inte en skrivning — använd den fritt för att verifiera signeringsläge utan att vänta på mailnotiser):** Ärendebeskrivningen citerade ett signeringsläge "verifierat 2026-08-19" av DevOps. En live-koll (`opensign.js status AfWbAMb1nY`) visade att läget redan hunnit ändras — Mattias Wiking hade signerat sedan dess. **Regel: ett signeringsläge i en ticketbeskrivning är en färskvara redan efter ett dygn; kör alltid en live statuskontroll innan du rapporterar eller agerar på det, särskilt i en obevakad körning där ingen har sett mailnotiserna.** Detta är samma disciplin som redan gäller platsstatus-kontroller (Steamworks-grindar, se 2026-08-04-noten) — poll, invänta aldrig ett mail.

## 2026-08-17 — Ankra på currentDate, aldrig på daily_briefing. Och moms följer fakturadatum, inte betaldatum [run / czp]

**Project:** Runatyr Q2-moms + CZP | **Category:** datum, moms, underlagsjakt, självrättelse

**Learning (det farligaste felet i hela sessionen): jag läste `daily_briefing.md` och trodde att dess datum var idag.** Briefingen låg kvar från den 13 augusti medan sessionen faktiskt kördes den 17:e. Följden blev att jag sa till Robert att Runatyrs Q2-moms förföll "på måndag den 17:e, inte idag" när han själv misstänkte att det var samma dag. Han hade rätt. Samma fel gav fel datum för CZP:s skattekontobetalning på 63 841 kr. **`daily_briefing.md` är en genererad fil som ligger kvar tills nästa körning, och filens rubrikdatum säger ingenting om vilken dag det är nu.** Sessionens `currentDate` är den enda auktoritativa källan, exakt som [[feedback_anchor_on_currentdate]] redan säger. Sekundär kontroll: `date` i skalet, eller mtime på färska filer. Kolla det **innan** du räknar en enda deadline, inte efter.

**Learning (momsdeklaration ur bankutdrag missar systematiskt periodens fakturor):** Runatyrs Q2 byggdes ur kontoutdraget eftersom Bokio har noll verifikat för 2026. Bankflödet för april till juni innehöll ingen Bahnhof-post alls, men två Bahnhof-fakturor hade **förfallodag** i kvartalet (1000508427 på 5 038 kr, förfall 30 maj; 1000514672 på 5 984 kr, förfall 28 juni) och betalades först 7 juli. Under faktureringsmetoden hör de till Q2. En ren bankrekonstruktion hade tappat 1 007,60 kr i avdrag på den ena, och det är 75 % av hela deklarationen. **Regel: när du rekonstruerar moms ur ett kontoutdrag, sök alltid igenom mailen efter fakturor och betalningspåminnelser med förfallodag i perioden, och kolla nästa periods betalningar för poster som hör bakåt.** Bestäm dessutom metoden först, faktureringsmetod eller kontantmetod, för den avgör vilken period varje post hamnar i. Ledtråd om metoden: se hur föregående period redovisades.

**Learning (påminnelsemailen bär beloppet när fakturan saknas):** Bahnhofs betalningspåminnelser anger fakturanummer, OCR, förfallodag **och beloppet inkl moms** i klartext. När fakturan inte går att hitta är påminnelsen ett användbart andrahandsunderlag för att räkna momsen. Leverantörens supportsvar bar dessutom exakt vilken period fakturan avsåg, vilket var det som gjorde posten försvarbar att ta med.

**Learning (ett abonnemang kan stå på ett annat bolag än det ditt ärendesystem påstår):** followups `czp-018` och `czp-020` var skapade som CZP-ärenden om obetalda Bahnhof-fakturor. Abonnemanget är tecknat av **Runatyr AB**, kundnummer B123056. Ingen hade kollat avtalsparten, bara att en faktura var obetald. **Läs alltid fakturamottagaren i mailet innan du bokför en kostnad eller drar dess moms i ett bolag.** Det avgjorde här vilket bolag som fick göra avdraget.

**Tags:** currentdate, stale-daily-briefing, missad-deadline, moms, faktureringsmetod, kontantmetod, fakturadatum-vs-betaldatum, bankrekonstruktion, bahnhof, runatyr, kvartalsmoms, 17-augustiregeln

## 2026-08-16 — Verifiera utbetalningen INNAN körningen, inte efter; och en testkörning som defaultar till skarpt läge larmar på riktigt [czp / czp-023]

**Project:** CZP (czp-023, första Steam-utbetalningen efter entitetsbytet) | **Category:** platform-ops, steam, watcher-design, självrättelse

**Learning (den viktigaste: ett "verifiera att X landar rätt"-ärende ska inte vänta på X):** Ärendet var formulerat som en observation — vänta till 26–28 aug och läs hälsningsraden i betalningsmailet. Men allt som *avgör* vart pengarna går går att läsa i förväg, och tio dagar innan körningen finns det tid att rätta. Läs `/pub/view/<pid>` och bekräfta **payee-namn, maskerad IBAN, SWIFT, valuta, om bankändringen fortfarande ligger "pending approval by a Valve administrator", utbetalningströskeln och källskattesatsen** innan körningen. Alla sju var rätt på CZP 418393, vilket förvandlade ärendet från "hoppas det blir rätt" till "konfigurationen är bevisad, kvar är bara att se pengarna". **Regel: när ett ärende säger "verifiera att pengarna landar rätt", verifiera först allt som styr destinationen — observationen är sista steget, inte det enda.**

**Learning (kolla att utbetalningen ens kommer att ske — tröskeln tystar annars hela beviset):** Valve betalar inte under **$100 USD** och APDS fick faktiskt "under tröskeln"-mail i feb, apr och aug 2025. Ett sådant mail bevisar *ingenting* om payee. Kontrollera periodens intäkt före körningen: CZP juli 2026 = **$5 197 / 4 510 units**, alltså långt över golvet. Dessutom: **utbetalningströskeln är en inställning per konto** ($50–$1 000), så även med hög intäkt kan en högt satt tröskel hålla pengarna. Läs det valda värdet, inte optionslistan.

**Learning (bekräfta att backdateringen flyttade INTÄKTEN, inte bara apparna):** att apparna ligger på rätt partner bevisar inte att intäkten omfördelades. Enkel korskontroll: **CZP:s lifetime revenue $5 256 mot juli allena $5 197** — kontot bär i praktiken bara den överlåtna perioden, vilket bevisar att Valve attribuerade juli till CZP enligt ikraftträdandedatumet 1 juli. Jämför alltid lifetime mot periodens siffra efter en backdaterad överlåtelse.

**Learning (`s.name || s.id` i ett recon-skript tillverkar ett falskt namn som nästa selektor tyst missar):** min första recon listade selects som `{name: s.name || s.id}` och rapporterade `payment_hold_threshold` som ett *name*. Elementet har i själva verket **`id="payment_hold_threshold"` och inget name-attribut alls**, så `select[name=payment_hold_threshold]` returnerade null — och min drift-kontroll var skriven som `if (cfg.threshold && cfg.threshold !== EXPECTED)`, dvs. **null passerade som godkänt**. Två regler: (1) i recon, rapportera `nameAttr` och `id` som separata fält, aldrig hopslagna med `||`; (2) i varje sentinel ska **oläsbart fält larma lika högt som felaktigt fält** — `!cfg.x` ska ge "kunde inte läsa x", aldrig tyst pass.

**Learning (SJÄLVRÄTTELSE — en watcher som defaultar till skarpt läge larmar skarpt under test):** jag regressionstestade hälsningsrads-parsern genom att spela upp det kända APDS-mailet från 28 juli. Skriptet ärvde syskonwatcherns konvention `mode = argv.find(...) || '--once'`, och `node -e` lämnar `process.argv` med **ett enda element**, så min pushade `--smoke`-flagga hamnade på index 1 och `slice(2)` såg den aldrig. Resultat: en skarp **🚨 "utbetalningen gick till konkursboet"** till Discord och en falsk larmrad i ärendefilen, mitt i natten. Städat: rad borttagen, state återställd, rättelse postad i kanalen. **Fixen är strukturell, inte disciplin:** (1) sidoeffekter kräver ett **explicit** `--once`, default är dry-run; (2) om `STEAM_PAYOUT_MAIL_CUTOFF` är satt (= vi spelar upp historik) tvingas dry-run oavsett flaggor. **Regel för alla watchers: den farliga vägen ska kräva ett uttryckligt argument, och testläge ska vara omöjligt att förväxla med skarpt läge.**

**Learning (mailankomsten bevisar inget — och båda entiteterna kan få mail samma månad):** APDS och CZP notifierar **samma adress** (finance@aurorapunks.com), så bara hälsningsraden skiljer dem. Viktigare: konkursboet kan legitimt få en **eftersläpande avräkning** för intäkt före 1 juli samtidigt som CZP får julibetalningen. En watcher som läser *senaste* mailet gör då en helt korrekt utgång till falsklarm. Utvärdera **hela mängden**: bara "APDS betald OCH inget till CZP" är ett verkligt fel; båda betalda är väntat och ska flaggas som avstämningspost mot Carler, inte som larm.

**Learning (APDS-sidan går aldrig att kontrollera obevakat):** APDS-kontot (naturenistockholm_2) använder **mobilautentiseraren**, CZP-kontot (aurorapunks_user) får **Steam Guard via mail** och kan självläka i cron via `steam-guard-code.js`. Alla obevakade kontroller måste därför byggas mot CZP-sidan; "visar konkursboet också juliintäkt?" är per definition en Robert-fråga.

**Tags:** czp-023, apb-026, steam, steamworks, 418393, 301411, payout, payment_hold_threshold, id-inte-name, oläsbart-är-inte-godkänt, watcher-default-dry-run, falsklarm, självrättelse, hälsningsrad, trailing-settlement, carler, mobilautentiserare

## 2026-08-16 — Engagemangsbesked hos SEB: leverans, beställning och varför revisorn ändå inte fått det (aurora-punks / apb)

**SEB levererar engagemangsbeskedet som "Audit Statement" från avsändaren `SEBAuditStatements@seb.se`**, med ämnesraden `SEB Audit Statement for <BOLAG> per <datum> | Case ID <nnnnnnnn>`. Bilagan är en **Azure Information Protection-krypterad PDF** (`<CaseID>_Email.pdf`) som öppnas i Edge eller Azure-appen. Sök alltså inte bara på "engagemangsbesked" i mailen, det ordet förekommer inte i SEB:s leveransmail. Det var precis den fällan som gjorde att AP:s besked per 2025-12-31 (Case ID 99765421, levererat 2026-06-03) såg ut att saknas.

**Beställning:** i **Business Arena** (SEB:s företagsinternetbank), **200 kr per besked**. Vid beställningen väljs mottagare: en själv, revisorn direkt, eller båda, per post eller mail. Bekräftat av SEB:s Anna Eklund redan 2024-06-10 ("Detta beställer du själv via internetbanken. Här kan du även välja att skicka det direkt till revisorn") och av seb.se 2026.

**Fällan som kostade AP två månader:** beskedet beställdes utan att revisorn angavs som mottagare, så det gick bara till `robert@aurorapunks.com` och blev liggande krypterat i inkorgen medan Christine tre gånger efterlyste det. **Ange alltid revisorn som mottagare direkt i beställningen**, och kryptering gör dessutom vidarebefordran opålitlig eftersom rättigheterna kan vara låsta till beställarens adress.

**Försök inte öppna den krypterade filen, beställ om istället.** Inspektion av AP:s fil 2026-08-16: omslaget är en tom platshållarsida, det riktiga dokumentet (3 sidor) ligger som inbäddad krypterad fil `MicrosoftIRMServices Protected PDF.pdf`. Publiceringslicensen i klartext visar utfärdare "SEB - SE", tenant `9a8ff9e3-0e35-4620-a724-e9834dc50b51`, licensserver `cdeaa490-98e6-47e9-a6a4-8eb572e86a8f.rms.eu.aadrm.com`, ägare `RD1000069@seb.se`. **Innehållsnyckeln finns inte i filen** och rättighetslistan ligger själv krypterad i `Encrypted-Rights-Data`, så det går inte ens att avgöra vem som får öppna den. Varje läsare måste autentisera mot SEB:s RMS-tenant och hämta en use license. Microsofts läsare finns bara för Windows, Mac, iOS och Android, **inte Linux**, så VPS:en kan aldrig lösa det. Vägarna för en mottagare är Edge 83+ inloggad med arbetskonto, eller Microsofts gratis "RMS for individuals" om adressen saknar Entra ID (aurorapunks.com ligger på Google Workspace). Roberts beslut 2026-08-16: strunta i filen, beställ om i Business Arena med revisorn som mottagare. **Det är den generella regeln, filen är en återvändsgränd, beställningen är lösningen.**

**Befordrat 2026-08-16:** den generella SEB-fakta (beställningsväg, pris, leveransformat, varför filen inte går att öppna) ligger nu som kanoniskt referensminne i [[reference_seb_engagemangsbesked]]. Läs den först, den här posten behåller AP-specifika detaljer.

**Tags:** seb, engagemangsbesked, audit-statement, business-arena, revision, aurora-punks, apb, parameter-revision

## 2026-08-16 — Revisorns "dokumentation av ägarinnehav som styrker konto 1350" betyder INTE bolagets egen aktiebok (aurora-punks / apb)

**Missförståndet:** Christine Lef bad om "dokumentation av ägarinnehav (aktiebok e.d.) samt eventuell värdering, som styrker innehaven på konto 1350". Robert skickade AP:s **egen** aktiebok/ägarförteckning. Frågan kvarstod, och rundgången kostade en månad.

**Rätt läsning:** konto **1350 = Andelar och värdepapper i andra företag**. Revisorn vill se underlag för vad *bolaget äger i andra bolag*, alltså aktieägaravtal/SHA, teckningsbevis och värderingar per innehav, inte vem som äger bolaget. Samma sak gäller 1310/1315 för dotterbolag. Skicka aktieboken bara när frågan gäller ägarbilden eller kontrollen av bolaget självt.

**AP:s 1350-liggare** finns som Sheet `10mAz2jYAYBYh1DhfbYDivSpNP4hZMHTNjtM3FL_jbfk` ("Aurora Punks AB - Aktieinnehav"), med årsvisa saldon 2020 till 2025 och SHA-länk per rad: Upstream Arcade (15 %), LootLocker (avyttrat 2023), Runatyr, Red Marmoset (15 %), Eddaheim-konvertibler (löpte ut), Northify, No89 (sålt 2025-04-24). **Obs avstämningsglapp:** saldo 2024-12-31 2 972 945 kr minus enda 2025-rörelsen −999 267 kr ger 1 973 678 kr, men liggaren anger 0 kr per 2025-12-31. Sannolikt omklassning till 1310/1315 som aldrig skrevs in. Stäm av med redovisningskonsulten innan liggaren går till revisorn.

**AP:s bokslutsmapp** är `Aurora Punks Board / _deliverables_working` (`1TmSqmdwPY115LXwlFHNDyCniQkEzxGCh`) i den delade enheten. Modellen som används: redovisningskonsult och styrelseordförande får **writer**, revisorn får **reader**. Kontrollera alltid att filer som påstås ligga där faktiskt gör det. DekoDu-reversen låg kvar i "Downloads" i två månader efter att mailet sagt att den fanns i mappen.

**Befordrat 2026-08-16:** 1350-liggaren är nu kanoniskt bokförd i [[project_aurora_punks]] under cap table, inklusive avstämningsglappet. Den här posten behåller resonemanget om varför aktieboken är fel svar.

**Tags:** konto-1350, aktieinnehav, aktiebok, revision, underlag, aurora-punks, apb, drive-delning, parameter-revision

## 2026-08-13 — En SIE-fil bevisar bara vad som fanns vid #GEN, och Fortnox "felaktigt lösenord" maskeras som MFA [czp / czp-000]

**Project:** CZP Finances (byråövergång Sifferrådet) | **Category:** sie, fortnox, tooling, bevisföring

**Learning (den dyra: registreringsdatum ≠ bokföringsdatum, och SIE:n bär bara det som registrerats före exporten):** Jag rapporterade att IndieARK-rapporterna 26.04-26.06 var ofakturerade, med SIE-filen som grund. Robert invände direkt: hur kan du se det utan att logga in? Han hade rätt. **Faktura 93 bokfördes 2026-06-10 men registrerades 2026-06-24**, alltså två dagar efter att min lokala SIE drogs den 22:a. Verifikatraden `#VER B 43 20260610 "..." 20260624` bär båda datumen: det första är bokföringsdatum, det sista är registreringsdatum. En SIE-export innehåller bara verifikat som var **registrerade** vid exporttillfället, oavsett hur långt bak bokföringsdatumen går. **Regel: läs `#GEN` FÖRST och uttala dig aldrig om tiden efter det datumet.** Formuleringen ska vara "ej fakturerad per <GEN-datum>", aldrig "ofakturerad". Samma fälla gäller varje "saknas i bokföringen"-slutsats, särskilt mot en byrå som registrerar i klump var tredje vecka.

**Learning (leta efter en färskare SIE på Drive innan du bråkar med Fortnox):** min lokala fil var från 22 juni, men `rag_search` på en helt annan fråga råkade returnera `gdrive:1XtddyFSx16a9v_fnhXQqmfwJc2Ql5wID` `CZP_SIE4_2026.se`, **genererad 21 juli**, med en månad extra data. Den låg inte i `czp-finances/` och inte i `assistant/uploads/`. Sök Drive på filnamn OCH kör en rag_search innan du drar slutsatsen att den senaste filen du har lokalt är den senaste som finns.

**Learning (Fortnox-login: "Felaktigt lösenord" rapporteras som MFA_REQUIRED och du väntar i evighet på ett SMS som aldrig kommer):** `fortnox-login2.js` avgör MFA-läget enbart på att URL:en fortfarande är `/fortnoxid-ui-login/password` efter submit. Vid fel lösenord ligger man kvar på exakt samma URL, så skriptet loggade `MFA_REQUIRED - waiting for SMS code` och pollade `/tmp/fortnox-mfa-code.txt` i tjugo minuter medan sidan i själva verket sa **"Felaktigt lösenord. Inloggningen misslyckades."** Screenshotten `/tmp/fx2-mfa.png` avslöjade det på en sekund. **Regel: när skriptet säger MFA_REQUIRED, öppna screenshotten innan du ber Robert om en kod.** Och kör **max ett inloggningsförsök** med okänt lösenord, Fortnox låser kontot vid upprepade fel.

**Learning (rotorsaken, och den gäller varje hemlighet i `.env`): värdet låg inom enkla citattecken och parsern skickade med dem.** Lösenordet innehåller `#`, så det hade citerats i filen: `FORTNOX_PASSWORD='...#...'`. Env-parsern i fortnox-skripten var `l.match(/^([A-Z0-9_]+)=(.*)$/)` följt av `env[m[1]] = m[2]`, vilket tar allt efter likhetstecknet **inklusive citattecknen**. Fortnox fick alltså apostroferna med i lösenordet. Robert var säker på att lösenordet fungerade, och han hade rätt. **Diagnosmetod som inte exponerar hemligheten:** läs raden som bytes och skriv ut längd, `endswith(b'\r')`, inledande/avslutande blanksteg, om den börjar med `'` eller `"`, och om den innehåller `#`. Det räckte för att se felet utan att skriva ut lösenordet. **Fixat 2026-08-13** i `fortnox-login2.js` och `fortnox-sie-export.js`: `.replace(/\r$/,'').replace(/^(['"])([\s\S]*)\1$/,'$2')`. Samma bugg finns sannolikt i andra hemmasnickrade `.env`-parsers i repot, kolla dem innan du felsöker en till "fel lösenord".

**Learning (IndieARK/Yaozuo faktureras av CZP, inte av APDS, trots att rapporten är ställd till APDS):** Yaozuo Games rapporterar Strike Force Heroes-andelen (10 % av net sales på konsol) till "Aurora Punks Development Services AB", som är i konkurs. Faktureringen har hela 2026 gått via **CZP**: fakturorna 51, 52, 63, 73, 81 och 93, alla betalda. Samma mönster som Vessels of Decay, där Headup-avtalet är tecknat med APDS men faktureringen sker via CZP. **Låt inte adressaten på en royaltyrapport avgöra vilket bolag som fakturerar, kolla kundreskontran.** Kontering: **3305** försäljning tjänster utanför EU, dimension objekt 6 = "7" Strikeforce Heroes, ingen moms, **ruta 40**. OBS att fakturorna 51-73 felaktigt bokfördes på **3105** (varor utanför EU, ruta 36) innan bytet skedde vid faktura 81. Valutakursdifferens vid betalning på 7960. Fortnox fakturaservice tar bara SEK och EUR, så USD-fakturor ställs ut utan fakturaservice.

**Tags:** sie-gen-datum, registreringsdatum-vs-bokföringsdatum, czp, fortnox-login2, falskt-MFA_REQUIRED, lockout-risk, indieark, yaozuo, strike-force-heroes, 3305-vs-3105, ruta-40, apds-rapport-czp-faktura

## 2026-08-06 — Ett D-U-N-S-nummer går ofta att fastställa ur mailarkivet, och koncerner med namnhistorik har FLERA [apb / apb-043]

**Project:** Aurora Punks (apb-043) | **Category:** platform-compliance, källsökning, d&b

**Learning (sök beställningsbekräftelsen innan du loggar in någonstans):** Frågan "vilket D-U-N-S ligger på Apple-teamet?" såg ut att kräva portalinloggning (som Apple inte ens visar — Membership details listar inget D-U-N-S). Svaret låg i stället i mailarkivet: D&B/Bisnodes **beställningsbekräftelse** ("DUNS bekräftelse", avsändare `kredit.se@bisnode.com`) anger orgnr + tilldelat nummer svart på vitt, och tidsstämpeln mot Apples enrollment-mail samma dag bevisar vilket nummer kontot sattes upp med. Sök `DUNS OR "D-U-N-S"` i båda brevlådorna före varje portal- eller supportväg.

**Learning (fällan: en koncern med namnbyten/konkurser har flera D-U-N-S, och de blandas ihop i samma tråd):** AP AB (559256-9718) = **353420335**; WLBS (559217-4196, i konkurs) = **350685539**. Henrik svarade med WLBS:s nummer på Roberts fråga om AP AB:s, i samma tråd, samma förmiddag. Den som skummar tråden tar fel nummer och uppdaterar konkursboets post. **Verifiera alltid orgnumret i själva bekräftelsen**, inte i rådgivarens svar.

**Learning (Apples D&B-väg för adressändringar):** för Organization-konton är D&B-posten det Apple litar på; adressändring körs via `support.dnb.com/?CUST=APPLEDEV` (~2 arbetsdagars ledtid innan Apple ser den), därefter svar på supportärendet så Apple verifierar mot D&B. En D&B-submission är en extern registerändring = MUST-ASK i obevakad körning; förbered fälttabellen och stanna där.

**Tags:** apb-043, duns, 353420335, 350685539, dnb, appledev, bisnode-bekräftelse, wlbs-fälla, scalfr6l25

## 2026-08-04 — Steams app-transfer end-to-end: fyra steg, fyra garantier, och backdatering GÅR [apb / apb-026]

**Project:** Aurora Punks (apb-026) | **Category:** steam, platform-ops, playwright, juridik

**Learning (hela kedjan, körd skarpt):** överföringen är **fyra separata steg**, inte ett: (1) avsändaren initierar i Transfer Tool `/pub/apptransfers/<partner>`, (2) mottagaren accepterar via en hemlig länk, (3) **avsändaren bekräftar** i ett andra steg som är lätt att missa, (4) Valve slutgranskar. Efter steg 1 står status *Awaiting Confirmation From Transferee*, efter steg 2 *Awaiting Confirmation From Transferer*, efter steg 3 *Pending Approval From Valve*. Missar man steg 3 ser allt ut att gå framåt medan ingenting händer.

**Learning (backdatering fungerar, och den är värd pengar):** ikraftträdandedatumet är "the first day that the sales will be attributed to the transferee". Vi satte **1 juli 2026 den 4 augusti** och Valve tog det utan invändning. Det flyttade hela julis intäkter från konkursboet till CZP. **Testa alltid tidigast rimliga datum först** med ett senare som fallback, i stället för att anta att bara innevarande månad går.

**Learning (bekräftelsesteget är en juridisk handling, inte ett OK-klick):** steg 3 kräver fyra Legal Promises: att avsändaren inte längre innehar rättigheterna per datumet, att mottagaren gör det, att avsändaren **endast får medel till och med dagen före**, och att apparna inte längre omfattas av avsändarens SDA. För ett konkursbolag är det garantier ställda för boets räkning. **Det är alltid Roberts klick, aldrig agentens** — visa honom de fyra punkterna ordagrant och vänta på go.

**Learning (mottagarlänken går att hämta själv):** behöver man acceptanslänken utan att vänta på mailet ligger den i onclick-attributet på knappen "View Receiver Link" (`ShowPromptDialogWithProps({ defaultValue: 'https://partner.steamgames.com/pub/apptransferrequest?transferid=…&token=…' })`). Läs attributet direkt, den renderas aldrig som en `href`.

**Learning (WebAPI share-back finns inte i flödet):** trots att beslutet 2026-07-24 var "share-back PÅ vid ominitiering" finns **ingen sådan ruta** någonstans i transfern. Initieringsformuläret har bara mail, orsak och datum; bekräftelsesidan bara de fyra garantierna. Det är en inställning per app efteråt. Anta inte att ett beslut om en platformsinställning går att verkställa i det flöde där det fattades.

**Tags:** steam, steamworks, app-transfer, 301411, 418393, apb-026, legal-promises, backdatering, view-receiver-link

## 2026-08-04 — Valve verifierar skattestatus UTAN att mejla. Poll dashboarden, vänta aldrig på ett mail [apb / apb-026]

**Project:** Aurora Punks (apb-026, Steam APDS→CZP) | **Category:** platform-onboarding, steam, bevakning

**Learning:** CZP:s skatteinformation hos Valve/Lilaham **verifierades 29 juli 22:35 och det kom inget mail om det**. Båda brevlådorna genomsökta: sista Valve-utskicket var 24 juli. Vi satt fem dagar på en öppen grind utan att veta, eftersom accept-watchern var avarmad och ingen pollade. Valve mejlar när de **vill ha något** ("Action Required: Important Tax Information") men inte när de **släpper** något. **Regel: varje Steamworks-grind ska pollas, aldrig inväntas per mail.** De tre sidorna som bär sanningen, på partner-ID:t: `/taxrequirement/view/<partner>/<req>` (ska säga "This tax requirement is closed"), skatteuppgiftssidan (ska säga "Din organisations skatteinformation har verifierats"), och dashboardens "Viktiga handlingar"-räknare. Går räknaren ner till bara kosmetiska poster (postadress, telefonnummer) är bank och skatt klara, det finns ingen separat kvittens för bankgodkännandet.

**Learning (utfallet är värt att spara som prejudikat):** W-8BEN-E:n för ett svenskt AB med LOB-svaret *"Company that meets the ownership and base erosion test"* + **treaty Article 17** gav **0 % källskatt på både Royaltyupphovsrätt och Royaltyfilm**. Formuläret ligger kvar nedladdningsbart som `W8BEN-E-<datum>.pdf` på skatteuppgiftssidan, så nästa entitet kan kopiera exakt samma svar i stället för att gissa om artikeln.

**Learning (sekvensen, hela kedjan bekräftad):** NDA → **SDA** → bank + skatt öppnas → KYC-dokument till Lilahams Dropbox → verifiering → *först då* går app-transfern att köra. Bankfältet fanns inte alls före SDA:n, och KYC-steget syntes inte förrän skatteintervjun var inlämnad. Räkna med fyra grindar, inte två.

**Tags:** steam, steamworks, 418393, 301411, apb-026, w8ben-e, taxidentity, lilaham, article-17, ingen-notifiering

## 2026-08-01 — Fortnox Lön går INTE att skrapa headless, till skillnad från bokföringssidan (CZP, byråavslut)
**Project:** CZP (Sifferrådet-avslut, övertagande av lön) | **Category:** tooling, fortnox, playwright, gränsdragning

**Learning (lönemodulen är en återvändsgränd för Playwright):** SIE-export och lobby-data läses tillförlitligt, men **Fortnox Lön gör motstånd på varje väg jag provade**. Modulen ligger på `/app/<sid>/lon/kalendarie/<n>/sub/registrera` och renderas i en **iframe** (`webapp-ui`), så `page.innerText` ger bara skalet, man måste iterera `page.frames()`. Värre: (1) modulens egna flikar Register/Rapporter reagerar varken på `el.click()` i `evaluate` eller på Playwrights riktiga klick i framen, vyn står kvar på Kalender; (2) klickar man skalets "Register" får man **bokföringens** registermeny (Artiklar, Kontoplan, Kunder) i stället för lönens; (3) `<n>` i URL:en är **inte anställd-id** — n=1..8 gav alla "KALENDER - 1 - ROBERT BÄCKSTRÖM", så anställda går inte att räkna upp den vägen; (4) länklistan i framen innehåller hela appens hjälptexter, så href-jakt på "personalregister"/"semesterskuld" ger URL:er som landar på `common/pagenotfound`. **Så här gör du:** lägg inte mer tid på att skrapa lönemodulen. Personalregister, semesterskuld och ackumulatorer hämtas antingen genom att Robert exporterar rapporterna manuellt, eller genom att **begära dem av byrån som en normal överlämningspost** — billigare och dessutom ett auktoritativt underlag.

**Learning (lönedata finns inte i SIE, och det är lätt att tro motsatsen):** Robert antog att "det mesta borde gå att läsa från SIE-filerna". SIE bär **huvudboksposter** (7010, 7510, 2710 som summor), inte det en lönekörning kräver: personnummer, skattetabell, **ackumulatorer år till datum per anställd**, semesterdagar och semesterlöneskuld, åldersberoende arbetsgivaravgift, förmåner. Utan ackumulatorerna blir både skatteavdrag och AGI fel. **Regel:** vid system- eller byråbyte är lönen alltid en egen datamigrering, aldrig en biprodukt av bokföringsexporten. Flytta aldrig lön mitt i ett år om det går att undvika.

**Learning (svenska deklarationsdatum: 17:e i januari och augusti):** Moms och arbetsgivardeklaration förfaller den 12:e månaden efter, **utom i januari och augusti då det är den 17:e**. Det förklarade varför Henrik erbjöd sig att ta "det som har deadline 17 aug" — det var juliperioden. Avvikelsen flyttar ett brytdatum med fem dagar.

**Learning (avslutsmekanik som återkom här):** Sifferrådets allmänna villkor **§5: "gäller tillsvidare utan uppsägningstid"** — inget avtalat slutdatum finns att luta sig mot, brytdatumet blir rent praktiskt förhandlat. **§2.2:** material ska hämtas inom tre kalendermånader efter räkenskapsperioden, annars arkiveringsavgift eller överlämning till tredje part på klientens kostnad. **Fortnox har tre månaders uppsägningstid på licenser**, så ett årsskiftesbyte kräver uppsägning senast 30 september. Kolla tidigt vem som är **deklarationsombud** — här var byrån ombud för både bolaget och Robert privat, vilket måste bytas hos Skatteverket innan man kan lämna in själv.

**Tags:** fortnox, fortnox-lön, playwright-återvändsgränd, iframe-webapp-ui, SIE-saknar-lönedata, ackumulatorer, byråavslut, Sifferrådet, §5-ingen-uppsägningstid, deklarationsombud, 17-augusti-regeln, CZP

## <!-- ARCHIVE-INDEX -->Archived learnings index

27 older entries were rotated into `archive/admin/` to keep this file loadable in one pass.
Nothing was deleted. They are still indexed by RAG — `rag_search(query, source="agents")` finds them,
or open the archive file below (each has its own Contents block, so you can offset-read a single entry).

### 2026-Q3 — 27 entries → [`2026-Q3.md`](archive/admin/2026-Q3.md)

- 2026-07-31 — Roberts lön/utdelningsutrymme CZP 2026: 3:12-reformen, K10-kedjan och två röda…
- 2026-07-27 — Steam tax onboarding slutar i en Lilaham KYC-dokumentbegäran + passuppladdning…
- 2026-07-27 — Portföljbolag: styrelsetråden ligger på PRIVATA mailen, och aktieboken måste su…
- 2026-07-24 — "Signed, awaiting counter-signature" was a misread: verify agreements in the LI…
- 2026-07-24 — Ickedeterministisk output från deterministisk input = transportfel, inte tolkni…
- 2026-07-24 — Utlägg utanför Pleo: kortet på kvittot avgör om posten alls hör hemma i rapport…
- 2026-07-24 — Stäm ALLTID av utläggsrapporten mot bokföringen innan den går till redovisnings…
- 2026-07-24 — Utläggsrapporten ska gå på KONTANTBASIS mot privatkontot, inte på fakturadatum
- 2026-07-22 — Ränteavstämning på ett låneskuldkonto: läs ALDRIG bara skuldkontot (CZP/ML AB)
- 2026-07-22 — SIE-filer i bokslutszip från redovisningsbyrå: kolla RAR innan du namnger
- 2026-07-21 — Utläggskvitton: poppler renderar "Skannad"-PDF:er blankt, fotade kvitton funkar
- 2026-07-21 — SIE-uttag Fortnox: KLART för CZP (8 år), OMÖJLIGT för övriga 6 (ingen bokföring…
- 2026-07-21 — Övriga bolags SIE finns i MAILEN (byrån bifogar dem), + Ha Bra Liv ska räknas i…
- 2026-07-21 — Läs klientens egen historik med revisor/rådgivare INNAN du bygger en karaktäris…
- 2026-07-21 — Underlag till bokföringsbyrå blir räkenskapsinformation (BFL 1:2) — märk upp det
- 2026-07-21 — Runatyr VAT corrections: filing process + quantification workflow
- 2026-07-18 — Bokio reimports can lose source data; always verify against original SIE
- 2026-07-17 — Runatyr ÅR 2025: fyra saker som återkommer på småbolagsbokslut (run-013)
- 2026-07-17 — Fortnox: års-medveten SIE-export (dra historiska räkenskapsår autonomt)
- 2026-07-17 — Alla SIE alla bolag → RAG: verktygsläge, tenant/år-luckor, kollisionsprotokoll
- 2026-07-17 — Återvinning/1675: riktningen på avräkningskontot avgör försvaret (apb/czp/APDS)
- 2026-07-17 — Post-konkurs plattformsroyalty: identifiera SEB-poster åt förvaltaren (APDS/Ell…
- 2026-07-16 — AP nedskrivning VoD + KBR 2025: metod, tidsgränser och mina egna felkällor
- 2026-07-16 — Steam/Google-Group traps: spam-filed 2FA codes, an ambiguous Valve error, and w…
- 2026-07-16 — CZP:s faktiska finansiella läge per april 2026: utdelning stoppas av försiktigh…
- 2026-07-15 — AP:s revisor = Parameter Revision AB (skild från redovisningskonsult) — 2026-07…
- 2026-07-15 — AP:s speltillgång "Vessels of Decay" - förläggare, ägande, intäktsrutt, bokfört…
