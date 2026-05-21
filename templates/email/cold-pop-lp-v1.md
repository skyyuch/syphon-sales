# Cold Email — Prime-of-Prime / LP Buyer (English) v1

**Audience**: Hedge funds, prop desks, mid-sized brokers shopping for LP
**Use when**: 對方明顯在找新的 LP（招聘 LP relationship manager、近期 LP 切換新聞）
**Tone**: Direct, institutional, focus on liquidity depth + onboarding speed

---

## Variables
- `{{first_name}}`
- `{{company}}`
- `{{trigger}}` — 為什麼現在找你（招聘 / 新聞 / 引薦）
- `{{volume_tier}}` — 估計對方規模
- `{{instrument_hook}}` — 對方最在意的產品（例 XAU/CNH for 中國市場 broker）

---

## Template

**Subject**: {{instrument_hook}} liquidity for {{company}}

Hi {{first_name}},

{{trigger}} — got me thinking you might be evaluating LP options.

Quick context on xSyphon:
- $1B+ daily notional, 12+ Tier-1 prime brokers aggregated
- 5ms median execution, zero last look, 99.7% fill ratio
- 5-10 business days from signed agreement to live
- FSC Mauritius regulated, MiFID II / FCA compliant
- {{instrument_hook}} is one of our deeper books

I'd skip the deck. Happy to share a tailored connectivity proposal within 24 hours if you can share rough volume profile.

Or 15 min if easier: {{cta_link}}

Best,
{{my_name}}

---

## Variants by instrument hook
- China-focused: "XAU/CNH liquidity for {{company}}"
- LATAM: "USD/BRL + USD/MXN streaming for {{company}}"
- Crypto-curious: "Crypto CFDs on the same FIX as your FX"
- Pure FX: "Tier-1 FX aggregation for {{company}}"

## Changelog
- v1 (2026-05-20): initial draft

## Performance
| Sent | Opens | Replies | Reply Rate |
|------|-------|---------|------------|
| 0    | 0     | 0       | -          |
