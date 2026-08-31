---
name: feedback_author_pass_all_mail
description: "Varje mailutkast går genom The Author innan det skapas i Gmail. Ingen längd-, mottagar- eller språkgräns, gäller alla agenter."
metadata:
  node_type: memory
  type: feedback
---

**Robert 2026-08-31: "se till att alla mail drafts from nu görs av the author."**

Varje Gmail-utkast ska ha passerat The Authors röstpass innan det skapas. Inga undantag för korta
svar, interna mottagare, svenska mail eller "det här är bara en bekräftelse".

**Varför:** Robert granskar utkast i Gmail och skickar dem själv, ofta inom minuter. Ett utkast som
hoppat över passet är därför inte ett utkast, det är ett mail på väg ut i fel röst. Det som utlöste
regeln var Xbox-mailet till Reed Hunt samma dag: sakligt korrekt, men 400 ord långt och fullt av
fraser som positionerar innehållet i stället för att säga det ("Worth noting alongside it", "One
thing does follow from it", "For completeness on"). Roberts omdöme: *"wall of text, massor av
onödiga AI slop fraser."* The Author kortade det till 280 ord med rättelsen i första meningen.

**How to apply:**
- Ordningen är: skriv utkastet på din egen modell, skicka den nästan färdiga texten till The Author
  (Fable, Agent-verktyget), skapa Gmail-utkastet av det som kommer tillbaka. Aldrig tvärtom, och
  aldrig "jag skapar utkastet nu och röstpassar sen".
- Briefen till The Author ska bära mottagare, kanal, trådhistorik och vad mailet ska åstadkomma.
  Utan det kör passet på generisk register och du får tillbaka nästan samma text.
- Gäller huvudassistenten och varje spawnad eller namngiven agent. CorpBot, BizDev och PM skriver
  inte mail direkt till Drafts.
- Undantaget i [agents/_registry.md](agents/_registry.md) för "trivial internal text" gäller
  Discord-enradare och interna anteckningar, aldrig mail.
- Saknas en personprofil i `skills/voice/people/` för mottagaren, säg det till Robert efteråt och
  erbjud att bygga en. Det är exakt vad som hände med Reed Hunt.

Relaterat: [[writing_voice_robert]] · [[feedback_no_em_dashes]] · [[feedback_no_hype_language]] ·
[[feedback_verify_draft_sent]]
