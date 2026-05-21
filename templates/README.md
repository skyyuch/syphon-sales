# 銷售模板庫

## 結構
- `email/` — 郵件模板（cold、follow-up、proposal cover）
- `linkedin/` — LinkedIn connection、InMail、回覆模板
- `pitch/` — Pitch deck 大綱、demo 腳本

## 變數系統
所有模板用 `{{variable}}` 標記變數，常用：
- `{{first_name}}` — 對方稱呼
- `{{company}}` — 對方公司
- `{{role}}` — 對方職位
- `{{pain_point}}` — 推測的痛點
- `{{specific_observation}}` — 我對他們的具體觀察（讓 email 不像群發）
- `{{cta}}` — Call to action（連結或具體要求）

## 命名範例
- `email/cold-broker-uk-v1.md`
- `email/followup-no-reply-7day-v1.md`
- `linkedin/connection-cto-v1.md`
- `pitch/whitelabel-3min-demo-v1.md`

## 何時建立新模板
- 同一情境用了 3 次以上 → 提取成模板
- 一個模板回應率特別好 → 開 v2 並標記為主推

## A/B 測試紀錄
所有模板底部記：
- 發送次數
- 開信率 / 回覆率
- 改版日期 + 改了什麼
