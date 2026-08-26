---
name: reference_codev_mandate_pattern
description: "Annoying partner-formuleringen: hur AP tar produktägarskap utan att en teknisk grundare som vägrar co-dev känner sig fråntagen sin kod"
metadata:
  node_type: memory
  type: reference
  modified: 2026-08-26
---

Återkommande låsning i co-dev-affärer: den tekniska grundaren vägrar co-dev därför att
hen läser det som att någon annan tar över koden. På Disposable Corps sa medgrundaren
till utgivaren att det enda sätt det kunde fungera på var om det tekniska stödet
"only listens to him", och affären stod stilla i en månad på det.

**Formuleringen som löste det** (Robert till Anthony Wong, LUG, 2026-08-26, accepterad
direkt i en delad kanal där utgivarens grundare satt med):

> "I will be the annoying partner who asks for fixes and make sure they understand its
> needed, then we discuss solutions and if Paul says he wanna do it we set a deadline for it."

**Varför det fungerar:** det delar upp ägarskapet längs en gräns utvecklaren kan acceptera.
AP äger **produktbesluten, scopet och tidplanen**. Utvecklaren behåller **implementationen**.
Ingen blir fråntagen sin kod, men fixlistan får en motpart som driver den och sätter datum.
Det är starkare än "AP tar över" i praktiken, eftersom takeover-formuleringen aktiverar
precis den invändning som blockerar.

**Hur det tillämpas:** när en plan hänger på att designbeslut faktiskt kan fattas, skriv
arbetssättssektionen som rollfördelning i stället för som mandatkrav. Erbjud dessutom en
kort betald genomlysningsfas som kan starta utan att frågan är avgjord, så affären inte
står still medan någon ska vinna diskussionen.

**Kvarvarande risk att skriva in:** modellen har ingen sanktion om utvecklaren missar
överenskomna deadlines. Testa den i liten skala i genomlysningsfasen innan lång löptid
binds upp. Sett på [[project_disposable_corps]]; besläktat med [[bizdev_learnings]].
