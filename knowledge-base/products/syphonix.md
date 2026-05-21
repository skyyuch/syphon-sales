# Syphonix — AI-Native Execution System

> 用 AI Agent 取代大量人工運營，少人團隊也能跑 FX 經紀業務

## One-liner
"An AI-native execution infrastructure that prices, routes, and risk-manages every trade in nanoseconds — so a small ops team can run institutional-scale FX flow."

## 核心數據
| 指標 | 數值 |
|------|------|
| Median execution latency | Sub-100ns |
| Pricing pipeline latency | 900ns end-to-end |
| Engine throughput | 1.2M+ events/sec |
| Configurable parameters | 2,500+ |
| Currency pairs monitored | 50+ |
| Inference volume processed | $2T+ |

## 五個產品模組

### 1. Syphon OS — AI 操作系統（底層）
- Foundation + Intelligence layer
- Rust 寫的高效能核心
- Kernel bypass networking、multi-agent 協調
- **不單獨銷售**，是其他模組的底層

### 2. Syphon Aether — 智能層
- 4 個 pre-trained agents：Pricing、Routing、Risk、Liquidity scoring
- Agent decision loop < 1 second
- 支援 OpenAI / Anthropic / Google 的 LLM，也支援 .onnx / .bin 自訂模型
- **不單獨銷售**，與 Evo 一起部署

### 3. Syphon Evo — 執行引擎（核心商品）
四大模組：
- **Pricing** — 動態 spread、per-client markup、regime detection
- **Liquidity** — 12+ venues 聚合、自動 maker scoring
- **Execution** — 智能路由、A/B Book AI 決策、sub-100ns fill
- **Risk** — Inline pre-trade、NOP/margin gates、tail risk、自動 hedging

### 4. Syphon Connect — FIX 橋接（最容易切入的產品）
- FIX 4.4 native
- **零 rip-out**，不換 MT4/MT5/橋接商
- 2-3 週上線
- 支援 OneZero / PrimeXM / Centroid / Gold-i / Tools for Brokers
- **賣點**：35%+ 執行品質提升（first month）

### 5. White Label — 全套白標
- 4-6 週全套上線
- 含品牌化 GUI（web + mobile）、KYC/AML、CRM、後台、reporting
- 可帶 xSyphon LP 或客戶自帶 LP
- 24/7 運維支援

## 目標客戶（按產品）
| 產品 | 主要目標 |
|------|---------|
| Syphon Connect | 既有 FX broker，想升級執行品質 |
| Syphon Evo | 中大型 broker，需要全套執行棧重構 |
| White Label | 新進入市場者、想擴展品牌的 fintech |
| Aether（含在 Evo 內） | 有自己模型的 quant 團隊 |

## 不適合的客戶
- ❌ 日均 < $500M FX 的小型操作（CP 不夠）
- ❌ 只想要單純報價系統、不要 AI 的客戶（我們的核心價值就是 AI）
- ❌ 完全自建技術棧、不想接外部系統的客戶

## 關鍵賣點優先順序
1. **AI 持續學習，越用越好** — 不是 static rule-based
2. **零 rip-out**（Syphon Connect）— 降低切換成本
3. **少人運營** — Head of Ops 一個人能管 4 個 desk
4. **完整方案** — 不只是 EMS，是 pricing + liquidity + execution + risk 一體
5. **可組 xSyphon LP** — 一個合約搞定系統 + 流動性

## 常見異議與回應
> 「我們已經有 MT5 + OneZero，幹嘛換？」
- 不用換。Syphon Connect 是 plug-in，跟你既有的 stack 並存
- 第一個月 35% 執行品質改善（fill rate、spread、reject rate）就能看到價值

> 「AI 黑箱風險？」
- 2,500+ 參數全部可配置，每個 agent 決策有完整 audit trail
- Human-in-loop 模式可設定哪些決策需要人工 approve

> 「Sub-100ns 是真的嗎？」
- Engine benchmark，不是 cloud round-trip
- 需要 co-located deployment（LD4/NY4/TY3/SG1）才能達到
- 客戶可申請 latency profile 報告

> 「2-3 週真能上線？」
- Syphon Connect 因為 FIX-native + 不換 stack，是真的
- White Label 4-6 週是含 KYC/AML 設定的端對端

## 整合的橋接 / 平台
- MetaTrader 5
- OneZero（bridge / hub）
- PrimeXM（bridge / hub）
- Centroid（bridge / hub）
- Gold-i（bridge / hub）
- Tools for Brokers（bridge / hub）

## 定價邏輯
- Connect：subscription + per-volume fee
- Evo：annual platform fee + revenue share on execution gain
- White Label：setup fee + monthly + revenue share
- 都可以打包進 xSyphon LP 的 commercial 結構

## 待補充
- [ ] 真實客戶案例（網站只有匿名引言）
- [ ] 各模組具體 pricing tier
- [ ] 與 oneZero Hub、PrimeXM XCore 的功能對比
