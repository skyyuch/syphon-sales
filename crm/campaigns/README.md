# Campaigns — 發送活動 / Outreach Cadence 管理

> 多個 prospect 的「批次發送計劃」放這裡。單一 prospect 的互動紀錄仍在 `crm/prospects/<company>.md`。

## 命名規範
`YYYY-MM-<segment>-<batch-name>.md`

範例：
- `2026-05-cgse-bullion-batch1.md` — 2026 年 5 月，CGSE 金商第一批
- `2026-07-au-pure-retail-batch1.md` — 2026 年 7 月，澳洲純零售第一批

## 每個 campaign 檔案的結構
1. **Campaign metadata**（segment、prospects 列表、KPI）
2. **發送排程表**（每家何時發 cold / follow-up #1/2/3）
3. **發送前 checklist**（素材、變數、IP warm-up）
4. **收回覆接管流程**（如何脫離 cadence 進入 discovery）
5. **降級 / 結案規則**（什麼時候判定「無回覆」）
6. **數據追蹤表**（每封 sent / open / reply）

## 與其他資料夾的關係
| 資料夾 | 內容 |
|--------|------|
| `crm/prospects/` | 個別 prospect 檔案 — 單一公司完整 context |
| `crm/active-deals/` | 已脫離 cadence、進入正式商談 |
| `crm/campaigns/` | **batch 級執行排程** — 跨多家的時間軸 |
| `templates/email/` | 模板本體（可被多個 campaign 重用） |
| `playbooks/` | 銷售方法論（不變的策略） |

## 何時建新 campaign
- 累積 3+ 個同 segment prospect 要同時 outreach
- 或單一大客戶需要多輪精細編排（給該大客戶獨立 campaign 檔）

## 何時結案 campaign
- 全部 prospects 已脫離 cadence（成交 / 降級 P2 / 拒絕）
- 改 frontmatter `status: closed` + 寫一段 retrospective（reply rate、學到什麼）
- 不要刪除 —— 是未來 batch 的學習素材
