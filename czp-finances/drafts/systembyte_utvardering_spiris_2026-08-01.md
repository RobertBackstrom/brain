# Utvärdering: Spiris som ersättare för Fortnox (CZP)

**Startad:** 2026-08-01 · **Ägare:** CorpBot · **Beställd av:** Robert
**Status:** pågående, inga beslut fattade

## Varför

Sifferrådet (Henrik Franzén) sa upp det löpande uppdraget 2026-07-27. CZP tar över
bokföring och lön i egen regi. Fortnox behålls tills vidare, men Robert vill bort från
det på sikt: dyrt, och API:t ligger bakom dyrare licensnivåer, vilket blockerar den
automation som är hela poängen med att köra det själva.

Spiris (tidigare Visma eEkonomi, ombrandat 2025) är kandidat nummer ett eftersom API:t
är **detsamma på samtliga prisnivåer** och utvecklarkonto är gratis. Det är precis den
låsning vi vill bort från.

## Beslutsdatum som styr

| Datum | Vad |
|---|---|
| 2026-08-17 | Sifferrådet lämnar julis moms + AGI (sista de gör) |
| 2026-09-12 | Första egna inlämningen, augustiperioden |
| **2026-09-30** | **Sista dag att säga upp Fortnox med verkan vid årsskiftet (3 mån uppsägningstid)** |
| 2027-01-01 | Föreslaget bytesdatum |

Utvärderingen måste alltså vara klar med rekommendation **före 30 september**, annars
förlorar vi ett år.

## Varför bytet ska ske vid årsskiftet, inte tidigare

Bokföring går att flytta mitt i ett år med en SIE-import. Lön gör det inte. Vid ett
lönebyte mitt i året måste ackumulatorer år till datum per anställd bäras över mellan
systemen, och det är det enskilt mest felbenägna momentet i svensk löneadministration.
Fel där slår igenom på skatteavdrag, AGI och kontrolluppgifter. CZP har fyra på lön.

## Kriterier

Rangordnade. Nummer 1 och 2 är avgörande, resten är vägning.

1. **Öppet API på den prisnivå vi faktiskt köper.** Inklusive lön, inte bara bokföring.
   Fortnox faller på just detta.
2. **Svensk lön som håller:** AGI-fil till Skatteverket, arbetsgivaravgifter per
   åldersgrupp, semesterlöneskuld, kontrolluppgifter, fyra anställda.
3. Månadsmoms (CZP redovisar moms månadsvis, bekräftat av Robert 2026-08-01).
4. SIE-import av hela 2026 så att jämförelseår och ingående balanser blir rätt.
5. Bankkoppling SEB, leverantörsfakturaflöde med attest, kvittohantering.
6. Total månadskostnad vid fyra anställda, jämfört med dagens Fortnox-nota.
7. Årsredovisning och INK2, eller i vart fall exportformat som en byrå kan ta emot om
   vi köper den biten styckvis.

## Prisbild (webbkällor 2026-08-01, ej verifierad mot offert)

| Paket | Pris | Not |
|---|---|---|
| Starta | 199 kr/mån | bokföring |
| Driva | 349 kr/mån | + fakturering |
| Skala | 549 kr/mån | |
| Växa | 749 kr/mån | med lönehantering |
| Lyfta | 1 249 kr/mån | flera administratörer, budget och prognos |

En annan källa anger bokföring + fakturering + lön till 518 kr/mån, så lönepaketets
pris är inte entydigt mellan 518 och 749. Ett AB med **en** anställd anges landa på
400 till 600 kr/mån. CZP har fyra, så räkna med påslag. Alla paket uppges ha gratis
deklarationstjänst och digital årsredovisning första året.

**Att göra:** begär skarp offert för fyra anställda i stället för att lita på
jämförelsesajter.

## Referensalternativ

- **Fortnox**, nuläget. Bäst API i branschen, men låst till dyrare nivåer.
- **Lundify** (ex Björn Lundén), från 269 kr/mån, byggt för byråer, djup lön.
- **Dooer**, 0 kr/mån, AI-kategorisering, mobilfokus, ingen support. Löndelen tveksam.
- **Wint**, 2 190 kr/mån, ersätter både program och byrå: bokföring, lön, moms, ÅR.
  Detta är köp-i-stället-för-bygg-alternativet och rätt referenspris när Sifferrådets
  slutfaktura kommer.

## Öppna frågor

1. Vilken Spiris-nivå krävs för att API:t ska täcka **lön**, inte bara bokföring?
2. Kostnad per anställd utöver paketpriset?
3. Går AGI att lämna programmatiskt, eller genereras bara en XML som en människa laddar
   upp hos Skatteverket? (Bokio gör det senare. Skillnaden avgör hur mycket vi kan
   automatisera.)
4. Klarar SIE-importen ett brutet övertagande mitt i 2026 om vi mot förmodan måste
   flytta tidigare?
5. Vad blir Fortnox faktiska månadskostnad idag? Behövs för jämförelsen och är inte
   framtagen. Ligger på abonnemangssidan, abonnemangsnr 908387.

## Nästa steg

1. Skaffa gratis utvecklarkonto hos Spiris och läs API-dokumentationen för lönedelen.
2. Begär offert för fyra anställda.
3. Ta fram Fortnox nuvarande månadskostnad ur abonnemangssidan.
4. Testinstans med SIE-import av CZP 2026 när den finns.
5. Rekommendation till Robert senast **2026-09-20**, tio dagar före uppsägningsfristen.

## Logg

- 2026-08-01: utvärdering startad. Kriterier och prisbild från webbkällor. Inga
  leverantörskontakter tagna, ingen offert begärd, inget testkonto skapat.
