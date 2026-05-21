---
company: Goodwill Gold Group (Hong Kong) Limited
website: https://www.goodwillgroup.com.hk  # 待驗證確切官網 URL
country: HK
hq_city: Hong Kong
type: bullion-dealer
size: 100M-500M-daily
size_confidence: estimated  # 公開研究估算，需驗證
regulator: CGSE (E-Trading Member No. 050)
status: prospect
first_contact: 2026-05-21
last_contact: 2026-05-21
owner: me
priority: P1
icp_fit: cgse-bullion
channel_focus: retail
playbook: new-broker-launcher  # 主路徑：White Label（FX 擴張）+ LP
products_interested: [syphon-whitelabel, xsyphon-metals, xsyphon-fx]
estimated_arr_usd: 250000  # White Label setup + LP 打包，金商 ARR 中高位
contact_tel: (852) 39788188
---

# Goodwill Gold Group（信譽金行 / 信譽金集團）

## ICP 資格檢查
- [x] 對方**沒有**自家 LP / Prime / Clearing 子品牌（待用 LinkedIn + 官網 final 驗證）
- [x] 對方**沒有**對其他 broker 提供 White Label（待驗）
- [x] 規模在 xSyphon 最低門檻（M ADV+）以上
- [x] ICP segment 已確認：**CGSE Bullion**（純零售金商，可能想擴 FX）

## 背景
- **公司簡介**：信譽金集團（Goodwill Gold Group），香港金銀業貿易場（CGSE）**E-Trading 行員（編號 050）**，純零售金商，核心業務電子盤倫敦金銀、99 金、人民幣公斤金條。**廣告投入較積極**（地鐵、財經媒體），品牌定位面向香港本地散戶 + 中國 IB。
- **規模與市場**：典型純零售金商，相較領峰、百利好等較聚焦純黃金（FX 業務若有也是次要）。日均交易量公開資料未揭露，依品牌投入推估 **$100M-$500M daily**，**待驗證**。
- **技術現況推測**：純金商配置 —— 自研 GUI（網 + APP）+ CGSE 連接 + 1-2 家上游金 LP。FX 業務若有，可能是「品牌延伸」而非主力。
- **戰略機會點（與其他金商差異化）**：
  - 香港金商近年**普遍想擴 FX 業務**（黃金客戶量級遇成長天花板，FX 是天然延伸）
  - 但金商**沒有 FX 系統 / 沒有 FX LP / 沒有 FX 風控 know-how** → 自建 6-12 個月 + 高 setup cost
  - **Syphonix White Label + xSyphon LP 是完美方案**：4-6 週上線 FX 業務、不用自建技術、不用找 FX LP、一個合約搞定
- **主要痛點推測**：
  1. **黃金業務成長遇瓶頸**，FX 是必然方向，但缺技術與 LP。
  2. 既有 IB 網絡可立即被 reused 推 FX 給同一批客戶（顯著 ROI）。
  3. 純金商背景 → 對「複雜技術整合」恐懼大，**「全套交鑰匙」對話最有共鳴**。
- **推薦組合（依 `cross-sell-matrix.md`）**：
  > 客戶現況屬於「**想開新 FX 經紀（無系統）**」/ Segment B「CGSE 金商，想擴 FX」
  >
  > 主推：**Syphon White Label**（4-6 週 FX 平台 + 帶 xSyphon LP，一個合約）
  >
  > **這是 5 家 CGSE 候選中唯一適合 White Label 路徑的對象**（其他 4 家以金為核心、暫無擴 FX 強烈動機 / 已有 FX 業務無需 WL）。
  >
  > 加值：xSyphon XAU/CNH 仍可同時切入（保留既有金業務的升級機會）。

## 關鍵人物
> 注意：所有姓名 / email / LinkedIn URL 必須由我親自從 LinkedIn / 官網確認後再填入。AI 不得編造。

| 姓名 | 職位 | LinkedIn | Email | 性格筆記 |
|------|------|----------|-------|---------|
| TBD  | 董事總經理 / CEO | TBD | TBD | White Label 戰略決策者 |
| TBD  | 業務發展總監 | TBD | TBD | FX 擴張商業價值對話 |
| TBD  | 交易部主管 | TBD | TBD | LP 切入（金 LP） |
| TBD  | IT / 數位轉型主管 | TBD | TBD | White Label 技術對話 |

**待研究 action**：
- [ ] LinkedIn search `"信譽金" OR "Goodwill Gold"` filter senior
- [ ] **重點驗證**：信譽金是否已有 FX 業務 / 是否公開講過想擴 FX
- [ ] 確認信譽金的 IB 網絡規模（IB 是 FX 擴張的天然 channel）
- [ ] 公司電話 (852) 39788188

## 互動紀錄（最新在上）

### 2026-05-21 — Initial research
管道：自動研究（CGSE 官方 E-Trading Member List, last updated 2026-05-21 13:00）
摘要：從 CGSE 認可電子交易商名單篩選後建檔。Goodwill 為 5 家 P1 之一，**唯一一家走 White Label 路徑**（FX 擴張機會 + xSyphon LP 打包）。下一步先驗證信譽金是否已有 FX 業務 / 擴張意圖。

---

## 下一步
- [ ] **優先**：驗證信譽金是否有 FX 業務 / 擴張新聞稿（負責人：me / 截止：2026-05-26）
  - 若**已有 FX 業務** → 改路徑為「Connect 升 A/B Book + xSyphon LP」
  - 若**無 FX 業務但有擴張跡象** → 維持 White Label 路徑
  - 若**完全純金 + 無擴張意圖** → 退回「xSyphon XAU/CNH 單一產品試接」
- [ ] LinkedIn 找出董事總經理 + 業務發展總監（負責人：me / 截止：2026-05-30）
- [ ] 起草中文 outreach v1：「金商擴 FX 業務的最短路徑」角度（負責人：me / 截止：2026-06-02）

## 客戶問過、待回覆
- [ ]（尚無互動）

## 內部備註
[CONFIDENTIAL]
- White Label 是 5 家中最高 ARR 潛力（setup $50-150k + monthly $15-50k + LP revenue share）
- 但 White Label 對話只在「對方確實想擴 FX」時才成立，**否則就是空中樓閣**
- 純金商對「自建 FX 6-12 個月」的恐懼是 White Label 最強賣點 — 要把這個時間 / 成本對比講清楚
- 如果信譽金已用某品牌 FX 平台 → 退回 Connect 路徑
- 風險：信譽金可能對「白標 = 失去品牌控制」有顧慮，要強調 brand-fronted / 後台白標
- Cross-sell 倒序機會：先賣 XAU/CNH 進場 → 跑順後談 White Label FX 擴張（**這可能比 day 1 推 WL 更實際**）

## Cross-sell 機會
- **第一階段**（now → 3 個月）：**雙軌**並進 — (a) xSyphon XAU/CNH 試接（low-risk entry）+ (b) Syphon White Label 戰略對話（high-ARR 探索）
- **第二階段**（3-6 個月）：依信譽金反應決定優先順序 —— FX 擴張意願強就推 WL；否則深化金 LP
- **第三階段**（6-12 個月）：如 WL 上線 → Connect 升 A/B Book；金業務深化 → xSyphon EM FX 補產品
- **不推**：Evo full stack（過度，金商不需要）
