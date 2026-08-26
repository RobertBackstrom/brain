# CZP Finances - output log

## 2026-08-19 — Reversen omgjord, ägarlånsrättelse, Shosha/WMY-kontering (CorpBot)

**Lånereversen reviderad och återutsänd**
- Robert vill inte att reversen presumerar en skuld från CZP till AP, eftersom avtalet mellan bolagen inte är klart. Punkt 4 om avräkning mot "Långivarens upparbetade skuld till Låntagaren" **borttagen**, punkt 5:s avräkningsalternativ borttaget, och punkt 7 utökad med att reversen inte tar ställning till något annat mellanhavande.
- Daterad om till **2026-08-19** (pengarna går över samma dag). Gamla OpenSign-dokumentet **XKRCivr0QV makulerat**, nytt **AfWbAMb1nY** utsänt och registrerat i watchern.
- **OpenSign-mailet går inte fram.** API:t rapporterar `emailed: true` men ingen leverans finns i brevlådan, varken denna gång eller vid första utskicket. Robert fick signeringslänken direkt i stället. DevOps-ärende: verifiera `sendmailv3`-leveransen från sign.runatyr.games.

**Ägarlånet CZP → AP, rättelse (Roberts besked)**
- Julireversens 50 000 består av **40 000 (3 juli, "ÄGARLÅN UT") + 10 000 (6 juli, "ÄGARLÅN, KOR")**. Båda ska vara ägarlån till AP AB, inte återbetalning till Robert. Henrik bokförde 40 000 mot 2893, vilket är fel.
- **Blocker: CZP saknar konto för AP AB.** 1714 är APDS (konkursbolaget). 1719 är ledigt och föreslås som "Fordran på Aurora Punks AB". Underlag: `drafts/bokforing_agarlan_CZP_AP_juli_2026.md`.
- Att kontrollera: verifikat A 37 (2026-02-26, "Aurora Punks AB / Ägarlån CZP", 25 000) ligger också mot 1714 och kan vara samma feltyp.

**Shosha / Water Me & You (`drafts/bokforing_shosha_wmy_juli_2026.md`)**
- Kreditfakturorna 100 och 101 krediterar faktura 79 och 87. Betalningen 2026-07-24 om 109 717,24 matchas mot **faktura 97**.
- Krediteringarna ska vändas mot **3105 och ursprungligt SEK-belopp** (75 883,50 respektive 75 404,00), inte mot dagskurs, annars nollas inte fakturorna på 1510.
- Alla rader märks dimension 6 objekt **12 "Water, Me and You"**.

**Kontobeslut: 3305 framåt för både Shosha och Yaozuo**
- Intäktsdelning och samutveckling är **tjänst**, hör hemma på 3305 (ruta 40), inte 3105 (ruta 36, varuexport). Ingen kronaeffekt, ingen utgående moms i något av fallen.
- Skälet att bry sig: ruta 36 signalerar fysisk varuexport och går att stämma av mot Tullverket. Vi har redovisat ~293 tkr varuexport till Serbien och ~32 tkr till Kina utan tullhandlingar bakom.
- **Beslut: 3305 från och med nu, gamla fakturorna lämnas orörda.** Ingen omprövning av redan lämnade perioder.
- Yaozuo bytte i praktiken redan vid faktura 81. Obokförda 102 och 105 går på 3305 med objekt 7.

**Nytt minne:** [[feedback_numbered_questions]] — frågor till Robert ska numreras så han kan svara i nummerföljd.

## 2026-08-18 — Lånerevers 50k, Runatyr-faktura, Fortnox-kartläggning (CorpBot)

**Bankavstämning CZP 2026 (SIE #GEN 2026-08-18 mot kontoutdrag t.o.m. 2026-08-18)**
- Kontoutdrag sparade i ren UTF-8 till `umbrella/czp_finances/bank_statements/` och uppladdade till CZP `_financials/Bank_Statements` `1ogAe7nErTBqGDbA9LHsU8PHdkJBQ2qEA`. Indexerade i RAG.
- Bokfört 1930 = 714 995,14. Bank = 806 016,10. **Differens 91 020,96.**
- Differensen ligger på **tre dagar och fem bankrader**, allt annat stämmer på öret:
  | Datum | Text | Belopp | Status |
  |---|---|---:|---|
  | 2026-07-06 | KORTFRIST LÅ | −15 000,00 | obokförd, kontering ej fastställd |
  | 2026-07-06 | ÄGARLÅN, KOR | −10 000,00 | obokförd, kontering ej fastställd |
  | 2026-07-16 | RUNATYR AB | +2 000,00 | obokförd, ska mot 1713 |
  | 2026-07-16 | H16548119566 | +4 303,72 | obokförd, avsändare okänd |
  | 2026-07-24 | SHOSHA GAMES | +109 717,24 | obokförd kundbetalning |
- **Metodnot:** en rak radmatchning gav 28 falska avvikelser eftersom banken visar buntade bankgirobetalningar (LBE/LBS) medan Fortnox bokför varje leverantör separat. Netta per dag i stället, då kollapsar buntningen och bara de äkta luckorna blir kvar.
- **Shosha-betalningen kan inte matchas än:** kundfakturorna 97–105 är utställda men obokförda. 109 717,24 ≈ 10 000 EUR till 10,97, sannolikt faktura 97 (förfall 2026-07-16). Kursdifferens bokas på 3960/7960 som tidigare Shosha-betalningar (jfr C 12 och C 24).
- **Levfakturor klara att betala, ej blockerade av ovanstående:** 884 Skokloster, 896 Ark Island, 898 Lost Hive, 901 Fortnox.
- **ÖPPEN FLAGGA — julireversens 50 000 syns inte som utbetalning.** Ingen överföring om 50 000 till AP finns i CZP:s konto. Den 3 juli gick 40 000 ut märkt "ÄGARLÅN UT" men bokfördes mot **2893 skulder till närstående** (alltså återbetalning till Robert), inte mot fordran på AP. Jämför februari, där "Ägarlån CZP" till AP gick mot **1714**. Behöver redas ut innan den nya reversen betraktas som lån nummer två, annars finns två signerade reverser och ett penningflöde.
- Skattekonto bokfört −1 276, stämmer mot Fortnox lobby. Sparkonto: bokfört 0,00 mot bankens 1,24.



**Lånerevers CZP → AP, 50 000 SEK (nr 2)**
- Dokument: `umbrella/aurora_punks/drafts/Lanerevers_CZP_AP_2026-08-18.md`. Identisk med julireversen (kortfristigt ovillkorat aktieägarlån, räntefritt, återbetalning senast 2026-12-31, avräknas mot CZP:s upparbetade skuld till AP) med ändamålet löpande utgifter + revisorskostnader, plus ny punkt 7 som klargör att den gäller vid sidan av reversen från 6 juli.
- OpenSign docId **XKRCivr0QV**, ordnad signering Robert (0) → Wiking (1) → KM Troedsson (2). Manuell fältplacering på sida 2, y 291/357/379. Registrerad i `opensign-watch.js` för auto-advance, arkiveras till AP `_legals` `1K6g0CydsFfdJ-jCBE4HoHaxy5nkpQVwP` vid slutförande.
- **AP tecknas två i förening.** Robert bad om "mig och Wiking"; KM måste med annars är AP inte bunden. Robert står bara på CZP-raden (ABL 8:23).
- Följebrev till Wiking + KM som Gmail-utkast, osänt (draftId r-6615899698574747731).

**Faktura RUNATYR-2026-001 till CZP**
- Underlaget fanns i två versioner: specifikationsarket (18 rader, 28 700,08) och den lokala markdownen (20 rader, 29 532,08). Differensen 832,00 = marselen, Ellevio 415 + GodEl 417, som bara finns i 20-radersversionen. Den senare är den Q1-deklarationen bygger på och därmed den rätta.
- Utskicksfaktura: `umbrella/runatyr/drafts/Faktura_RUNATYR-2026-001_utskick.md`, PDF renderad. Behåller nummer och datum 2026-03-31 så Runatyrs redan inlämnade Q1 stämmer. CZP bokför vid mottagande och drar momsen i augustiperioden. Ingen rättelse behövs i något av bolagen.
- Betalningsrad: avräkning mot CZP:s fordran på Runatyr (konto 1713) i stället för bankgiro.
- Gmail-utkast till CZP:s Fortnox-inkorg `inbox.lev.908387@arkivplats.se` med PDF bifogad, **osänt**.
- Nytt verktyg: `assistant/gmail-draft-attach.js` (utkast med bilagor; `gmail-draft.js` klarar bara text).

**FEL UPPTÄCKT: dubbelavdrag i Runatyrs Q2-moms**
- Rad 19-20 i RUNATYR-2026-001 är marselen (Ellevio 415, GodEl 417), vidarefakturerad till CZP och avdragen av Runatyr redan i **Q1**. Samma två betalningar räknades in igen i Q2 eftersom de betalades 28 april och 18 maj.
- Ruta 48 i den inlämnade Q2-deklarationen är därför **166 kr för hög** (rätt ca 1 183, inte 1 349). Kvittas mot de 1 453 kr som ändå skjuts till Q3 → netto ca +1 287 där.
- Rotorsak: aprilbetalningarna är marsfakturor. Ellevio april = 447 (betald 3 juni), GodEl april = 427 (betald 25 maj).

**Fortnox-kartläggning CZP (läs-bar, `assistant/fortnox-state.js`, nytt skript)**
- **7 transaktioner att hantera** under Bokföring från kontoutdrag. Detta blockerar betalkörningen.
- 1 leverantörsfaktura att attestera, förfaller 2026-08-28. Kundkännedom behöver förnyas.
- Leverantörsreskontra: 9 fakturor, 375 515,63 kr, 0 förfallna.
- Skattekonto −1 276 kr (hämtat 2026-08-18 06:00), SEB 806 016,10 kr. AGI-betalningen 63 841 har gått igenom.
- **IndieARK var redan fakturerad:** kundfaktura 102 (450 USD, majrapporten, 2026-07-06) och 105 (382 USD, junirapporten, 2026-08-18), båda obetalda. Mitt tidigare "ofakturerad" byggde på SIE, som bara bär bokförda verifikat. Kundreskontran är källan, inte SIE-filen. `drafts/indieark_faktura_2606_underlag.md` rättad.


## 2026-08-13 - Byråövergång Sifferrådet, Skatteverket-avstämning, IndieARK, Carolinas lön (CorpBot)

**Byråövergången**
- Henriks sista mail (10 aug, privata brevlådan, tråd `19fa37288605741c`): levfakturorna bokförda, förslag att Robert kör betalningar/bokföring/löner från nu medan Sifferrådet stämmer av t.o.m. 2026-07-31, lämnar momsen och deklarerar juli-lönerna. INK2 inlämnad 24 juli. Obesvarad i tre dygn.
- Utkast på svar skapat i privata brevlådan (draftId `r2275479766363703409`), osänt. Bekräftar upplägget, ber om bekräftelse att Carolinas MS2 ligger i juli-AGI:n, flaggar momsperiod-glappet (Henrik skrev "Q2", Emelie skrev junimomsen) och deklarationsombudsbytet efter 17 aug.

**Skatteverket**
- Inlämnat enligt Sifferrådet: juli-AGI + junimoms (deadline 17 aug), INK2 (24 juli).
- Öppet och kräver BankID: Skatteverket "Du har saker att göra" (13 aug 02:30, privata) samt två Kivra-aviseringar 11 aug om nytt brev, till **Runatyr AB** inte CZP.
- Datumrättelse: MS2-skatten angavs i mail till Sifferrådet som "senast 12 augusti". Rätt datum är 17 augusti (augustiundantaget).

**IndieARK / Strike Force Heroes**
- Underlag: `drafts/indieark_faktura_2606_underlag.md`. Kvar att fakturera är junirapporten IA-R-APD2026008, **USD 382,74**. Konto 3305, objekt 6 = "7", ruta 40, ingen moms.
- Rättelse under arbetet: jag rapporterade först att 26.04-26.06 var ofakturerade. Fel. Faktura 93 (aprilrapporten) bokfördes 10 juni men registrerades 24 juni, alltså efter min lokala SIE-export den 22:a.
- Fynd: fakturorna 51-73 ligger på 3105 (varor utanför EU, ruta 36) medan 81 och 93 ligger på 3305 (tjänster, ruta 40). Beslut behövs om rättelse.

**Carolinas lön (K2C-ljud)**
- MS2 11 700 brutto betalades manuellt 24 juli. Verifierad mot färsk SIE längre ned: bokförd och med i juli-AGI:n.
- MS3 22 500, riktdatum ca 4 aug. Finns inte i böckerna.

**Fortnox-access löst, färsk SIE dragen (`#GEN 20260813`, 740 verifikat)**
- Rotorsak till "felaktigt lösenord": värdet i `.env` ligger inom enkla citattecken (lösenordet innehåller `#`), och env-parsern skickade med citattecknen. Fixat i `fortnox-login2.js` och `fortnox-sie-export.js`: strippar CR och matchande omgivande citattecken. Inloggningen gick sedan igenom utan MFA.
- **Carolinas MS2 är korrekt bokförd.** Lönekörning 2026.M.07, anställd 900613004, objekt "Sands of Duat": brutto 10 447 + semesterersättning 1 253,64 = 11 700,64, personalskatt 1 371, arbetsgivaravgift 3 676,34. Betalningen bokförd A 239 den 24 juli mot 2910. Nettot i körningen är 10 330 mot utbetalda 10 329, en krona ligger kvar på 2910.
- **MS3 finns inte i böckerna.** Varken betald eller bokförd, riktdatum var ca 4 augusti.
- **Skattekontot 17 augusti: 63 841 kr, obetalt.** Levfakt 897, bokförd 2026-08-17, ingen Levbet. Stämmer exakt mot 2710 personalskatt 26 232 + 2730 arbetsgivaravgifter 37 609. Skattekontosaldo 1630 är +49 044, bank 1930 är 92 461.
- **Månadsmoms bekräftad:** momsrapporter M1-M6 för januari till juni. Junimomsen är redovisad. Julimomsen är Roberts första egna, deadline 12 september, preliminärt **ca 242 tkr att betala**, drivet av Raw Fury-fakturan 103 (560 000 + 140 000 moms, K2C MS3, 30 juli).
- **IndieARK:** sista Yaozuo-fakturan i böckerna är nr 93. Majrapporten (USD 450,62) är alltså också ofakturerad, inte bara junirapporten.
- Övriga obetalda leverantörsfakturor: 884 Skokloster, 896 Ark Island, 898 Lost Hive, 901 Fortnox. Leverantörsskulder totalt 439 357.

**Beslut från Robert 2026-08-13**
- IndieARK-fakturan omfattar bara junirapporten, USD 382,74. Majrapporten kontrollerar han själv mot Kevins betalningar.
- Skattekontobetalningen 17 aug hanterar han själv, inget underlag behövs.
- Kvar hos CorpBot: MS3 för Carolina är obetald och obokförd, ingen instruktion given än.

**Tidigare blockering (löst samma dag)**
- `fortnox-login2.js` föll på lösenordssteget med "Felaktigt lösenord" och felrapporterade det som `MFA_REQUIRED`, varpå den väntade på en SMS-kod som aldrig skickades. Stoppat efter ett försök för att undvika kontolåsning. Lösenordet var korrekt, se rotorsaken ovan.
- Färskaste tillgängliga SIE utan inloggning: Drive `1XtddyFSx16a9v_fnhXQqmfwJc2Ql5wID`, genererad 2026-07-21. Lokala kopian i `czp-finances/` är från 22 juni.

## 2026-07-24 - ML-skuld, Q2+juli-utlägg, gdrive-fix (CorpBot)

**ML AB skuldavstämning + erkännande av skuld**
- Byggde full avstämning av CZP:s skuld till Magnus Liljedahl AB ur SIE 2020-2026 (konto 2890 + 8420), dagligt saldo, ränta 4% actual/365.
- Kapital per 2026-06-30: 3 103 355 kr. Vald position (Robert): 3 355 832 kr inkl obetald ränta 252 477. Fallback 3 416 893.
- Nyckelfynd: ränta HAR fakturerats 2021-2023 på konto 8420 (336 325 tot), slutade 2024. Magnus överdebiterade 65 620 vs 4%.
- Leverabler i `_legals/_working/`: `ml_skuld_avstamning_2026-06-30.csv`, `ml_skuld_underlag_till_lawyer.md`, GDoc "Erkännande av skuld - CZP till Magnus Liljedahl AB (UTKAST 2026-07-24)".
- 4 öppna punkter till Henrik innan påskrift (faktura 622, 25k-gap, moms 6300, A322).

**Q2 + juli utläggsrapport (utanför Pleo)**
- Kontantbasis mot Roberts privatkonto (Skandia VISA 3081). Q2 6 384,71 (moms 940,80) + juli 4 376,14 (moms 492,23) = 10 760,85.
- Avstämt mot SIE 2026 så inget Pleo-bokfört kom med (4 poster bortsorterade: GWS apr/maj, Anthropic apr/maj under "CLAUDE.AI SUBSCRIPTION").
- Google Sheet delad med hej@sifferradet.se; kvittomappar Q2+Q3 delade; Telia-fakturor uppladdade.
- **Mail skickat till Emelie (hej@sifferradet.se) 2026-07-24 23:45** - verifierat i Sent.
- Öppna: 2 Grand Hotel F&B-notor saknar kvitto (284+110); Telia marsfaktura 1 659 aldrig rapporterad tidigare; GWS jun 126,50 EUR nekad/obetald.

**SIE-arkiv + gdrive-read.js-fix**
- AP 2024 SIE (ur Henriks AP.zip) uppladdad till AP `Bokföring/2024`. 2023 finns ej som SIE, bara som jämförelseår i 2024-filen.
- Rotorsak till "oläsbara" PDF:er hittad: `gdrive-read.js` korrumperade binärt via `data += chunk`. Fixat med Buffer.concat + supportsAllDrives. db-279 rättad (mitt tidigare poppler-fynd var feldiagnos).

## 2026-08-19 (kväll) — Fortnox-inmatning, CorpBot

**Skapat konto 1719 "Fordran på Aurora Punks AB"** (aktivt, samma namnkonvention som 1711–1718;
1719 var ledigt mellan 1718 Monowo och 1720). Behövs för ägarlånsrättelsen och för A 37.

**Kontobyten på kundfakturor, verifierade mot live-Fortnox:**

| Faktura | Ändring |
|---|---|
| 97, 98, 99 (Shosha) | radkonto 3105 → **3305**, projekt 12 oförändrat |
| 102, 105 (Yaozuo) | "Rounding"-raden 3105 → **3305**, huvudraden låg redan rätt, projekt 7 |
| 100, 101 (krediteringar) | **orörda på 3105** — de krediterar 79/87 som ligger på 3105 |

Krediteringarna var redan rätt riggade: 100 har kurs 10,8405 och 101 har 10,772, alltså exakt
originalkurserna på 79 och 87. Reskontran nollas därmed utan restpost. Ingen åtgärd behövdes.

**Bankfeeden (7 ohanterade poster) identifierad — motparterna som saknades i SEB:s CSV:**

| Datum | Post | Motpart enligt Fortnox |
|---|---|---|
| 2026-07-05 | Ägarlån, kort 10 000 ut | **Aurora Punks AB** |
| 2026-07-05 | Kortfrist lån 15 000 ut | **Runatyr AB** |
| 2026-07-15 | 2 000 in | Runatyr AB |
| 2026-07-15 | 4 303,72 in | **Yaozuo**, 450,00 USD, ref "SALES SHARING FROM INDIEARK" = faktura 102 |
| 2026-07-23 | 109 717,24 in | Shosha, 10 000 EUR = faktura 97 |
| 2026-08-01 / 08-15 | 0,00 och 14 797,00 | Skattekonto |

SEB:s CSV kapar textfältet vid 12 tecken och tar bara med mottagarkonto ibland, så bankfeeden i
Fortnox är rätt källa för motpart. Skrivet till admin_learnings.

**Blockerare: kundfakturorna går inte att bokföra.** `bookKeep`-flaggan står på 0 för allt från
och med 2026-07-06, mot 1 på allt till och med 2026-06-10:

| Faktura | Datum | bookKeep | Verifikat |
|---|---|---|---|
| 87 | 2026-05-31 | 1 | B44 |
| 93 | 2026-06-10 | 1 | B43 |
| 97, 102 | 2026-07-06 | **0** | saknas |
| 104 | 2026-07-31 | **0** | saknas |

Utskriftsflödet kör igenom utan fel (`PUT savebeforesend=1` → `POST sendv2` → `document-v1/print`,
alla 200/201) men skapar inget verifikat. Automatlåsning av period är avstängd och räkenskapsåret
2026 är öppet, så det är inte en låst period. Ingen kontroll för flaggan hittad i gränssnittet.

**Två fel upptäckta på vägen:**
1. Levfaktura **902** Red Marmoset, 72 000 kr: attesterad 2026-08-17, konteringen balanserar
   (2440/4531/2645/2614, omvänd skattskyldighet), men fakturadatum står som **2026-05-08** medan
   originalet är daterat 05/08/2026 i brittiskt format, alltså **5 augusti**. Förfallodatum
   2026-08-28 stämmer med originalet. Detta är den enda levfakturan som inte ligger under betalning.
2. Kundfaktura **104** Netlight Consulting AB står på **21 118,00 USD**. Netlight är ett svenskt
   bolag och beloppet ser ut som kronor.

### Rotorsak funnen 2026-08-19: behörighet, inte låst period

Bankfeeden ger felmeddelandet i klartext när man öppnar en transaktion:

> "Du saknar behörighet för att skapa och koppla verifikat. En systemadministratör kan hjälpa dig
> ändra behörigheten."

Robert Bäckströms Fortnox-användare får alltså inte skapa verifikat. Det förklarar allt tre på en
gång: kundfakturorna 97 till 105 (`bookKeep=0`, inget verifikat vid utskrift), levfaktura 902
(attesterad men "Ej bokförd"), och de sju ohanterade bankposterna. Det är inte en låst period,
automatlåsningen är avstängd och räkenskapsåret 2026 är öppet.

Brytpunkten i data stämmer med överlämningen: allt till och med 2026-06-10 har `bookKeep=1` och
verifikat, allt från 2026-07-06 har `bookKeep=0` och saknar verifikat.

Konsulter med fulla moduler på abonnemanget: **Amer Alsalek** och **Emelie Andersson**
(Sifferrådet). Användare: Robert Bäckström (registrerad firmatecknare), Carolina Foghammar Nömtak,
Gustav Andreas Carlberg. Modullicenserna ligger på 1/1.

Åtgärd: en systemadministratör måste ge Roberts användare rätten att skapa och koppla verifikat.
Därefter går hela batchen att mata in i ett svep.

**Utfört på begäran:** förfallodatum på levfaktura 902 ändrat från 2026-08-28 till **2026-08-21**
för betalning imorgon. Fakturadatum står kvar på 2026-05-08 i väntan på besked.

**Övrigt att hantera:** Aurora Punks AB:s abonnemang är låst enligt tenant-listan och behöver
låsas upp av en systemadministratör. Kundfaktura 104 till Netlight Consulting AB står på
21 118,00 USD.

### 2026-08-19 forts. — behörigheten fixad, första bokföringen gjord

Robert la till bokföringsrättigheterna. Rättighetslistan gick från 166 till 171 poster; tillkomna
är `bf.bookvoucher`, `bf.altervoucher`, `bf.createaltervoucher`, `bf.createvoucheraccrual` och
`bf.delvoucher`. `/bf/voucher/new` renderar nu 22 fält och en Bokför-knapp, och bankfeedens
behörighetsvarning är borta.

**Bokfört ur bankfeeden, serie A:**

| Datum | Text | Kontering |
|---|---|---|
| 2026-07-05 | Aurora Punks AB / Ägarlån, kort | 1719 debet 10 000 / 1930 kredit |
| 2026-07-05 | Runatyr AB / Kortfrist lån | 1713 debet 15 000 / 1930 kredit |
| 2026-07-15 | Runatyr AB / Delåterbetalning kortfristigt lån | 1930 debet 2 000 / 1713 kredit |

Netto juli: fordran på Runatyr ökar 13 000, fordran på AP AB ökar 10 000.

**Levfaktura 902 är bokförd, VER.NR D96**, förfallodatum ändrat till 2026-08-21 så den kommer med
i morgondagens betalning. Mekanismen som saknades: en leverantörsfaktura bokförs inte genom att
sparas, utan genom att markeras i `/lf/sinvoicelist` och köras via **Bokför** i listfoten.
Fakturan hade `authorizeFlowIsDone=true` men `authorizeBookKeep=false`, alltså attesterad men inte
bokföringsattesterad. Fakturadatum står kvar på 2026-05-08 i väntan på besked.

**Kvar, blockerat på behörighet:** `kf.bookinvoice` och `kf.bookinvoicepay` under Fakturering
saknas fortfarande, så kundfakturorna 97 till 105 går inte att bokföra och därmed inte heller
betalningarna Shosha 109 717,24 och Yaozuo 4 303,72 som ligger i bankfeeden.

**Kvar, kräver eftertanke:** de två skattekontoposterna. Bankraden LBS −14 797 den 12 augusti är
redan automatbokförd, så skattekontosidan ska kopplas till samma verifikat via "Koppla verifikat"
med vidgat datumintervall, inte bokföras som ett nytt verifikat.

**Noterat:** ägarlånsutbetalningen matchade två regelverk samtidigt, "ÄGAR" och "ÄGARLÅN UT",
vilket är varför den inte automatbokfördes. Regelverken bör städas.

### 2026-08-19 slut — kundfakturorna kvarstår olösta

Rättigheterna är nu kompletta, 192 poster, inklusive `kf.bookinvoice` och `kf.bookinvoicepay`.
Trots det bokförs inte kundfakturorna 97 till 105:

- Utskrift via `sendv2` med `sendType: "print"` returnerar 201 men skapar inget verifikat.
- `sendType: "dontSend"` ("Skicka ej") returnerar **500** med tom felkropp.
- Kundfakturalistan har ingen Bokför-knapp i footern, till skillnad från leverantörslistan.
- Ingen Bokför-åtgärd på fakturasidan. Automatlåsning av period är av, räkenskapsåret öppet,
  FÖRVALT-kolumnen är informativ utan kontroller.
- `bookKeep` är en statusspegel, inte en inställning: 1 på bokförda (79 = B35), 0 på obokförda.

Detta ser ut som ett fel i själva fakturorna eller i konfigurationen, skapade 2026-07-06 och framåt.
Nästa steg är Fortnox support eller Henrik, inte fler försök i gränssnittet. Fakturorna ska INTE
bokföras som manuella verifikat, det skulle bryta kopplingen till kundreskontran.

### 2026-08-20 — ägarlånen omförda till 1719 (verifikat A264)

Originalverifikaten, framsökta via fritextsökning "Ägarlån" i verifikationslistan:

| Ver | Datum | Belopp | Låg på | Fel |
|---|---|---:|---|---|
| A37 | 2026-02-26 | 25 000 | 1714 debet | APDS i stället för AP AB |
| A204 | 2026-07-03 | 40 000 | 2893 debet | skuld i stället för fordran |
| A259 | 2026-08-19 | 50 000 | 2893 debet | samma |

A259 var okänd sedan tidigare och visar att **överföringen på 50 000 enligt lånereversen är gjord
2026-08-19** och automatbokförd av regeln "ÄGARLÅN UT".

**Omföring bokförd som A264, 2026-08-20:**

| Konto | Debet | Kredit |
|---|---:|---:|
| 1719 Fordran på Aurora Punks AB | 115 000,00 | |
| 1714 Fordran på Aurora Punks Development Services AB | | 25 000,00 |
| 2893 Skulder till närstående personer, kortfristig del | | 90 000,00 |

Differens 0,00, kontrollerad i en torrkörning innan bokföring. Ett omföringsverifikat i stället för
tre, daterat i innevarande period så inga stängda månader berörs. Rättelsen är rent
balansräkningsmässig, ingen moms- eller resultateffekt.

**Saldo på 1719 efter detta: 125 000** (A261 10 000 + A264 115 000). Fordran på APDS (1714) minskar
med 25 000 och skulden till närstående (2893) med 90 000.

Skriptet ligger kvar som `assistant/fx-omforing.js` med en `--dry`-flagga; det bokför bara om
differensen är noll.

### 2026-08-20 — hur de internationella fakturorna har hanterats historiskt

Analys av SIE-exporten `assistant/uploads/CZP_2026_SIE4_20260818.se`, 748 verifikat.

**Henrik bokförde dem genom det vanliga flödet, inte manuellt.** Tio verifikat i serie B med
texten "Kundfaktura <kund> (<fakturanr>)" för Shosha och Yaozuo under 2026, och nio i serie C med
"Kundbet ...". Registreringsdatum ligger två till tre veckor efter bokföringsdatum, han körde i
omgångar. Antagandet att internationella fakturor brukar bokföras manuellt stämmer alltså inte.

**Kursdifferenser** bokförs automatiskt i betalningsverifikatet mot 3960 (vinst) eller 7960
(förlust). 2026 hittills: 3960 −21 339,11 och 7960 +22 249,01, netto cirka 910 kr i förlust.

| Kund | Netto kursdifferens (plus = förlust) |
|---|---:|
| Netlight Consulting AB | −7 018,66 |
| Epoch | +4 838,17 |
| Shosha Games doo Beograd | +1 311,56 |
| Yaozuo Games Ltd | +994,20 |
| BADASS Studios Limited | +49,07 |
| Headup GmbH | +0,30 |

**Bankkostnader** ligger separat på 6570, inte nettade mot fakturan. 4 231,00 kr på 28 poster
hittills 2026, i tre former: "COSTH17514983931" 50 till 60 kr per inkommande internationell
betalning (cirka 19 st), "10000 BANKTJÄNSTER" 230 till 494 kr per månad, och tre poster på 320 kr
(15 juni, 17 och 21 juli) för utgående internationella betalningar.

**Observation:** Yaozuo-betalningarna kommer konsekvent in 1,5 till 4,1 procent lägre än fakturerat.
Delar av det är sannolikt korrespondentbanksavgifter som dras vid källan och som då hamnar på 7960
som kursförlust i stället för på 6570. Totalt knappt 1 000 kr, ingen brådska men värt att veta.

**Rättelse av tidigare påstående:** kundfaktura 104 till Netlight på 21 118,00 USD är korrekt.
Netlight faktureras i utländsk valuta varje månad med svensk moms på 2611, sex fakturor hittills i
år på 195 till 205 tkr. 21 118 USD landar mitt i det spannet. Min tidigare flaggning var fel.

**Slutsats för 97 till 105:** de ska bokföras genom det vanliga flödet som tidigare. Att det inte
går är ett fel att lösa, inte något att kringgå med manuella verifikat.

## 2026-08-20 — avstämningsprocess uppsatt + CZP löner augusti

**Process:** `skills/bookkeeping_reconciliation_run.md`, indexerad under nytt kluster "Ekonomi &
Bokföring". Robert säger ett bolag plus eventuellt fokus, CorpBot stämmer av mot Fortnox och
Skatteverkets kalender. Bolag i rotationen: CZP (Fortnox), Runatyr och **Zenland Games AB
559385-0547** (kontoutdrag från Robert).

**Löner augusti 2026**, underlag i `drafts/loner_augusti_2026.md`. Utbetalning 2026-08-25.

| Namn | Brutto | Skatt | Netto | Arb.avg |
|---|---:|---:|---:|---:|
| Robert Bäckström | 55 000,00 | 12 550,00 | 42 450,00 | 17 281,00 |
| Gustav Andreas Carlberg | 53 000,00 | 12 311,00 | 40 689,00 | 16 652,60 |
| Carolina Foghammar Nömtak (MS3) | 22 500,00 | enligt tabell | | 7 069,50 |
| Elias Strandberg (2 h à 220) | 440,00 | enligt tabell | | 138,25 |

**Carolina:** avtalets Enclosure 1 punkt 7 ger MS3 = 22 500, måldatum 2026-08-04, alltså redan
förfallet. Rätten är enligt 6.2 inte villkorad av att Raw Fury betalat.

**Elias:** timlönen är **220 kr/h** sedan 2026-07-15, inte 188. Timarken visar 2 h i juli.
Datumen i arket är feltypade som 2027. Timavtalet (OpenSign `ZiR26oSoI2`) är inte bekräftat
signerat. Skattetabell saknas på personalkortet.

**Gustav:** tog ut semester i juli, L24 visar 53 000 uppdelat på 2 119,52 + 50 880,48. Kvarvarande
semesterdagar behöver hämtas ur Fortnox semesterrapport före körningen.

**Skatteverket:** augusti-AGI och julimomsen förfaller båda 2026-09-14 (den 12:e är lördag).
Julimomsen är inte lämnad, preliminärt cirka 242 tkr att betala drivet av Raw Fury-fakturan 103.

**Även gjort idag:** levfaktura 902 rättad till augusti via A267/A268; ägarlånen omförda till 1719
via A264; Playwright ominstallerat efter att npx-cachen tömts, 18 skript ompekade.

### 2026-08-20 forts. — skattetabell Elias, Gustavs semester

**Elias Strandberg, skattetabell 31 kolumn 1.** Personnummer 20010606-7036, 25 år, skriven i
Bandhagen som ligger i Stockholms kommun. Stockholm 2026: 18,22 + 12,33 + 0,07 begravningsavgift
= 30,62 procent, verifierat mot skattetabeller.se och SCB. Kryssvalidering: Henrik skrev
2025-07-17 att Gustav skattar enligt tabell 31, samma kommun. Förbehåll: kyrkoavgift ger en annan
tabell, och Fortnox kan hämta rätt uppgift från Skatteverket på personnumret. Timavtalet är
signerat enligt Robert.

**Gustav, semester 2026-07-13 till 2026-08-07 = 20 vardagar, 160 timmar.** Inga röda dagar.
Fortnox öppna löneperiod är 2026.M.09 med avvikelseperiod augusti, alltså ligger avvikelser en
månad efter lönen: 15 dagar i juli regleras i M.08 den 25 augusti, 5 dagar i augusti i M.09 den
25 september.

**Blockerare:** avtalet ger 25 dagar med förskottssemester men lönebeskedet visade 5 dagar redan
i mars 2026 (Roberts mail till Henrik 2026-03-16). Förskottsdagarna är aldrig inlagda. Registreras
20 dagar mot 5 bokas 15 som obetald semester och nettolönen sjunker. Förskottsdagarna måste in på
personalkortet först.

**Öppet tekniskt problem:** Fortnox lönemodul går inte att styra via `fx.js`. Kalendern är låst
till anställd 1 (Robert), `/lon/kalendarie/<id>` omdirigerar tillbaka till 1, och rutterna
`/lon/personal`, `/lon/register/personal` och `/lon/anstalld` svarar inte. Registreringen av
frånvaron behöver antingen en anvisning om hur man byter anställd, eller göras av Robert.

### 2026-08-24 — färsk SIE: kundfakturorna är bokförda, momsperioderna analyserade

Ny export `assistant/uploads/CZP_2026_SIE4_20260824.se`, 775 verifikat mot 748 den 18 augusti.

**Kundfakturorna gick igenom.** Blockeraren är löst:

| Ver | Faktura | Kontering |
|---|---|---|
| B52 | 97 Shosha | 3305 110 315,00 |
| B56 | 98 Shosha | 3305 110 315,00 |
| B55 | 99 Shosha | 3305 44 126,00 |
| B53 | 102 Yaozuo | 3305 4 342,31 |
| B50 / B51 | 100 / 101 kreditfakturor | 3105 75 883,50 och 75 404,00, exakt originalbeloppen |
| C56–C59 | matchning | nollar 79 och 87 utan restpost |
| C60 | betalning Shosha | 109 717,24, kursförlust 597,76 |
| C61 | betalning Yaozuo | 4 303,72, kursförlust 38,59 |

Kursförlusten på Yaozuo blev exakt de 38,59 jag räknade fram i förväg. **Kvar: faktura 105**
(Yaozuo, 382 USD, 2026-08-18) är fortfarande obokförd.

Även bokfört: E108 betalning av levfaktura 902 (72 000, 2026-08-21), A265 skattekonto 1 276,
A266 bankavgift 320, A258 Kronofogden 140 000 mot 1634.

**Maj är återöppnad men momsen är oförändrad.** Diff mellan de två SIE-exporterna: majs
momskonton är identiska före och efter mina bokningar. D96 och A267 tar ut varandra exakt på
2614, 2645 och 4531. Perioden återöppnades bara för att verifikat landade i den.

Skillnaden mellan M5 (193 798) och de 212 210 Fortnox nu visar är en **periodförskjutning på
2641 mellan april och maj**: +18 412,50 i april och −18 412,50 i maj, alltså noll över de två
månaderna. Samma fenomen finns mellan juni och juli med 1 200 kr, vilket förklarar varför skärmen
visar 282 228 för juli medan M7 bokförde 281 028.

| Månad | 2641 ingående moms |
|---|---:|
| april | +18 412,50 |
| maj | −18 412,50 |
| juni | +1 200,00 |
| juli | −1 200,00 |
| augusti | +22 234,95 |

**Rekommendation: klarmarkera inte maj innan vi sett vad Fortnox vill bokföra.** Skapar den ett
nytt M-verifikat på 18 412 blir det en rättelse mot Skatteverket för en skillnad som inte finns i
sak.

**Rättelse av tidigare uppgift:** jag skrev att julimomsen preliminärt var cirka 242 tkr. Rätt
siffra är **281 028 enligt M7**, 282 228 enligt Fortnox omräkning. Klarmarkerad i Fortnox betyder
att rapporten är färdig och bokförd, inte att den är inlämnad. Deklarationen ska fortfarande in
senast 2026-09-14.

### 2026-08-24 kväll — lönemodulen öppnad, Gustavs semester registrerad

**Lön saknades i abonnemanget.** Programlistan hade Bokföring, Fakturering, Tid, Leverantörsfaktura-
attest, Kvitto & Utlägg och Resa, totalt 861 kr/mån inklusive Fortnox Access. Lön och
Anläggningsregister fanns bara på fliken Konsulter, alltså via Sifferrådets egen licens genom
byråsamarbetet. Robert beställde Lön och tilldelade den till sin användare. Rättigheterna gick
från 192 till 227 poster, varav 44 `lon.*` inklusive `lon.register_personal`, `lon.run_create`
och `lon.run_pay`.

**Gustavs semestersaldo, hämtat ur Visa Saldo:**

| | Antal | Registrerat | Utbetalt | Kvar |
|---|---:|---:|---:|---:|
| Betalda dagar | 25,00 | 2,00 → **22,00** | 2,00 | 23,00 |
| Sparade dagar | 5,00 | 0,00 | 0,00 | 5,00 |
| Obetalda / förskott | 0,00 | 0,00 | 0,00 | 0,00 |

**Rättelse av tidigare påstående:** förskottssemester behövdes inte. Semesterårsavslutet 2026-03-31
gav Gustav hela årsrätten på 25 betalda dagar. De 5 dagar som lönebeskedet visade i mars 2026 var
det gamla semesterårets rest, inte det nya årets rätt.

**Registrerat i Fortnox, orsak Semester, 8 timmar per dag:**

| Period | Vardagar | Avvikelseperiod | Lönekörning |
|---|---:|---|---|
| 2026-07-13 till 2026-07-31 | 15 | juli | 2026.M.08 |
| 2026-08-03 till 2026-08-07 | 5 | augusti | 2026.M.09 |

Registrerat gick 2 → 17 → 22, alltså exakt +15 och +5. Kalendern visar 152 frånvarotimmar för juli
eftersom inställningen "Automatisk registrering på arbetsfria dagar" står på Ja och fyller helgerna,
men helgdagarna belastar inte semesterdagarna. Kvar efter körningarna: 3 betalda plus 5 sparade.

**Verktyg:** `assistant/fx-franvaro.js <anst-id> <orsak> <fr.o.m.> <t.o.m.> <tim/dag> [--dry]`.
Navigeringen i lönemodulen kräver att man går via Kalender → Visa lista → klicka raden; hash-rutten
`/lon/kalendarie/<id>` fungerar först efter att listan laddats. Fältnamnen i frånvarodialogen är
`form-kalendarie-registrera-franvaro-{regkod,startdatum,slutdatum,dagar,timmar,projekt,creator}`.

**Sessionskonflikt:** Fortnox tillåter en inloggning per användare. När Robert är inne i sin
webbläsare kastas Playwright-sessionen ut med "Du har blivit utloggad". Kör inte samtidigt.

**Kvar:** Elias personalkort. Jag har personnummer 20010606-7036, adress Skebokvarnsvägen 376,
124 50 Bandhagen, timlön 220 kr/h och skattetabell 31 kolumn 1, men **inte hans bankkonto**.

### 2026-08-24 sent — Elias Strandberg upplagd som anställd

Bankuppgifterna hämtade ur Roberts arbetsmailbox: Elias skickade dem själv 2024-06-04 och
2024-08-05, **13460608730 Danske Bank** = clearing 1346, konto 0608730. Inget nyare finns.
Adressen i de mailen (Lovisedalsvägen, Älta) är gammal; timavtalet från juli 2026 har
Skebokvarnsvägen 376, 124 50 Bandhagen, som Elias själv föreslog. Det spelar roll eftersom Älta
ligger i Nacka kommun med annan skattesats medan Bandhagen är Stockholm, alltså tabell 31.

Sidofynd: OpenSign-kvittot 2026-07-16 bekräftar att **timavtalet är signerat av alla parter**.
Ett annat sökträff-spår, clearing 8327-9 i en Sifferrådet-tråd, visade sig gälla **Daniel Hansen**
och inte Elias.

**Upplagd som anställd 900613005:**

| Fält | Värde |
|---|---|
| Personnummer | 20010606-7036 |
| Adress | Skebokvarnsvägen 376, 124 50 Bandhagen |
| Clearing / konto | 1346 / 0608730, Danske Bank |
| Anställningsdatum | 2026-07-17 |
| Anställningsform | Särskild visstidsanställning |
| Löneform | Timlön, 220,00 kr/h |
| Personaltyp | Tjänsteman |
| Skattetabell | 31, kolumn 1, huvudarbetsgivare |
| Betalda semesterdagar | 0 |

Noll semesterdagar följer avtalets § 4.1: **220 kr/h är inklusive 12 % semesterersättning, och
inga separata semesterdagar tillkommer.** § 4.2 slår dessutom fast att lön betalas månadsvis i
efterskott mot loggade timmar, vilket bekräftar att juli-timmarna hör till augustikörningen.

Fortnox visade en dialog "Valt anställningsdatum ger 18 betalda semesterdagar istället för
nuvarande 0. Vill du ändra?". Den lämnades obesvarad och kortet sparades med 0 dagar, vilket är
rätt enligt avtalet. Filtret "Ej kompletta" i personalregistret returnerar noll rader, alltså
passerar kortet Fortnox fullständighetskontroll.

**Verktyg:** `assistant/fx-anstalld.js spec.json [--dry]`. Fältnamnen är
`form-personal-{information|anstallning|loneuppgifter|skatt|semester}-<fält>`.
Rutten är `/lon/personalregister` med knappen "Skapa anställd".

### 2026-08-24 natt — augustilönen skapad, 2026.M.08

Lönebesked skapade för period **2026.M.08**, avvikelseperiod 2026-07-01 till 2026-07-31,
utbetalningsdag **2026-08-25**.

| Anst | Namn | Bruttolön | Skatt | Att utbetala |
|---|---|---:|---:|---:|
| 1 | Robert Bäckström | 55 000,00 | −12 550,00 | 42 450,00 |
| 900613003 | Gustav Carlberg | 56 418,50 | −13 776,00 | 42 643,00 |
| 900613004 | Carolina Foghammar Nömtak | 22 500,80 | −3 543,00 | 18 958,00 |
| 900613002 | Petter Mikaelsson | 0,00 | 0,00 | 0,00 |
| 900613005 | Elias Strandberg | **0,00** | 0,00 | 0,00 |
| | **Summa** | **133 919,30** | **−29 869,00** | **104 051,00** |

**Gustavs 56 418,50** är semesterregistreringen som slår igenom: 53 000 plus 3 418,50, vilket är
exakt 15 dagar × 0,43 % semestertillägg. **Carolinas 22 500,80** är MS3, alltså 20 090 plus 12 %
semesterersättning, i linje med hur MS2 räknades i juli (10 447 + 1 253,64).

**Elias står kvar på 0 och behöver två fält på personalkortet.** Hans lönebesked har rätt
underlag men fel pris:

| Löneart | Antal | Belopp | Källa |
|---|---:|---:|---|
| 11 Timlön | 88,00 tim | 0,00 | SCH (schemat) |
| 11 Timlön | 2,00 tim | 0,00 | BER |
| 10 Arbetstid, tid 2026-07-26 | 2,00 tim | 0,00 | KAL |

Närvaroregistreringen landade rätt (rad 3), men **timlönen 220 och arbetsschemat sparades aldrig**
på kortet. Uppläsning bekräftar `arbschema=HEL`, `sysgrad=100,00`, `timlon=0,00`, medan
anställningsdatum 2026-07-17 och skattetabell 31 sitter kvar sedan skapandet. Heltidsschemat är
dessutom farligt: sätts timlönen med HEL kvar blir SCH-raden 88 × 220 = 19 360 kr fel.

**Kvar att göra på Elias, i den här ordningen:**
1. Personalkort → **Anställning** → arbetsschema **"0 - 0-schema timanställd"** (finns i registret,
   0 %). Kontrollera att sysselsättningsgrad, veckotimmar och dagtimmar går till noll.
2. → **Löneuppgifter** → timlön **220,00**. Spara.
3. Lönekörning → Elias lönebesked → **Skapa om lönebesked** → OK.
4. Kontrollera att bara 2,00 tim återstår och att bruttolönen blir **440,00**.

**Därefter för hela körningen:** klarmarkera, skicka lönebesked, bokföringsunderlag, betalning,
och arbetsgivardeklaration senast 2026-09-14. Petters tomma lönebesked kan raderas om det inte
ska med.

**Verktyg tillagda:** `fx-narvaro.js`, `fx-personalkort.js`, `fx-lonekorning.js`. Notera att
`fx-personalkort.js` fyller fälten korrekt men att Spara inte persisterar — orsaken är inte
utredd.

**Elias skatteavdrag (beslut 2026-08-24):** augustibeskedet ger 0 kr preliminärskatt på 440 kr
brutto, vilket är korrekt enligt tabell 31:1. Robert valde att låta det stå för augusti och ta
frågan före septemberkörningen. Den öppna frågan är om CZP är Elias huvudarbetsgivare, för är det
inte det ska 30 % dras som sidoinkomst i stället för tabellavdrag. Följdpunkt `czp-026`.

### 2026-08-24 — augustilönen klarmarkerad, skickad och bokförd

**Slutliga belopp, period 2026.M.08, utbetalningsdag 2026-08-25:**

| Anst | Namn | Brutto | Skatt | Att utbetala |
|---|---|---:|---:|---:|
| 1 | Robert Bäckström | 55 000,00 | −12 550,00 | 42 450,00 |
| 900613003 | Gustav Carlberg | 56 418,50 | −13 776,00 | 42 643,00 |
| 900613004 | Carolina Foghammar Nömtak | 22 500,80 | −3 543,00 | 18 958,00 |
| 900613005 | Elias Strandberg | 440,00 | 0,00 | 440,00 |
| | **Summa** | **134 359,30** | **−29 869,00** | **104 491,00** |

**Utfört:** fyra lönebesked klarmarkerade och skickade (flikarna visar Skickade 4, Skapade 1).
Bokföringsunderlag skapat med verifikations-id 312 till 315 och bokfört. Resultat: **L27 till L30**,
alla daterade 2026-08-25. Kontrollerat mot verifikationslistan: exakt fyra M.08-verifikat, inga
dubbletter trots att bokför-knappen klickades flera gånger av mitt skript.

Gustavs L28 på 110 715,69 ser hög ut men stämmer: 56 418,50 brutto plus 17 726,69 i avgifter plus
semesterlön och semesteravdrag om 36 570 vardera, alltså 15 dagar × 4,6 % av 53 000, som tar ut
varandra i resultatet.

**Petters tomma lönebesked lämnades orört**, varken klarmarkerat eller skickat.

**FEL SOM MÅSTE RÄTTAS: arbetsgivaravgifter saknas på Elias.** L30 har bara två rader,
7210 debet 440,00 mot 2910 kredit 440,00. Det saknas **7510 debet / 2730 kredit 138,25 kr**
(440 × 31,42 %). Lönebeskedet visar "Prel. arbetsgiv.avg %: 0". Roberts L27 på 72 281 innehåller
sina 17 281 i avgifter, så felet sitter på Elias personalkort och inte i körningen.

Trolig orsak: samma sak som gjorde att timlön och arbetsschema inte sparade när kortet skapades,
alltså att Skatt-flikens fält inte initierats vid sparningen. Fältet heter `skatt-ejarbavgift`
och det finns även `skatt-arbavgrabatta`.

Konsekvens: avgiftsunderlaget i augusti-AGI:n blir 440 kr för lågt, alltså 138,25 kr för lite i
arbetsgivaravgifter till Skatteverket. Måste rättas före deklarationen 2026-09-14.

**Arbetsgivardeklarationen gick inte att skapa än.** Väljaren för AGI-period i
bokföringsunderlaget är tom, den öppnar först när augusti är stängd.

**Betalningen är inte lagd.** 104 491 kr ut ur bolaget kräver Roberts eget godkännande i SEB med
BankID, så den lämnas till honom.

**Verktyg tillagda:** `fx-klarmarkera.js`, `fx-skicka-lonebesked.js`, `fx-bokfor-lon.js`,
`fx-bokfor-kor.js`.

### 2026-08-24 — löneutbetalningsväg, Telia-utlägg, hemmakontor

**Löner betalas inte via leverantörscheckouten.** Fortnox Betalservice säger själv "endast
leverantörs- och skattebetalningar i SEK". Rätt väg är Lön → Lönekörning → fliken **Skickade** →
knappen **"Skapa utbetalningslista"** med tillhörande Utför.

Sidofynd i Roberts skärmbild: kontot i checkouten var **sparkontot** SE74 5000 0000 0526 6333 4480
med 1,24 kr, inte företagskontot 52661032177 med 806 tkr. Det är sannolikt därför "Skicka för
signering" var grå.

Historiskt har CZP betalat nettolöner som **manuella överföringar**, inte via lönefil:
CFOGHAMMAR L −10 329 (2026-07-24), LÅN GUSTAV −40 689 (2026-04-24), LÅN MARS −42 450 (2026-04-01),
LBE5532-9924 −40 689 (2026-03-26).

**Telia saknas helt i böckerna.** Noll verifikat på Telia, Telenor, Tele2 eller mobil under 2026.
De privata utläggen är alltså inte bokförda. Kontering när underlagen kommer: 6212 Mobiltelefon
eller 6230 Datakommunikation, motkonto återbetalning till Robert.

**Hemmakontor: avrådan i nuläget.** CZP har **112 392,60 kr i lokalhyra** 2026 på två fakturor från
**NeCo Software AB** (D17 50 081,60 och D51 62 311,00) plus 3 890 i el på 5020. Skatteverkets
grundkrav för att ett bolag ska få hyra arbetsrum i ägarens bostad är att bolaget **saknar annan
lokal** där arbetet kan utföras. Med löpande hyra till NeCo håller inte det argumentet.

Om upplägget ändå blir aktuellt (om NeCo-lokalen sägs upp) gäller:
- Hyran beskattas hos Robert som **inkomst av kapital**, 30 %.
- **Schablonavdraget 40 000 kr gäller inte** vid uthyrning till eget bolag; endast faktisk
  merkostnad får dras av.
- Hyra över marknadsmässig nivå omklassas till lön.

**Renare alternativ:** låt bolaget bära bredband, mobilabonnemang och kontorsutrustning direkt.
Avdragsgillt, normalt ingen förmånsbeskattning vid tjänstebruk, och löser Telia-frågan på köpet
genom att flytta abonnemanget till bolaget.

**Väntar på Robert:** underlagen för Telia-utläggen, och besked om NeCo-lokalen fortfarande löper.

### 2026-08-25 — missad leverantörsreskontra i gårdagens pass (CorpBot)

Robert påpekade att leverantörsfakturorna inte togs upp i passet 2026-08-24. **Det är mitt fel.**
Steg 2 i [[../skills/bookkeeping_reconciliation_run]] säger att `/lf/sinvoicelist` ska hämtas varje
körning och att fokuset styr djupet, inte omfånget. Gårdagens pass gick från SIE-analysen rakt in i
lönekörningen och öppnade aldrig reskontran.

Obetalda leverantörsfakturor enligt Roberts skärmbild 2026-08-25, totalt **663 685,08**:

| Nr | Leverantör | Belopp | Moms | Förfaller | Läge |
|---|---|---:|---:|---|---|
| 898 | Lost Hive Studios AB | 84 375,00 | 16 875,00 | 2026-08-28 | bokförd D92 |
| 903 | Lost Hive Studios AB | 128 250,00 | 25 650,00 | 2026-08-28 | ej i SIE 24/8 |
| 904 | Ha Bra Liv Stockholm AB | 3 000,00 | 600,00 | 2026-09-02 | ej i SIE 24/8 |
| 905 | Runatyr AB | 29 532,08 | 4 930,00 | **2026-08-20, förfallen** | ej i SIE 24/8 |
| 906 | Bright Gambit AB | 137 500,00 | 27 500,00 | **2026-08-24, förfallen** | ej i SIE 24/8 |
| 907 | Skattekonto 1655918274713 | 281 028,00 | 0,00 | 2026-09-14 | julimomsen |

SIE-exporten 2026-08-24 19:49 har bokförda levfakturor till och med 902, alltså är 903 till 907
antingen registrerade efter exporten eller obokförda. Verifieras vid nästa inloggning.

**905 ska inte betalas via bankgiro.** RUNATYR-2026-001 är enligt loggen 2026-08-18 avsedd att
avräknas mot CZP:s fordran på Runatyr, konto 1713.

Likviditet: företagskontot 806 016,10 minus augustilönen 104 491 ger 701 525. Täcker hela kön.

Ingen Fortnox-inloggning gjord, Robert är inne i systemet och sessionerna slår ut varandra.

### 2026-08-25 forts. — konteringsmallar klara, momsfel funnet på 905

Förberett offline inför sweepen, mönster hämtade ur SIE 2026-08-24:

| Nr | 2440 kredit | 2641 debet | Kostnad debet | Källa |
|---|---:|---:|---|---|
| 903 Lost Hive | 128 250,00 | 25 650,00 | 4600 102 600,00, objekt 6 "19" | som D92 |
| 904 Ha Bra Liv | 3 000,00 | 600,00 | 2890 2 400,00 | som D79 |
| 906 Bright Gambit | 137 500,00 | 27 500,00 | 6991 110 000,00 | som D86/D87 |
| 907 Skattekonto | 281 028,00 | 0,00 | 1630 281 028,00 | som D90 |

**Momsen på 905 är felregistrerad i Fortnox.** Skärmbilden visar moms 4 930,00. Fakturan
RUNATYR-2026-001 har moms **3 316,88**; de 4 930 är raden "tjänst från utländsk leverantör"
(Google Workspace 4 565 + Obsidian Sync 365), alltså ett underlag utan moms, inte ett momsbelopp.
Bokförs den som registrerad drar CZP **1 613,12 kr för mycket i ingående moms** i augustiperioden.
Rättas före bokföring.

Rätt kontering för 905, betalning via avräkning mot 1713, inte bankgiro:
2440 kredit 29 532,08 / 2641 debet 3 316,88 / kostnader debet 26 215,20 fördelat på
6212 telefon 1 506,93, programvaror 4 930,00, 5410 inventarier 7 874,00 + 9 430,40 + 1 103,98,
6110 kontorsmaterial 319,68, friskvård 145,00, 5460 förbrukning 239,92, 5020 el 665,58.

Sidonotering, låg prio: fakturans egen summering går inte ihop med radbeloppen. Raderna summerar
till 29 532,37, sammanställningen säger 29 532,08. Underlaget för 25 % står som 13 266,09 men
raderna ger 13 266,49. Differensen 0,29 kr lämnas som den är, Runatyrs Q1-moms är redan inlämnad
och en rättelse kostar mer än den är värd.

### 2026-08-25 — leverantörssweepen körd, fyra bokförda, 905 stoppad (CorpBot)

Fortnox-inloggning gjord efter Roberts klartecken. Ny SIE `assistant/uploads/CZP_2026_SIE4_20260825b.se`.

**Bokfört, fyra verifikat:**

| Ver | Faktura | Kontering |
|---|---|---|
| D97 | 903 Lost Hive Studios | 2440 −128 250 / 2641 25 650 / 4600 102 600, objekt 6 "19" Sands of Duat |
| D98 | 904 Ha Bra Liv Stockholm | 2440 −3 000 / 2641 600 / 2890 2 400 |
| D99 | 906 Bright Gambit | 2440 −137 500 / 2641 27 500 / 6991 110 000 |
| D100 | 907 Skattekonto, julimomsen | 2440 −281 028 / 1630 281 028 |

Alla fyra låg redan rätt konterade av Fortnox automatik. Enda tillägget var projekttaggen 19 på
D97, som D92 hade men den nya fakturan saknade. Verifierat mot färsk SIE, inga dubbletter.

**905 Runatyr är INTE bokförd, och ska inte bokföras som kostnad.**

Verifikat **A76 "Utlägg Robert Q1 2026"** den 2026-03-31 bokför redan samma utlägg, mot 2820
Kortfristiga skulder till anställda. Fem belopp matchar Runatyr-fakturans radsummor exakt:

| Konto | A76 | RUNATYR-2026-001 |
|---|---:|---:|
| 6210 Telekommunikation | 1 506,93 | Telia jan+feb+mar 1 506,93 |
| 4535 tjänst utanför EU | 4 565,00 | Google Workspace 4 565,00 |
| 4531 tjänst inom EU | 365,00 | Obsidian Sync 365,00 |
| 6110 Kontorsmateriel | 319,68 | 319,68 |
| 7621 Sjuk- och hälsovård | 145,00 | Friskvård 145,00 |

A76 summerar till 37 690,58 på 2820 och innehåller alltså mer än fakturans 29 532,08, men
överlappet är fullständigt. Bokförs 905 som kostnad dubbelbokas både kostnaden och den ingående
momsen. A76 drog dessutom 4 962,39 i ingående moms medan fakturan anger 3 316,88.

Momsfältet på 905 är dessutom felregistrerat till 4 930,00, vilket är raden "tjänst från utländsk
leverantör", inte ett momsbelopp. Kostnadsraden står som 4600 Legoarbeten 24 602,08.

Rekommenderad hantering, ej utförd: bokför 905 som **2440 kredit 29 532,08 / 2820 debet
29 532,08** utan momsrad. Det byter bara motpart på en skuld som redan finns, från Robert privat
till Runatyr, och rör varken kostnad eller moms. Betalning sker sedan via betalsättet
**"Runtyr (1713)"** som finns i Fortnox utbetalningsvy, inte via bankgiro.

Kvittningsunderlaget behöver uppdateras. `Kvittningsbekraftelse_Runatyr_CZP_2026-05-13.md` utgår
från att faktura 43 har saldo 26 100. **Saldot är nu 8 100.** Med 1713 på 83 340 är Runatyrs
nettoskuld till CZP 61 907,92 efter kvittning.

**Övrig avstämning:**

- Bankfeeden är tom, "Allt är bokfört och klart".
- Företagskontot har **387 895,10**, inte de 806 016 jag citerade tidigare. Den siffran var
  hämtad ur en äldre skärmbild. Sparkontot har 1,24.
- Betalningslista skriven till `drafts/betalningslista_2026-08-25.md`. Kassan räcker till den
  28 augusti. Underskottet uppstår på andra Lost Hive-fakturan och når 465 964 vid julimomsen.
- Kundreskontran har 880 661,29 varav 630 915 förfallet: APDS 512 500 sedan 2025-06-07,
  Shosha 10 000 EUR sedan 2026-08-07, Runatyr 8 100 sedan 2026-05-28.
- Majperioden ligger fortfarande som "att hantera" med inrapporteringsdag 2026-07-13.
- Nytt verktyg: `assistant/fx-levfaktura.js`, öppnar en levfaktura via listan, dumpar
  konteringen, kan sätta projekt och bokföra. Bokför-knappen är en split-action-span,
  `span.js-supplierinvoice-split-action-label`, inte en button-roll.
