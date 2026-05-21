# Scripts — 營銷自動化工具

> Python 腳本，零外部依賴（用 stdlib 即可），把 markdown 內容變成可發送物料。

## 工具列表
| Script | 用途 |
|--------|------|
| `mail_merge.py` | 把 hydrated email variants + config → 5 個 `.txt` + 5 個 `.html` ready-to-send |

## 環境要求
- Python 3.8+（macOS 已內建 `python3`）
- **無需 pip install 任何套件**

---

## mail_merge.py 使用方法

### Step 1：複製 config example
```bash
cd scripts
cp config.example.py config.py
```

### Step 2：編輯 config.py
填入：
- `SENDER` 區塊：你的中英文姓名、email、Calendly link
- 5 家公司的 `contact_name`、`contact_title`、`contact_email`
  - 用 `crm/campaigns/2026-05-cgse-bullion-batch1-toolkit.md` 內的 LinkedIn URL 找出聯絡人
  - 用 Hunter.io / Apollo.io 推測 email 格式

### Step 3：跑腳本
```bash
python3 mail_merge.py
```

> **沒 config.py 也能跑！**腳本會自動 fallback 用 `config.example.py`，
> 輸出到 `output.example/cgse-batch1/`（已 commit 範例，供新 agent 對齊樣式）。
> 你的真實版本在 `output/cgse-batch1/`（已 gitignore）。

### Step 4：拿到 output
- `scripts/output/cgse-batch1/{company}-cold.txt` — 純文字 body，**直接複製貼 Gmail compose**
- `scripts/output/cgse-batch1/{company}-cold.html` — 瀏覽器打開預覽 email 長相
- `scripts/output/cgse-batch1/index.html` — 主控台，一覽 5 家連結 + blockers 狀態

### Step 5：發送
- Gmail 工作流：`open scripts/output/cgse-batch1/index.html` → 點對應 company →
  複製 `.txt` 內 body → 貼到 Gmail compose → 確認 To/Subject → Send
- Outlook 工作流（macOS）：雙擊 `.txt` 用文字編輯打開 → 複製 → 貼到 Outlook 草稿
- 已發送：手動更新 `crm/campaigns/2026-05-cgse-bullion-batch1-tracker.csv` 的 `cold_sent_date`

---

## 為什麼 config.py / output/ 不 commit
- `config.py` 含真實聯絡人 email（敏感）→ gitignore
- `output/` 含真實聯絡人 email + 個人簽名 → gitignore
- 每次跑都會覆蓋（不需要版本控制）

`scripts/output.example/` **有** commit，用範例 config 生成，全是 placeholder。
作用：未來新 agent / 新電腦 setup 時，可以對齊 output 樣式而不需自己跑。

---

## 未來可擴充
- [ ] `mail_merge_followup.py` — 自動依 calendar 算 follow-up #1/#2/#3 對應日期
- [ ] `linkedin_search_open.py` — 自動開啟 5 家的 LinkedIn search URL（用 `webbrowser` 模組）
- [ ] `crm_sync.py` — 把 `crm/prospects/*.md` frontmatter 匯出 CSV / 同步外部 CRM
- [ ] `tracker_update.py` — 從 Gmail API / IMAP 自動更新 tracker CSV 的 opened / replied 狀態
