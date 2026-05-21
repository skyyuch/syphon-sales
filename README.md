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

---

## 資料夾結構

```
syphon-sales/
├── .cursor/rules/          # AI 規則（每次對話自動載入）
├── knowledge-base/         # 產品 / 競品 / FAQ 知識庫
│   ├── products/           # ★ xsyphon.md, syphonix.md, cross-sell-matrix.md
│   ├── competitors/        # 競品研究
│   └── faq/                # ★ objection-handling.md
├── templates/              # 銷售模板
│   ├── email/              # Cold email、follow-up
│   ├── linkedin/           # Connection note、InMail
│   └── pitch/              # Demo 腳本、Discovery 問題
├── crm/                    # 客戶資料（single source of truth）
│   ├── prospects/          # 潛客
│   ├── active-deals/       # 推進中
│   └── closed/             # 已成 / 已棄
├── playbooks/              # 銷售劇本
│   ├── new-broker-launcher.md
│   ├── existing-broker-upgrade.md
│   └── pop-institutional.md
├── research/               # 市場研究
│   ├── market/
│   ├── competitors/        # 事件追蹤（與 knowledge-base/competitors 不同）
│   └── regulatory/
└── content/                # 內容素材
    ├── posts/              # LinkedIn 短文
    ├── case-studies/       # 客戶案例
    └── insights/           # 長文洞察
```

★ = 已填好內容，可直接使用

---

## 日常工作流程

### 接觸新潛客
1. 找到對方公司 → 從 `crm/prospects/_template.md` 複製建檔
2. 查 `knowledge-base/competitors/` 看對方目前用什麼
3. 對照 `knowledge-base/products/cross-sell-matrix.md` 決定推什麼
4. 從 `playbooks/<對應劇本>.md` 找首次接觸話術
5. 從 `templates/email/` 或 `templates/linkedin/` 複用模板
6. 互動後立即更新 `crm/prospects/<company>.md` 互動紀錄

### 對方提了新問題我答不出
1. 先答「讓我確認後回覆」
2. 確認後把問答補到 `knowledge-base/faq/objection-handling.md`
3. 若是產品規格層級，補到對應 `knowledge-base/products/*.md`

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
- [ ] iFX EXPO 等行業活動參會者預掃描（如有需要）
- [ ] Lead scoring 模型（基於 frontmatter）
