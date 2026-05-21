---
company: Hantec Markets Holdings Ltd
website: https://www.hantecmarkets.com
country: HK
hq_city: Hong Kong
type: retail-broker
size: 500M-1B-daily
size_confidence: estimated  # 公開研究估算，需驗證
regulator: SFC (HK), FCA (UK), FSC (Mauritius), JFSA-equivalent (Jordan)
status: prospect
first_contact: 2026-05-21
last_contact: 2026-05-21
owner: me
priority: P1
playbook: pop-institutional  # 主路徑：LP-led；次路徑：existing-broker-upgrade
products_interested: [xsyphon-fx, xsyphon-metals, syphon-connect]
estimated_arr_usd: 180000  # LP $120k + Connect trial $60k 區間中位
---

# Hantec Markets（亨達集團）

## 背景
- **公司簡介**：1990 年於香港成立，集團名 Hantec Group / Hantec Markets。歷經三十餘年發展，從香港本土 FX/bullion 經紀延伸至 UK（FCA）、Cyprus、Jordan、Mauritius，是少數香港土生土長並做到國際多牌照的零售 FX broker。
- **規模與市場**：客戶以亞洲（HK、Taiwan、Mainland China affiliates、Middle East）為主；產品線含 FX、貴金屬（XAU/XAG 為核心，香港金商背景）、CFD、stocks。日均交易量公開資料未揭露，依牌照層級、員工人數（200+）與 30 年品牌推估 **$500M-$1B daily** 區間，**待驗證**。
- **技術現況推測**：採用 MT4/MT5 + 自有後台（多年累積、可能部分自建橋接）。長期穩定運作的代價通常是系統僵化、難快速納入新 LP / 新產品。
- **主要痛點推測**：
  1. 既有 LP mix 在 **XAU/CNH** 與 **EM FX**（USD/HKD、USD/CNH）的深度可能不足，亞洲客戶這塊量大。
  2. 系統使用多年，core stack 不會輕易換 → 任何「需要 rip-out」的提案會被拒。
  3. 中港兩地 retail flow 偏 toxic（牛熊轉換頻繁），對 maker scoring + A/B Book 決策有改善空間。
- **推薦組合（依 `cross-sell-matrix.md`）**：
  > 客戶現況屬於「**想要更深 LP，系統已自建**」→ 主推 **xSyphon LP**（XAU/CNH 為錨）+ 試用 **Syphon Connect**（純 plug-in、不換 stack）
  >
  > 不要在第一輪提 Syphon Evo / White Label —— Hantec 自有 stack 30 年，全套替換的對話會被秒拒。

## 關鍵人物
> 注意：以下為「研究方向」，**所有姓名 / email / LinkedIn URL 必須由我親自從 LinkedIn / 官網確認後再填入**。AI 不得編造。

| 姓名 | 職位 | LinkedIn | Email | 性格筆記 |
|------|------|----------|-------|---------|
| TBD  | Head of Trading / Dealing（香港） | TBD | TBD | 第一觸點：LP 切入 |
| TBD  | Head of Liquidity / Brokerage Services | TBD | TBD | LP 決策者 |
| TBD  | CTO / Head of Technology | TBD | TBD | Connect 切入 |
| TBD  | Managing Director（HK office） | TBD | TBD | 高層 cross-sell |

**待研究 action**：
- [ ] LinkedIn search `"Hantec Markets" Hong Kong` filter by Head of Trading / Liquidity / CTO
- [ ] 官網 contact page / About us 確認 senior team
- [ ] 透過行業活動（不參加 EXPO，但可借第三方論壇）找 warm intro

## 互動紀錄（最新在上）

### 2026-05-21 — Initial research
管道：自動研究
摘要：建立檔案，依 `cross-sell-matrix.md` 判定為「LP-led + Connect 試用」路徑。下一步進入關鍵人物 LinkedIn research。

---

## 下一步
- [ ] LinkedIn 找出 Head of Trading + Head of Liquidity（負責人：me / 截止：2026-05-28）
- [ ] 起草 outreach v1：以 **XAU/CNH 深度** 為 hook（負責人：me / 截止：2026-05-30）
- [ ] 確認 Hantec 是否已是 OneZero / PrimeXM / Centroid 客戶（影響 Connect 切入話術）（負責人：me / 截止：2026-06-02）

## 客戶問過、待回覆
- [ ]（尚無互動）

## 內部備註
[CONFIDENTIAL]
- Hantec 30 年品牌＋多重監管 → 對「新進 LP」的 onboarding due diligence 會比新生代 broker 嚴格，要備好 Mauritius FSC GB25204632 + MiFID II / FCA 框架文件
- 不要 oversell sub-100ns；Hantec 不是 latency-sensitive prop desk，**LP 深度 + 產品覆蓋（XAU/CNH）** 才是 hook
- 競品威脅：Hantec 自家 prime（Hantec Prime / FXPrime）可能已是內部 LP，要小心是否被視為「直接競爭」
- 若 Hantec 表達興趣 → 後續可探索是否能反向成為 Syphonix 的 **distribution channel**（他們的亞洲 IB 網絡）

## Cross-sell 機會
- **第一階段**（now → 3 個月）：xSyphon LP — XAU/CNH 為錨，EM FX 為加分
- **第二階段**（3-6 個月，LP 跑順後）：Syphon Connect 免費 1 週 shadow 分析，給數據說話
- **第三階段**（6-12 個月，如關係深化）：探索 Aether risk agent（XAU 客戶 toxicity scoring 是亞洲特殊場景）
- **不推**：White Label（已有自家品牌）、Syphon Evo full stack（rip-out 不可能）
