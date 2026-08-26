---
name: reference_rag_content_coverage
description: "What RAG makes searchable: mail full; Drive now indexes ALL files by filename + extracts PDF/Office/Sheets(all tabs)/pptx + OCRs scanned PDFs & images on admin/legal drives."
metadata:
  node_type: memory
  type: reference
---

# RAG content coverage - what is searchable, and how

The RAG index (`assistant/rag.db`, tools `mcp__rag__rag_search` / `board.runatyr.games/api/wiki/search`) as of 2026-07-21. "Indexed" now means at minimum filename-searchable; most documents are full-content searchable.

## Mail - fully content-searchable
Work (`gmail`, ~61k msgs back to 2021) + personal (`gmail-personal`, ~23k back to 2014), re-synced ~every 30 min by `rag-external-sync.timer`.

## Drive - three tiers (2026-07-17/21 overhaul)
1. **Full content:** Google Docs/Slides; **Google Sheets - ALL tabs** (was first-tab-only; now xlsx-export -> SheetJS per tab); text-layer PDFs; uploaded **.xlsx/.xls/.xlsm/.ods** (SheetJS), **.docx** (mammoth), **.pptx/.pptm** (jszip), **.doc** (word-extractor, OLE-sniffed), **.ppt** (cfb text atoms; .pot text-decoded), **.odt/.odp** (jszip ODF), **.rtf** (stripper, image-hex removed); text/md/csv/json; SIE bookkeeping exports.
2. **OCR'd content (admin/legal drives only):** scanned/signed **PDFs** AND scanned **images** (jpg/png/tiff) with no text layer are OCR'd (tesseract swe+eng) on the OCR-enabled drives. Off those drives, a scanned PDF/image is filename-only.
3. **Filename-only stub (every other file):** images off OCR drives, video, audio, archives, octet-stream, etc. get a row whose content includes the filename -> FTS-searchable by name, `noEmbed` (zero embed budget, no vector). This deliberately replaced the old db-076 "drop pure binaries entirely" behavior. Only true junk (.DS_Store/Thumbs.db/desktop.ini) gets no row.

**OCR-enabled drives** (`CFG.OCR_DRIVE_IDS`, env `RAG_OCR_DRIVE_IDS`): financials `0AMBeS-GYxphsUk9PVA`, Aurora Punks Admin `0AM6InBfd-HOMUk9PVA`, Aurora Punks `0ACOk67Zhg9zlUk9PVA`, CZP `0AAaQFbRZFdpKUk9PVA`, Platform Sales `0AOyWGnEm_iycUk9PVA`, legals `0AI_AdW5gwShNUk9PVA`, Runatyr `0AJbB97KnFqgnUk9PVA`.

## Practical implications
- **Everything is at least filename-searchable now** - if an agent "can't find" a file, search its likely filename, then its content.
- **Size cap 30MB** (raised from 5MB, 2026-07-21): the old cap silently skipped 847 real documents as `too_large` - mostly large PDFs (614) and pitch decks. Extracted text is capped at 1M chars per file (`GDRIVE_MAX_EXTRACTED_CHARS`) so one huge workbook can't blow the embed budget.
- **Multi-tab Sheets:** all tabs captured. Sheets over Google's ~10MB xlsx-export cap fall back to first-tab CSV.
- **Scanned docs:** content-searchable only on the OCR drives (PDF or image). Elsewhere = filename only; move to an admin/company drive to get OCR.
- **Still stubs (no extractor):** Outlook .msg, VS .suo, and other true binaries; image scans OCR can't read. Every common document format is now content-searchable.
- **Backfill/retry CLIs** (`node assistant/rag-external-indexer.js ...`): `--retry-ocr` (scanned PDFs), `--retry-xlsx`, `--retry-docx`, `--retry-sheets` (all-tabs), `--retry-legacy` (.doc/.ppt/.rtf/.odt), `--retry-toolarge`, `--gdrive` (full re-walk = applies everything incl. image-OCR + filename stubs). The 30-min timer keeps new files current automatically.
- Extractor deps: `xlsx` (SheetJS), `mammoth` (docx), `jszip` (pptx/ODF), `word-extractor` (.doc), `cfb` (.ppt), poppler+tesseract (OCR, swe+eng). `indexContent({noEmbed})` = FTS row without a vector.
