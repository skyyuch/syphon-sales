# Email Draft — Zircon Sydney Due Diligence Response
**草稿，發送前請確認所有 [FILL IN] 欄位**
**日期**: 2026-06-10
**收件人**: Eric Lim, Chief Dealing Officer, Zircon Sydney

---

**Subject**: xSyphon — Response to Revised Due Diligence Questionnaire

Dear Eric,

Thank you for the revised questionnaire and for the thoughtful reframing. We note your team has focused the evaluation appropriately on liquidity provision, FIX connectivity and execution services — we are happy to respond in full.

---

**Corporate & Regulatory Information**

xSyphon Ltd is a regulated liquidity aggregation entity operating exclusively in the institutional space. We do not operate a retail brokerage.

- **Regulatory licence**: Financial Services Commission of Mauritius (FSC), Licence No. GB25204632. Our operational framework aligns with MiFID II and UK FCA standards for institutional counterparty relationships.
- **Principal operating entity**: xSyphon Ltd
- **Years in operation**: Approximately 2 years
- **Key jurisdictions serviced**: xSyphon services institutional counterparties globally, with a primary client base across APAC and EMEA. Client onboarding is subject to the local regulatory requirements of each counterparty's jurisdiction. Our FSC (Mauritius) licence and MiFID II-aligned operational framework support institutional relationships across most major markets, including ASIC-regulated counterparties in Australia.

---

**Liquidity & Product Coverage**

- **Asset classes**: G10 FX, EM FX (incl. USD/CNH, USD/HKD), Precious Metals (XAU/USD, XAG/USD, XPT/USD, and our exclusive **XAU/CNH** product), Crypto CFDs (BTC, ETH, USDT, USDC, BCH — cash-settled). Full instrument list is in the attached Liquidity Specification Sheet.
- **Liquidity source composition**: Aggregated from Tier-1 prime brokers and regional banks. Detailed composition is available under NDA.
- **Market depth**: Institutional multi-tier book; depth data by instrument available in the specification sheet.
- **Trading sessions**: FX and Precious Metals — 24/5 (Sun 22:00 UTC to Fri 22:00 UTC); Crypto CFDs — 24/7

---

**Pricing & Commercial Structure**

Indicative spreads for major FX pairs, Gold and Silver are included in the attached Liquidity Specification Sheet and sample commercial proposal. Spreads on G10 majors start from 0.2 pips.

- **Commission structure**: USD 8 per million (FX and Precious Metals)
- **Volume-based tiers**: Subject to commercial discussion.
- **Minimum monthly commitments**: None for qualified counterparties
- **Credit line**: Not currently available. Accounts are operated on a pre-funded basis.

---

**Execution Quality**

- **Execution model**: Hybrid (A-Book / B-Book)
- **Last Look policy**: Zero Last Look. All quotes are firm.
- **Slippage**: Positive and negative slippage data tracked; available upon request.
- **Major volatility events**: Available upon request.

---

**FIX & Connectivity**

- **FIX protocol**: FIX 4.4
- **Connectivity options**: FIX 4.4 (primary, co-located), REST API, WebSocket, MT4 Bridge, MT5 Gateway
- **Supported bridge providers**: PrimeXM, OneZero, MT4 Bridge, MT5 Gateway
- **Co-location sites**: LD4 (London), NY4 (New York), TY3 (Tokyo), SG1 (Singapore)
- **Average execution latency**: 5ms
- **Uptime**: 99.98%
- **Redundancy and failover**: Fully redundant systems with automatic failover across data centres; full detail in SLA

---

**Credit & Risk Framework**

- **Aggregate NOP limit**: USD 150,000,000
- **Per-instrument NOP limits** (key products):
  - XAU/USD: USD 80,000,000
  - XAG/USD: USD 30,000,000
  - XAU/CNH: USD 10,000,000
  - USD/CNH: USD 10,000,000
  - USD/HKD: USD 10,000,000
- **Margin Call Level**: 130% (Net Equity / Margin Requirement, excluding extended credit)
- **Stop Out Level**: 50%
- **Margin schedule**: Tiered by open position size (Tier 1 < $20M / Tier 2 $20M–$50M / Tier 3 > $50M). Major G10 pairs at 0.5% / 1.0% / 2.0%; XAU/USD and XAU/CNH at 1.0% / 2.0% / 3.0%. Full margin schedule attached in Trading Conditions document.
- **Margin call and liquidation procedures**: Governed under our standard counterparty agreement (ISDA/CSA or equivalent), tailored per account following credit review.
- **Negative balance protection**: As an institutional liquidity provider operating on a margin framework, negative balance scenarios are structurally prevented by our Stop Out mechanism (50% level). Accounts are liquidated before equity reaches zero. Formal negative balance protection as defined under retail regulatory frameworks (e.g. ESMA guidelines) does not apply to institutional counterparty agreements.

---

**Reporting & Operational Support**

- **Reporting**: Real-time and end-of-day reports via portal and API; trade-level, instrument-level and counterparty-level views available
- **Reconciliation**: Dedicated operational support for post-trade reconciliation
- **Account management**: Each client is assigned a dedicated relationship manager and a technical onboarding contact
- **Support hours**: 24/5 during market hours; escalation procedures documented in the SLA
- **Onboarding timeline**: 5–10 business days post-documentation for standard FIX connectivity

---

**Documentation**

We are preparing the following package and will send across by [FILL IN — e.g. "end of this week" / specific date]:

- Corporate profile
- Liquidity Specification Sheet
- Trading Conditions (June 2026) — incl. margin schedule and NOP limits
- FIX API documentation
- Service Level Agreement (SLA)
- Sample commercial proposal
- Onboarding requirements checklist

---

**Regarding KYC Submission**

We understand there was difficulty accessing the portal link provided. Please send your KYC documents directly to [KYC_EMAIL] and copy me at [YOUR_EMAIL]. We will confirm receipt promptly and keep you updated on the review timeline.

---

We look forward to progressing the discussion. If it would be helpful, we are also happy to arrange a short technical call with our connectivity team to walk through FIX specifications and co-location options directly.

Kind regards,
[YOUR NAME]
[YOUR TITLE]
xSyphon
[YOUR EMAIL]
[YOUR PHONE]

---

## 發送前 Checklist

- [x] 確認 `Years in operation` — 約 2 年
- [x] 確認 Bridge provider：PrimeXM、OneZero、MT4 Bridge、MT5 Gateway
- [x] 重大波動事件數據 — 略過，改為「Available upon request」
- [x] Negative balance protection — 機構端以 50% Stop Out 機制取代，已說明
- [ ] 確認 KYC 收件 email 地址
- [ ] 確認文件包交付日期
- [ ] 附上文件：Liquidity Spec Sheet、Trading Conditions (June 2026)、FIX doc、Corporate Profile
- [ ] 發送前由你親自審閱全文
