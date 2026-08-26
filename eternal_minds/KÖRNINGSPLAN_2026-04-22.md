# Eternal Minds AB Signeringsflöde — Körningsplan 2026-04-22

**Status:** Väntar på Roberts svar för (1) signerarmejladdresser och (2) väg-val (A eller B)

**Deadline:** 2026-05-07 (14 dagar från EGM-datum 2026-04-23)

**Tid kvar:** 16 dagar (båda vägar passar)

---

## 📝 Dokument redo för signering

Alla 6 dokument ligger som Google Docs i GDrive-mappen:  
**Folder:** CZP → Projects_2 → Eternal Minds AB → Deliverables → Bolagsverket 2026-04-23  
**Folder-ID:** 1eRr48v92fYO8zECRwiwG8ms9wqyTroWF

**Dokument som kräver signering:**
1. **01_underskrift_per_capsulum** — medgivande till per capsulum-format
   - Signeras av: Bibbi Wikman, Robin Hofström
   - Antal signaturer: 2

2. **03_röstlängd** — röstberättigade aktieägare
   - Signeras av: Bibbi Wikman, Robin Hofström
   - Antal signaturer: 2

3. **04_stammoprotokoll** — protokoll från skriftligt beslut
   - Signeras av: Bibbi Wikman, Robin Hofström
   - Antal signaturer: 2

4. **05_konstituerande_styrelseprotokoll** — val av VD, firmateckning
   - Signeras av: Robin Hofström, Johan Robert Bäckström
   - Antal signaturer: 2

5. **07_samtycke_robin_vd** — Robins medgivande till VD-roll
   - Signeras av: Robin Hofström
   - Antal signaturer: 1

**Total signaturer behövda:** 9 (från 3 personer: Bibbi, Robin, Robert)

---

## 🔄 VAL A: AUTOMATISERAD (om db-046 klarar)

**Förutsättning:** Robert har genererat DocuSeal API-nyckel + webhook-secret och konfigurerat VPS `.env`

**Steg:**
1. CorpBot hämtar PDFer från GDrive
2. Kallar `docuseal.createSubmissionFromPdf` för varje dokument
3. DocuSeal skickar signeringslänkar till Bibbi, Robin, Robert
4. Webhook uppdaterar em-001-ticket när signeringarna är klara
5. CorpBot hämtar signerade PDFer automatiskt

**Tidsåtgång:** 1-2 dagar (signerare behöver tid på sig)

**Blocker just nu:** Robert måste konfigurera DocuSeal API-nyckel + webhook

---

## 🔄 VAL B: MANUELL (kan starta nu)

**Steg:**

### 1. Exportera PDFer från Google Docs (30 min)
```
För varje dokument:
1. Gå till https://drive.google.com/drive/folders/1eRr48v92fYO8zECRwiwG8ms9wqyTroWF
2. Öppna dokumentet
3. File → Download → PDF
4. Spara med rätt namn
```

**Filnamn efter export:**
- 01_underskrift_per_capsulum.pdf
- 03_röstlängd.pdf
- 04_stammoprotokoll.pdf
- 05_konstituerande_styrelseprotokoll.pdf
- 07_samtycke_robin_vd.pdf

### 2. Ladda upp till DocuSeal och skapa signeringsflöde (30 min)
```
1. Logga in på https://docuseal.com med robert@aurorapunks.com
2. Create submission (eller use Template om den finns)
3. För varje PDF: markera signerare och skicka
```

**Signerare per dokument:**
- 01, 03, 04, 07: Bibbi Wikman + Robin Hofström
- 05: Robin Hofström + Johan Robert Bäckström

### 3. Följa upp signeringarna (1-2 dagar)
```
1. DocuSeal skickar email-notiser när varje signer signerar
2. Du kan följa status i DocuSeal UI
3. Hämta signerade PDFer när alla klart
```

### 4. Spara signerade PDFer (30 min)
```
1. Ladda ner från DocuSeal
2. Spara i samma GDrive-mapp eller subfolder "_Signed"
3. Namngivning: <original>_SIGNED.pdf
```

**Tidsåtgång:** 30 min setup + 1-2 dagar signering

**Blocker just nu:** Behöver Bibbi:s och Robins mejladresser

---

## ✅ CHECKLISTA FÖRE VAL

- [ ] Roberts svar mottaget: mejladresser + väg-val
- [ ] Om väl A: DocuSeal API-nyckel + webhook konfigurerad
- [ ] Om väl B: PDFer exporterade

---

## 📌 TIDSLINJE

| Datum | Vad | Status |
|-------|-----|--------|
| **2026-04-22** (idag) | Väg-val från Robert | ⏳ VÄNTAR |
| **2026-04-22 eller senare** | Signeringsflöde startas | 🔄 NÄSTA STEG |
| **2026-04-24–26** | Signeringarna genomförda | 📝 DRIFT |
| **2026-04-27–05-07** | Anmälan till Bolagsverket | 📋 SISTA VECKAN |

---

**Nästa handling:** Robert svarar, CorpBot fortsätter med vald väg.
