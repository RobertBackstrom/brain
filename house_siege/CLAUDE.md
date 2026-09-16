# House Siege - CLAUDE.md

## Engagement
- **Role:** Co-dev partner och produktionsledning. Vi bygger, de finansierar och äger.
- **DB prefix:** `hsg`
- **Status:** active (uppstart 2026-09-16)
- **Agent owner:** BizDev (deal och pitch), PM (scope och tidplan) när produktion startar

## Vad det är
Två fastighetsmän med tre spelkoncept söker en utvecklingspartner. Materialet kom in via en
Drive-mapp delad av Bibbi Wikman 2026-09-16 (`fastighetskillar`,
`1UF7rLcil_zCWuMmP8Vd-wIUqH8z3L_VJ`, delad till Roberts **personliga** Gmail, inte
robert@aurorapunks.com).

**Robert har valt att fokusera enbart på House Siege.** De andra två koncepten
(Mommy's in a Meeting, Babysitter Panic) ligger parkerade och ska inte drivas vidare
utan nytt besked.

House Siege: asymmetrisk multiplayer där ett lag försvarar ett förstörbart hus och det andra
river det. House Integrity är en synlig delad health bar. Över 50 procent vid tidens slut
vinner försvararna.

## Nyckelpersoner
- **Markus Månsson** - grundare. Styrelseordförande Fastighetsägarna Södra Länsavdelningen,
  Månsbro Fastigheter. **Notera:** Månsbro ägs av bröderna Lars-Åke och Per-Axel Månsson,
  inte av Markus. Deckets "~3 mdkr" är inte verifierat.
- **Oscar Nordqvist** - grundare. Förvaltarforum.se. **Notera:** LinkedIn anger *säljare*,
  decket anger *försäljningschef*. "Rako Fastighets AB (~150 MSEK)" gick inte att hitta alls.
- **Bibbi Wikman** - bibbi@coldpx.com, Cold Pixel. Kanalen in. Se [[project_cold_pixel_dig_in]].

## Regler för det här projektet
1. **Grundarnas egna siffror är obekräftade.** Verifiera mot allabolag innan någon av dem
   återanvänds i vårt material eller citeras mot tredje part. Se
   [[feedback_verify_client_facts_primary_source]].
2. **Deras deck är delvis rå LLM-output.** `Mommy's in a meeting - pitch deck.pdf` inleds med
   "Ja. Här är ett 10-sidigt AAA-pitchdeck...". Återanvänd aldrig deras formuleringar rakt av
   i något vi sätter vårt namn på.
3. **Ingen IP-position.** Beslut 2026-09-16: vi tar recoup plus rev-share, inte ägande.
   Skriv aldrig att vi äger något i House Siege.
4. **Konstriktningen är medvetet ful.** Friendslop, inte polerad AI-render. Se dokumentet.
   Föreslå aldrig AI-genererad key art till det här projektet.
5. **Kommersiell modell:** 120 000 SEK per manmånad, 70 procent cash och 30 procent deferred,
   deferred recoupas 2,5x vid release, därefter 15 procent rev-share. Mönstret kommer från
   [[project_disposable_corps]].
6. **Polden Publishing är måttstock, inte mottagare.** Använd deras siffror som sanity check
   på våra KPI:er. Pitcha dem inte utan nytt besked.

## Kundsida
`pitches/house-siege/index.html` publicerad på **https://pitch.aurorapunks.com/house-siege**,
gated med användaren `housesiege`. **Redigering av mappen är inte publicering:** kör
`./assistant/sync-pitches.sh --apply house-siege` och verifiera mot live-URL:en efteråt.
Sidan är den skrubbade versionen. Allt i listan "Regler" ovan som rör grundarnas meriter,
deras deck eller vår marginal ligger medvetet **inte** på sidan. Håll det så.

## Material
- `market_comp_and_scope_2026-09-16.md` - huvuddokumentet: comp-pass, core loop, art direction,
  Scope A och Scope B med tidplan och budget
- `output_log.md` - leveranslogg
- `drafts/` - lokala arbetskopior

## Källmaterial (deras)
Drive-mappen `fastighetskillar`. Sju filer: `Investor_pitch_v10.pptx` (34 slides, svenska,
huvuddecket), tre koncept-PDF:er och tre key art-PNG:er. Indexerat i RAG under
`source=gdrive-personal`. **Arbetskontot ser inte mappen** (den är delad till privatadressen),
så läs den via RAG, inte via gdrive-MCP:n.
