---
company: Doo Prime (Doo Group)
website: https://www.dooprime.com
country: HK
hq_city: Hong Kong (Doo Group HQ)
type: retail-broker
size: 500M-1B-daily
size_confidence: estimated  # 集團規模可能更高，需驗證
regulator: SFC (HK Type 1/2/4/9), FSA (Seychelles), FSC (Mauritius), MAS (SG), ASIC (AU), VFSC (Vanuatu)
status: prospect
first_contact: 2026-05-21
last_contact: 2026-05-21
owner: me
priority: P1
playbook: existing-broker-upgrade  # 主路徑：Evo-led（少數適合全面升級對話的香港 broker）
products_interested: [syphon-evo, xsyphon-fx, xsyphon-metals, xsyphon-crypto]
estimated_arr_usd: 400000  # Evo $250k + LP $150k 區間中位，集團型客戶 ARR 較高
---

# Doo Prime / Doo Group

## 背景
- **公司簡介**：成立於 2014 年，總部設於香港，Doo Group 旗下品牌包含 Doo Prime（多資產 broker）、Doo Financial、Doo Clearing、Doo Wealth、Doo Tech 等。從零售 FX 起家，已延伸至 securities brokerage、wealth management、clearing、payment、technology 一站式金融集團。
- **規模與市場**：客戶遍及亞太、歐洲、美洲；產品線含 FX、Metals、Indices、Stocks（含 US、HK、A-share）、Futures、Bonds、Crypto CFD。**多牌照矩陣**是同類最完整之一（SFC + MAS + ASIC + FSC + FSA + VFSC）。日均交易量公開資料未揭露，依集團規模與多元業務推估保守 **$500M-$1B daily** 區間，實際可能更高，**待驗證**。
- **技術現況推測**：集團型 broker，通常採取 **混合 stack**：MT4/MT5 + 自建後台 + 自建 clearing（Doo Clearing）+ 第三方橋接。**Doo Tech** 子品牌暗示有自己的工程團隊，這既是門檻也是機會 —— 對話需要技術深度。
- **主要痛點推測**：
  1. **多 entity / 多 jurisdiction 統一定價** 是集團型 broker 的長期難題（每家用本地系統 → 報價不一致 → arbitrage 風險）。
  2. **多資產統一風控**（FX + Stocks + Crypto + Futures），不同 desk 各自為政是常態，集團 CRO 一直在找解。
  3. Doo Clearing 自家做 clearing，但**上游 LP 的 Tier 1 深度**永遠是議題；多一家 quality LP（特別是 XAU/CNH、EM FX）有戰略價值。
- **推薦組合（依 `cross-sell-matrix.md`）**：
  > 客戶現況屬於「**既有 broker，想全面升級**」→ 主推 **Syphon Evo**（pricing + liquidity + execution + risk 四模組統一棧）+ 加值 **xSyphon LP**（整合定價）
  >
  > Doo 是少數**有資本、有工程文化、有多 entity 統一定價痛點**的香港 broker，是 Evo 對話最自然的對象。
  >
  > **備選 fallback**：若 Doo 表達「太大不能換」→ 退回 Syphon Connect 切某一 desk（例如 metals desk 試點）+ xSyphon LP。

## 關鍵人物
> 注意：以下為「研究方向」，**所有姓名 / email / LinkedIn URL 必須由我親自從 LinkedIn / 官網確認後再填入**。AI 不得編造。

| 姓名 | 職位 | LinkedIn | Email | 性格筆記 |
|------|------|----------|-------|---------|
| TBD  | Chief Technology Officer / Head of Doo Tech | TBD | TBD | Evo 對話最重要對象（技術深度） |
| TBD  | Chief Risk Officer / Head of Risk | TBD | TBD | 多資產統一風控痛點 |
| TBD  | Head of Liquidity / Head of Brokerage | TBD | TBD | LP 切入 |
| TBD  | COO / Head of Operations | TBD | TBD | 多 entity 整合決策層 |
| TBD  | CEO（如能觸及） | TBD | TBD | 戰略合作對話 |

**待研究 action**：
- [ ] LinkedIn search `"Doo Group" OR "Doo Prime" Hong Kong` filter CTO / CRO / Head of Trading
- [ ] 搜尋 Doo Tech 的 GitHub / job posts → 推測技術 stack（自建程度多深）
- [ ] 確認 Doo Clearing 的上游 prime brokers（公開資料 / 監管文件）

## 互動紀錄（最新在上）

### 2026-05-21 — Initial research
管道：自動研究
摘要：建立檔案，依 `cross-sell-matrix.md` 判定為「Evo-led 全面升級對話」路徑，是 5 家 P1 中唯一適合直接談 full stack 的對象。下一步進入 CTO / CRO LinkedIn research。

---

## 下一步
- [ ] LinkedIn 找出 CTO + CRO + Head of Liquidity（負責人：me / 截止：2026-05-28）
- [ ] 研究 Doo Tech 公開技術 footprint（job posts / engineering blog）（負責人：me / 截止：2026-06-02）
- [ ] 起草 outreach v1：以**多 entity 統一定價 + 多資產統一風控** 為 hook，避開「換系統」這種威脅性語言（負責人：me / 截止：2026-06-05）
- [ ] 準備備選 fallback 提案：若 Evo 對話失敗 → metals desk 試點 Connect + LP

## 客戶問過、待回覆
- [ ]（尚無互動）

## 內部備註
[CONFIDENTIAL]
- 高 ARR 潛力客戶（估 $400k+，集團型可能上 $1M+ 區間），優先級提到 **P1 上層**
- Doo Tech 自有工程團隊 → 對「AI 黑箱」會敏感，要把 2,500+ 可配置參數 + audit trail 講足
- 競爭威脅：oneZero / PrimeXM 通常已是集團型客戶供應商；不要直接挑戰，要強調 **AI-native vs rule-based** 的根本差異
- Doo Clearing 自家做 clearing → 表面看是競品（PoP），但實際上他們也需要上游 LP，xSyphon 可作為**互補上游**（不是替代）
- 戰略價值：若 Doo 成為旗艦客戶，對亞洲市場其他 broker 的銷售有 reference 效應

## Cross-sell 機會
- **第一階段**（now → 6 個月）：Evo 對話 OR 退回 Connect metals desk 試點 + xSyphon LP（XAU/CNH 為錨）
- **第二階段**（6-12 個月）：Aether risk agent 對 Doo Clearing 風控賦能；多 entity 統一定價 POC
- **第三階段**（12-24 個月）：戰略夥伴關係 —— 探索 Doo 成為亞洲 distribution channel 或 reference site
- **可探討**：Doo Wealth + Syphonix asset manager toolkit；Doo Crypto 業務 + xSyphon Crypto CFD
