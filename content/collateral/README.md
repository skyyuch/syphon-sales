# Sales Collateral — 銷售輔助素材

> 與 `posts/` / `insights/` / `case-studies/` 不同 —— Collateral 是**直接給 prospect 的 leave-behind 素材**：1-pager、ROI 計算表、product sheet、proposal cover、等。

## 三個原則
1. **每份 collateral 對應一個具體銷售情境**（不是「通用品牌素材」）
2. **能單獨成立**：對方收到附件可以不看 email 也理解
3. **行動導向**：每份末尾有清楚 CTA（聯絡誰、做什麼）

## 命名規範
`<topic>-for-<audience>-<format>-<lang>-v<n>.md`

範例：
- `xau-cnh-for-cgse-bullion-1pager-tc-v1.md`
- `cgse-bullion-fx-expansion-roi-en-v1.md`
- `xsyphon-onboarding-proposal-cover-en-v1.md`

## 此資料夾與外部設計工具的關係
這裡的檔案是**內容稿 + 設計建議 + placeholder 標注**，**不是最終 PDF / Figma**。
- Markdown 是源文件（version control、AI editable）
- 排版輸出到 PDF / PNG 後存到外部（Google Drive / Notion / 公司 DAM）
- 對應 PDF 的 link / file name 在 markdown 內標注

## Placeholder 規範
所有需要從產品團隊 / 行銷團隊 / 法務團隊取得的具體數字，標注：
- `[需產品團隊提供：xxx]` — 紅色，發送前必須填
- `[需法務確認：xxx]` — 紅色，發送前必須填
- `[2025 公開資料，待 2026 更新：xxx]` — 黃色，可暫用但要更新

## 何時建新版本（v2、v3）
- 結構性改動（章節順序、CTA 大改、語言對換）→ 新主版本
- 數據更新、錯字、小幅措辭 → 直接改 v1，記 changelog

## 與其他資料夾的關係
| 資料夾 | 用途 |
|--------|------|
| `templates/email/` | Outreach 與 follow-up 模板（**內含 collateral 引用**）|
| `templates/pitch/` | Discovery / demo 腳本 |
| `content/posts/` | LinkedIn 短文（建立品牌） |
| `content/insights/` | 長文洞察（建立 thought leadership） |
| `content/case-studies/` | 成單後的客戶案例 |
| **`content/collateral/`** | **發給 prospect 的 leave-behind 素材** |
