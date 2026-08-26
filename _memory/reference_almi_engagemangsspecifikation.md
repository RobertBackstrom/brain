---
name: reference_almi_engagemangsspecifikation
description: "Hur man beställer engagemangsspecifikation hos Almi, vad den kostar, hur den levereras och varför det signerade dokumentet man får direkt inte är beskedet"
metadata:
  node_type: memory
  type: reference
---

Almis motsvarighet till bankens engagemangsbesked heter **engagemangsspecifikation** och visar
kapitalskuld och säkerheter per ett valt datum. Revisorn begär den vid varje bokslut där bolaget har
eller har haft ett Almi-engagemang.

**Beställs via Almis e-tjänst**, länkad från `https://www.almi.se/kontaktcenter/laneadministration/`
under "För att beställa en engagemangsspecifikation använder du vår e-tjänst". Formuläret är en
publik Scrive-blankett som öppnas utan inloggning
(`https://go-printer.scrive.com/link/9579b629-741f-465f-963a-3d41a86dd30b`, samma sak som
`etjanster.almi.se/oversikt/external/914`). **350 kr från 2026.** Fälten är bolagsnamn,
organisationsnummer och det datum specifikationen ska avse. Signeras med BankID.

**Fällan: det du får tillbaka direkt är beställningen, inte beskedet.** Scrive mailar ett förseglat,
BankID-signerat dokument som heter "Engagemangsspecifikation" men vars innehåll är rubricerat
**"Beställning av Engagemangsspecifikation"**, med Almi AB som initierare och dig som signerare. Det
innehåller inga skuldsiffror, vilket lätt läses som ett tomt besked. Kontrollera tre saker innan du
drar den slutsatsen: rubriken på sidan, att du står som signerare (ett besked kräver inte din
signatur), och verifikatets tidsstämplar (fylls i på under en minut). Själva specifikationen kommer
separat till den mailadress som angavs i beställningen. Hände AP 2026-08-25, dokument-ID
09222115557587138881.

**Leveransen går till beställaren, inte till revisorn.** Blanketten har ett enda mottagarfält och det
blir bolagets egen adress. Räkna med att vidarebefordra själv. Samma miss som kostade två månader på
SEB-sidan, se [[reference_seb_engagemangsbesked]].

**Dröjer den:** `infolanadm@almi.se` eller låneadministrationen på 063-453 03 00, med dokument-ID:t
som referens.

**Har fordran flyttats till inkasso kan specifikationen komma tillbaka tom.** Almi lägger obeståndsärenden
hos **Alpidus Inkasso** (bankgiro 5557-1418), och då syns engagemanget inte nödvändigtvis hos Almi själv.
Fallback som duger som revisionsbevis: skriftlig bekräftelse från handläggaren på Almi (för AP: Jonas
Backman, chef obestånd, `jonas.backman@almi.se`, 063-453 03 09) plus betalningsbevis från banken. Se
[[project_ap_ek_2025_almi_agarlan]].
