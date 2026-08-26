---
name: feedback_numbered_questions
description: "Varje fråga till Robert ska vara numrerad och tydligt märkt, så att han kan svara i nummerföljd. Gäller både prosa och frågeverktyget."
metadata:
  node_type: memory
  type: feedback
---

När flera frågor ställs till Robert **måste varje fråga vara numrerad och tydligt märkt**, så att
han kan svara "1. ... 2. ... 3. ..." i nummerföljd utan att gissa vilken fråga som är vilken.

Robert påpekade detta 2026-08-19 efter att ha fått tre frågor i frågeverktyget plus flera
resonemang i prosan, utan numrering. Han kunde inte referera till dem i sitt svar.

**Så här:**
- Numrera frågorna **1, 2, 3** och behåll numreringen konsekvent genom hela turen. Om frågorna
  ställs i `AskUserQuestion`, låt rubriken eller frågetexten bära numret ("1. Vilket konto...").
- Ställ inte samtidigt öppna följdfrågor i prosan som konkurrerar med de numrerade. Kontext och
  fynd hör hemma i prosan, **frågorna bara i den numrerade listan**.
- Håller han ordningen i svaret ("1. ... 2. ...") ska svaren mappas tillbaka på samma nummer i
  nästa svar, så spåret går att följa.

**Varför:** Robert svarar ofta på flera frågor i ett svep, i löpande text. Utan nummer blir det
tvetydigt vilket svar som hör till vilken fråga, och risken för feltolkning i ett
bokförings- eller avtalsärende är för hög.

**Numret räcker inte — varje punkt som kräver Roberts handling ska bära sin destination.**
Utökat 2026-08-19: OpenSign kunde inte skicka mail för att ett Google-applösenord hade dött. Jag
skrev "väntar på ett nytt applösenord från dig" utan att säga **var** han hämtar det, och han fick
själv fråga vad det ens var för lösenord och om det gällde inloggning. Fördröjningen var helt
onödig, för svaret var en URL.

Varje punkt som blockerar på Robert ska alltså innehålla:
1. **Numret**, så han kan svara i ordning.
2. **Exakt destination** — full URL, filsökväg eller "Zero Trust → Access → Applications", inte
   "i Googles inställningar". Klickbart där det går.
3. **Vilket konto eller kontext** som ska användas, när det är tvetydigt (`robert@aurorapunks.com`
   och inte det privata, vilket bolag, vilken guild).
4. **Vad han ska göra med resultatet** — klistra in här i chatten, spara i LastPass, godkänna.
5. **Vad som händer sen**, i en halv mening, så han vet om det är klart efter hans steg.

Om han behöver ställa en följdfråga för att kunna utföra punkten var punkten inte färdigskriven.

Kompletterar [[feedback_ask_via_question_ui]] (frågor går alltid via frågeverktyget, aldrig som
inline-punkter) och [[feedback_numbered_lists_in_reports]] (rapporter och fynd numreras).
