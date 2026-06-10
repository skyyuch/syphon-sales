# xSyphon — Liquidity Provider

> 機構級流動性聚合商，毛里裘斯持牌
> **最後更新**：2026-06-10
> **資料來源標注**：
> - `[WEB]` = xsyphon.com 官網（2026-06-10 爬取）
> - `[PDF]` = Trading Conditions June 2026（William Liao 簽署）
> - `[CONFIRMED]` = 由 Sky 口頭確認
> - `[UNVERIFIED]` = 來源不明，對外使用前須核實

## One-liner
"AI-driven institutional liquidity for FX, precious metals, and crypto CFDs — aggregated from Tier-1 prime brokers, zero last look, 5ms execution." `[WEB]`

## 核心數據
| 指標 | 數值 | 來源 |
|------|------|------|
| Daily notional volume | $1B+ | `[WEB]` |
| Global offices | 6 | `[WEB]` |
| Avg. execution latency | 5ms | `[WEB]` |
| Uptime | 99.98% | `[WEB]` |
| Onboarding time | 5–10 business days | `[WEB]` |
| Fill ratio | 待內部確認 | `[UNVERIFIED]` |
| Rejection rate | 待內部確認 | `[UNVERIFIED]` |
| Tier-1 LP 數量 | 待核實（過往資料稱 12+） | `[UNVERIFIED]` |
| Co-location | LD4 / NY4 / TY3 / SG1 | `[WEB]` |

## 牌照
- **Issuer**: Financial Services Commission of Mauritius (FSC) `[WEB]`
- **License No.**: GB25204632 `[WEB]`
- **Compliance**: MiFID II, UK FCA frameworks `[WEB]`
- **地址**：Unit 13, Socota Phoenicia, Sayed Hossen Road, Phoenix, Mauritius `[PDF]`

## 產品涵蓋

### FX `[WEB]`
- **G10 Majors**：EUR/USD, GBP/USD, USD/JPY, AUD/USD, USD/CAD, USD/CHF（+ NZD/USD 待確認）
- **EM FX**：USD/CNH, USD/TRY, USD/BRL, USD/ZAR, USD/MXN, USD/HKD
- 最低 ticket size：1,000 units `[WEB]`

### Precious Metals `[WEB]`
- XAU/USD（Gold，from 1 oz）
- XAG/USD（Silver，from 50 oz）
- XPT/USD（Platinum）
- **XAU/CNH**（Gold vs Offshore CNH，from 50g — 獨家產品）`[WEB]`
- 支援 allocated / unallocated settlement `[WEB]`

### Crypto CFDs `[WEB]`
- BTC/USD, ETH/USD, USDT/USD, USDC/USD, BCH/USD
- Cash-settled，24/7
- ⚠️ 未出現在 Trading Conditions June 2026 PDF 中；官網有確認但需確認現行商業條款

## 交易時間 `[WEB]`
- FX + Precious Metals：24/5（Sun 22:00 UTC — Fri 22:00 UTC）
- Crypto CFDs：24/7（含週末）

## 連接方式 `[WEB]`
| Protocol | 用途 |
|----------|------|
| FIX 4.4 | 機構主流、co-located 客戶 |
| REST + WebSocket | Web app、客製平台 |
| MT4 Bridge | 既有 MT4 經紀商 |
| MT5 Gateway | MT5 多資產經紀商 |
| Custom GUI | 機構交易桌，可白標 |

**Co-location**：LD4 (London), NY4 (New York), TY3 (Tokyo), SG1 (Singapore) `[WEB]`

**支援 Bridge Providers**：PrimeXM, OneZero `[CONFIRMED]`（+ MT4 Bridge / MT5 Gateway 自有）

## 定價 `[PDF]` `[WEB]`
- **Commission**：USD 8 per million（FX + Precious Metals，all-in）`[PDF]`
- **Spreads**：G10 主要貨幣對從 0.2 pips 起 `[WEB]`
- **Volume tier**：Subject to commercial discussion `[CONFIRMED]`
- **Credit line**：目前不開放；所有帳戶 pre-funded `[CONFIRMED]`
- **最低門檻**：M ADV+ `[WEB]`

## 執行品質
- **執行模式**：Hybrid（A-Book / B-Book）`[CONFIRMED]`
- **Last Look**：Zero Last Look — 官網明確標示 `[WEB]`
- **Slippage**：Positive / negative 均追蹤，可按需提供 `[WEB]`
- **MiFID II reporting**：全交易 timestamp，符合 MiFID II best execution `[WEB]`

## 風控條件 `[PDF]`
| 項目 | 數值 |
|------|------|
| Aggregate NOP 上限 | USD 150,000,000 |
| XAUUSD NOP 上限 | USD 80,000,000 |
| XAGUSD NOP 上限 | USD 30,000,000 |
| XAUGCNH NOP 上限 | USD 10,000,000 |
| USDCNH NOP 上限 | USD 10,000,000 |
| USDHKD NOP 上限 | USD 10,000,000 |
| Margin Call Level | 130%（Net Equity ÷ Margin Requirement，不含延伸信用） |
| Stop Out Level | 50% |

**保證金分級**（Tier 1 < $20M / Tier 2 $20M–$50M / Tier 3 > $50M）`[PDF]`：
- G10 主要貨幣對：0.5% / 1.0% / 2.0%
- CHF 相關貨幣對：0.5% / 10.0% / 20.0%（SNB 風險，Tier 2+ 大幅跳升）
- USDCNH / USDHKD：5.0% / 10.0% / 20.0%
- XAUUSD / XAUGCNH：1.0% / 2.0% / 3.0%
- XAGUSD：3.0% / 5.0% / 20.0%

## 重要限制（對外溝通必知）`[CONFIRMED]`
- **Credit line 目前不開放**：所有帳戶均為 pre-funded，不提供信用額度
- **美國客戶不接受**：W-8 / CFTC 合規門檻極高；對外溝通地域只提 APAC + EMEA，不提 Americas
- **執行模式是 Hybrid**：官網說 STP 是行銷語言，實際可 B-book；對外用「Hybrid (A-Book / B-Book)」

## 目標客戶 `[WEB]`
- ✅ Retail brokers（M ADV+）
- ✅ Hedge funds、Prop trading firms
- ✅ Asset managers、Regional banks
- ✅ Payment service providers（FX 結算需求）
- ✅ 想做 XAU/CNH 的亞洲 broker（罕見產品）
- ✅ 想要 PoP（Prime-of-Prime）的中小型機構

## 不適合的客戶
- ❌ 散戶 / 個人交易者（不接受）`[WEB]`
- ❌ 日均 < $1M 的小型 IB（不符合最低門檻）`[WEB]`
- ❌ 純加密貨幣 spot 客戶（只做 CFD）`[WEB]`
- ❌ 美國客戶（W-8 / CFTC，實際上不接）`[CONFIRMED]`

## 常見異議與回應
> 「毛里裘斯牌照夠嗎？」
- FSC 等同 Tier 2 牌照，符合 MiFID II / FCA 框架；機構業務（非散戶）足夠
- 對方若有 FCA / ASIC，可以 booking 在他們的實體下，我們做 LP

> 「你們的 last look policy？」
- Zero Last Look，官網明確標示 `[WEB]`

> 「為什麼選你們而不是 Saxo / LMAX？」
- 差異化在 XAU/CNH、5ms 執行、5-10 天快速 onboarding

## 待核實項目
- [ ] Fill ratio 真實數字（問 risk team）
- [ ] Rejection rate 真實數字（問 risk team）
- [ ] Tier-1 LP 數量（「12+」未在官網或文件找到依據）
- [ ] Co-location 具體 cross-connect 選項（問技術團隊）
- [ ] Crypto CFDs 的正式商業條款文件（不在 Trading Conditions PDF）
- [ ] Last look 的正式書面政策文件（官網有標但無合約文字）
