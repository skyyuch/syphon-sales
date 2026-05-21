---
company: PU Prime (Pacific Union)
website: https://www.puprime.com
country: HK
hq_city: Hong Kong (group ops); operating entities multi-jurisdiction
type: retail-broker
size: 500M-1B-daily
size_confidence: estimated  # 公開研究估算，需驗證
regulator: FSCA (South Africa), FSC (Mauritius), CIMA (Cayman); HK presence
status: prospect
first_contact: 2026-05-21
last_contact: 2026-05-21
owner: me
priority: P1
playbook: pop-institutional  # 主路徑：LP-led + Connect 試用
products_interested: [xsyphon-fx, xsyphon-metals, syphon-connect]
estimated_arr_usd: 160000  # LP $100k + Connect trial $60k 區間中位
---

# PU Prime (Pacific Union)

## 背景
- **公司簡介**：Pacific Union 集團旗下零售 FX/CFD broker 品牌，香港運營，多牌照（FSCA 南非、FSC 模里西斯、CIMA 開曼）。主打 retail + IB 模式，產品線含 FX、Metals、Indices、Commodities、Crypto CFD、Stocks CFD。
- **規模與市場**：客戶以**亞太 + 拉美 + 中東 + 非洲新興市場**為主，**IB-heavy** 是核心增長引擎。日均交易量公開資料未揭露，依品牌成長軌跡、IB 網絡規模推估 **$500M-$1B daily**，**待驗證**。
- **技術現況推測**：典型 IB-driven broker 配置 —— MT4/MT5（MT4 仍是新興市場 IB 主力）+ 第三方橋接 + 數家 LP。**有自己的後台 CRM 與 IB portal**（IB 業務驅動 → 工程資源投在 partner-facing tool）。Core execution stack 偏「夠用就好」，**LP mix** 才是執行品質的主要瓶頸。
- **主要痛點推測**：
  1. **新興市場客戶交易 EM FX**（USD/ZAR、USD/MXN、USD/TRY、USD/BRL）+ **XAU/USD** 比例高 → 對應 LP 在這些 pairs 的深度直接影響毛利。
  2. **IB-heavy = flow 多元化**（不同地區 IB 帶不同 toxicity profile），需要更細的 maker scoring，但他們不會為此換 stack → Connect plug-in 是 sweet spot。
  3. 多 entity 多牌照 → **跨 jurisdiction booking 與 LP 多接** 是長期戰術需求，xSyphon 一個 FIX session 接 FX + Metals + Crypto 對運維是節省。
- **推薦組合（依 `cross-sell-matrix.md`）**：
  > 客戶現況屬於「**想要更深 LP，系統已自建**」（不是「想全面升級」）→ 主推 **xSyphon LP**（EM FX + XAU 為錨）+ 後續試用 **Syphon Connect**
  >
  > **不要**第一輪講 Connect / Evo。PU Prime 的痛點在 LP 深度與多元化，先用 LP 拿到第一個合約，**3-6 個月後**再用「我們可以給你 fill rate 改善 35% 的儀表板」帶出 Connect 對話。

## 關鍵人物
> 注意：以下為「研究方向」，**所有姓名 / email / LinkedIn URL 必須由我親自從 LinkedIn / 官網確認後再填入**。AI 不得編造。

| 姓名 | 職位 | LinkedIn | Email | 性格筆記 |
|------|------|----------|-------|---------|
| TBD  | Head of Liquidity / Head of Brokerage | TBD | TBD | LP 主決策者 |
| TBD  | Head of Trading / Dealing | TBD | TBD | 執行品質痛點對話 |
| TBD  | Head of Risk | TBD | TBD | 多 jurisdiction risk |
| TBD  | COO / Head of Operations | TBD | TBD | 長期關係維護 |

**待研究 action**：
- [ ] LinkedIn search `"PU Prime" OR "Pacific Union" Hong Kong` filter senior trading / liquidity roles
- [ ] 確認 PU Prime 主要交易產品結構（公開 spread 表 → 推測客戶交易組合）
- [ ] 確認 PU Prime 的橋接商與既有 LP（如能找到）

## 互動紀錄（最新在上）

### 2026-05-21 — Initial research
管道：自動研究
摘要：建立檔案，依 `cross-sell-matrix.md` 判定為「LP-led + 後續 Connect」路徑，與 Hantec 同類但客戶 base 偏新興市場（EM FX 為錨 vs Hantec 偏 XAU/CNH）。下一步進入 LinkedIn research。

---

## 下一步
- [ ] LinkedIn 找出 Head of Liquidity + Head of Trading（負責人：me / 截止：2026-05-28）
- [ ] 起草 outreach v1：以 **EM FX 深度（USD/ZAR、USD/MXN、USD/TRY）+ XAU** 為 hook，避開技術術語（負責人：me / 截止：2026-06-02）
- [ ] 準備 1-pager：「Emerging Market FX Liquidity Profile」（負責人：me / 截止：2026-06-08）

## 客戶問過、待回覆
- [ ]（尚無互動）

## 內部備註
[CONFIDENTIAL]
- 與 Hantec 區隔：Hantec 用 **XAU/CNH** 為錨（HK / China focus），PU Prime 用 **EM FX basket**（emerging markets）為錨
- IB-driven broker 對「Onboarding 5-10 天」特別有感（vs 銀行 3-6 個月）—— 要強調速度
- Mauritius FSC 同框架 → DD 文件相互熟悉，能加速 KYC
- 競爭威脅：B2Broker（也做 EM FX LP）在 IB-driven broker 圈知名度高，**不要直接挑戰**，要強調 **AI-driven aggregation + 零 last look + 12 Tier-1 上游** 三點差異
- 風險：對方可能已用 GBE Prime / TraderEvolution 之類 LP，初次接觸要先 listen 而非 pitch

## Cross-sell 機會
- **第一階段**（now → 2 個月）：xSyphon LP — EM FX 為錨，XAU 為加分
- **第二階段**（3-6 個月，LP 跑順後）：Syphon Connect 免費 1 週 shadow 分析 → 用數據逼出第二筆預算
- **第三階段**（6-12 個月）：Aether liquidity scoring agent（IB-heavy broker 對 maker quality 自動排序特別有價值）
- **不推**：Evo full stack（PU Prime 不會買全套）、White Label（已有自有品牌）
