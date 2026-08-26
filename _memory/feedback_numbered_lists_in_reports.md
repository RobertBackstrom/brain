---
name: Numbered lists, not bullets, in reports
description: All multi-point output to Robert must use numbered lists (1, 2, 3) so he can respond to individual points by number. Bullet points are not OK.
type: feedback
originSessionId: 188abd35-612b-4791-9526-7d7b8af629f9
modified: 2026-08-14T11:47:32.082Z
---
Aldrig använd bullet-listor i rapporter, statussvar, eller andra strukturerade output till Robert. Alltid numrerad lista (1, 2, 3, ...).

**Why:** Robert läser rapporter och svarar ofta på enskilda punkter separat. Med numrerade listor kan han säga "punkt 3 — gör så här" istället för att behöva citera hela bullet-meningen. Bullets gör det mycket svårare att referera till en specifik del av output.

**How to apply:**
- Alla "Återstår"-listor, "Risker"-listor, "Nästa steg"-listor, "Frågor"-listor → numrerade.
- Alla flerstegsplaner, beslutspunkter, alternativ-listor → numrerade.
- Även när listan är inom en bredare paragraf — om det är fler än ett alternativ/punkt, numrera.
- Undantag: kodexempel, filsökvägs-listor, tagg-listor och liknande där referensbarhet inte är poängen — där är bullets eller komma-separerat OK.
- I markdown-dokument som är för intern användning (memon, agent learnings, wiki) gäller samma regel — Robert läser även dem och vill kunna referera per punkt.

**Gäller ALLA instruktioner — förstärkt 2026-08-12.** Robert: *"what is next step, give it to me in a
number list (always do that with instruction)"*. Varje gång jag ger honom något att **göra** — nästa
steg, bootstrap-kommandon, en runbook, en åtgärdslista — ska det vara en numrerad lista, aldrig
prosa och aldrig rubriker med kommandoblock löst hängande under. Han står ofta vid en annan maskin
och betar av dem i ordning, så numret är både referens och position i sekvensen. Kodblock får ligga
inuti ett numrerat steg, men steget självt måste ha ett nummer.

**Källa:** Robert 2026-05-04 (RLR-arbetet, Lawyer-agenten), förstärkt 2026-08-12 (DevOps,
Tailscale-bootstrap av Petters maskin — jag gav bootstrap-stegen som prosa och blev tillsagd).
