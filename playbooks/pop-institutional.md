# Playbook — PoP / Hedge Fund / Prop Desk（純 LP 客戶）

> 這類客戶**只要 LP，不要系統**。專注 xSyphon 的賣點，不要硬塞 Syphonix。

## 客戶畫像
- Hedge funds：FX / 多資產，主動交易
- Prop desks：高頻、量化、套利
- 中型 broker 想要 PoP 補強既有 LP mix
- 規模：$50M-$5B daily

## 獵客信號
- 招聘 "FX Trader" / "Algorithmic FX Strategist"
- 監管文件提到擴大 FX 業務
- 引薦：既有客戶介紹、銀行/律所引介
- 二級信號：對方 trading platform 更新（暗示更積極執行）

## 首次接觸話術
> "Direct enough — xSyphon is a Mauritius-licensed LP with $1B+ daily, 12 Tier-1 aggregated, 5ms execution, zero last look. {{instrument_hook}} is a particularly deep book. Want a tailored connectivity proposal in 24 hours? Just need rough volume + instrument mix."

## Discovery 重點
1. 目前 LP mix？多少家？平均 fill rate？
2. 主要交易產品（pairs、size、time of day）？
3. 用 FIX 還是其他協議？Co-located 在哪？
4. 對 last look 政策的態度？
5. 既有 PB / clearing 關係？

## Demo 重點
- **不要 Demo Syphonix**（除非對方主動問）
- 給 latency profile 數據
- 給 historical fill rate / rejection rate by pair
- 強調 XAU/CNH、EM FX 等難找的產品
- Onboarding timeline（5-10 天 vs 銀行 3-6 個月）

## 異議處理重點
> 「為什麼不直接接 LMAX / Saxo Prime？」
- 你規模到了嗎？他們對 < $5B 客戶很慢
- 我們 PoP 結構讓你拿到接近 Tier 1 的價格
- XAU/CNH 他們不做或很貴

> 「毛里裘斯牌照夠嗎？」
- 對機構業務（你是 professional client）完全合規
- 我們的 LP 上游是 12 家 Tier 1 銀行 + PoP
- MiFID II / FCA framework 對齊

> 「Crypto 接觸？」
- 我們做 cash-settled CFD，不做 spot
- 同一 FIX session 接 FX + Metals + Crypto，省整合成本

## 典型成交週期
- Inquiry → KYC：1-2 週
- KYC → live：5-10 個工作天
- **總計**：3-5 週（最快的銷售類型）

## ARR 範圍
- 純 LP revenue share，依交易量
- 估計年化：**$30k - $500k+**（高度依賴對方規模）

## 何時嘗試交叉銷售 Syphonix
- 對方在 deal 後 3-6 個月，**主動抱怨內部系統時** → 才提
- 不要在 LP onboarding 階段提，會混淆訊息

## 常見死局
- 對方堅持要 ECN exchange model（不接受 STP）→ 不適合
- 規模 < $1M daily ADV → 直接介紹 Tier 2 Referral 引薦給更小 broker
