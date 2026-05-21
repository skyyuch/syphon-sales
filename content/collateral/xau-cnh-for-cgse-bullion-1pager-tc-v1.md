# 1-Pager — XAU/CNH for CGSE Bullion Dealers (繁中為主) v1

**Use case**：發給 CGSE E-Trading 金商作為 follow-up 附件 / discovery call leave-behind / IB partner-facing material
**Audience**：
- 主要：金商 Head of Dealing / 老闆
- 次要：金商 IB 主管（可能直接 forward 給 IB 看）
- 三級：IB 自己看（再 forward 給中國終端客戶）
**Format**：A4 雙面 PDF（中文正面 + 英文背面）
**Language**：繁中為主、英文小字標注關鍵術語 + 完整英文版於背面
**Lifetime**：6 個月（2026 H2 數據更新時改 v2）

> 配合 follow-up：`templates/email/cgse-bullion-followup-tc-v1.md` Track A #1
> 配合 playbook：`playbooks/cgse-bullion-dealer.md`

---

## 三層讀者的閱讀路徑（設計時必須考慮）
| 讀者 | 閱讀時間 | 最重要看到的 |
|------|---------|------------|
| 金商老闆 | 30 秒 | 「這對我的 IB / 我的 P&L 有什麼價值」 |
| IB 主管 | 1-2 分鐘 | 「我能不能用這個拿新客戶 / 留住舊客戶」 |
| 終端客戶（中國散戶） | 看不到，由 IB 口述轉譯 | （IB 主管會抽 3 句話給客戶聽） |

→ 設計上：**最頂部 hero 區必須在 5 秒內傳達商業價值**（不是技術規格）。

---

## 設計 / 排版建議

### 整體
- **A4 直版**（210 × 297 mm），雙面
- **繁中正面 + 英文背面**（金商給合規 review 通常要英文版）
- **印刷品質**：可印刷但主要為 PDF 數位閱讀

### 顏色
- **主色**：xSyphon 品牌色（待確認，建議深藍 #1A2B4A 或墨綠 #1F3A2E）
- **強調色**：金色 #C9A961（呼應「金」業務）
- **警示 / 重點**：磚紅 #B33A3A（用於「獨家」、「bilateral」這類詞）
- **背景**：暖白 #FAF8F4（避免純白刺眼）

### 字體
- **繁中標題**：思源宋體 / 蘋方繁體 Bold
- **繁中內文**：思源黑體 / 蘋方繁體 Regular
- **英文 / 數字**：Inter 或 IBM Plex Sans（搭配繁中黑體）
- **數字強調**：等寬字（避免不同寬度的「99.7%」變形）

### 視覺元素
- 一個 **hero icon** 或 abstract graphic（金條 + 人民幣符號交疊，**抽象化避免商標問題**）
- 1-2 個 **數據圖表**（spread 對比柱狀 + 深度堆疊）
- **xSyphon logo**（待確認最終 logo 檔案）
- **CGSE 提及**：**不要**放 CGSE logo（避免被誤認背書），用文字「適用於 CGSE Recognized E-Trading Members」即可
- 二維碼（連結到 Calendly 或 1-pager 完整版線上頁面）

---

## 正面內容（繁體中文）

> 以下為**完整文字稿**，可直接交設計師排版。`[xxx]` 為 placeholder。

---

### Hero 區（頂部 1/4 頁）

**主標題（大字 / 36pt+）**
> XAU/CNH — 給香港金商的獨家機會

**副標題（中字 / 20pt）**
> 中國離岸人民幣計價 loco London 金，**bilateral 雙邊報價**，不是 cross 合成。

**Hero metric box（三個並列方塊）**
| 指標 | 數值 |
|------|------|
| 報價類型 | **Bilateral**（雙邊直接報價） |
| Onboarding | **5-10 個工作天** |
| 最低 ticket | [需產品團隊提供：50g 起] |

---

### Why Now（為什麼是現在）

**Section 標題**
> 為什麼您的 IB 開始問人民幣金

**內文（3 段，每段 1-2 句）**

中國離岸人民幣（CNH）資產配置近三年複合增長率約 [需研究：建議引用 SWIFT 2026 Q1 RMB Tracker 數字 25-30%]，香港作為 CNH 最大離岸中心，存款規模超過 [需更新：截至 2025 約 8,000 億 RMB]。

亞洲零售投資者對「人民幣計價 + 倫敦金深度」的雙重需求顯著上升 —— 既要對沖人民幣貶值風險，又要 loco London 流動性。

但本地金商普遍給不出 XAU/CNH 的 **bilateral 直接報價**，多數方案是 XAU/USD × USD/CNH 的 cross 合成，spread 寬、深度薄。

> **小字註腳**：數據來源 — SWIFT RMB Tracker 2026 Q1 / 香港金管局 [HKMA] CNH Deposit Statistics

---

### What We Offer（產品規格）

**Section 標題**
> xSyphon XAU/CNH 規格

**規格表（4 欄表格）**

| 維度 | xSyphon XAU/CNH | 市場常見 cross 合成 |
|------|----------------|---------------------|
| 報價類型 | **Bilateral 雙邊** | XAU/USD × USD/CNH 合成 |
| 典型 spread | [需產品團隊提供：例 $X.XX / oz] | [需產品團隊提供：例 $Y.YY / oz，比 xSyphon 寬 N%] |
| 深度（亞洲時段 SG1） | [需產品團隊提供：top-of-book $X kg available] | 散布於兩個合成 leg，不穩定 |
| 最低 ticket | 50g 起 | 依 cross leg 不同 |
| Last look | **零 last look** | 視 LP |
| 結算 | T+2 | T+2 |
| 24h 報價 | 是 | 視 LP 拼接 |

**Co-location（5-10 工作天 onboarding 的技術基礎）**
- LD4（倫敦）/ NY4（紐約）/ TY3（東京）/ **SG1（新加坡，亞洲時段最深）**

---

### Why xSyphon（信任建立）

**Section 標題**
> 為什麼是 xSyphon

**4 個 bullet（每個 1 行）**
- 機構級流動性聚合：12+ Tier-1 prime brokers，日均成交量 $1B+
- **零 last look**，合約明寫
- 持牌 LP：**Mauritius FSC (License No. GB25204632)**，合規 MiFID II / UK FCA 框架
- 客戶 base 已覆蓋亞洲多家機構，文件流程順 → 不是 3-6 個月，是 5-10 工作天

---

### For Your IB（給金商銷售團隊看的價值）

**Section 標題**
> 給貴司 IB 多一個別人沒有的賣點

**內文（2 段）**

中國 IB 客戶持續詢問人民幣計價的離岸金產品。本地金商若能提供 **bilateral XAU/CNH**（而非 cross 合成），等於給 IB 一個新的差異化故事 —— 既不影響既有金業務，又拉新客戶 / 留住舊客戶。

**典型整合場景**：
- ✅ 新增到既有金商品列表，**不替換**任何現有 LP
- ✅ 給 IB 推 marketing material（中文版），可直接 forward 給終端客戶
- ✅ Bilateral spread 比合成穩定，IB 可給客戶承諾「無 widening surprise」

---

### CTA（底部 1/5 頁）

**主標題**
> 想看一份貴司的 connectivity proposal？

**內文（3 行）**
- 給我們大致的 daily 金 volume + IB 結構
- 24 小時內收到 tailored 報價樣本 + commercial 結構 + onboarding timeline
- 或 15 分鐘簡短電話：[Calendly link 二維碼]

**聯絡資訊**
- 業務聯絡：[姓名] / [email] / [電話]
- xSyphon Ltd / Mauritius FSC GB25204632
- xsyphon.com

---

## 背面內容（English）

> Same structure, English version for compliance review.

---

### Hero
**Title**：XAU/CNH — Exclusive Opportunity for HK Bullion Dealers
**Subtitle**：Offshore CNY-denominated loco London Gold. **Bilateral pricing, not synthetic cross.**

**Hero metric box**
| Metric | Value |
|--------|-------|
| Pricing | **Bilateral** (direct) |
| Onboarding | **5-10 business days** |
| Min ticket | [TBD: 50g+] |

---

### Why Now

**Heading**：Why your IBs are starting to ask for CNH-priced gold

The offshore CNY (CNH) asset allocation pool has grown at [TBD: cite SWIFT 2026 Q1 ~25-30% CAGR] over the past three years. Hong Kong, as the largest CNH offshore center, holds over [TBD: ~RMB 800B in CNH deposits as of 2025].

Asian retail investors increasingly demand **CNH-denominated loco London gold** — they want both yuan-hedging optics and London-grade liquidity in a single product.

But most bullion dealers can't offer **bilateral XAU/CNH pricing**. The common workaround — synthesizing via XAU/USD × USD/CNH — produces wider spreads and fragmented depth.

> Sources: SWIFT RMB Tracker 2026 Q1, HKMA CNH Deposit Statistics

---

### What We Offer

**Heading**：xSyphon XAU/CNH Specifications

| Dimension | xSyphon XAU/CNH | Synthetic Cross |
|-----------|----------------|-----------------|
| Pricing | **Bilateral** | XAU/USD × USD/CNH |
| Typical spread | [TBD] | [TBD, wider by N%] |
| Depth (Asia / SG1) | [TBD] top-of-book | Split across legs |
| Min ticket | 50g | Depends on legs |
| Last look | **None** | LP-dependent |
| Settlement | T+2 | T+2 |
| 24h streaming | Yes | LP-dependent |

**Co-location**：LD4 / NY4 / TY3 / **SG1 (deepest in Asia hours)**

---

### Why xSyphon

- Institutional aggregation: 12+ Tier-1 prime brokers, $1B+ daily notional
- **Zero last look**, contractually
- Licensed LP: **Mauritius FSC (License No. GB25204632)**, MiFID II / UK FCA aligned
- Asian institutional client base already onboarded → 5-10 business days, not 3-6 months

---

### For Your Sales Team

**Heading**：A new story for your IBs

Mainland Chinese IBs are increasingly asked for offshore CNY-denominated gold products. Bullion dealers offering **bilateral XAU/CNH** (not synthetic) give their IBs a differentiated narrative — adding a new revenue stream without disrupting existing gold flow.

**Typical integration**：
- ✅ Adds to your existing product list, **replaces nothing**
- ✅ IBs can pitch with branded marketing collateral (Chinese version available)
- ✅ Bilateral spread is stable — IBs can promise clients "no widening surprise"

---

### CTA
**Heading**：Want a connectivity proposal tailored to your flow?

- Share rough daily gold volume + IB structure
- Receive within 24 hours: indicative pricing + commercial structure + onboarding timeline
- Or a 15-min call: [Calendly QR]

**Contact**
- [Name] / [email] / [phone]
- xSyphon Ltd / Mauritius FSC GB25204632
- xsyphon.com

---

## 發送前 Checklist（**這份 1-pager 必須完成才能用**）

### 內容層（**最重要的 blocker**）
- [ ] **產品團隊提供具體 XAU/CNH spread 數字**（例 "$0.35 / oz at top-of-book"）
- [ ] **產品團隊提供深度數字**（例 "$2M top-of-book during Asia hours"）
- [ ] **產品團隊提供最低 ticket**（公開文件是 50g 起，需確認是否仍是這個數字）
- [ ] **行銷團隊提供 vs 市場 cross 合成的具體對比** spread / 深度差異
- [ ] **市場研究團隊提供最新 CNH 宏觀數據**（SWIFT、HKMA、BIS 三選一引用）
- [ ] **法務確認**：「適用於 CGSE Recognized E-Trading Members」這句措辭不構成擔保 / 背書

### 設計層
- [ ] xSyphon 最終 logo 檔案
- [ ] 品牌色碼（hex code 確認）
- [ ] 設計師 / Canva 模板 ready
- [ ] Calendly link 已設置（建議專屬此 campaign 的 event type，方便追蹤）
- [ ] PDF 輸出後 file size < 2MB（避免被 email 過濾）

### 發行層
- [ ] PDF 命名規範：`xSyphon_XAU_CNH_for_HK_Bullion_TC_2026Q2_v1.pdf`
- [ ] 上傳到 Google Drive / Notion，取得**可直接點開的 link**（不要要求對方下載）
- [ ] 同步 attachment 版本（金商保守，部分人不點 link）
- [ ] 內部 share to BD team + 業務團隊

### 法務 / 合規層
- [ ] Footer 加入 disclaimer：「This document is for informational purposes only and does not constitute an offer to provide liquidity services. Terms subject to final agreement.」
- [ ] FSC license number 顯示位置 + 字級符合 Mauritius FSC marketing material 規範
- [ ] CNH 相關市場數據引用 source（避免被認為自造數字）
- [ ] 「Bilateral pricing」措辭法務 review（technical term，不能 mislead）

---

## 二代版本（v2）的潛在改進方向
- 加入**匿名 case study side bar**（首家用戶上線後 1 個月的 IB 反饋）
- 加入**spread heat map**（不同時段 / 不同 size 的 spread 動態）
- 加入**vs CGSE 場內人民幣公斤金條合約**的對比（差異化：場內合約是 spot 無 leverage、xSyphon 是 CFD 可 leverage）
- 中文版加入**簡體版**（給 IB 直接 forward 給中國大陸客戶）
- **行動版排版**（不只 A4，加一個正方形 social post 版）

---

## 配合素材（後續可建）
- [ ] `xau-cnh-spread-comparison-deck-tc-v1.md` — 給 discovery call 的 demo deck
- [ ] `xau-cnh-faq-tc-v1.md` — IB / 終端客戶常見問題 + 標準答覆
- [ ] `cgse-bullion-onboarding-checklist-tc-v1.md` — 簽約後的 onboarding 清單

---

## Changelog
- v1 (2026-05-21): initial content draft, awaiting product team data and design execution

## Production Status
- [ ] Content reviewed by self
- [ ] Content reviewed by product team
- [ ] Content reviewed by legal
- [ ] Design draft (designer / Canva)
- [ ] Final PDF produced
- [ ] Link / file shared with BD team
- [ ] **Ready to send** ← 必須勾選此項才能發出 follow-up #1
