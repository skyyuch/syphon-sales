---
company: Acetop Precious Metals Limited
website: https://www.acetop.com
country: HK
hq_city: Hong Kong
type: bullion-dealer
size: 100M-500M-daily
size_confidence: estimated  # 公開研究估算，需驗證
regulator: CGSE (E-Trading Member No. 145); 部分海外實體可能有 FSA/FCA，待驗
status: prospect
first_contact: 2026-05-21
last_contact: 2026-05-21
owner: me
priority: P1
icp_fit: cgse-bullion
channel_focus: retail
playbook: existing-broker-upgrade  # 主路徑：LP-led + Connect 升 A/B Book
products_interested: [xsyphon-metals, xsyphon-fx, syphon-connect]
estimated_arr_usd: 140000  # LP $90k + Connect $50k 區間中位（金商 ARR 結構不同於 FX broker）
contact_tel: (852) 22768888
---

# Acetop Precious Metals（領峰貴金屬）

## ICP 資格檢查
- [x] 對方**沒有**自家 LP / Prime / Clearing 子品牌（待用 LinkedIn + 官網 final 驗證）
- [x] 對方**沒有**對其他 broker 提供 White Label（待驗）
- [x] 規模在 xSyphon 最低門檻（M ADV+）以上 — CGSE E-Trading 行員，量級足夠
- [x] ICP segment 已確認：**CGSE Bullion**（純零售金商）

## 背景
- **公司簡介**：領峰貴金屬，香港金銀業貿易場（CGSE）**E-Trading 行員（編號 145）**，主營電子盤倫敦金銀、99 金、人民幣公斤金條等。公開定位為純零售金商，面向香港、中國大陸（IB 引流）、東南亞華人圈散戶。
- **規模與市場**：CGSE E-Trading 行員中**較知名的零售品牌**，廣告與品牌投入相對積極。日均交易量公開資料未揭露，依品牌知名度與行員資歷推估 **$100M-$500M daily**（金商規模本就低於 FX broker），**待驗證**。
- **技術現況推測**：典型 CGSE 金商配置 —— 自研或外購 GUI（網頁 + APP）、後台連 CGSE 電子盤、loco London 部分接外部 LP（常見如 CFH、Advanced Markets 的金產品線、或本地金商互換）。**FX 業務若有，多半為近年新增**，stack 未必統一。
- **主要痛點推測**：
  1. **XAU/USD 是核心商品**，但 spread 與深度直接決定毛利；上游 LP 在亞洲時段（特別是中港台 IB 客戶活躍時段）若供給不足，零售報價就被擠壓。
  2. 中國 IB 客戶對**人民幣計價金**有天然需求（CGSE 本身有人民幣公斤金條合約），但**XAU/CNH（離岸人民幣計價的 loco London 金）**作為 OTC 報價，本地金商通常拿不到 bilateral 深度 —— 這是 xSyphon 獨家可解。
  3. 若已擴 FX 業務，A/B Book 多半仍是 static rule（金商不擅 FX 路由邏輯），毛利率被 IB 跟單 flow 啃。
- **推薦組合（依 `cross-sell-matrix.md`）**：
  > 客戶現況屬於「**既有 broker，執行差但不想換系統**」/ Segment B「CGSE 金商」
  >
  > 主推：**xSyphon LP — XAU/CNH 為錨**（這是別人給不出來的，講具體 spread 與深度）
  >
  > 加值：**Syphon Connect** — 若 Acetop 已有 FX 業務，免費 1 週 shadow 分析 A/B Book 升級空間
  >
  > **不要**第一輪講 Evo / White Label，金商核心是「拿更深的金 + 多一個獨家產品」，不需要重構系統。

## 關鍵人物
> 注意：所有姓名 / email / LinkedIn URL 必須由我親自從 LinkedIn / 官網確認後再填入。AI 不得編造。

| 姓名 | 職位 | LinkedIn | Email | 性格筆記 |
|------|------|----------|-------|---------|
| TBD  | 行政總裁 / 董事總經理 | TBD | TBD | 高層 cross-sell 對話 |
| TBD  | 交易部主管 / Head of Dealing | TBD | TBD | LP 主決策者 |
| TBD  | 業務發展總監 / Head of BD | TBD | TBD | XAU/CNH 商業價值對話 |
| TBD  | IT 主管 / Head of Tech | TBD | TBD | Connect 技術切入 |

**待研究 action**：
- [ ] LinkedIn search `"領峰貴金屬" OR "Acetop Precious Metals"` filter senior dealing / BD / IT
- [ ] 確認領峰是否已有 FX 業務（影響 Connect 切入話術）
- [ ] CGSE 官網 / 公司網站確認 senior team 名單
- [ ] 公司電話 (852) 22768888 — 可作為冷郵件後的 follow-up channel（**最後手段，先走 LinkedIn**）

## 互動紀錄（最新在上）

### 2026-05-21 — Initial research
管道：自動研究（CGSE 官方 E-Trading Member List, last updated 2026-05-21 13:00）
摘要：從 CGSE 認可電子交易商名單（52 家）篩選後建檔。Acetop 為 5 家 P1 之一，cross-sell 路徑為「LP（XAU/CNH 為錨）+ Connect 試用」。下一步進入 LinkedIn 關鍵人物 research。

---

## 相關檔案索引
- **Playbook**：`playbooks/cgse-bullion-dealer.md`
- **Campaign**：`crm/campaigns/2026-05-cgse-bullion-batch1.md`（**Position #1**，首封日 2026-05-26 二，第一個發測模板）
- **Cold Email**：`templates/email/cgse-bullion-lp-cold-tc-v1.md` **Variant A**（XAU/CNH 為錨）
- **Follow-up**：`templates/email/cgse-bullion-followup-tc-v1.md` Track A，**Variant A1** 已 hydrated
- **Discovery Script**：`templates/pitch/cgse-bullion-discovery-call-tc-v1.md`（call 前 30 分鐘讀）
- **1-Pager 附件**：`content/collateral/xau-cnh-for-cgse-bullion-1pager-tc-v1.md`（Follow-up #1 必備）
- **Cross-sell 路徑**：LP（XAU/CNH 為錨）+ Connect 試用（次階段）
- **研究 toolkit**：`crm/campaigns/2026-05-cgse-bullion-batch1-toolkit.md`（LinkedIn / Hunter.io / Google search 集合）
- **追蹤試算表**：`crm/campaigns/2026-05-cgse-bullion-batch1-tracker.csv`
- **Mail merge 輸出範例**：`scripts/output.example/cgse-batch1/acetop-cold.{txt,html}` + `index.html` 主控台
- **1-Pager 渲染版（列印 PDF）**：`content/collateral/assets/xau-cnh-1pager-tc-v1.html`

## 下一步
- [ ] LinkedIn 找出交易部主管 + 業務發展總監（負責人：me / 截止：2026-05-28）
- [ ] 起草**中文版** outreach v1：以 **XAU/CNH bilateral 深度** 為唯一賣點開場（負責人：me / 截止：2026-05-30）
- [ ] 準備 1-pager：「XAU/CNH for CGSE Bullion Dealers」中文（負責人：me / 截止：2026-06-05）

## 客戶問過、待回覆
- [ ]（尚無互動）

## 內部備註
[CONFIDENTIAL]
- CGSE 金商 cohort 客戶語言**主要繁體中文**，所有 outreach 用繁中
- **不要用 FX broker 的 sub-100ns / 35% fill rate 話術** — 金商核心痛點是「金的深度 + 獨家產品」，技術語言會聽不進去
- XAU/CNH 是 xSyphon **獨家賣點**，務必強調是 **bilateral 報價（不是 cross 合成）**
- 競爭威脅：本地金商互換（行員之間直接 cover）可能已是穩定流動性來源；要強調 xSyphon 是「補上他們拿不到的 Tier 1 上游」而不是「替換現有」
- 領峰若反應好，可作為其他 CGSE 行員的 reference site（同業口碑在金商圈很重要）

## Cross-sell 機會
- **第一階段**（now → 2 個月）：xSyphon XAU/CNH 試接（單一產品先進場）
- **第二階段**（2-4 個月）：xSyphon 完整 loco London 金/銀 LP + EM FX（如領峰已做 FX）
- **第三階段**（6-12 個月）：Syphon Connect 升 A/B Book（如 FX 業務成長）
- **不推**：Syphon Evo full stack（金商不需要）、White Label（已有自家品牌）
