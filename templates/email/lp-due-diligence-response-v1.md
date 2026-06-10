# LP Due Diligence Response — Standard Template v1

**使用情境**：對方（經紀商、機構客戶）在正式 onboarding 前要求對 xSyphon 作為 LP 進行供應商盡職調查
**客戶類型**：ASIC / FCA / MAS 等受監管機構
**語氣**：Professional, data-led, factual — 這是正式商業回覆，不是 sales pitch
**注意**：⚠️ 具體 spread 數字、信用條款、保證金要求必須由商業/合規團隊確認後再填入，不要自行填寫

---

## 變數列表

- `{{prospect_name}}` — 對方公司名稱（e.g. Zircon Sydney）
- `{{contact_first_name}}` — 對方聯絡人名字
- `{{contact_title}}` — 對方職位
- `{{my_name}}` — 你的名字
- `{{my_title}}` — 你的職位
- `{{doc_delivery_date}}` — 預計正式文件包交付日（e.g. "by end of this week"）
- `{{commercial_team_contact}}` — 商業/合規團隊聯絡人（負責具體報價）
- `{{kyc_status_note}}` — KYC 進度說明（e.g. "我們已確認可透過 email 接收文件"）

---

## Template

**Subject**: xSyphon — Response to Due Diligence Questionnaire | {{prospect_name}}

Dear {{contact_first_name}},

Thank you for the revised questionnaire. We appreciate the effort to align the scope with the liquidity and execution services under discussion. We are pleased to respond below.

---

### Corporate & Regulatory Information

**Corporate structure**: xSyphon Ltd is a standalone liquidity aggregation entity. The company is wholly independent and does not operate a retail brokerage.

**Regulatory licence**:
- Issuer: Financial Services Commission of Mauritius (FSC)
- Licence No.: GB25204632
- Compliance framework: aligned with MiFID II and UK FCA standards for institutional counterparties

**Principal operating entity**: xSyphon Ltd

**Years in operation**: [FILL IN — confirm with internal team]

**Key jurisdictions serviced**: xSyphon services institutional counterparties globally, with a primary client base across APAC and EMEA. Client onboarding is subject to the local regulatory requirements of each counterparty's jurisdiction. Our FSC (Mauritius) licence and MiFID II-aligned operational framework support institutional relationships across most major markets. [FILL IN — if the prospect is from a specific jurisdiction, add a line confirming prior experience with that regulator, e.g. ASIC, FCA, MAS]

---

### Liquidity & Product Coverage

**Available asset classes**:
- G10 FX Majors: EUR/USD, GBP/USD, USD/JPY, AUD/USD, USD/CAD, USD/CHF, NZD/USD
- EM FX: USD/CNH, USD/HKD, USD/TRY, USD/BRL, USD/ZAR, USD/MXN (and others)
- Precious Metals: XAU/USD, XAG/USD, XPT/USD — and **XAU/CNH** (exclusive product, 50g minimum lot)
- Crypto CFDs: BTC/USD, ETH/USD, USDT/USD, USDC/USD, BCH/USD (cash-settled, 24/7)
- Indices CFDs and Energy CFDs: available — full instrument list provided in the Liquidity Specification Sheet

**Liquidity source composition**: aggregated from 12+ Tier-1 bank and non-bank LPs. Exact composition shared under NDA upon request.

**Number of underlying liquidity providers**: 12+

**Typical market depth**: institutional-grade, multi-tier book. Depth data by instrument available in the Liquidity Spec Sheet.

**Available trading sessions**:
- FX, Metals, Indices, Energy: 24/5
- Crypto CFDs: 24/7

---

### Pricing & Commercial Structure

**Indicative spreads**: Instrument-level indicative spreads for major FX pairs, Gold, Silver and major indices are included in the attached Liquidity Specification Sheet and sample commercial proposal. Final pricing is subject to volume tier and credit arrangement.

**Commission structure**: Mark-up / pip-based, tiered by monthly notional volume. Flat platform fee + tighter spread available for higher-volume accounts.

**Volume-based pricing tiers**: [FILL IN — confirmed by commercial team at proposal stage]

**Minimum monthly commitments**: [FILL IN — confirm with commercial team; typically none for qualified counterparties]

**Credit line availability**: Available subject to standard credit assessment and ISDA/CSA or equivalent documentation.

---

### Execution Quality

**Execution model**: Agency (pure STP/NDD). xSyphon does not take a principal position against client flow.

**Last Look policy**: **Zero Last Look** — all quotes are firm. No re-quotes, no asymmetric rejection.

**Average fill rate**: 99.7%

**Average rejection rate**: <1%

**Slippage statistics**: Available upon request; positive and negative slippage data tracked and reportable.

**Performance during major volatility events**: [FILL IN — request specific event data from risk team, e.g. NFP, Fed rate decisions. Highlight uptime and fill consistency.]

---

### FIX & Connectivity

**FIX API specifications**: FIX 4.4 (primary institutional protocol)

**Connectivity options**:
- FIX 4.4 — co-located institutional clients
- REST API + WebSocket — custom platform and web app integration
- MT4 Bridge — existing MetaTrader 4 brokers
- MT5 Gateway — multi-asset MT5 brokers
- Custom GUI — available for institutional trading desks

**Hosting / co-location**: LD4 (London), NY4 (New York), TY3 (Tokyo), SG1 (Singapore)

**Supported bridge providers**: [FILL IN — confirm compatibility with PrimeXM, OneZero, and others with technical team]

**Latency benchmarks**:
- Median execution latency: 5ms (co-located clients)
- Region-specific benchmarks available in technical documentation

**Redundancy and failover**: Multi-region co-location with automatic failover. Full redundancy details in SLA documentation.

---

### Credit & Risk Framework

**Margin requirements**: [FILL IN — subject to counterparty credit assessment]

**Margin call procedures**: [FILL IN — outlined in ISDA/CSA or equivalent agreement]

**Liquidation policy**: [FILL IN — confirm with risk team]

**Credit exposure limits**: Set on a per-counterparty basis following credit review.

**Negative balance protection**: [FILL IN — confirm applicability for institutional counterparty structure]

---

### Reporting & Operational Support

**Reporting tools**: Real-time and end-of-day reporting available via portal and API. Trade-level, instrument-level and counterparty-level reports supported.

**Trade reconciliation support**: Yes — dedicated operational support for post-trade reconciliation.

**Dedicated account management**: Yes — each client is assigned a dedicated relationship manager and technical onboarding contact.

**Technical support hours**: 24/5 during market hours; escalation procedures documented in SLA.

**Escalation procedures during market events**: Documented in SLA; direct escalation path to senior risk desk available during high-volatility periods.

---

### Documentation Package

The following documents are being prepared and will be delivered {{doc_delivery_date}}:

- [ ] Corporate profile
- [ ] Liquidity Specification Sheet (instrument list, typical spreads, depth)
- [ ] FIX API documentation
- [ ] Service Level Agreement (SLA)
- [ ] Sample commercial proposal
- [ ] Onboarding requirements and timeline (typically 5–10 business days post documentation)

---

### Regarding KYC Submission

We understand there was difficulty accessing the KYC portal link. {{kyc_status_note}}. Please send your KYC documents directly to [KYC_EMAIL] and copy me at [YOUR_EMAIL]. We will confirm receipt and update you on the review timeline.

---

We look forward to progressing this discussion. Should you have any questions on the above or wish to arrange a technical call with our connectivity team, please do not hesitate to reach out.

Kind regards,
{{my_name}}
{{my_title}}
xSyphon

---

## 使用注意事項

1. **`[FILL IN]` 標記的欄位**在發送前必須由商業/技術/合規團隊確認並填入
2. **具體 spread 數字**不要口頭承諾，放在 Liquidity Spec Sheet 附件
3. **信用條款**（margin call、liquidation policy）需合規團隊過目
4. **Bridge provider 相容性**（PrimeXM、OneZero 等）需技術團隊確認
5. 發送前附上已有的文件（Corporate Profile、Liquidity Spec Sheet、FIX doc）

## Changelog
- v1 (2026-06-10): initial draft, triggered by Zircon Sydney due diligence request
