# Fotoprotokoll för pre-grade

Analysen är exakt så bra som bilderna. Det här protokollet är inte pedanteri: varje
bild du hoppar över gör att en hel PSA-kriteriegrupp faller bort ur bedömningen, och
rapporten skriver då ut att den inte gick att bedöma.

## Vad varje bild låser upp

| Bild | Låser upp | Om den saknas |
|---|---|---|
| `front.jpg` | Centrering framsida (mätt optiskt), kantslitage, helhetsintryck | Inget går att bedöma alls |
| `back.jpg` | Centrering baksida, fläckar, wax stain | Baksidans centreringstak faller bort |
| `raking.jpg` | Ytrepor, print lines, roller lines, gloss | Ytan sätts till "ej bedömbar" och takas på 9 |
| `corner-tl/tr/bl/br.jpg` | Hörnskärpa och fransning | Hörnen sätts till "ej bedömbara" och takas på 9 |

Utan `raking.jpg` och hörnbilder kan verktyget alltså aldrig säga "10 trolig". Det är
med flit. Skillnaden mellan 9 och 10 sitter i just det de bilderna visar.

## Grundregler

1. **Inget plastfickeri.** Ta kortet ur sleeve och toploader. Plast ger reflexer,
   döljer kantslitage och skjuter centreringsmätningen fel.
2. **Kontrasterande enfärgad bakgrund.** Mörkgrå eller svart matt yta. Kortdetektionen
   letar efter kortets ytterkontur, och ett vitt kort på vitt bord hittas inte.
3. **Kortet ska fylla minst 60 procent av bilden.** Under 35 procent avbryter mätningen.
4. **Ingen blixt rakt på.** Den bränner ut folien. Använd fönsterljus eller två diffusa
   lampor från sidorna.
5. **Lås vitbalansen** om kameran tillåter det, och håll samma ljus genom hela batchen.
6. **Skarpt.** Tryck mot fokus, eller använd stativ. Oskärpa gör både yta och kanter
   obedömbara.

## De sju bilderna, per kort

### 1. `front.jpg` och 2. `back.jpg`
Kameran **rakt ovanifrån**, optiska axeln vinkelrät mot kortet. Det här är den enda
bilden där vinkeln är kritisk: centreringen mäts i pixlar, och lutar du kameran mäter
du fel. Lägg kortet plant, håll telefonen parallellt med bordet, hela kortet i bild med
lite marginal runtom. Jämnt diffust ljus, inga skuggor över kortet.

**Efter baksidan vänder du tillbaka till framsidan.** Strökljusbilden och alla fyra
hörnmakron tas på framsidan.

Verktyget rättar perspektiv upp till ungefär 12 graders lutning, men gissa inte på det.
Rakt ovanifrån är gratis.

### 3. `raking.jpg`
Samma vy som framsidan, men **byt ljuset**: en enda punktljuskälla lågt från sidan, cirka
20 till 30 grader över kortets plan. Släckt takbelysning. Ytan ska glittra och repor ska
kasta skuggor. Bilden kommer se ful ut, det är meningen. Ta gärna två, en med ljuset från
vänster och en från höger, och döp dem `raking.jpg` och `raking-2.jpg`.

### 4 till 7. `corner-tl.jpg`, `corner-tr.jpg`, `corner-bl.jpg`, `corner-br.jpg`
Makro på varje hörn. Så nära du kommer med bibehållen skärpa, hörnet ska fylla en rejäl
del av bilden. Har telefonen makroläge, använd det. Här letar vi vitning, fransning och
avrundning, allt i storleksordningen tiondels millimeter.

## Mappstruktur

Ett kort per mapp, mapparna i en batch:

```
tcg_webshop/intake/2026-08-03/
  charizard-base-4/
    front.jpg
    back.jpg
    raking.jpg
    corner-tl.jpg
    corner-tr.jpg
    corner-bl.jpg
    corner-br.jpg
    card.json          (valfri, se nedan)
  umbreon-vmax-alt/
    ...
```

Filnamnet styr rollen. Prefixen `front`/`fram`, `back`/`bak`, `raking`/`snedljus`/`angle`,
`corner`/`horn` känns igen. Övriga bilder skickas med som extra underlag.

## `card.json`, valfri

Lägg den bredvid bilderna om du redan har comp-priser, så räknas EV ut i rapporten:

```json
{
  "raw_sek": 1200,
  "psa10_sek": 6500,
  "psa9_sek": 2400,
  "psa8_sek": 1500
}
```

Utan den blir rapporten en ren skickbedömning utan ekonomi.

## Kör

```bash
cd ~/projects/tcg_webshop
python3 -m pregrade.run --batch 2026-08-03
```

Rapporter hamnar i `reports/2026-08-03/`, en markdown per kort plus `summary.csv` med
hela batchen. Behandlade mappar flyttas till `intake/_processed/`.

Vill du bara ha centreringen, snabbt och utan modellanrop:

```bash
python3 -m pregrade.run --batch 2026-08-03 --no-vision
```
