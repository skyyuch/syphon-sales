# CRM — 客戶資料管理

> 所有客戶 / 潛客資料的單一真相來源（single source of truth）。

## 三階段
```
prospects/      → 未進入正式商談
active-deals/   → 有明確商機、推進中
closed/         → 成交 / 放棄
```

## 新增 prospect 步驟
1. 從 `prospects/_template.md` 複製一份
2. 改名為 `<company-slug>.md`（小寫、連字符）
3. 填好 frontmatter
4. 加入第一筆互動紀錄

## Frontmatter 必填欄位（給 AI 易讀）
```yaml
---
company: 
website: 
country: 
type: retail-broker | prop-trading | hedge-fund | pop | asset-manager | bank | psp | new-entrant
size: <1B-daily | 500M-1B-daily | 100M-500M-daily | <100M-daily
regulator: 
status: prospect | qualified | proposal | negotiating | won | lost
first_contact: YYYY-MM-DD
last_contact: YYYY-MM-DD
priority: P0 | P1 | P2
products_interested: [xsyphon-fx, xsyphon-metals, xsyphon-crypto, syphon-connect, syphon-evo, syphon-whitelabel]
estimated_arr_usd: 
---
```

## 移動規則
- prospect → active-deal：對方明確表達評估意願 + 開始討論商業條款
- active-deal → won/lost：合約簽署 / 對方明確拒絕 / 6 個月無進度

## AI 可以幫我做什麼
- 每週列出「該跟進」的清單（last_contact > 7 天 + status active）
- 標記交叉銷售機會（已用 xSyphon LP 但沒提過 Syphonix 的客戶）
- 異常偵測：突然 inactive 的高優先客戶
