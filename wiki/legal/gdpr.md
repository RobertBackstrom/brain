---
title: GDPR / Data Protection
owner: Lawyer agent
status: skeleton
last_reviewed: 2026-05-03
primary_sources: GDPR (EU) 2016/679, dataskyddslagen (2018:218), imy.se
---

# GDPR / Data Protection

Reference. Not legal advice. Real lawyer required for any breach response or IMY interaction.

## Roles

- **Controller** — determines purposes and means of processing.
- **Processor** — processes on behalf of controller.
- **Joint controller** — decides jointly with another party.

For Robert's projects: typically controller for own platforms (Death Board, Hive, cc-hive). Processor when running automation on behalf of clients (rare, but check).

## Platform-side PII inventory

Death Board, Hive, cc-hive — what PII flows where. Fill as audited.

- (Pending audit — load when Robert prioritizes.)

## DPA (Data Processing Agreement)

- Required when acting as processor for a controller (Art. 28 GDPR).
- AP AB master DPA — does it exist? Verify in `czp_legal/templates/`.

## Subject rights

- Access, rectification, erasure, portability, objection, restriction.
- Response deadline: 1 month, extendable to 3 months for complex requests.

## Breach notification

- IMY: within 72 hours of becoming aware (Art. 33).
- Data subjects: without undue delay if high risk (Art. 34).

## IMY (Integritetsskyddsmyndigheten)

- Swedish supervisory authority.
- Sanction levels — up to 4% of global turnover or €20M.
- Common enforcement areas: cookie consent, tracking pixels, employee monitoring, public sector PII handling.

## Kvarliggande persondata efter konkurs/upplösning - radera, inte migrera; vakta de facto-ansvar

En "deletedUsersData"-typ av kvarliggande kopia (f.d. anställdas/användares persondata) i konkurs-/upplösningssammanhang:

- **Radera, inte arkivera.** Utgångspunkt: en kopia som bara ligger kvar saknar typiskt rättslig grund (`art. 6.1`); berättigat intresse (`art. 6.1 f`) bär inte "i-fall-vi-behöver". Lagringsminimering (`art. 5.1 e`) + ändamål uppfyllt (`art. 17.1 a`) -> ska raderas. Att kopiera in mappen i en ny, snyggare struktur förlänger aktivt en olaglig lagring - gör saken värre.
- **Enda delmängd som får/ska bevaras:** bokföringsknuten data (löneunderlag m.m.) via rättslig förpliktelse (`art. 6.1 c`), där raderingsplikten är undantagen (`art. 17.3 b`) pga bokföringslagens 7-åriga arkiveringsplikt (`BFL 7 kap. 2 §`). Bevara den oförändrad och separat, radera resten.
- **Skarpaste risken - de facto personuppgiftsansvar.** När ett bolag upplöses via konkurs upphör det som juridisk person och kan inte längre vara personuppgiftsansvarigt. Om ett kvarvarande koncernbolag sitter på en kopia riskerar det bli **de facto ansvarigt** för föräldralös data det saknar grund att behandla. Omorganisering/kopiering är precis det som utlöser den risken.
- **Praktik:** datakarta -> (i) bokföringsknutet: bevara oförändrat/separat, radera efter arkiveringstid; (ii) övrigt: radera, migrera inte. Rör konkursbolag i pågående konkurs -> stäm av med förvaltaren innan radering. Svensk överlagring `dataskyddslagen (2018:218)`; tillsyn IMY.

(AP Drive-migrering, db-256; lawyer 2026-07-10)

## Robert's positions

(Pin here when established.)

## Open questions

(Track here when discovered.)
