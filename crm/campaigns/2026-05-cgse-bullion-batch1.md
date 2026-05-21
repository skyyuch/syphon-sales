---
campaign: 2026-05 CGSE Bullion Dealer Outreach — Batch 1
segment: cgse-bullion
status: planning  # planning / active / completed / aborted
launch_date: 2026-05-26
close_date: 2026-07-15  # 預估，含 follow-up #3 + 緩衝
prospects_count: 5
total_estimated_arr_usd: 750000
owner: me
playbook: cgse-bullion-dealer
templates_used:
  - cgse-bullion-lp-cold-tc-v1
  - cgse-bullion-whitelabel-cold-tc-v1
  - cgse-bullion-followup-tc-v1
---

# Campaign — 2026-05 CGSE Bullion Dealer Batch 1

## 目標
- 驗證 CGSE 金商 segment 的 outreach 模板回應率（baseline 數據）
- 確認 XAU/CNH 為錨的話術是否能引出 discovery call
- 識別 5 家中最快回應 / 最不回應的特徵，校準後續 batch 的篩選邏輯

## KPI
| 指標 | 目標 | Stretch |
|------|------|---------|
| Cold email open rate | > 40% | > 60% |
| Cold email reply rate | > 10% (至少 1 家回) | > 20% (2 家回) |
| Discovery call 成交數 | ≥ 1 | ≥ 2 |
| 至少進入 qualified status | ≥ 1 家 | ≥ 2 家 |

> **這是 batch 1，主要目的是學習**。即使 5 家全部無回應，也能得出「模板需調整」的明確 signal。

---

## 發送排程總表

> **設計原則**：
> - 避開週一（金商週末復盤忙）、週五下午（亞洲時段量大）
> - 5 家錯開 2-3 個工作天，避免 follow-up 同日湧入
> - 規模較大 / 模板穩的先發（測試模板效果，再決定後續調整）
> - ICP 待驗證的（皇御、信譽金）放後面 → 給時間先驗證 ICP

| # | 公司 | 路徑 | 首封日 | F/U #1 (D+7) | F/U #2 (D+21) | F/U #3 (D+35) | 結案判斷 |
|---|------|------|--------|--------------|---------------|---------------|----------|
| 1 | 領峰貴金屬（Acetop, #145） | LP | **2026-05-26 (二)** | 2026-06-04 (四) | 2026-06-18 (四) | 2026-07-02 (四) | 2026-07-03 |
| 2 | 百利好金融（Plotio, #126） | LP | **2026-05-28 (四)** | 2026-06-08 (一) ⚠️ | 2026-06-22 (一) ⚠️ | 2026-07-06 (一) ⚠️ | 2026-07-07 |
| 3 | 皇御金融（Royal Capital, #076） | LP+多產品 | **2026-06-02 (二)** | 2026-06-11 (四) | 2026-06-25 (四) | 2026-07-09 (四) | 2026-07-10 |
| 4 | 第一亞洲商人（First Asia, #114） | LP（最弱 CTA） | **2026-06-04 (四)** | 2026-06-15 (一) ⚠️ | 2026-06-29 (一) ⚠️ | 2026-07-13 (一) ⚠️ | 2026-07-14 |
| 5 | 信譽金行（Goodwill, #050） | WL + LP fallback | **2026-06-09 (二)** | 2026-06-18 (四) | 2026-07-02 (四) | 2026-07-16 (四) | 2026-07-17 |

> ⚠️ **百利好 + 第一亞洲的 F/U 落在週一** —— 為避開「金商週末復盤忙」，這 6 個發送點建議**手動延後 1 天到週二**（即 06-09、06-23、07-07；06-16、06-30、07-14）。已在「每家詳細時間軸」內標出。

---

## 發送前 Master Checklist（首封發出**前 24 小時**完成）

### 系統 / 帳號層
- [ ] 已驗證所選 email 帳號的 SPF / DKIM / DMARC（避免進垃圾信）
- [ ] 確認近 14 天 sending volume 無暴增（IP 不被視為冷啟動 spam）
- [ ] Calendly link / 公司簽名 / 法律 footer 已備妥
- [ ] 若用 outreach tool（Apollo / Lemlist / 其他）→ tracking pixel + reply detection 已啟用

### 素材層（**這是當前最大 blocker**）
- [ ] `xSyphon_XAU_CNH_for_HK_Bullion_TC.pdf` — Follow-up #1 LP 必備
- [ ] `CGSE_Bullion_FX_Expansion_ROI_TC.xlsx` — Follow-up #1 WL 必備（給信譽金）
- [ ] `2026_H1_CGSE_Bullion_LP_Report.pdf` — Follow-up #3 LP 用
- [ ] 匿名同業 case study 內部資料 — Follow-up #2 WL 用（需 NDA confirmation）
- [ ] Calendly 已設「30 分鐘 CGSE 金商 discovery call」事件類型 + 繁中描述

### 內容層（每家發送當天 morning check）
- [ ] 對方關鍵人物（Head of Dealing / IB 主管）姓名、稱呼、email 已確認（LinkedIn / 官網驗證）
- [ ] hydrated variant 中所有 `[替換項]` 已填入真實值
- [ ] `{{specific_observation}}` 是**我親自看到的事實**（不是 AI 推測）
- [ ] 主旨無 `Re:` 或全大寫（avoid spam filter）
- [ ] 連結 hover 預覽正確（Calendly / 附件）

---

## 每家詳細時間軸

### 1. 領峰貴金屬 Acetop（#145） — LP path

| 日期 | 星期 | 動作 | 模板 | 備註 |
|------|------|------|------|------|
| 2026-05-26 | 二 | **首封 cold** | `cgse-bullion-lp-cold-tc-v1.md` Variant A | 第一個發，驗證模板效果 |
| 2026-06-04 | 四 | Follow-up #1 | `cgse-bullion-followup-tc-v1.md` Variant A1 | 附 XAU/CNH 1-pager |
| 2026-06-18 | 四 | Follow-up #2 | 通用 Track A #2 | 換角度：宏觀數據 |
| 2026-07-02 | 四 | Follow-up #3 / Breakup | 通用 Track A #3 | Closing loop + 行業報告 |
| 2026-07-03 | 五 | **降 P2** 若無回應 | 更新 `crm/prospects/acetop-precious-metals.md` frontmatter | `priority: P2` |

**判斷成功**：開信即正向信號；回信任何形式（含「先不需要」）已是 above average。

---

### 2. 百利好金融 Plotio（#126） — LP path（IB-heavy 強調 SG1 深度）

| 日期 | 星期 | 動作 | 模板 | 備註 |
|------|------|------|------|------|
| 2026-05-28 | 四 | **首封 cold** | `cgse-bullion-lp-cold-tc-v1.md` Variant B | 強調亞洲時段 SG1 深度 |
| 2026-06-09 | 二 | Follow-up #1 | Variant B1（待 hydrated）⚠️延後自原 06-08 一 | 附 XAU/CNH 1-pager |
| 2026-06-23 | 二 | Follow-up #2 | ⚠️延後自原 06-22 一 | 換角度：IB 結構洞察 |
| 2026-07-07 | 二 | Follow-up #3 / Breakup | ⚠️延後自原 07-06 一 | Closing loop |
| 2026-07-08 | 三 | **降 P2** 若無回應 | 更新 prospect frontmatter | |

---

### 3. 皇御金融 Royal Capital（#076） — LP + 多產品打包

| 日期 | 星期 | 動作 | 模板 | 備註 |
|------|------|------|------|------|
| **～2026-06-01** | – | **ICP 驗證 deadline** | LinkedIn + 官網 | 確認集團無 institutional/prime 業務，否則改路徑或降級 |
| 2026-06-02 | 二 | **首封 cold** | `cgse-bullion-lp-cold-tc-v1.md` Variant C | 多產品打包話術 |
| 2026-06-11 | 四 | Follow-up #1 | Variant C1（待 hydrated） | 附 XAU/CNH 1-pager + 多產品價值 |
| 2026-06-25 | 四 | Follow-up #2 | 通用 Track A #2 | |
| 2026-07-09 | 四 | Follow-up #3 / Breakup | 通用 Track A #3 | |
| 2026-07-10 | 五 | **降 P2** 若無回應 | | |

> ⚠️ 若 06-01 前驗證發現皇御**有** institutional 業務 → 取消此 campaign 排程，僅保留 prospect 檔案，未來改用 Syphonix-only 路徑單獨 outreach。

---

### 4. 第一亞洲商人金融 First Asia Merchants（#114） — LP 最弱 CTA

| 日期 | 星期 | 動作 | 模板 | 備註 |
|------|------|------|------|------|
| 2026-06-04 | 四 | **首封 cold** | `cgse-bullion-lp-cold-tc-v1.md` Variant D | **CTA 是要 1-pager 不是通話** |
| 2026-06-16 | 二 | Follow-up #1 | Variant D1（待 hydrated）⚠️延後自原 06-15 一 | |
| 2026-06-30 | 二 | Follow-up #2 | ⚠️延後自原 06-29 一 | |
| 2026-07-14 | 二 | Follow-up #3 / Breakup | ⚠️延後自原 07-13 一 | |
| 2026-07-15 | 三 | **降 P2** 若無回應 | | |

> 第一亞洲是 5 家中估 ARR 最低（$90k），**重點是測試「最弱 CTA」對 reply rate 的影響**。對比 Variant A/B/C 收集模板學習素材。

---

### 5. 信譽金行 Goodwill Gold Group（#050） — White Label + LP fallback

| 日期 | 星期 | 動作 | 模板 | 備註 |
|------|------|------|------|------|
| **～2026-06-08** | – | **ICP 驗證 deadline** | LinkedIn + 官網 + 新聞 | 驗證信譽金是否有 FX 擴張信號 |
| 2026-06-09 | 二 | **首封 cold** | `cgse-bullion-whitelabel-cold-tc-v1.md` Variant Goodwill | 內含 LP fallback CTA |
| 2026-06-18 | 四 | Follow-up #1 | Variant Goodwill1 | 附 ROI 計算表 |
| 2026-07-02 | 四 | Follow-up #2 | 通用 Track B #2 | 匿名同業 case study |
| 2026-07-16 | 四 | Follow-up #3 / Breakup | 通用 Track B #3 | |
| 2026-07-17 | 五 | **降 P2** 若無回應 | | |

> ⚠️ 若 06-08 前驗證發現信譽金**無** FX 擴張信號 → 改用 LP path 模板（同 4 家通用），收回 WL Hydrated Variant 留下次測試。

---

## 收回覆接管流程

**收到任何回覆當下立即執行**：

1. **停止此公司的後續 follow-up**（從 calendar 移除排程，避免 cadence + 個人回應同時發出）
2. **更新 `crm/prospects/<company>.md`**：
   - frontmatter：`status: qualified`（如對方願意 demo） / `last_contact: <date>`
   - 加入互動紀錄（管道、摘要、對方說了什麼）
3. **24 小時內個人回覆**（不要再用 template，要真人寫）
4. **依 `playbooks/cgse-bullion-dealer.md` Discovery 流程接續**
5. **若安排 discovery call** → 用 `templates/pitch/cgse-bullion-discovery-call-tc-v1.md` 準備

**回覆語氣分類** → 接管動作：

| 對方回覆類型 | 動作 |
|-------------|------|
| 「有興趣，安排 call」 | Calendly 立即發；prospect → `qualified` |
| 「先發資料看看」 | 個人化發 1-pager + 提一個 follow-up 問題；prospect 維持 `prospect` |
| 「目前不需要 / 已有 LP」 | 禮貌回覆 + 標記 6 個月後再試；prospect 維持 `prospect` |
| 「請聯絡 XXX」（內部轉介） | 立即去信新 contact，引述對方建議；prospect 不變 |
| OOO（自動回覆） | 不算回覆，繼續 cadence |
| 拒絕 / unsubscribe | prospect → `lost` + 寫原因 |

---

## 降級 / 結案規則

### 自動降 P2 的條件（無需我額外判斷）
- Follow-up #3 發出後 + 1 個工作天仍無任何回應
- 對方明確「現在不需要 + 短期內也不會」

### 提早結束 cadence 的條件
- 收到任何「請勿再聯絡」訊息 → 立即停止 + `status: lost`
- 對方公司被 CGSE 列入「觀察行員名單」 → 暫停 cadence，等狀態確認
- 對方公開有合併 / 收購 / 重大重組新聞 → 暫停 4-6 週

### 6 個月後重試的 trigger
- 對方公司新聞：擴 FX、新聘 Head of Trading、IPO、新地區擴張
- 行業事件：人民幣金重大波動、LP 行業整合
- 重新試時建新 campaign（不要 reuse 此檔案）

---

## 數據追蹤表（每封發送後 7 天內更新）

### Cold（首封）
| 公司 | 發送日 | Sent | Opened | Replied | Reply Type | Notes |
|------|--------|------|--------|---------|------------|-------|
| 領峰 | 2026-05-26 | – | – | – | – | – |
| 百利好 | 2026-05-28 | – | – | – | – | – |
| 皇御 | 2026-06-02 | – | – | – | – | – |
| 第一亞洲 | 2026-06-04 | – | – | – | – | – |
| 信譽金 | 2026-06-09 | – | – | – | – | – |

### Follow-up #1
| 公司 | 發送日 | Sent | Opened | Replied | Notes |
|------|--------|------|--------|---------|-------|
| 領峰 | 2026-06-04 | – | – | – | – |
| 百利好 | 2026-06-09 | – | – | – | – |
| 皇御 | 2026-06-11 | – | – | – | – |
| 第一亞洲 | 2026-06-16 | – | – | – | – |
| 信譽金 | 2026-06-18 | – | – | – | – |

### Follow-up #2 / #3
> 待 #1 數據收齊後再決定是否填表 —— 若 5 家全部 #1 後仍 0 回應，**模板有問題，應該調整模板而不是發 #2**。

---

## Campaign Retrospective（campaign 結束後填）

### 結果摘要
- Total sent: __
- Total opens: __ (rate __%)
- Total replies: __ (rate __%)
- Discovery calls 成交: __
- Qualified 數: __
- Lost 數（明確拒絕）: __
- 降 P2 數: __

### 學到的事
- 哪個 Variant reply rate 最高？為什麼？
- 哪個 hook（XAU/CNH / IB 賣點 / 多產品 / WL）最有共鳴？
- CTA 強弱對 reply rate 的影響？
- 哪些對方異議是模板沒覆蓋的？

### 對下一 batch 的啟示
- 模板要改的部分：
- 排程節奏要調的部分：
- 額外要準備的素材：

### 知識庫沉澱
- [ ] 新異議補進 `knowledge-base/faq/objection-handling.md`
- [ ] 新洞察補進 `playbooks/cgse-bullion-dealer.md`
- [ ] 模板更新到 v2（如改動 > 結構性）
