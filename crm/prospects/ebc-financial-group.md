---
company: EBC Financial Group
website: https://www.ebc.com
country: HK
hq_city: Hong Kong (group HQ); operating entities in UK / AU / KY
type: retail-broker
size: 500M-1B-daily
size_confidence: estimated  # 公開研究估算，需驗證
regulator: FCA (UK), ASIC (AU), CIMA (Cayman); HK presence
status: prospect
first_contact: 2026-05-21
last_contact: 2026-05-21
owner: me
priority: P1
playbook: existing-broker-upgrade  # 主路徑：Connect-led
products_interested: [syphon-connect, xsyphon-fx, xsyphon-metals]
estimated_arr_usd: 220000  # Connect $120k + LP $100k 區間中位
---

# EBC Financial Group

## 背景
- **公司簡介**：2020 年成立的新生代 FX broker 集團，總部設於香港，運營實體分布於 UK（FCA）、Australia（ASIC）、Cayman Islands（CIMA）。品牌行銷積極（FC Barcelona 合作贊助等），主打 high-end retail + professional segment。
- **規模與市場**：客戶以亞洲 retail + IB-driven flow 為主，近兩年積極擴張中東、東南亞、拉美 IB 網絡。日均交易量公開資料未揭露，依牌照層級、品牌投資強度與成立後成長軌跡推估 **$500M-$1B daily**，**待驗證**。
- **技術現況推測**：典型新生代 broker 配置 —— MT4/MT5 + 第三方橋接（OneZero / PrimeXM / Centroid 其中之一）+ 數家 LP。架構新，但執行品質受限於「橋接商的路由邏輯 + LP mix 深度」。
- **主要痛點推測**：
  1. **IB-heavy flow 偏 toxic**（IB 客戶往往跟單、reverse arbitrage），需要更聰明的 A/B Book 決策（不是 static rule）。
  2. 新品牌持續砸行銷預算 → 需要 **fill rate / spread 量化證據** 來說服 partners 留下來，傳統橋接給不出這種儀表板。
  3. LP mix 在 XAU、EM FX、Crypto CFD 可能有缺口；對成長期 broker，「一個 FIX session 接 FX + Metals + Crypto」很有吸引力。
- **推薦組合（依 `cross-sell-matrix.md`）**：
  > 客戶現況屬於「**既有 broker，執行差但不想換系統**」→ 主推 **Syphon Connect**（2-3 週、零 rip-out、35% 執行品質提升）+ 加值 **xSyphon LP**（B-Book hedge 自然延伸）
  >
  > **不要先講 Evo**。新生代 broker 預算分散在行銷，不會在 day 1 對全套執行棧重構付費。先用 Connect 跑出數字、用數字逼出第二筆預算。

## 關鍵人物
> 注意：以下為「研究方向」，**所有姓名 / email / LinkedIn URL 必須由我親自從 LinkedIn / 官網確認後再填入**。AI 不得編造。

| 姓名 | 職位 | LinkedIn | Email | 性格筆記 |
|------|------|----------|-------|---------|
| TBD  | Head of Trading / Execution | TBD | TBD | Connect 主要決策者 |
| TBD  | Head of Liquidity / Brokerage | TBD | TBD | LP 切入 |
| TBD  | Chief Risk Officer | TBD | TBD | A/B Book 決策、flow toxicity 痛點對話 |
| TBD  | Head of IB / Partnerships | TBD | TBD | 了解 partner flow 結構（背景情報用，不主推） |

**待研究 action**：
- [ ] LinkedIn search `"EBC Financial" OR "EBC Group" Hong Kong` filter senior trading / risk roles
- [ ] 確認 EBC 目前使用哪家 bridge / hub（OneZero / PrimeXM / Centroid）
- [ ] 確認 EBC 公開講過的 LP 名單（影響話術：避免與既有 LP 直接挑戰）

## 互動紀錄（最新在上）

### 2026-05-21 — Initial research
管道：自動研究
摘要：建立檔案，依 `cross-sell-matrix.md` 判定為「Connect-led + xSyphon LP 加值」。下一步進入關鍵人物 LinkedIn research 與技術 stack 確認。

---

## 下一步
- [ ] LinkedIn 找出 Head of Trading + CRO（負責人：me / 截止：2026-05-28）
- [ ] 確認 EBC 使用的橋接商與主要 LP（透過公開資料 + LinkedIn job posts）（負責人：me / 截止：2026-06-02）
- [ ] 起草 outreach v1：以「IB flow 量化分析 + 35% fill quality」為 hook，提供 1 週免費 shadow（負責人：me / 截止：2026-06-05）

## 客戶問過、待回覆
- [ ]（尚無互動）

## 內部備註
[CONFIDENTIAL]
- EBC 品牌行銷投入大（足球贊助），對「資料驅動的對外溝通素材」會有正面回應 —— 我們的儀表板數據可包裝成 partner-facing 報告
- 成立年資短（2020）→ 內部 dealing team 規模可能 10-20 人，**少人運營** 這個 Syphonix 核心賣點對他們特別有共鳴
- 多牌照（FCA / ASIC / CIMA）→ 對 Mauritius FSC 的 LP onboarding 流程熟悉，DD 不會卡太久
- 風險：對方可能用 oneZero hub 已綁三年，要先問清楚 lock-in 期

## Cross-sell 機會
- **第一階段**（now → 2 個月）：Syphon Connect — 1 週免費 shadow 分析 → POC → cutover
- **第二階段**（POC 後 1-3 個月）：xSyphon LP（從 XAU 或 EM FX 切入，最低風險）
- **第三階段**（6-12 個月）：若 EBC 開始談「多 entity 統一定價 / 跨 jurisdiction risk」→ 升級 Evo full stack
- **可探討**：Syphonix Crypto CFD 接入（EBC 若想做 crypto 但無自有 stack）
