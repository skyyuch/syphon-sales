---
company: Royal Capital Precious Metals (Asia) Limited
website: https://www.royal-capital.com.hk  # 待驗證確切官網 URL
country: HK
hq_city: Hong Kong
type: bullion-dealer
size: 100M-500M-daily
size_confidence: estimated  # 公開研究估算，需驗證
regulator: CGSE (E-Trading Member No. 076)
status: prospect
first_contact: 2026-05-21
last_contact: 2026-05-21
owner: me
priority: P1
icp_fit: cgse-bullion
channel_focus: mixed  # retail + 集團多元金融
playbook: existing-broker-upgrade  # 主路徑：LP + Connect（多產品打包）
products_interested: [xsyphon-metals, xsyphon-fx, syphon-connect]
estimated_arr_usd: 160000  # LP $100k + Connect $60k 區間中位
contact_tel: (852) 37537900
---

# Royal Capital Precious Metals（皇御金融集團）

## ICP 資格檢查
- [x] 對方**沒有**自家 LP / Prime / Clearing 子品牌（**待用 LinkedIn + 官網重點驗證**，皇御集團多元，需確認是否有 institutional 對外服務）
- [x] 對方**沒有**對其他 broker 提供 White Label（待驗）
- [x] 規模在 xSyphon 最低門檻（M ADV+）以上
- [x] ICP segment 已確認：**CGSE Bullion**（純零售為主，集團型多元金融）

> ⚠️ **驗證重點**：皇御集團（Royal Capital Group）可能有證券、期貨等姊妹公司，需確認**不在 institutional liquidity / prime brokerage** 業務 —— 若有，仍可建檔但 cross-sell 路徑需調整為「只談 Syphonix」。

## 背景
- **公司簡介**：皇御金融集團旗下貴金屬交易公司，香港金銀業貿易場（CGSE）**E-Trading 行員（編號 076）**。「皇御」品牌涵蓋貴金屬、證券、期貨等多元金融服務（集團型而非單一金商），但 Royal Capital Precious Metals 這個實體**專注貴金屬電子盤**。
- **規模與市場**：客戶以香港 + 中國 IB 引流為主，集團型背景代表**有資本進行系統升級**。日均交易量公開資料未揭露，依集團規模推估 **$100M-$500M daily**，**待驗證**。
- **技術現況推測**：集團型金商，技術配置常見 **混合 stack** —— 自研 GUI + 外部橋接 + 多家上游金 LP。集團 IT 資源較單體金商多，**對 Syphon Connect 這種 plug-in 的技術對話接受度較高**。
- **主要痛點推測**：
  1. **多元金融集團** → 跨產品線（金、證券、期貨）的**統一報價 / 統一風控** 是 long-term 議題。
  2. **XAU/USD 為主，但中國客戶人民幣需求增** → XAU/CNH 是新賣點。
  3. 集團型 → 可能想擴 FX 業務（許多金商近年都在嘗試），**統一執行平台** 比單純加 LP 更有戰略意義。
- **推薦組合（依 `cross-sell-matrix.md`）**：
  > 客戶現況屬於「**既有 broker，執行差但不想換系統**」/ Segment B「CGSE 金商，集團型」
  >
  > 主推：**xSyphon LP（XAU/CNH + EM FX 打包）+ Syphon Connect 試用**
  >
  > 集團型客戶適合**多產品打包對話**：「一個 FIX session 接金 + EM FX + 未來 Crypto CFD」對運維是顯著節省。
  >
  > Fallback：若皇御對全面對話遲疑 → 退回單一產品 XAU/CNH 試接。

## 關鍵人物
> 注意：所有姓名 / email / LinkedIn URL 必須由我親自從 LinkedIn / 官網確認後再填入。AI 不得編造。

| 姓名 | 職位 | LinkedIn | Email | 性格筆記 |
|------|------|----------|-------|---------|
| TBD  | 集團行政總裁 | TBD | TBD | 戰略層對話 |
| TBD  | 貴金屬部總經理 | TBD | TBD | LP 主決策者 |
| TBD  | 業務發展總監 | TBD | TBD | 多產品打包對話 |
| TBD  | CTO / IT 主管 | TBD | TBD | Connect 切入 |

**待研究 action**：
- [ ] LinkedIn search `"皇御金融" OR "Royal Capital" Hong Kong precious metals` filter senior
- [ ] **重點驗證**：皇御集團是否有 institutional / prime services 業務（若有需重評 ICP）
- [ ] 確認 Royal Capital 是否已有 FX / 證券業務的 cross-sell 機會
- [ ] 公司電話 (852) 37537900

## 互動紀錄（最新在上）

### 2026-05-21 — Initial research
管道：自動研究（CGSE 官方 E-Trading Member List, last updated 2026-05-21 13:00）
摘要：從 CGSE 認可電子交易商名單篩選後建檔。Royal Capital 為 5 家 P1 之一，集團型多元 → cross-sell 路徑為「LP + Connect 多產品打包」。下一步必須**先驗證集團是否有 institutional 業務**，影響 ICP 判斷。

---

## 相關檔案索引
- **Playbook**：`playbooks/cgse-bullion-dealer.md`
- **Campaign**：`crm/campaigns/2026-05-cgse-bullion-batch1.md`（**Position #3**，首封日 2026-06-02 二，**ICP 驗證 deadline 06-01**）
- **Cold Email**：`templates/email/cgse-bullion-lp-cold-tc-v1.md` **Variant C**（多產品打包，集團型）
- **Follow-up**：`templates/email/cgse-bullion-followup-tc-v1.md` Track A，**Variant C1 待 hydrated**
- **Discovery Script**：`templates/pitch/cgse-bullion-discovery-call-tc-v1.md`
- **1-Pager 附件**：`content/collateral/xau-cnh-for-cgse-bullion-1pager-tc-v1.md`
- **Cross-sell 路徑**：LP + Connect 多產品打包（金 + EM FX + 未來 Crypto CFD）
- ⚠️ **發送前 blocker**：必須先驗證皇御集團是否有 institutional / prime 業務（若有 → 取消 campaign 排程，改用 Syphonix-only 路徑）

## 下一步
- [ ] **優先**：官網 + LinkedIn 驗證皇御集團是否有對外 LP / prime 業務（負責人：me / 截止：2026-05-26）
- [ ] LinkedIn 找出貴金屬部總經理 + CTO（負責人：me / 截止：2026-05-30）
- [ ] 起草中文 outreach v1：「集團型金商的 LP + 系統打包」角度（負責人：me / 截止：2026-06-02）

## 客戶問過、待回覆
- [ ]（尚無互動）

## 內部備註
[CONFIDENTIAL]
- 集團型金商比單體金商更難談（決策層多、流程長），但 ARR 上限更高
- **必須先做 ICP 驗證再花時間 outreach**：若皇御集團有 institutional LP 業務，xSyphon 是競品，要立即改為「只談 Syphonix Connect」
- 多產品打包對話的話術參考：`knowledge-base/products/xsyphon.md` —「同一 FIX session 接 FX + Metals + Crypto」
- 若 Royal Capital 對話深入 → 集團其他金融線（證券、期貨）可能也是後續 cross-sell 機會
- 風險：皇御若已是 LMAX / Saxo Prime 的金客戶，xSyphon 的金產品線要靠 XAU/CNH 差異化勝出

## Cross-sell 機會
- **第一階段**（now → 3 個月）：xSyphon XAU/CNH 試接 + Syphon Connect shadow 分析（如有 FX 業務）
- **第二階段**（3-6 個月）：xSyphon 完整 metals LP + EM FX
- **第三階段**（6-12 個月）：若皇御擴 Crypto CFD → xSyphon Crypto；若擴 FX 業務 → Connect 升 A/B Book
- **不推**（暫時）：Evo full stack（除非集團主動表達 stack 重構意願）、White Label（已有自家品牌）
