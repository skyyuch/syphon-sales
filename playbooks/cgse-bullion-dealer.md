## Playbook — 香港金銀業貿易場（CGSE）E-Trading 金商

> **核心切入點**：xSyphon 的 **XAU/CNH（金/離岸人民幣）** 是 CGSE 金商拿不到的獨家產品。所有對話從這裡開始，**不要從 FX broker 的 sub-100ns / 35% fill rate 話術切入**。

## 客戶畫像

### Quantitative
- CGSE Recognized E-Trading Member（截至 2026-05-21 共 52 家）
- 日均交易量 **$50M-$300M**（金商規模本就低於 FX broker，少數品牌大的可能 $500M+）
- 員工規模 30-150 人
- 客戶結構：80%+ retail + 20% IB 引介散戶

### Qualitative
- 主要產品：**loco London 倫敦金/銀**（OTC）、99 金、人民幣公斤金條、港元公斤金條
- 客戶語言：**繁體中文為主**（少數簡中、英文）
- 地域：香港本地散戶 + 中國 IB 引流 + 東南亞華人圈
- 決策節奏：**比 FX broker 慢**，傳統金商常需老闆親自決定
- 對「AI / 自動化」較保守（影響交易員工作）

### 必須驗證的 ICP 排除信號
- 對方公司網站有 `Prime` / `Liquidity Services` / `Clearing` / `Institutional` 頁面
- 提供 White Label 給其他金商或 FX broker（同行）
- 母集團有 institutional 業務（如 Hantec Bullion 屬 Hantec Prime，必須排除）

> 已知必須排除的 CGSE 行員：**Hantec Bullion (#163)**、**WCG Markets HK (#012)**、**Henyep Gold Dealers (#026)**、**Emperor Gold & Silver (#102)** —— 見 `knowledge-base/products/cross-sell-matrix.md`。

## 獵客來源

### 一級來源
- **CGSE 官方 E-Trading Member List**：https://cgse.com.hk/chines/en/cgse-recognized-e-trading-member-list
- **CGSE 行員公告 / 本場公告**：可看到行員業務變動、新加入、被停業
- **CGSE 觀察行員名單**：被勒令停業的反向篩選（這些不要追）

### 二級信號（機會成熟的徵兆）
- 對方近期推新產品（IB 廣告、新 APP 上線）→ 正在擴張
- LinkedIn 招聘「黃金交易員 / Liquidity Manager / 業務發展總監」
- 對方公開講「擴 FX 業務」或「擴東南亞市場」→ White Label 對話成立
- 中國 IB 客戶人民幣需求增（宏觀新聞）→ XAU/CNH 對話成立
- 同業（如領峰、百利好）動作 → 競爭壓力下對方更願意聽

## 首次接觸話術

### 主路徑：純 LP（XAU/CNH 為錨）
> 「{{first_name}} 您好，注意到貴司是 CGSE E-Trading 行員（編號 {{cgse_no}}）。直接說：xSyphon 是毛里裘斯持牌 LP，**XAU/CNH（金/離岸人民幣）是我們的獨家報價，bilateral 不是合成 cross**。中國 IB 客戶近兩年對人民幣計價金需求增，貴司若願意給 IB 多一個賣點，我可以 24 小時內準備一份 connectivity proposal —— 只需要您給我大概的 daily 金 volume + IB 客戶結構。」

### 備選：LP + Connect 多產品打包（集團型金商）
> 「{{first_name}} 您好，看到貴司在 {{specific_observation}}（例：新加 FX 業務、擴東南亞 IB）。集團型金商常見的痛點是**金 / FX / 未來 Crypto CFD 各用一套 LP + 一套執行邏輯，運維成本高**。xSyphon 一個 FIX session 接 metals + FX + Crypto，Syphon Connect 是 plug-in 不換 stack。先從 XAU/CNH 試一個產品，看看是否值得深入。」

### 備選：White Label（金商想擴 FX 但無 FX 技術）
> 「{{first_name}} 您好，看到很多 CGSE 行員近兩年都在嘗試擴 FX 業務 —— 客戶量級在金這塊已遇成長天花板，FX 是天然延伸。但金商的痛點是**沒 FX 技術、沒 FX LP、沒 FX 風控 know-how**，自建 6-12 個月 + 高 setup cost。Syphonix White Label 4-6 週上線（含 KYC/AML + 後台 + GUI）+ xSyphon LP 一個合約搞定。值得 15 分鐘聊聊嗎？」

## Discovery 重點

1. 目前金 LP 有幾家？是 CGSE 內部互換還是接外部（如 CFH、Advanced Markets）？
2. 主力交易產品是 loco London 金、99 金、還是人民幣公斤金條？比例？
3. **客戶有沒有問過「人民幣計價的 loco London 金」這種需求？**（XAU/CNH 切入點）
4. IB 網絡規模？中國 IB 佔比多少？IB 客戶活躍時段？
5. 有沒有 FX 業務？若有，FX LP 是哪家？若無，有沒有想擴的計劃？
6. 系統是自研還是用第三方？電子盤 GUI 是自家的還是 white-label？
7. 過去 12 個月最大的 LP-related incident 是什麼？（spread 飆升、報價中斷、結算糾紛）

## Demo 重點

### 要強調的
- **XAU/CNH live 報價 + bilateral 深度**（這是其他 LP 給不出來的，**永遠先 demo 這個**）
- 亞洲時段（SG1 co-located）金的深度截圖（亞洲 IB 客戶活躍時段是金商最痛點）
- loco London 金/銀的完整深度（5-10 個 maker 同時報價）
- 零 last look 政策（金商客戶對 reject 特別敏感，IB 會抱怨）
- Onboarding 5-10 個工作天（傳統金 LP 通常 1-3 個月）

### 要避免的
- ❌ Sub-100ns latency 話術（金商不是 HFT，聽不進去）
- ❌ AI-native / agent-driven 詞彙（傳統金商反 AI）
- ❌ 「換掉你的金 LP」這種威脅性 framing（要講「補一個獨家上去」）
- ❌ 大段技術架構（金商的決策層通常不是 CTO，是老闆或 dealing head）
- ❌ 英文 demo（除非對方明確要求）—— 預設繁中

## 異議處理重點

> 「我們已經用同一家金 LP 多年，關係很穩定」
- 完全理解，不是要您換 —— 是**補一個獨家產品**上去
- XAU/CNH 是您現有 LP 給不出的，新增不會影響既有關係
- 看看 IB 客戶反應，再決定要不要深化

> 「XAU/CNH 我沒看到客戶在問」
- 中國離岸人民幣資產配置近三年顯著上升（**這是宏觀趨勢，不是 broker-specific 需求**）
- 您的 IB 沒主動問是因為「沒有產品所以沒辦法賣」
- 我們可以提供一份 1-pager 給您的 IB 試水

> 「毛里裘斯牌照我們不太熟」
- FSC 等同於 Tier 2 牌照，合規 MiFID II / UK FCA 框架
- 對機構業務（CGSE 行員 vs LP 之間是機構關係）足夠
- 文件 1 週內可給您的合規 review

> 「我們是傳統金商，不接受 AI / 黑箱」
- xSyphon 是 LP，**核心服務是給您報價 + 深度，AI 是後台用來決定 maker priority，您完全看不到**
- 文件上沒有「AI 黑箱」字眼，您給合規看的合約就是傳統 LP 合約
- （**注意**：對傳統金商，刻意不講 Syphonix 系統，只談 LP）

> 「我們電話量太小，你們看不上」
- xSyphon 最低 M ADV（million daily volume）即可
- CGSE E-Trading 行員平均量級都在此範圍以上
- 我們的 onboarding 對中小金商有快速通道

## Demo / POC 流程

- **第一週**：XAU/CNH 試報價（紙上模擬，不影響生產）
- **第二週**：給 1-pager 讓 IB 試水中國客戶反應
- **第三週**：簽 LP 合約 + KYC
- **第四週**：FIX session 配置 + UAT
- **第五-六週**：production live（單一產品 XAU/CNH）
- **第三個月後**：擴展到完整 loco London 金/銀

## 典型成交週期
- 首次接觸 → 第一次回覆：5-15 個工作天（金商較慢）
- 回覆 → discovery call：1-3 週
- Discovery → KYC：3-6 週
- KYC → 第一個產品 live：2-4 週
- **總計**：3-5 個月（單一產品 entry）

## ARR 範圍
- **純 XAU/CNH 單一產品**：$30k-$90k/年（依量）
- **完整 metals LP（XAU/USD + XAU/CNH + XAG）**：$80k-$200k/年
- **多產品打包（metals + EM FX + Crypto CFD）**：$150k-$400k/年
- **White Label FX 擴張 + LP**：$250k-$500k/年（setup $50-150k + monthly + revenue share）

> 整體 CGSE 金商 cohort ARR 區間比 FX broker 低，但**競品少、決策層短、客戶忠誠度高**，是穩定可預測的 segment。

## 常見死局（不要再追的信號）
- 對方有 prime / clearing 子品牌（ICP 不符 —— 見 cross-sell-matrix 排除清單）
- 對方規模 < $50M daily（量太小，xSyphon onboarding ROI 不夠）
- 對方明確「黃金業務正在收縮，重心轉證券 / 房地產」
- 對方 3 次 outreach 無回覆 → 降 P2，6 個月後再試
- 對方剛被 CGSE 列入「觀察行員名單」（合規或財務有問題）

## Cross-sell 順序
1. **單一產品入門**：XAU/CNH 試接（最低風險、最不威脅既有關係）
2. **產品擴展**（3-6 個月）：擴到完整 metals LP
3. **跨資產**（6-12 個月）：EM FX、Crypto CFD（如金商有相關業務）
4. **系統升級**（12-24 個月）：Syphon Connect / White Label（如金商擴 FX）
5. **戰略合作**（24 個月+）：金商 IB 網絡反向引介 Syphonix 給更小同行

## 與其他 playbook 的關係
- **不適用**：`new-broker-launcher.md`（CGSE 金商有牌 + 有業務，不是新進業者）
- **部分適用**：`existing-broker-upgrade.md`（Connect 切入邏輯類似，但話術完全不同）
- **部分適用**：`pop-institutional.md`（LP-first 思維類似，但 CGSE 金商比 hedge fund 保守很多）
- **本 playbook 補的 gap**：傳統繁中市場 + 金商特有產品（XAU/CNH、99 金）+ 保守決策節奏

## 對應 templates
- `templates/email/cgse-bullion-lp-cold-tc-v1.md` — 純 LP cold（繁中），主路徑
- `templates/email/cgse-bullion-whitelabel-cold-tc-v1.md` — White Label cold（繁中），給想擴 FX 的金商

## 待補
- [ ] CGSE 行員的具體 ARR 區間（成單 2-3 家後校準）
- [ ] 中文 demo 腳本（XAU/CNH live 報價）
- [ ] CGSE 行業活動 / 共同人脈 mapping
