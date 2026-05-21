---
company: CWG Markets (Central Wealth Group)
website: https://www.cwgmarkets.com
country: HK
hq_city: Hong Kong
type: retail-broker
size: 500M-1B-daily
size_confidence: estimated  # 公開研究估算，需驗證
regulator: FCA (UK), FSA (St Vincent); HK operating presence
status: prospect
first_contact: 2026-05-21
last_contact: 2026-05-21
owner: me
priority: P1
playbook: existing-broker-upgrade  # 主路徑：Connect-led + XAU/CNH 為 LP 切入錨
products_interested: [syphon-connect, xsyphon-metals, xsyphon-fx]
estimated_arr_usd: 180000  # Connect $100k + LP（XAU/CNH 為主）$80k 區間中位
---

# CWG Markets（中匯國際）

## 背景
- **公司簡介**：總部設於香港的零售 FX/CFD broker，深耕**華語市場**（中國大陸 IB 網絡、台灣、東南亞華人圈），擁有 UK FCA 與 St Vincent FSA 牌照，產品線含 FX、Metals、Indices、Energy、Crypto CFD。
- **規模與市場**：客戶以**華人 retail + 中國 IB-driven flow** 為核心，產品結構偏 **XAU/USD（黃金）+ EUR/USD + 油品**（典型中文市場交易組合）。日均交易量公開資料未揭露，依品牌歷史、IB 網絡密度推估 **$500M-$1B daily**，**待驗證**。
- **技術現況推測**：典型華語市場 broker 配置 —— MT4/MT5（MT4 仍佔 IB 客戶大宗）+ 第三方橋接（Centroid / PrimeXM 在華語市場常見）+ 數家 LP。技術不是強項，**通路與 IB 關係**才是。
- **主要痛點推測**：
  1. **XAU/USD 是主力交易品**，但 LP 在金的深度與 spread 直接影響 IB 留存。客戶若知道**XAU/CNH（金/離岸人民幣）**這種獨家產品，對中國 IB 是新賣點。
  2. IB 跟單 flow 偏 toxic，A/B Book 決策若仍是 static rule，**毛利率被啃**。
  3. 中文市場客戶**對牌照敏感度低、對 spread 敏感度高**；任何能**讓 spread 緊一檔**的 LP 替換都有立即財務影響。
- **推薦組合（依 `cross-sell-matrix.md`）**：
  > 客戶現況屬於「**既有 broker，執行差但不想換系統**」→ 主推 **Syphon Connect**（不換 MT4 / 不換既有 IB 配置）
  >
  > **獨家錨點**：xSyphon 的 **XAU/CNH** 是亞洲 broker 罕見產品，**這是切 CWG 的最強單點**。即使他們對系統升級遲疑，「給你一個別人沒有的產品讓你的 IB 賣給中國客戶」這個故事非常具體。
  >
  > **打包**：Syphon Connect 升級路由（IB flow 自動 A/B Book）+ xSyphon LP（XAU/CNH 為錨，後續延伸 EM FX、Crypto CFD）。

## 關鍵人物
> 注意：以下為「研究方向」，**所有姓名 / email / LinkedIn URL 必須由我親自從 LinkedIn / 官網確認後再填入**。AI 不得編造。

| 姓名 | 職位 | LinkedIn | Email | 性格筆記 |
|------|------|----------|-------|---------|
| TBD  | Head of Trading / 交易主管 | TBD | TBD | Connect + LP 主決策者 |
| TBD  | Head of IB / 機構業務 | TBD | TBD | XAU/CNH 商業價值對話 |
| TBD  | Head of Operations / 營運主管 | TBD | TBD | A/B Book 痛點 |
| TBD  | CTO（如有） | TBD | TBD | Connect 技術切入 |

**待研究 action**：
- [ ] LinkedIn search `"CWG Markets" OR "Central Wealth" Hong Kong` filter Head of Trading / IB
- [ ] 確認 CWG 主推產品是否仍是 XAU/USD + EUR/USD（透過官網 spread 表）
- [ ] 確認 CWG 的橋接商（中文市場常見 Centroid / PrimeXM）

## 互動紀錄（最新在上）

### 2026-05-21 — Initial research
管道：自動研究
摘要：建立檔案，依 `cross-sell-matrix.md` 判定為「Connect-led，但 LP（XAU/CNH）才是真正切入點」。中文市場客戶要用**商業價值**（多一個產品 → IB 多一個賣點 → 多賺）對話，不是用「sub-100ns」這種技術語言。下一步進入 LinkedIn research。

---

## 下一步
- [ ] LinkedIn 找出 Head of Trading + Head of IB（負責人：me / 截止：2026-05-28）
- [ ] 起草 **中文版** outreach v1：以 **XAU/CNH** 為唯一賣點開場，don't dilute（負責人：me / 截止：2026-05-30）
- [ ] 準備 1-pager：「XAU/CNH for Chinese-facing brokers」中英雙語（負責人：me / 截止：2026-06-05）

## 客戶問過、待回覆
- [ ]（尚無互動）

## 內部備註
[CONFIDENTIAL]
- 中文市場 outreach 用**繁體中文 / 簡體中文**比英文 reply rate 高（依 `03-language-style.mdc`）
- 不要用「revolutionary / AI-native」這類英文行銷詞，中文工程師客戶反感
- XAU/CNH 是 **xSyphon 獨家**，要在 outreach 第一句講清楚這是 **bilateral 報價（不是合成）**
- 競爭威脅：Centroid + 既有 LP（如 CFH、Advanced Markets）可能已是穩定配置，要強調「不需要換」
- 若 CWG 表達興趣 → 後續可探索是否能反向用 CWG 的 IB 網絡推 Syphonix 白標給更小的中文 broker（兩段式價值）

## Cross-sell 機會
- **第一階段**（now → 2 個月）：xSyphon XAU/CNH 試接 → 1 個月後評估 IB 反應
- **第二階段**（2-4 個月）：Syphon Connect 切 IB flow（A/B Book 自動化）
- **第三階段**（6-12 個月）：xSyphon EM FX（USD/CNH、USD/HKD）+ Crypto CFD（如 CWG 想做 crypto 但無自有 stack）
- **不推**：Evo full stack（CWG 不會買）、White Label（已有自有品牌與 IB 網絡）
