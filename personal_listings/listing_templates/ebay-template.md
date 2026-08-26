# eBay Listing Template (English)

Used by Lister to draft `drafts/<sku>/ebay.md`. Lister fills the placeholders with comp data and vision intake; Robert reviews when threshold-gated.

## Title (max 80 chars)
`<Brand> <Model> <key spec> <condition tag>`

Example: `Be Quiet! Pure Base 500 Gaming PC – Intel i5-12400F RTX 4060 8GB 32GB RAM – Used`

## Price
- **Buy It Now:** `<asking_price_eur or _usd>` (region per app setup)
- **Best Offer:** consider enabling for items > €200; auto-decline below 80% of BIN
- **Condition:** New | Used – Like New | Used – Good | Used – Acceptable | For parts or not working

## Category
`<eBay category id from category_thresholds.yml mapping>`

## Item specifics
Fill all available specifics (Brand, Model, MPN, Storage, GPU, RAM, etc.) — eBay search ranking depends on it.

## Description

```
<2-3 sentences on what the item is. No buzzwords.>

Specifications:
- <bullet 1>
- <bullet 2>
- <bullet 3>

Condition: <short, honest condition note. Mention any visible flaws.>

Shipping: <method + tracked yes/no + handling time>
Payment: eBay managed payments
Returns: <policy>

Smoke-free home, ships from Sweden.
```

## Shipping
- Default: PostNord with tracking, EU + UK
- Heavy items (>2kg): Schenker / Bring; specify dimensions and weight
- Combine shipping for multi-item buyers

## Photos
- Minimum 4 photos. First photo is the hero — full item, neutral background, good light.
- Detail shots of any flaws.
- Spec labels / serial numbers (when relevant) — crop or redact personal info.

## Voice rules
- No hype words ("must-have!", "rare!", "amazing!").
- Be brief. Facts > sales pitch.
- Always end with "Smoke-free home, ships from Sweden."
- English throughout. International audience — avoid Swedish-specific shipping abbreviations.
