# Disposable Corps: buggar och observationer från spelsessioner

Roberts egna körningar av det publika bygget (Steam app 3579070, demo 3617330). Underlag till
genomlysningsmånaden och till fixlistan i `drafts/dev_plan_high_level.md`. Rapporteras inte
vidare till Armoured Dudes eller LUG utan Roberts godkännande.

| # | Datum | Var | Vad | Allvarlighet | Status |
|---|---|---|---|---|---|
| 1 | 2026-08-26 | Tutorial, lobby | Tutorialtexten staplas: minst fem instruktionsblock renderas samtidigt ovanpå varandra i samma textyta, helt oläsligt | Blockerande för onboarding | Ny |
| 2 | 2026-08-26 | Tutorial | Två VO-röster spelar samtidigt | Blockerande för onboarding | Ny |
| 3 | 2026-08-26 | Lobby | Placeholder-testdata syns i UI: lobbynamnet är "dsadasdasdasd" | Kosmetisk, men syns i varje skärmdump | Ny |
| 4 | 2026-08-26 | Lobby | Spelarporträtt renderas som tomma vita rutor (VinylSole, Zulupox, Krokben) | Kosmetisk | Ny |

## Bugg 1 och 2 är sannolikt samma rotorsak

De hänger ihop och pekar åt två möjliga håll. Skillnaden avgör hur dyrt det är att fixa.

**Hypotes A, lokaliseringen: alla språk är aktiva samtidigt.** I skärmdumpen ligger det som ser
ut som CJK-glyfer under och mellan de engelska raderna. Om samma mening ritas en gång per språk,
och VO:n spelas en gång per språk, förklarar en enda bugg båda symptomen. Butikssidan listar
engelska, förenklad och traditionell kinesiska med full audio, alltså finns minst tre VO-spår
och tre textvarianter att stapla. Det är den billiga varianten: språkval appliceras inte på
tutorial-lagret.

**Hypotes B, tutorialstegens livscykel: steg rivs inte ner innan nästa startar.** Då renderas
steg 1 till 5 samtidigt och deras VO överlappar. Dyrare, för då är det stegmaskineriet som är
trasigt, inte en inställning.

**Testet som skiljer dem åt, tar tio sekunder:** läs de överlappande raderna. Är det **samma
mening på flera språk** är det hypotes A. Är det **olika instruktioner** ur olika tutorialsteg
är det hypotes B. Lyssna likadant på de två rösterna: säger de samma sak på olika språk, eller
olika saker?

## Varför det här är värt att spara

Anthonys fellista från 2026-06-12 sa "UI/UX är dåligt" och "spelarna förstår inte vad de ska
göra". Det här är den konkreta mekaniken bakom den bedömningen: tutorialen är inte bara dåligt
skriven, den är trasig. En spelare som möter det här i första minuten får aldrig veta vad spelet
går ut på. Det stärker UX-raden i planen och det är precis den sortens fynd genomlysningsmånaden
ska producera systematiskt.
