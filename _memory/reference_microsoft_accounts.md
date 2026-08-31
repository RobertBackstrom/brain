---
name: reference_microsoft_accounts
description: "Microsoft-kontotopologin för AP/CZP: vilket konto som äger vad i Partner Center, royaltyportalen och SupplierWeb, plus vendornumren och de fem entitetssträngarna."
metadata:
  node_type: memory
  type: reference
---

# Microsoft: vilket konto äger vad

Fem system, olika inloggningar, olika behörighetsmodeller. Att blanda ihop dem är den vanligaste
tidsförlusten i Xbox-ärenden. Uppdaterad 2026-08-31.

## Kontona

| System | Konto som fungerar | Not |
|---|---|---|
| **Partner Center** (produkterna, butiksnamnet, avtalen) | `finance@aurorapunks.com`, **ägarkonto** | `robert@aurorapunks.com` är Developer-only och kan inte ändra roller. Hektors `andreassonhektor@gmail.com` är legacy Owner-MSA, inte enda vägen. |
| **Royalty Statement Portal** (`royalty.microsoft.com`) | `robert@aurorapunks.com`, **work/school-kontot** | finance@ tillagd som administratör 2026-08-31 men får `UnAuthorizedAccess` tills kontot accepterat registreringsinbjudan till finance@-brevlådan. |
| **SupplierWeb / payee** | hanteras av `p2pvisup@microsoft.com` | CZP saknar supplier-profil och vendor-ID, en ny måste skapas. |
| **RoyCare** (portalsupport) | `roycare@microsoft.com` | Lägger inte till kontakter själva, hänvisar till portalens egna administratörer. Eskalering: `escalroy@microsoft.com`. |
| **ID@Xbox** (kontoägande, TLA, entitet) | `idam@xbox.com`, teamaliaset | Reed Hunt svarar därifrån. Eskalering: `XBOXPubEsc@microsoft.com`. |

**`robert@aurorapunks.com` är TVÅ Microsoft-konton**, ett work/school i Entra och ett personligt,
på samma adress. Inloggningen frågar vilket du menar. Royaltyportalen vill ha work-kontot. Det här
är sannolikt orsaken till flera tidigare "inloggningen krånglar"-rundor.

## Vendornumren

| Vendor | Bolag | Läge |
|---|---|---|
| **0003066327** | Aurora Punks Development Services AB | Aktiv payee. Saldo 140,16 USD, under minimibeloppet 200 USD. Kontrakt 7781010. |
| **0003039381** | White Lines Black Spaces AB | Legacy men publicerar fortfarande statements. Saldo 16,85 USD. Kontrakt 7267337. |

Microsofts precedens vid entitetsbyte är **en ny supplier-profil, inte en namnändring**. Därför
finns två vendornummer parallellt.

## De fem entitetssträngarna, och de är inte överens

Partner Centers company account säger **White Lines Black Spaces AB**. Avtalen säger **WLBS AB dba
Aurora Punks**. SupplierWeb säger **APDS AB**. Legacy-vendorn säger WLBS. Och **Entra-tenantens
visningsnamn säger Aurora Punks Development Services AB**, vilket bara syns när man registrerar en
inloggningsmetod. Alla fem ska rättas vid entitetsbytet till CZP, och den sista glöms alltid bort.

**Juridisk person och publisher display name är skilda fält.** Det förstnämnda står på Legal
info-sidan och går att ändra. Det sistnämnda är butiksvänt, går inte att ändra efter registrering,
och är anledningen till att kontot med spelen ska behållas och döpas om i stället för att
produkterna flyttas. Xbox-butiken visar "Published by Atomic Elbow, Aurora Punks".

## Automation

`assistant/ms-session.js` (inloggning med TOTP-MFA, profil per konto, `account: 'royalty'|'finance'`),
`msrsm-royalty-reports.js` (hämtar statements), `msrsm-user-admin.js` (portalens användarlista),
`ms-totp.js`. Creds i `assistant/.env` som `MS_ROYALTY_*` (robert@) och `MS_FINANCE_*` (finance@),
metadata i `secrets_registry.md`. Statementhistoriken ligger i `aurora_punks/royalty/xbox/`.

Relaterat: [[project_apds_czp_rights_chain]] · [[project_sir_whoopass]] ·
[[reference_steam_partner_accounts]] · [[reference_ap_contractor_mail]]
