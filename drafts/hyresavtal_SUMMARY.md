# Rental Agreement (Hyreskontrakt) - Work Summary

**Date**: 2026-04-14  
**Agent**: CorpBot  
**Ticket**: gen-008-hyreskontrakt  
**Status**: Blocked on input (needs_input: true)

---

## What I've Done

### 1. Created Comprehensive Swedish Office Lease Template
**File**: `drafts/hyresavtal_kontor_czp_draft.md`

Created a complete, legally compliant Swedish commercial office lease agreement (hyresavtal för lokal) following **Jordabalken chapter 12** (Land Code) requirements.

The template includes all standard sections:
- Parties and premises description
- Rental period (both fixed-term and indefinite options)
- Rent amount and payment terms
- Deposit provisions
- Maintenance responsibilities
- Termination clauses
- Insurance requirements
- Move-in/move-out protocols
- Breach remedies
- Swedish law compliance

All specific details that need to be filled in are marked with **[BRACKETS]**.

### 2. Researched Swedish Commercial Lease Law
- Studied Jordabalken requirements
- Identified key differences from residential leases
- Documented standard notice periods and legal requirements
- Found reliable Swedish lease template resources

### 3. Added Cross-Project Learnings
Updated `agents/memory/admin_learnings.md` with:
- Swedish commercial lease legal framework
- Standard clauses and structure
- Deposit mechanics
- Template resources
- Context discovery pattern for future rental agreements

---

## What's Blocking Completion

The template is ready but **10 critical details** are missing. See the ticket for full list, but key ones are:

### Critical Information Needed:

1. **Who is the landlord?** (Name, org nr, contact details)
2. **Exact premises details** (Unit number, floor, exact sqm)
3. **Monthly rent amount** (Confirm the 10,000 SEK/month from K2C P&L)
4. **What's included in rent?** (Electricity, internet, cleaning, etc.)
5. **Contract start date** (The ticket was due 2026-03-25 - is this already active?)
6. **Landlord's bank details** for payments
7. **Is this already set up informally?** (Office costs show in Apr P&L)

### Context Clues:
- CZP registered office: Timmermansgatan 43, 118 55 Stockholm
- K2C P&L allocates 10,000 SEK/month for office (Apr-Jun 2026)
- No existing lease found in Google Drive
- Could be: traditional lease, coworking space (WeWork-style), or shared office

---

## Next Steps for Robert

### Immediate:
1. **Answer the 10 questions** in the ticket (or confirm if office is already set up)
2. **If it's a coworking space** (e.g., WeWork, United Spaces), the "lease" might be simpler - just a membership agreement
3. **If it's a traditional lease**, gather landlord details and review the template

### After Details Provided:
1. Fill in all [BRACKETED] fields in the draft
2. Upload to **Google Drive** in CZP corporate folder:
   ```bash
   node assistant/gdrive-upload.js drafts/hyresavtal_kontor_czp_draft.md "CZP/Legal/Contracts"
   ```
3. Review with landlord
4. Both parties sign (use DocuSeal if digital signature needed: robert@aurorapunks.com)
5. File signed copy in CZP corporate records

---

## Template Quality Notes

The template I created:
- ✅ Complies with Jordabalken chapter 12
- ✅ Includes all essential Swedish commercial lease clauses
- ✅ Provides both fixed-term and indefinite options
- ✅ Bilingual (Swedish with English section headers)
- ✅ Protects both landlord and tenant interests
- ✅ Ready to customize and use

**Sources consulted**:
- [Enkla Juridik](https://enklajuridik.se/foretagsjuridik/hyresavtal-lokal/)
- [Wonder.legal](https://www.wonder.legal/se/modele/hyresavtal-kontor)
- Företagarna, Itkett AB templates

---

## Open Questions

1. **Is the office space already occupied?** The due date was March 25, but today is April 14. K2C P&L shows office costs starting April. This suggests either:
   - The lease was set up informally and just needs documentation
   - It's a coworking membership (simpler than traditional lease)
   - It's still pending and causing issues

2. **Is Timmermansgatan 43 the correct address?** This is CZP's registered office, but is it actually a physical workspace or just a registration address?

---

**Status**: Waiting for Robert's input to proceed.
