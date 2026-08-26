// Fill EIF ESG Portfolio reporting format with Aurora Punks AB data from allabolag.
// Preserves original styling via exceljs.
const ExcelJS = require('exceljs');
const path = require('path');

const SRC = path.join(__dirname, 'EIF ESG Portfolio reporting format v2.xlsx');
const OUT = path.join(__dirname, 'EIF ESG Portfolio reporting format v2 - Aurora Punks AB filled.xlsx');

// Column E = "PC #1" (portfolio company column).
// Reference period per form: 2025-01-01 to 2025-12-31.
// Source: allabolag.se (2024 figures — 2025 ÅR not yet filed).
const cells = {
  // 0.1 Company fundamentals
  'E16':  'Aurora Punks AB',                    // 0.1.1   Company name
  'E17':  '5592569718',                          // 0.1.2   Business identification number (Swedish org nr, no hyphen)
  'E18':  'EUID',                                // 0.1.2.1 Identification system (Sweden = part of EU BRIS register)
  'E20':  'Sweden',                              // 0.1.3   Country of domicile
  'E22':  'Sweden',                              // 0.1.4   Primary country of operations
  // 0.1.5 / 0.1.5.1 Other EU country — left blank (no substantial ops outside SE)
  'E28':  '58.21',                               // 0.1.6   NACE Rev 2.1 — Publishing of computer games
                                                 //         (SNI registered as 00000 "näringsgren saknas",
                                                 //          but verksamhet matches 58.21)
  'E30':  0,                                     // 0.1.7   FTEs end of current reporting year (2025) — 0 per allabolag
  'E32':  0,                                     // 0.1.8   FTEs end of previous reporting year (2024) — 0 per allabolag
  'E34':  0,                                     // 0.1.9   Annual gross revenue (MSEK) — 0
  'E36':  0,                                     // 0.1.9.1 inside EU
  'E38':  0,                                     // 0.1.9.2 outside EU
  'E40':  8,                                     // 0.1.10  Total balance sheet assets (MSEK) — 7,966 Tkr ≈ 8 MSEK (FY2024)
  'E42':  8,                                     // 0.1.10.1 inside EU (all SE)
  'E44':  0,                                     // 0.1.10.2 outside EU
  'E46':  0,                                     // 0.1.11   Turnover (MSEK) — 0
  'E48':  0,                                     // 0.1.11.1 inside EU
  'E50':  0,                                     // 0.1.11.2 outside EU
  'E52':  'SEK',                                 // 0.1.12   Currency
  'E54':  'N',                                   // 0.1.13   Listed
  // 0.1.13.1 ISIN — n/a, blank

  // 3.1 Founders still employed (Robert is sole AP founder still active)
  'E174': 1,                                     // 3.1.10 Total founders still employed
  'E176': 0,                                     // 3.1.11 Female
  'E178': 0,                                     // 3.1.12 Non-binary
  'E180': 0,                                     // 3.1.13 Other
  'E182': 1,                                     // 3.1.14 Male (Robert)

  // 4.1 Board composition (Mattias chair, Andreea, Robert)
  'E235': 3,                                     // 4.1.1 Total board members
  'E237': 1,                                     // 4.1.2 Female (Andreea)
  'E239': 0,                                     // 4.1.3 Non-binary
  'E241': 0,                                     // 4.1.4 Other
  'E243': 2,                                     // 4.1.5 Male (Mattias, Robert)
  // 4.1.6 Under-represented groups — Robert to confirm
  // 4.1.7 Independent board members — Robert to confirm (typical: Mattias + Andreea = 2)
};

(async () => {
  const wb = new ExcelJS.Workbook();
  await wb.xlsx.readFile(SRC);
  const ws = wb.getWorksheet('EIF ESG');
  for (const [addr, value] of Object.entries(cells)) {
    ws.getCell(addr).value = value;
  }
  await wb.xlsx.writeFile(OUT);
  console.log('Wrote:', OUT);
  console.log('Cells filled:', Object.keys(cells).length);
})().catch(e => { console.error(e); process.exit(1); });
