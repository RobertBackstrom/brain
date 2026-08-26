---
name: project_image_intake
description: "Bildintag från telefonen - Drive-mappen Bilder_Inbox dräneras till /drop-lagret, OCR + vision ger sidecars, sökbara i RAG som source=drops. Första stället att leta efter en skärmdump eller referensbild."
metadata:
  node_type: memory
  type: project
---

Byggt 2026-08-20 (db-307). Efterföljare till db-299, vars telefonväg fastnade på att
iOS-genvägen var för krånglig. Löst med kvitto-intagets form i stället: spara till en
Drive-mapp.

**Detta är FÖRSTA stället att leta efter en bild.** Skärmdumpar, foton från omvärlden,
konstreferenser, UI-reffar.

```
rag_search("vad bilden föreställer", source="drops")
```

Sök på **innehåll, inte filnamn** - filnamnen är rena tidsstämplar. Varje träff bär
`local_path` i frontmatter, så du kan öppna själva bilden med Read.

**Intag (bokmärkt i Drive-appen):** `Bilder_Inbox` `1FxJGfsxnCOAWNbWb327Wm_JiAVUkwHEl` i
Roberts My Drive. Roten = otaggat. Valfri undermapp = projekttagg via mappnamnet, matchat
mot alias-listan i `image-intake.json`. `_processed` `1cLOUD7sx-ujxAt9oSGAP4qWDZ3-MBBpf` och
`_failed` `1ObKkcvgsNnwfzZKwxZTyz2VxGEpvgX3Y` är reserverade.

**Medvetet INTE en undermapp till `Kvitton_Inbox`:** den rotens klassificerare sveper och
skickar icke-kvitton till `_needs_review/` med Discord-ping, alltså rakt in i
bokföringsflödet. Se [[project_receipt_intake]].

**Kedjan:** timer var 5:e minut -> nerladdning till det befintliga `/drop`-lagret
(`assistant/uploads/drop/`, så drop.html och alla `/uploads/drop/<fil>`-URL:er lever vidare)
-> OCR (tesseract, `swe+eng`, psm 1) -> vision (Sonnet via claude-CLI, boxen har ingen
ANTHROPIC_API_KEY) -> sidecar `.md` i `uploads/drop-index/` -> RAG:s filbevakare inom ~30 s.

**Sidecaren är hela poängen.** RAG kan inte läsa en JPEG. Utan sidecar är bilden osökbar,
oavsett vilken väg den kom in.

**Fyra vägar in, ett lager.** Drive-vägen (telefonen), mail-till-sig-själv, bokmärket
`/drop`, och `POST /api/drop`. De tre senare skriver rakt in i `uploads/drop/` utan att veta
om sidecars, så varje körning sveper upp bilder som saknar en. Steady-state-kostnaden är noll.

**Projektgissning:** mappen vinner alltid över modellen. En gissning måste peka på ett känt
slug och nå konfidensgolvet (0,60) för att sättas, och märks då `project_guessed: true`. En
förkastad gissning skrivs ändå ut i sidecarens brödtext, så fritextsökning når den även när
projektfiltret inte gör det.

Config är `assistant/image-intake.json` - redigera den, inte koden. Full doc i
[[image_intake]]-skillen.
