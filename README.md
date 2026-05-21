# Syphon Sales Workspace

> Business Development workspace for **xSyphon**（流動性提供商）+ **Syphonix**（AI 執行系統）。
> 長期、可累積、AI 協作優先。

---

## 重要：開新 agent 前先讀這裡

每次開新對話，Cursor 會自動載入 `.cursor/rules/` 下所有 `alwaysApply: true` 的 rules。
**不需要每次重新解釋公司背景。**

讀 rules：
- `00-company-overview.mdc` — 兩家公司的關係與產品全貌
- `01-my-role.mdc` — 我的崗位與 AI 工作邊界
- `02-workflow.mdc` — 每次修改前必須做什麼
- `03-language-style.mdc` — 中英混合 + 寫作風格
- `04-knowledge-base.mdc` — 知識庫維護（globs: `knowledge-base/**`）
- `05-crm.mdc` — 客戶資料管理（globs: `crm/**`）
- `06-templates.mdc` — 模板管理（globs: `templates/**`）
- `07-git-versioning.mdc` — Git commit / push / 敏感資料規範

---

## Repo

- **GitHub**：https://github.com/skyyuch/syphon-sales（**Private**，含真實客戶資料）
- **Remote**：`git@github.com:skyyuch/syphon-sales.git`（SSH）
- **Branch**：`main`

---

## 資料夾結構

```
syphon-sales/
├── .cursor/rules/          # AI 規則（每次對話自動載入）
├── knowledge-base/         # 產品 / 競品 / FAQ 知識庫
│   ├── products/           # ★ xsyphon.md, syphonix.md, cross-sell-matrix.md
│   ├── competitors/        # 競品研究
│   └── faq/                # ★ objection-handling.md（含 CGSE 金商異議）
├── templates/              # 銷售模板（可重用）
│   ├── email/              # Cold email、follow-up
│   ├── linkedin/           # Connection note、InMail
│   └── pitch/              # Demo 腳本、Discovery 問題
├── crm/                    # 客戶資料（single source of truth）
│   ├── prospects/          # 潛客（單一公司 context）
│   ├── active-deals/       # 推進中
│   ├── closed/             # 已成 / 已棄
│   └── campaigns/          # ★ 批次發送排程（跨多家的時間軸）
├── playbooks/              # 銷售劇本（不變的策略）
│   ├── new-broker-launcher.md
│   ├── existing-broker-upgrade.md
│   ├── pop-institutional.md
│   └── cgse-bullion-dealer.md  # ★ HK 金銀業貿易場金商
├── research/               # 市場研究
│   ├── market/
│   ├── competitors/        # 事件追蹤（與 knowledge-base/competitors 不同）
│   └── regulatory/
└── content/                # 內容素材
    ├── posts/              # LinkedIn 短文
    ├── case-studies/       # 客戶案例（成單後）
    ├── insights/           # 長文洞察
    └── collateral/         # ★ 給 prospect 的 leave-behind（1-pager、ROI 表）
```

★ = 已填好內容，可直接使用

### 三個關鍵分層（避免內容散落）

| 層 | 資料夾 | 性質 | 變動頻率 |
|----|--------|------|---------|
| **策略** | `knowledge-base/` + `playbooks/` | 方法論、ICP、產品規格 | 月度 |
| **資產** | `templates/` + `content/collateral/` | 可重用的素材 | 季度 |
| **執行** | `crm/prospects/` + `crm/campaigns/` | 具體 prospect + 排程 | 每天 |

---

## 日常工作流程

### 接觸新潛客（單一）
1. 找到對方公司 → 從 `crm/prospects/_template.md` 複製建檔
2. **必做：ICP 資格檢查**（依 `knowledge-base/products/cross-sell-matrix.md` 的 ICP 排除規則，特別檢查對方是否自己也是 LP）
3. 查 `knowledge-base/competitors/` 看對方目前用什麼
4. 對照 `cross-sell-matrix.md` 決定推什麼
5. 從 `playbooks/<對應劇本>.md` 找首次接觸話術
6. 從 `templates/email/` 或 `templates/linkedin/` 複用模板（可能要 hydrated variant）
7. 在 prospect 檔案加「相關檔案索引」section，列出該家對應的所有檔案路徑
8. 互動後立即更新 `crm/prospects/<company>.md` 互動紀錄

### 批次 outreach（3+ 家同 segment）
1. 把每家分別建 prospect 檔案（依上面流程）
2. 建 `crm/campaigns/YYYY-MM-<segment>-<batch-name>.md`
3. 排發送節奏（錯開週二/週四、避開週一週五下午）
4. 完成 Master Checklist（系統 / 素材 / 內容三層）
5. 依 calendar 執行；收回覆即脫離 cadence 進入 discovery
6. Campaign 結束寫 retrospective + 知識庫沉澱

### 對方提了新問題我答不出
1. 先答「讓我確認後回覆」
2. 確認後把問答補到 `knowledge-base/faq/objection-handling.md`（**按 segment 分類**）
3. 若是產品規格層級，補到對應 `knowledge-base/products/*.md`
4. 若是該 segment 普遍痛點，補到對應 `playbooks/<segment>.md` 的異議處理章節

### 製作新的 prospect-facing 素材
1. 從 `content/collateral/README.md` 看分類規範
2. 寫 `content/collateral/<topic>-for-<audience>-<format>-<lang>-v1.md`（內容稿 + placeholder + 設計建議）
3. 完成 4 層 pre-send checklist（內容 / 設計 / 發行 / 法務）
4. 對應 PDF 上傳外部後，在 markdown 內標注 link / file name

### 寫 LinkedIn 內容
1. 從 `content/README.md` 主題池選一個
2. 寫到 `content/posts/YYYY-MM-DD-<slug>.md`
3. 發布後記錄 engagement 數字

---

## 設計原則

1. **DRY**：同樣資訊不寫第二次
2. **Single source of truth**：客戶資料只在 CRM、產品規格只在 KB
3. **Markdown 優先**：易讀、易 diff、AI 友善
4. **Frontmatter 結構化**：方便 AI 批量處理

---

## TODO（後續可加值的方向）

- [ ] 接入 LinkedIn API 自動同步互動
- [ ] CRM frontmatter → CSV 匯出腳本
- [ ] 每週自動掃描「該跟進」清單的腳本
- [ ] Lead scoring 模型（基於 frontmatter）
- [ ] 安裝 Xcode CLI tools + Homebrew + `gh`，方便未來 GitHub 操作
