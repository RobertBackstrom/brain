---
name: reference_fortnox_access
description: "Fortnox är åtkomligt autonomt via Playwright (creds i .env, betrodd enhet) — dra SIE/bokföring utan att be Robert logga in."
metadata: 
  node_type: memory
  type: reference
  originSessionId: e6e77877-9a22-46d3-88a8-a57e5f6d42ec
---

Fortnox (CZP/AP/APDS, Amer Alsalek) går att nå **autonomt från VPS:en** sedan 2026-06-23 — be inte Robert logga in manuellt först.

- **Creds:** `FORTNOX_USERNAME` (personnummer) + `FORTNOX_PASSWORD` i `assistant/.env`; registrerat i `secrets_registry.md` under `fortnox.login`.
- **Login:** använd **`node assistant/fortnox-login2.js`** (2026-07-13). `fortnox-login.js` (org.) går INTE längre — den betrodda profilen landar nu direkt på password-sidan (username förifyllt) så det gamla metodval-klicket ("Lösenord") timeout:ar. `-login2` hanterar båda flödena, fyller lösenord + Enter, MFA via `/tmp/fortnox-mfa-code.txt` om betrodd enhet gått ut. Sparar **betrodd enhet** i `assistant/.fortnox-profile` → ingen MFA på ~90 dagar.
- **`fortnox-login.js` är nu en shim** som delegerar till `fortnox-login2.js` (2026-07-13) — gamla namnet funkar igen.
- **Läsa kundreskontra (öppna kundfakturor, READ-ONLY):** `node assistant/fortnox-kundreskontra.js` — välj tenant via KLICK (direkt lobby-URL studsar), lista på `${base}/kf/invoicelist` (webapp-ui iframe), fakturadetalj+historik på `${base}/kf/invoice/<nr>` → "Visa historik". TOTALT/SALDO-kolumnerna = brutto INKL moms. Detaljer i CorpBot-learnings 2026-07-13.
- **Ladda ned faktura-PDF (READ-ONLY):** `node assistant/fortnox-invoice-pdf.js "<bolagsnamn>" <faktnr> <utpath.pdf>` (byggd 2026-07-13). Öppnar `/kf/invoice/<nr>`, avfärdar mall-popup, klickar **Förhandsgranska** → en `report/pages/loading.html`-popup genererar PDF:en asynkront och streamar den från `/api/documentsender/document-v1/preview/{F|C}/<nr>?fid=...` (content-type application/pdf; `fid` sätts av en POST `/api/kf/invoice/?preview=1`). Scriptet fångar den URL:en och HÄMTAR OM den via den autentiserade contexten (in-page-bodyn äts av pdf.js). Hanterar F (faktura) och C (kreditfaktura) automatiskt. Verifierat: CZP faktura 33 + kreditfaktura 48 för APDS-bevakningen.
- **Dra SIE:** `node assistant/fortnox-sie-download.js "<bolagsnamn>" <utpath>` (SIE-typ 4, helår, draget via UI; tenant-id är per-session, härleds ur lobby-URL).
- **Session-watchdog:** `node assistant/fortnox-probe.js` (byggd 2026-07-13, db-229) — READ-ONLY hälsokoll som laddar `.fortnox-profile`, går till tenant-select och verifierar att company-select nås (== login2:s `ALREADY_LOGGED_IN`). HEALTHY = tyst (exit 0) + förnyar session-cookien som bieffekt; LAPSED/ERROR = larm till `DISCORD_HEALTHZ_WEBHOOK` som namnger Fortnox + felläge + reauth-receptet nedan (exit 1). Triggar ALDRIG SMS (skickas först efter password-submit, vilket proben inte gör) och hänger aldrig (kör inte login2:s 10-min MFA-vänta). Flaggor: `--no-alert` (dry-run), `--json`. Schema: systemd-user-timer `fortnox-probe.timer` (Mon+Thu 06:30 Stockholm, enabled). Repo-kopia av unit i `assistant/systemd/`.
- **Betrodd enhet håller längre än 90 dgr:** cookies i `.fortnox-profile` (`fnox.id.session`, `fnox.id.device`, `fdid`) sattes 2026-06-22 och giltiga t.o.m. 2027-08 (förnyas vid varje lyckad login). Headless-login funkade utan MFA 2026-07-13. **Om en headless-körning ändå fastnar på `id.fortnox.se`/`mfa`:** Robert måste göra EN interaktiv reauth — kör `node assistant/fortnox-login2.js` (håller sessionen levande ~10 min), be Robert om den ALLRA SENASTE SMS-koden och skriv den till `/tmp/fortnox-mfa-code.txt` (`echo <kod> > /tmp/fortnox-mfa-code.txt`); scriptet matar in den, sparar om betrodd enhet → nästa 90+ dgr headless igen. Be aldrig om koden i förväg (varje ny session skickar en färsk kod).
- **Viktigt:** Fortnox REST API stödjer INTE SIE-export (borttaget i v3.1.0) → browser-automation är enda vägen. AP saknar räkenskapsår 2026 (bara 2025) → AP bokförs via CZP.

Detaljer + huvudboksmetodik i CorpBot-learnings (`agents/memory/admin_learnings.md`, 2026-06-22/23). Schemaläggning = [[project_the_assistant]] via db-229. Se även [[feedback_secrets_registry]].
