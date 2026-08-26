#!/usr/bin/env python3
# Build AP AB IP & licensing asset list (multi-tab, formula-driven) for AR 2025.
import sys
sys.path.insert(0, "/home/assistant/projects/assistant")
from make_xlsx import write_xlsx
F = lambda s: ('f', s)

oversikt = [
    ["AURORA PUNKS AB (559256-9718) - IP- & LICENSTILLGÅNGAR: ÖVERSIKT"],
    ["Underlag till ÅR 2025. Sammanställd av CorpBot 2026-06-22. UTKAST för Roberts granskning. Belopp i SEK."],
    [""],
    ["TVÅ VÄRDERINGSLINSER (summeras INTE ihop - två sätt att se samma tillgångar):"],
    ["  Bokfört  = vad som faktiskt står i AP:s balansräkning enligt K3 (det som går in i ÅR)."],
    ["  Indikativt = icke-lagstadgad kommersiell uppskattning per titel (förhandling/återköp/nedskrivning). Bokförs ej."],
    [""],
    ["Kategori", "Flik", "Bokfört värde (SEK)", "Indikativt värde (SEK)", "Kommentar"],
    ["IP i AP:s balansräkning (5M-posten)", "A", F("='A. AP IP i BR'!C8"), F("='A. AP IP i BR'!D8"),
        "Aggregerad Not 3-post. Spelportföljtitlarna (flik B) är KOMPONENTER av denna - ej additiva."],
    ["Spelportfölj-IP per titel (indikativt)", "B", "(komponent av 5M)", F("='B. Spelportfolj-IP'!G26"),
        "Kommersiell uppskattning per titel; fyll på tomma celler i flik B."],
    ["APDS-IP hos CZP (återköpsrätt)", "C", "(utanför AP BR)", F("='C. APDS-IP hos CZP'!E9"),
        "Potentiellt förvärv till köpeskilling (TBC). Ankaret saknas - bekräfta belopp."],
    ["Licens-/IP-avtal (fordringar, memo)", "D", F("='D. Licens- IP-avtal'!G14"), "",
        "Avtalsbelopp/fordringar. Runatyr-fordran 5M representerar RLR (finns även i B) - ej additivt."],
    ["Finansiella anläggningstillgångar (memo, ej IP)", "E", F("='E. Finansiella innehav'!C9"), "",
        "Koncernaktier + koncernfordran + minoritetsposter. För helhetsbild."],
    [""],
    ["SUMMERINGAR (formeldrivna - uppdateras när du fyller i detaljflikarna):"],
    ["A) Bokfört på AP:s BR (IP + finansiellt)", "", F("='A. AP IP i BR'!C8+'E. Finansiella innehav'!C9"), "",
        "Kontroll: ska = Summa anläggningstillgångar AP ÅR 2024 = 7 965 397."],
    ["B) Samlat indikativt IP-värde (portfölj)", "", "", F("='B. Spelportfolj-IP'!G26+'C. APDS-IP hos CZP'!E9"),
        "Portföljsyn: titel-indikativt + ev. APDS-återköp. Många celler tomma = fyll på."],
    [""],
    ["OBS: Bokfört och Indikativt adderas INTE ihop. Tomma indikativa celler = mänsklig input krävs (TBC). Se flik 'Metod & Scope'."],
]

metod = [
    ["METOD & SCOPE - Aurora Punks AB IP-/licenstillgångar (underlag ÅR 2025)"],
    ["Sammanställd av CorpBot 2026-06-22 för Amer Alsalek (redovisning). UTKAST - för Roberts granskning först."],
    [""],
    ["SCOPE (bekräftat med Robert 2026-06-22)"],
    ["1. Aurora Punks AB (moderbolaget) egen IP + licensavtal, inkl. Robot Lord Rising (RLR)."],
    ["2. IP köpt ur APDS konkursbo som nu ligger hos CZP Holding AB - AP har rätt att återköpa till köpeskillingen (flik C)."],
    ["3. WLBS/APDS historiska bokförda värden = proveniens/kostnadsbas, EJ AP-moderbolagets tillgångar (båda dotterbolagen i konkurs)."],
    [""],
    ["VÄRDERINGSGRUND - två kolumner (bekräftat: 'båda')"],
    ["Bokfört värde = anskaffningsvärde minus ack. avskrivningar/nedskrivningar enligt K3 (BFNAR 2012:1). Källa = ÅR-noter."],
    ["Indikativt värde = icke-lagstadgad kommersiell uppskattning. Saknas marknadskomp anges historiskt aktiverat utvecklingsvärde (kostnadsbas) eller lämnas tomt (TBC)."],
    ["Alla värdeceller är inmatningsbara; delsummor och översikt är formler som räknar om vid ändring."],
    [""],
    ["VIKTIGT FÖR ÅR 2025"],
    ["- AP-moderbolagets enda IP-post i BR 2024-12-31 = 5 000 000 kr (Not 3), ett aggregat. Enskilda titlar ej separat upptagna. Flik A bryter ned posten."],
    ["- Avskrivningstid 3 år linjärt (Not 1); årets avskrivning 2024 = 87 860 kr. Bedöm fortsatt avskrivning + ev. nedskrivning 2025."],
    ["- Uppskrivning 1 743 741 kr gjordes 2024 (uppskrivningsfond) - kräver fortsatt hållbarhetsprövning ÅRL 4:6."],
    ["- HÄNDELSE EFTER BALANSDAGEN: APDS i konkurs jan 2026 (efter räkenskapsåret 2025) - upplys i ÅR 2025; påverkar fordrings-/koncernvärdering."],
    ["- Runatyr IP-avtal: tillägg 2025-03-28 kristalliserade fordran 5 000 000 kr (RLR + Elric) - UNDER räkenskapsåret 2025. Flik D."],
    [""],
    ["ÖPPNA PUNKTER (kräver Roberts/Amers input)"],
    ["- CZP:s köpeskilling för APDS-konkurs-IP (återköpsankaret) = TBC. Ej hittad i index/Drive/mail - bekräfta belopp + avtal (flik C)."],
    ["- Ägarkonflikt 'Vessels of Decay': AP 100% i Intangibles-listan vs 'IP-ägare Neon Artery' i WLBS-ÅR. Bekräfta."],
    ["- Ägarkonflikt 'Hooja': extern klient i Intangibles-listan vs 'Own IP 50%' i WLBS-ÅR. Bekräfta."],
    ["- Org.nr: Drive-registret listar AP som 559088-2245; auktoritativt enligt ÅR är 559256-9718. Använd 559256-9718."],
    [""],
    ["KÄLLOR (Drive-ID / referens)"],
    ["AP ÅR 2024 (inlämnad) - 1Zk8q8KP8j_QMqYgmn_132hZmRMqEld56 (Not 3 IP-post)"],
    ["AP ÅR 2023 - 1It3u0Nhc8s9giyvdAsTHLZWw5b959Dpe"],
    ["WLBS ÅR 2023 - 1KgcRrdFmUxb2g-gZ9-j6HpdZ11mWm-tu (Not 3/4/5)"],
    ["Aurora Punks Intangibles - 16v1SrmKMoU8rG08ep1pIXH5hoEOZACDyeB8GHzEoBNI"],
    ["WLBS Immaterialrättigheter - 1WHWzvsn8Gi6_mn6y-UKcrioHB5awJD1UvAD842oYpvc"],
    ["IP-Avtal Runatyr-AP (+ tillägg 2025-03-28) - 19CaIVH9ushq7OtYsWfchjMgtqyiFueOfE4dXrx-3MmA"],
    ["WLBS-konkursbo -> APDS överlåtelseavtal (88 000 kr) - 1BHKOVCE2_2j5vHoRd2Z5cjvyJouqalxD"],
    ["Kravframställan APDS konkursbo (RLR+Elric) - gmail-personal thread 19ac07ee5cb06343"],
    ["RLR IP-epic (ägandekedja) - assistant/followups/rlr-000-epic.md"],
]

tabA = [
    ["A. AURORA PUNKS AB - IP I MODERBOLAGETS BALANSRÄKNING (Not 3, 2024-12-31)"],
    [""],
    ["Komponent", "Beskrivning", "Bokfört värde 2024-12-31 (SEK)", "Indikativt värde (SEK)", "Antagande / Kommentar", "Källa"],
    ["Ingående anskaffningsvärde (äldre)", "Koncessioner, patent, licenser, varumärken - äldre förvärv (sannolikt AP-varumärket + tidiga licenser)", 439301, "", "Oförändrat 2023->2024. Ej uppdelat per titel i ÅR - bekräfta innehåll.", "AP ÅR 2024 Not 3"],
    ["Inköp 2024 (aktiverat eget arbete)", "Aktiverat arbete för egen räkning 2024 - AP-finansierad vidareutveckling (RLR/Elric m.m. per IP-avtal Runatyr)", 3000000, 3000000, "Indikativt = kostnadsbas; realiserbart värde sannolikt lägre. Kopplad till fond för utvecklingsutgifter.", "AP ÅR 2024 RR + Not 3"],
    ["Ackumulerade avskrivningar", "Linjärt 3 år; ack. -183 042 (varav 2024 -87 860)", -183042, "", "Fortsätt avskriva 2025 om ej nedskrivning sker.", "AP ÅR 2024 Not 3"],
    ["Uppskrivning 2024", "Uppskrivning av anläggningstillgång till uppskrivningsfond", 1743741, "", "Kräver fortsatt hållbarhetsprövning ÅRL 4:6 inför 2025.", "AP ÅR 2024 Not 3 + EK"],
    ["= Redovisat värde immateriella (AP)", "Summa = anskaffning - avskrivning + uppskrivning", F("=SUM(C4:C7)"), F("=SUM(D4:D7)"), "Kontroll: ska = 5 000 000 mot BR.", "AP ÅR 2024 BR"],
    [""],
    ["Jämförande: AP ÅR 2023 redovisat värde immateriella", "", 344119, "", "Steg 344 119 -> 5 000 000 under 2024 (inköp 3M + uppskrivning 1,74M).", "AP ÅR 2023/2024"],
]

tabB = [
    ["B. SPELPORTFÖLJ-IP (Aurora Punks-gruppen)"],
    ["'Bokfört i AP' = enskilda titlar ej separat upptagna i moderbolagets ÅR (=0 här); värdet ingår i 5M-posten (flik A). 'Aktiverat i WLBS' = historisk utvecklingskostnad i dotterbolaget (nu i konkurs) = kostnadsbas för indikativt värde."],
    [""],
    ["Titel", "Typ", "Ägare / Ownership", "Status", "Aktiverat i WLBS (hist, SEK)", "Bokfört i AP (SEK)", "Indikativt värde (SEK)", "Kommentar", "Källa"],
    ["Aurora Punks", "Varumärke / Brand", "AP 100%", "Aktiv", "", 0, "", "Koncernens varumärke. Ingen marknadskomp.", "Intangibles-lista"],
    ["Robot Lord Rising (RLR)", "Spel-IP + seriealbum", "Runatyr -> AP (fordran 5M, ej formellt överlåten)", "Released (Steam) + Fortnite + serie (Caurette)", "", 0, 5000000, "Kostnads-/fordringsbas (Runatyr-fordran 5M; upparbetat 6,79M). Realiserbart lägre. Ägandekedja ej slutförd.", "IP-avtal + RLR-epic"],
    ["Chenso Club", "Spel-IP", "AP 100%", "Released, intäkter inkommer", "", 0, "", "IP ägs av AP, distribuerad via WLBS/APDS.", "Intangibles + WLBS-lista"],
    ["BlockEm", "Spel-IP", "AP 100%", "Live (Steam 2022, browser 2026)", 1235400, 0, 1235400, "Indikativt = historiskt aktiverat. Låg löpande intäkt -> realiserbart lägre.", "WLBS-lista"],
    ["Beyond the Filter", "Spel-IP", "AP (utv.avtal Meta<->WLBS)", "Utveckling pausad", 4731307, 0, "", "Stort aktiverat belopp men pausad -> väsentlig nedskrivningsrisk. Bekräfta Meta-avtalet.", "WLBS-lista"],
    ["Agents of Concordia", "Spel-IP", "AP 100%", "Ej angivet", "", 0, "", "Status oklar - bekräfta.", "Intangibles-lista"],
    ["Vessels of Decay", "Spel-IP", "AP 100% (KONFLIKT: WLBS-ÅR anger Neon Artery)", "Ej angivet", "", 0, "", "Ägarkonflikt - bekräfta. Källkod 50% WLBS.", "Intangibles + WLBS-ÅR"],
    ["Ooglians", "Spel-IP", "AP 100%", "Intäkter inkommer", "", 0, "", "IP ägs av AP, distribuerad via WLBS.", "Intangibles + WLBS-lista"],
    ["Windswept Interactive", "Studio / VR", "AP 100% (avknoppad 2023)", "Avknoppad till eget bolag", "", 0, "", "VR-team brutet ut -> Windswept Interactive AB (Behold +2M). Kontrollera status.", "WLBS ÅR 2023"],
    [""],
    ["-- Titlar med extern IP-ägare (EJ AP-ägd IP; endast intäktsström / aktiverad utveckling) --"],
    ["Gravity Circuit", "Produkt (rev share 10%)", "Extern klient (Domesticated Ants)", "Released, intäkter", 681449, 0, "", "IP ägs externt. Endast intäktsström - ej AP IP-tillgång.", "WLBS-lista + ÅR"],
    ["Hooja", "Produkt", "Extern klient (KONFLIKT: WLBS-ÅR 'Own IP 50%')", "Released, intäkter", 1729555, 0, "", "Ägarkonflikt - bekräfta; om AP-andel finns kan indikativt värde gälla.", "WLBS-lista + ÅR"],
    ["1993 Space Machine", "Produkt", "Extern klient", "Released", "", 0, "", "Helt avskrivet.", "WLBS-lista"],
    ["1993 Shenandoah", "Produkt", "WLBS 100%", "Released (Switch)", "", 0, "", "Bekräfta nuvarande innehavare efter WLBS-konkurs.", "Intangibles-lista"],
    ["Ghost Signal", "Produkt (rev share)", "Fast Travel Games (utgivare)", "Released", "", 0, "", "WLBS rev share - ej IP-tillgång.", "Intangibles-lista"],
    ["Son of Dracula", "Källkod", "WLBS 100%", "Ej släppt", "", 0, "", "Outnyttjad källkod/tillgång.", "Intangibles-lista"],
    ["Sir Whoopass", "Produkt (co-dev)", "Atomic Elbow (IP)", "Co-dev rev share", "", 0, "", "Ej IP-tillgång.", "WLBS ÅR 2023"],
    ["Iron Evil", "Produkt (co-dev)", "Iron Evil (IP)", "Co-dev", "", 0, "", "Ej IP-tillgång.", "WLBS ÅR 2023"],
    ["Innsmouth (Nr89)", "Samarbete -> konvertibler", "Nr89 AB", "Konvertibler hamnar i AP", "", 0, "", "Konvertibler i moderbolaget AP - se flik E.", "WLBS ÅR 2023"],
    [""],
    ["DELSUMMA", "", "", "", F("=SUM(E5:E24)"), F("=SUM(F5:F24)"), F("=SUM(G5:G24)"), "Indikativt (G) summerar ifyllda celler; fyll på fler titlar.", ""],
]

tabC = [
    ["C. APDS-KONKURS-IP HOS CZP HOLDING AB - AP:s ÅTERKÖPSRÄTT"],
    ["Bakgrund: WLBS-konkursbo överlät verksamheten till APDS (88 000 kr, dec 2024). APDS i konkurs jan 2026. Enligt RLR-epic gör APDS-förvaltaren EJ anspråk på IP:t. Robert: IP ligger nu hos CZP; AP har rätt att återköpa till köpeskillingen."],
    [""],
    ["Post", "Detalj", "CZP köpeskilling (SEK)", "AP återköpsrätt", "Indikativt värde (SEK)", "Kommentar", "Källa"],
    ["APDS-konkurs-IP (samlat)", "Spel-IP/teknik som flödat WLBS -> APDS -> (konkurs) -> CZP", "", "Ja - till köpeskillingen", "", "ÖPPEN PUNKT: köpeskilling + överlåtelseavtal CZP<->APDS-konkursbo ej hittat i index. Bekräfta belopp/avtal. = återköpsankaret.", "Robert 2026-06-22 + RLR-epic"],
    ["Referens: WLBS-verksamhet (88k-affären)", "Tekniska tillgångar (bilaga 1) + inventarier; WLBS-konkursbo -> APDS", 88000, "(historisk, redan i APDS)", 88000, "Endast referens för storleksordning på konkurs-prissättning. Avser dec-2024-affären, EJ CZP-affären.", "Överlåtelseavtal WLBS"],
    ["Underliggande titlar (bilaga 1)", "Gravity Circuit, Hooja, 1993 Space Machine, Beyond the Filter, Chenso Club, BlockEm, Ooglians", "", "", "", "Blandad ägarbild (extern vs AP) - återköp bör specificera vilka rättigheter som faktiskt överlåts.", "Bilaga 1 WLBS-avtal"],
    [""],
    ["DELSUMMA (endast APDS-IP, exkl. referensrad)", "", "", "", F("=E5"), "Referensraden 88k (E6) ej inkluderad - avser annan affär.", ""],
]

tabD = [
    ["D. LICENS- & IP-AVTAL"],
    [""],
    ["Avtal", "Parter", "Datum", "Berörd IP", "Ekonomiska villkor", "Status", "Värde / fordran (SEK)", "Källa"],
    ["IP-/Samarbetsavtal Runatyr-AP", "Runatyr AB <-> Aurora Punks AB", "2023-06-29 (tillägg 2025-03-28)", "Robot Lord Rising + spel-licens Elric of Melniboné", "Uteblivet majoritetsförvärv -> skadestånd 5M som räntefritt lån; återbetalas via IP-överlåtelse RLR+Elric till AP", "Tillägg signerat; IP ej formellt överlåten", 5000000, "19CaIVH9ushq..."],
    ["Elric of Melniboné (spel-licens)", "Runatyr (licenstagare) -> AP", "Via ovan", "Spel-licens/option Elric of Melniboné", "Ingår i Runatyr-fordran ovan", "Knuten till Runatyr-överlåtelsen", "", "IP-avtal + RLR-epic"],
    ["Kravframställan APDS-konkursbo", "Runatyr (krav) -> APDS konkursbo", "2026-01-02", "RLR + Elric källkod/assets", "Faktura 2 (substansvärde) anmäld i bouppteckning", "Anmäld; förvaltaren gör ej IP-anspråk", "", "gmail 19ac07ee..."],
    ["RLR namngivelse / Dark Riviera-licens", "AP (licensgivare) -> Dark Riviera AB; förlag Editions Caurette", "Löpande", "RLR seriealbum (Vol 1 Deus ex Machina m.fl.)", "Publishing-/licensrelation", "Aktiv; namngivelse-ärende hanterat", "", "rlr-000-epic"],
    ["CoDev/CoPub - Ark Island", "AP <-> klient", "Ej daterat i utdrag", "Spel + 'Aurora Punks Tools' (verktygslicens)", "Co-dev/co-pub; AP licensierar egna verktyg icke-exklusivt", "Avtal finns", "", "CoDev_AP_ArkIsland"],
    ["CoDev/CoPub - Ballard (Few Shall Return)", "AP <-> Ballard Games", "Ej daterat i utdrag", "Spel + 'Aurora Punks Tools'", "Co-pub; Ballard exklusiv exploateringsrätt; AP behåller egna verktyg", "Avtal finns", "", "CoDev_AP_Ballard"],
    ["WLBS-konkursbo -> APDS (verksamhet)", "WLBS konkursbo <-> APDS", "2024-12-20", "Tekniska tillgångar + inventarier (bilaga 1-2)", "Köpeskilling 88 000 kr exkl. moms", "Genomfört/signerat", 88000, "1BHKOVCE2..."],
    ["WLBS-konkursbo -> APDS (fordran Nr89)", "WLBS konkursbo <-> APDS", "2024-12-20", "Fordran mot Nr89 Studios AB", "Överlåtelse av fordran", "Genomfört", "", "1XezFL6Fia..."],
    ["Andelsöverlåtelse Runatyr (Yasin)", "Yasin Hillborg -> CZP/Robert", "Under förhandling 2025", "500 aktier Runatyr; RLR-intäktsdelning", "Alt 1: 8% RLR-intäkt (cap 200k) / Alt 2: 25 000 kr kontant", "Under förhandling", "", "gmail Andelsöverlåtelse"],
    [""],
    ["DELSUMMA - avtalsbelopp/fordringar", "", "", "", "", "", F("=SUM(G4:G12)"), "Fordringar/avtalsbelopp - EJ additivt till IP-värden (Runatyr-fordran 5M = RLR som även finns i flik B)."],
]

tabE = [
    ["E. FINANSIELLA INNEHAV (MEMO - EJ IP, för helhetsbild)"],
    ["Finansiella anläggningstillgångar, ej immateriella rättigheter. Tas med så Amer ser hela bilden."],
    [""],
    ["Innehav", "Typ", "Bokfört värde 2024-12-31 (SEK)", "Kommentar", "Källa"],
    ["Andelar i koncernföretag (WLBS)", "Dotterbolagsaktier", 0, "Anskaffning 9 000 000, helt nedskrivet. WLBS i konkurs.", "AP ÅR 2024 Not 4"],
    ["Fordringar hos koncernföretag", "Koncernfordran (WLBS)", 42403, "Brutto 14 434 365, nedskrivet -14 391 962.", "AP ÅR 2024 Not 5"],
    ["Andra långfristiga värdepappersinnehav", "Minoritetsposter (Red Marmoset 15%, Upstream Arcade 15%, Northify ~7%, Eddaheim, Nr89-konvertibler m.fl.)", 2922994, "Specificera per innehav vid behov (apb-011 minoritetsaudit). Ej IP.", "AP ÅR 2024 Not 6 + structure_ownership"],
    [""],
    ["SUMMA finansiella anläggningstillgångar (AP)", "", F("=SUM(C5:C7)"), "Per AP ÅR 2024 BR (= 2 965 397).", "AP ÅR 2024 BR"],
]

sheets = [
    ("Oversikt", oversikt),
    ("Metod & Scope", metod),
    ("A. AP IP i BR", tabA),
    ("B. Spelportfolj-IP", tabB),
    ("C. APDS-IP hos CZP", tabC),
    ("D. Licens- IP-avtal", tabD),
    ("E. Finansiella innehav", tabE),
]

out = "/home/assistant/projects/aurora_punks/drafts/AP_IP_Licens_Tillgangslista_2025_UTKAST.xlsx"
write_xlsx(out, sheets)
print("WROTE", out)

import zipfile
from xml.dom import minidom
with zipfile.ZipFile(out) as z:
    for n in z.namelist():
        if n.endswith(".xml"):
            minidom.parseString(z.read(n))
    print("VALID parts:", len(z.namelist()))
