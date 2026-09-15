# 1993 Space Machine - output log

## 2026-08-26 — projektmapp skapad, kostnads- och intäktsrapport till Krister (CorpBot)

Robert bad om en rapport till Krister Karlsson över kostnader och intäkter genom åren, ställd mot
förlagsavtalet. Mapp scaffoldad, rapport skriven till
`drafts/rapport_krister_kostnader_intakter_2026-08-26.md`. Internt underlag, inte utskickat.

## 2026-08-26 forts. — WLBS-bokföringen för 2023 hittad, rapporten uppdaterad (CorpBot)

Robert påpekade att huvudboken borde finnas i RAG eller i mail från Henrik eller Carler. Den
gjorde det. Henrik Franzén skickade `WhiteLinesBlackSpacesAB20240617_111337.se` den 2024-06-17,
nu sparad som `assistant/exports/sie/WLBS_2023_frmail.se`.

WLBS projektmärkte på dimension 6, objekt **16 "Internal - 1993"**, 118 transaktioner 2023:

| Post | Belopp |
|---|---:|
| Intäkt, 3105 + 3305 + kursvinst | −28 237,96 |
| Kostnad, 4600 + 5900 + 7210 + 7510 + kursförlust | 65 986,06 |
| **Resultat 2023** | **−37 748,10** |

Avtalsenligt avdragsgillt av kostnaderna är bara annonsering 9 600, legoarbeten och lokalisering
8 450 samt kursförlust 142. **De 47 798 i intern lön är inte en avdragspost i sektion 14.** Net
Revenue 2023 blir därmed 9 993 och Developer Share 4 997, men sektion 13 ger Service Spend
företräde så inget delas ut.

**WLBS konkursutbrott 2024-09-25** enligt Henriks INK2-mail 2025-08-20. Räkenskapsåren 2019 till
2022 och 2024 saknas fortfarande, se czp-030.

## 2026-08-26 sent — uppskattningsmodell för de saknade åren (CorpBot)

Robert: huvudböckerna för WLBS 2019 till 2022 och 2024 går inte att få fram, uppskatta i stället.
Avsnitt 10 tillagt i rapporten.

**Genombrottet är Steams "Life to date"-sektion.** Två snapshots finns i Drive och gör Steam-sidan
nästan exakt: 1 875,00 USD per 2021-10-31 och 7 325,44 USD per 2023-03-31. Plus 1 040 USD
uppskattat för april 2023 till konkursen ger **8 365 USD, cirka 79 600 SEK** för hela avtalstiden.
Rimlighetskontroll mot bokförda 8 918,64 SEK för 2023 stämmer.

Kanalfördelning ur WLBS 2023: Sony 43 %, Steam 32 %, Beep 25 %.

| Post | Uppskattat |
|---|---:|
| Gross Revenue hela avtalstiden | ca 203 000 (varav ca 153 000 faktiskt) |
| Avdrag, basfall | −271 000 |
| **Net Revenue** | **−68 000** |
| **Developer Share** | **0** |

Känslighetstestat: bara scenariot med lägsta avdrag och trettio procent högre intäkt ger Krister
något av betydelse, och båda antagandena går emot underlaget. Service Spend är den enda post som
verkligen avgör saken.

Valutakurser hämtade 2026-08-27 och korskontrollerade mot Frankfurter/ECB och exchangerate-api:
USD/SEK 9,52 (9,5178 mot 9,5229), EUR/SEK 11,08.

## 2026-08-28 — plattformsunderlagen hämtade ur mailen, enhetstabellen är nu faktisk (CorpBot)

Robert: bättre nyanserade säljrapporter bör gå att få ur respektive plattforms backend, och mail
och Drive bör innehålla utdrag. Mailen räckte långt.

**Beep Japan.** Hela dataserien låg som en zip på 2,8 MB i tråden "[Q3 2023 - Q2 2025] - Sales
Report", plus lösa månadsrapporter i den äldre tråden. 96 månadsrapporter parsade,
**2022-05 till 2025-09**:

| Kanal | Enheter | JPY |
|---|---:|---:|
| Digitalt PS4/PS5 | 467 | 161 868 |
| Digitalt Switch | 426 | 157 593 |
| Fysiskt PS4/PS5 | 455 | 1 070 160 |
| Fysiskt Switch | 620 | 1 945 850 |
| **Totalt Japan** | **1 968** | **3 335 471** |

Per år: 2022 156 enheter, 2023 523, 2024 1 036, 2025 253. Beloppen är Beeps intäkt före vår split,
inte det vi fick. Vår andel för aug 2023 till sep 2025 är de fakturerade 76 109 SEK.

**Sony.** 44 månadsstatements från SIE Europe hämtade, plus SIE America och Japan/Asien. 1993
Shenandoah har SKU **EP6444-CUSA40643_00-083866** och rapporteras per land och månad. Serien
**2023-09 till 2026-07: 249 enheter, 907 EUR**. Februari 2026 sticker ut med 58 enheter över
18 länder, sannolikt en rea. Sony skickar fortfarande statements till APDS trots konkursen.

**Nintendo.** Developer Portal publicerar Switch Download Sales-rapporter men mailen är bara
notiser utan bilaga. Game code för 1993 Shenandoah är **HAC-P-AX84C** under Aurora Punks
Development Services AB, PID 291215956. Kräver portalinloggning, se czp-032.

**Sidan uppdaterad.** Enhetstabellen på pitch.aurorapunks.com/royalty-1993 är nu byggd på
plattformarnas egna avräkningar i stället för uppskattningar. Summan står på **cirka 8 140 sålda
kopior**, varav cirka 5 610 intäktsgivande. Elva rader är nu märkta Bokfört mot tidigare fyra.

Filer: `assistant/uploads/beep/` (110 PDF plus zip), `assistant/uploads/psn/` (158 mappar, 58 xlsx).

## 2026-08-28 (kväll) — Nintendos hela säljhistorik hämtad ur Developer Portal

Robert påpekade att NDP-inloggningen redan finns automatiserad. Den gör den:
[ndp-session.js](../assistant/ndp-session.js) loggar in med `NDP_USER`/`NDP_PASS` ur `.env`,
hämtar MFA-koden ur Gmail och håller 30 dagars enhetstrust i en persistent Playwright-profil.
Byggd för devkit- och NDI-arbetet, återanvänd rakt av här.

**Var rapporterna låg.** Admin > Payments and Financial Reports, inte under produkterna. Sidan
renderar hela historiken som Liferay-dokumentlänkar (`/documents/23933/...`). JSON-API:t
`/o/payments/list/23933` svarar 500 vid refetch, så DOM-länkarna är den hållbara vägen.
Tre filtyper per månad: `DigitalSalesReport` (pdf, sammanställning och provisionsfaktura),
`DigitalSalesDetail` (csv, rad per titel, land och månad med enheter) och `DigitalSalesDetailByState`
(csv, US och CA per delstat).

**189 filer hämtade, juli 2020 till juli 2026, noll misslyckade.** Nya verktyg:
[ndp-sales-reports.js](../assistant/ndp-sales-reports.js) (hämtar) och
[ndp-aggregate.js](../assistant/ndp-aggregate.js) (summerar per titel, period, region och land).
Filerna i `assistant/uploads/nintendo/`, rådata per rad i `1993_nintendo_rader.csv`.

### 1993 Shenandoah på Nintendo eShop utanför Japan

| | Enheter | SEK netto till utgivaren |
|---|---:|---:|
| NOA, Amerika | 857 | 30 762 |
| NOE, Europa | 1 153 | 19 882 |
| NAL, Latinamerika | 81 | 1 019 |
| **Totalt** | **2 091** | **51 664** |

Per år: 2020 1 823 enheter (lanseringen i juli plus en djup rea i oktober och november), 2021 67,
2022 110, 2023 47, 2024 29, 2025 9, 2026 6. Toppländer USA 772, Storbritannien 305, Tyskland 285.
Beloppen är netto efter Nintendos provision om 30 procent.

**Avstämningen håller.** Detaljraderna för samtliga titlar summerar till 89 513,94 SEK, vilket
exakt motsvarar 89 138,70 i faktiskt remitterat plus 375,24 som Nintendo håller inne under
minimibeloppet. Sex månader saknar detalj-csv; deras pdf visar Sales Amount 0,00, alltså inga
sålda enheter, inte en lucka.

**Kontot bär fyra titlar till:** Chenso Club 200 enheter och 19 905 SEK, Hoplegs 423 och 17 453,
TaniNani 15 och 430, Chenso Club_H2 1 och 62.

### Två fynd som inte gäller siffrorna

1. **Betalningsmottagaren byttes i januari 2024** från White Lines Black Spaces AB till
   "Stockholm Core Office", Timmermansgatan 43, Stockholm. Organisationskoden i portalen är
   fortfarande WHITELINESBLACKSPACES.
2. **Bankkontot byttes i februari 2025** från SEB \*\*\*\*2191 till SEB \*\*\*\*4235, alltså efter
   WLBS-konkursen 2024-09-25. Vem som äger det kontot behöver fastställas. Se czp-033.

### Rapportsidan

`pitch.aurorapunks.com/royalty-1993` uppdaterad och verifierad live. Nintendo-raden gick från
"Ej hämtat" till tre bokförda rader. Summan sålda kopior **cirka 10 230**, varav cirka 7 700
intäktsgivande. Mottagen Gross Revenue **244 580 SEK** mot tidigare 202 916, vilket flyttar
återvinningen av Service Spend från 74,9 till **90,2 procent**. Oåtervunnet saldo 26 420 SEK.
Utfallet står sig: ingen utvecklarandel är förfallen, men marginalen är nu tunn nog att nästa
kvartal kan vända den.

## 2026-09-15 — Utgivaravtal Krister Karlsson ↔ Aurora Punks AB, första utkastet

Krister öppnade frågan igen 14 sep ("kanske vi ändå kan få till ett avtal, skall jag låta ChatGPT ta
fram ett?"). Robert svarade 15 sep 10:23 att vi har en mall. Utkast skrivet samma dag:
[publishing_agreement_krister_ap_2026-09-15.md](drafts/publishing_agreement_krister_ap_2026-09-15.md).

**Bas:** Curveball-avtalet mot The Gang Studio (4 sep 2026,
`18hUZ87Ng0WQS1SKT526YBqej0yJB74XtbZmTa6cwUD4`), svensk rätt, Stockholms tingsrätt. Därifrån kommer
konstruktionerna för Publisher Group Company och co-publishers, som är precis vad Robert bad om.

**Ekonomin är hämtad ur WLBS-avtalet 2019-09-20, inte nyuppfunnen.** 50 procent av Net Revenue till
utgivaren, avdragslistan i 1.5 är den gamla listan rensad från de poster som aldrig aktiverades
(sektion 12 om Developer Funding Repayment finns inte i det signerade avtalet och följer alltså inte
med). Service Spend-saldot på 26 420 SEK per 2026-08-28 förs över som Carried Service Spend Balance,
låst i kronor så att ingen valutadrift uppstår, och slocknar när det är återvunnet. Inget nytt
förskott, ingen ny recoupment.

**Fyra val som Robert gjorde inför skrivningen:** 50/50 enligt WLBS, nytt avtal som ersätter 2019
men bär över saldot, engelska, fast femårsperiod med automatisk förlängning om två år.

**Det Robert bad om, och var det sitter:**
- Sublicensiering till CZP: §2.2 (a), plus §2.3 och §8.3 så att CZP får hålla plattformskontona,
  fakturera och betala med befriande verkan.
- Co-publishers: §9, utan Kristers samtycke, betalda enbart ur AP:s halva.
- Ingen styrning av vem: §9.1 säger uttryckligen "at its own discretion".

**Medvetet utelämnat:** Gunnar 20 procent, Mattias 20 procent och Limit Break 8 procent namnges inte.
§4.3 lägger hela ansvaret för underandelar på Krister och gör AP till betalare enbart mot honom.
§14.3 låter honom ändå visa rapporten för dem.

**Öppen punkt som avtalet hanterar men inte löser:** Nintendo-kontot ligger kvar under
organisationskoden WHITELINESBLACKSPACES och Sony avräknar mot APDS. §3.3 ålägger utgivaren att
rätta registreringen. Se czp-033.

Följdupp `gen-297` (skriv ned ägandeupplösningen för Krister) är i praktiken levererad av det här
utkastet, men ligger kvar öppen tills Robert skickat det.

## 2026-09-15 (forts) — Reviewer-pass och tre strukturella omtag

The Reviewer (Fable, juridisk lins) gick igenom utkastet. PM:et ligger i
[reviewer_memo_publishing_agreement_2026-09-15.md](drafts/reviewer_memo_publishing_agreement_2026-09-15.md).
Fjorton rättelser applicerades direkt, tre fynd gick till Robert.

**Det bärande fyndet, verifierat mot primärkällan.** Överlåtelseavtalet med WLBS konkursbo
(`1BHKOVCE2_2j5vHoRd2Z5cjvyJouqalxD`, Penneo, signerat 2024-12-20 av Robert och förvaltaren Petter
Vaeren) har **Aurora Punks Development Services AB som köpare, inte Aurora Punks AB**. Punkt 2.1
säljer verksamheten med tekniska tillgångar, bilaga 1 noterar "1993 Space Machine, IP ägs av en
extern klient", punkt 2.2 undantar utestående fordringar och punkt 3.4 säger att köparen inte
automatiskt inträder i konkursbolagets avtal. AP AB finns inte i något led av kedjan
WLBS-bo, APDS, Bright Gambit, CZP. Nyans att hålla reda på: punkt 3.4 är skriven om
"samarbetsavtal med leverantörer", och Krister är licensgivare, inte leverantör, så ordalydelsen
träffar honom inte rakt av. Huvudregeln gäller ändå, och 2019-avtalet kräver hans skriftliga
samtycke vid överlåtelse. Något sådant samtycke finns inte i mail eller Drive.

**Roberts tre beslut, alla åt det rena hållet:**

1. **CZP signerar som Publisher**, inte AP. Det följer kedjan i stället för att hoppa över den.
   Bakgrund C skriver ut båda överlåtelserna vid datum, §16.1 (a) låter Krister samtycka i
   efterhand, (c) ger honom skadeslöshet mot båda konkursbona. AP AB blir Publisher Group Company
   och §2.2 (a) ger uttrycklig rätt att låta AP stå som utgivare på butikssidorna. Avsteg från
   [[feedback_ap_signs_czp_operates]], medvetet och bara för det här avtalet.
2. **De 26 420 kronorna släpps helt.** Sektion 6 heter nu "No recoupment": allt som uppstod under
   2019-avtalet slocknar på Effective Date, delning från första kronan. Tar bort hela
   konkursfrågan kring vem som äger återvinningsrätten.
3. **Marknadsförings- och portningsavdragen (f) och (g) är borta.** Avdragslistan är nu bara
   plattform, skatt, återbetalningar, fysiska varukostnader och valutaväxling. §3.4 och §10.1 säger
   rakt ut att utgivaren bär de kostnaderna själv. Det var Reviewerns starkaste
   jämkningsinvändning (`AvtL 36 §`) och den är nu borta.

**Konsekvens som måste hanteras: royaltyrapporten stämmer inte längre.**
`pitch.aurorapunks.com/royalty-1993` räknar Service Spend-återvinning och de gamla avdragen. Med
det nya avtalet är basen en annan och Krister har en förfallen andel från första kronan. Rapporten
behöver byggas om innan nästa körning (czp-031, planerad 2026-11-24).

Ekonomiskt är det här klart bättre för Krister än 2019-avtalet. Det är värt att säga rent ut i
följemailet, inte begrava.

## 2026-09-15 (forts 2) — Andra Reviewer-passet, femton rättelser

Pass 2 granskade bara det omskrivna: partsbytet, sektion 6 och avdragslistan. PM i
[reviewer_memo_publishing_agreement_2026-09-15_pass2.md](drafts/reviewer_memo_publishing_agreement_2026-09-15_pass2.md).
Samtliga femton fynd applicerade. Tre var allvarliga, och **två av dem var följdfel från Reviewerns
egna förslag i pass 1**, vilket är ett argument för att alltid köra ett andra pass efter en
strukturell omskrivning.

1. **Kedjan hoppade över Bright Gambit och sa "acquired".** Bakgrund C skrev "sold on by its
   bankruptcy estate and acquired by the Publisher", men APDS-boet sålde till **Bright Gambit AB
   (559351-6536)** 2026-01-18, och BG sålde vidare till CZP 2026-02-16. Avtalet daterat 16 februari
   har inget konkursbo som part. Kedjan står nu utskriven i fyra led, och §16.1 (a) ger Kristers
   samtycke till vart och ett, eftersom 2019-avtalet kräver samtycke per överlåtelse.
2. **Ansvarstaket kapade royaltyn.** §15.6, som kom in i pass 1, begränsade allt ansvar till 24
   månaders utbetalningar, alltså även skyldigheten att betala Kristers andel och skadeslösheten i
   §16.1 (c). Båda är nu undantagna.
3. **Överlevnadsklausulen tappade §16.1.** Pass 1 snävade §12.4 till "16.6 to 16.11", vilket tog
   bort både samtycket till kedjan och skadeslösheten mot konkursbona. Ett bo hör av sig efter
   avtalets slut om det hör av sig alls. §6.1 och §16.1 överlever nu.
4. **Sista luckan i avdragslistan stängd.** §1.5 (b) drog av "revenue shares payable to
   distributors", och ett portningshus på revenue share kunde etiketteras som distributör i stället
   för Co-Publisher. Nu står det rakt ut att den som utvecklar, portar, marknadsför, finansierar
   eller co-publishar är Co-Publisher oavsett vad partnern kallas.
5. **En dörr tillbaka för dyr portning.** §6.2 tillåter att en portningskostnad görs
   återvinningsbar, men bara skriftligt och **i förväg**. §3.4 och §10.1 pekar dit. En Switch 2-port
   kostar mer än spelet tjänar på ett år, och utan dörren hade den krävt ett ändringsavtal.

**AvtL 36 §-exponeringen är i praktiken borta.** Reviewerns tre jämkningsytor (obegränsade avdrag,
inget återfall, obegränsat ansvar för en privatperson) är alla stängda. Avtalet är nu generösare mot
upphovsmannen än både 2019-avtalet och marknadsstandard.

**Två saker för Robert utanför dokumentet:**
1. **Slutraten till Bright Gambit är varken fakturerad eller betald** (apb-051), och BG-avtalets
   punkt 4 har äganderättsförbehåll. CZP har tillträtt men inte fullbordat fånget. Be BG fakturera
   och betala före signering, annars är det sista ledet i kedjan formellt ofullständigt.
2. Undantaget från "AP tecknar, CZP utför" är inskrivet i [[feedback_ap_signs_czp_operates]] med
   testet: finns AP i kedjan som leder fram till positionen avtalet reglerar?

Kvarstår: Kristers postadress (`[address]` i partsblocket och §16.9), vem som äger musiken och
soundtracket på Steam 428890, och om Krister har F-skatt. De två sista ställs i följemailet.

## 2026-09-15 (forts 3) — Kedjan trimmad, dokumentet publicerat

**Robert ifrågasatte mellanstegen i bakgrunden, och hade rätt.** Bakgrund C räknade upp fyra led med
två konkurser, org.nr och datum. Det är mycket konkursdetalj att lägga framför en motpart som bara
vill veta vem han har att göra med, och det får kedjan att se skörare ut än den är.

Lösningen behåller den juridiska effekten och tar bort berättelsen. Bakgrund C är nu en mening:
verksamheten och utgivarpositionen har genom en serie överlåtelser övergått till utgivaren, den
sista fullbordad 2026-02-16. **§16.1 (a) är samtidigt breddad till en heltäckande samtyckesklausul**,
"every transfer ... however effected and whenever made". Den är starkare än uppräkningen, eftersom en
uppräkning riskerar att missa ett led. Krister behåller rätten att på begäran bekräfta samtycket
skriftligt mot ett konkursbo eller en plattformshållare, vilket är exakt det underlag Nintendo och
Sony efterfrågar i apb-054.

**Bright Gambit är slutbetald.** Robert bekräftade det 2026-09-15 med Fortnox huvudbok som källa.
Äganderättsförbehållet i BG/CZP-avtalets punkt 4 är därmed uppfyllt och CZP:s fång fullbordat.
Reviewerns invändning mot ordet "acquired" faller. [[project_apds_czp_rights_chain]] är rättad;
**apb-051 listar fortfarande slutraten som ofakturerad och behöver uppdateras.**

**Publicerat som Google-dokument** i CZP Holding-drivens `_legals/_working/`, enligt filkonventionen
att osignerade utkast ligger i `_working`:
[Publishing Agreement, 1993 Space Machine, Krister Karlsson och Creation Zero Point](https://docs.google.com/document/d/12WokLdIPWxxlWl7l7zjiXMJbV9kxvba9KzMWA1OHrU0/edit)
(`12WokLdIPWxxlWl7l7zjiXMJbV9kxvba9KzMWA1OHrU0`). Inte delat med någon utanför ännu.

Nyinvestering i teknisk portning ska kunna återvinnas, bekräftat av Robert. §6.2 tillåter det
skriftligt och i förväg, §3.4 och §10.1 pekar dit.

## 2026-09-15 (forts 4) — Rapporteringskadens fastställd

Kvartalsvis, inom 30 dagar efter kvartalets slut, med betalning inom samma frist (§8.1). Beslutat av
Robert. Skälen: det matchar czp-031-automationen, §8.2 gör den gatade sidan till rapporten så att
inget separat dokument behöver produceras, och kvartal ligger med marginal över lagkravet i
`URL 29 a §` som bara kräver information en gång om året. 2019-avtalet hade i teorin tätare
rapportering (30 dagar från varje mottagen intäkt) men den hölls aldrig.

**Ny §8.8, minimibelopp.** Rapport lämnas varje kvartal oavsett belopp, men utvecklarandel under
**1 000 SEK** får rullas vidare och betalas när ackumulerat belopp når dit. Rapporten ska ange vad
som rullats. Allt rullat betalas i sin helhet vid avtalets slut och när Krister begär det skriftligt.
Skälet är volymen: Nintendo sålde sex enheter under hela 2026, och ett kvartal kan landa på ett par
hundra kronor. Utan tröskeln blir det fyra fakturor om året på småbelopp från en privatperson, med
eventuellt skatteavdrag på varje.

§11.4 hänger ihop med kadensen: uteblir rapporten två kvartal i rad är det väsentligt avtalsbrott.

Google-dokumentet uppdaterat på samma länk och samma id
(`12WokLdIPWxxlWl7l7zjiXMJbV9kxvba9KzMWA1OHrU0`), via Drive API PATCH i stället för ny uppladdning,
så länken i tidigare loggposter fortsätter gälla.

## 2026-09-15 (forts 5) — Delat med Krister, mailutkast klart

**Dokumentet delat** med mrkristr@gmail.com som **kommentator**, med
`sendNotificationEmail=false`, så att Roberts mail är det första Krister ser. Behörighetslistan är
bara Robert (organizer) och Krister (commenter).

**Mailutkast** skapat i den befintliga tråden `1a04a0caf48a6608` ("Re: Royaltyrapport 1993"),
draftId `r-6034787136915503231`. Inte skickat, Robert skickar själv. Texten har gått genom The
Author enligt hard gate-regeln i [[feedback_author_pass_all_mail]].

**The Author fångade att adressen redan fanns.** Krister skickade den själv 2025-04-23 i
Outzone-tråden (`1965e05ed9b5187c`): **Sommarliden 22, 135 61 Tyresö**. Verifierad mot tråden, inte
tagen på förtroende. Partsblocket är ifyllt och fråga 1 i mailet är omskriven från "skicka din
adress" till "stämmer den fortfarande". Ett `[address]`-fält mindre och en fråga mindre att belasta
honom med.

**Öppen skuld som dök upp i samma tråd.** Robert lovade i april 2025 att beställa en renoverad
Samsung Galaxy S21 från Refurbed som ersättning för Outzone-projektet, Krister skickade adressen,
och i maj 2025 skrev Robert att det dragit ut på tiden på grund av kassaflödet. Krister svarade
"Tack, då vet jag. Hoppas det löser sig". **Telefonen levererades aldrig.** Det är en liten summa och
en obesvarad utfästelse som ligger kvar medan vi ber honom skriva under ett avtal. Värd att lösa
först, eller åtminstone nämnas.
