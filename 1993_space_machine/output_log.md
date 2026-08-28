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
