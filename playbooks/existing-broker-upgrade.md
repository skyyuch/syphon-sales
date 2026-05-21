# Playbook — 既有 Broker 想升級執行品質

> **核心切入點**：Syphon Connect 的「零 rip-out + 2-3 週上線」，最容易讓對方點頭試用。

## 客戶畫像
- 日均 $500M - $5B FX
- 已用 MT4 / MT5 + OneZero / PrimeXM / Centroid / Gold-i
- 已有多家 LP 關係，但抱怨 execution quality
- 內部 ops + dealing team 規模 5-30 人

## 獵客信號
- LinkedIn 上「Looking for [bridge / EMS / risk]」職缺
- 公開抱怨 LP 服務的論壇貼文
- 近期 MT5 升級新聞
- 在徵 "Head of Trading" / "Liquidity Manager" 職位
- 收購 / 合併新聞（整合期最痛）

## 首次接觸話術
> "{{specific_observation}}. Most brokers your size are leaving 15-30% spread efficiency on the table because A/B book routing is rule-based. Syphon Connect plugs into your existing MT5 + bridge via FIX — no rip-out, 2-3 weeks live. Median 35% fill quality gain in month one. Worth a look?"

## Discovery 重點
1. 目前 fill rate / rejection rate / avg spread 數字？（如答不出來 → 加分機會：我們的儀表板可以給你看）
2. A/B book 怎麼決策的？（規則 / 人工 / 模型）
3. 你最不滿意的 LP 是哪家？為什麼還沒換？
4. 內部 dealer 規模？週末 / 半夜誰看 risk？
5. 過去 12 個月最大的 incident 是什麼？

## Demo 重點
- **不要先講 Syphon Evo 全套**，從 Connect 開始
- 展示 maker scoring live 更新（vs 對方的 static config）
- 展示 flow toxicity scoring + A/B book 自動切換
- 展示 pre-trade risk gate（vs 對方的 post-trade report）
- **可選**：展示 xSyphon LP 的 XAU/CNH（亞洲 broker 必看）

## 異議處理重點
> 「我們執行已經夠好了」
- 你最近一次量化過 fill rate 嗎？我們可以做免費 1 週 shadow 分析，給你看數字
- 35% 改善是 client median，不是 best case；你的基準越好，改善越小，但仍可見

> 「2-3 週真的可以上線？」
- 因為我們不換 MT5 / 不換你的 LP / 不換你的 client
- 第一週 KYC + FIX session 配置
- 第二週 UAT shadow（你看數字決定要不要 cutover）
- 第三週 production live

> 「不想被 vendor lock-in」
- 標準 FIX 4.4，沒有 proprietary protocol
- 12 個月合約，可拆除回原狀
- 你的 LP 關係完全不變

## Cross-sell 順序
1. 先成 Connect（小合約、低風險、快見效）
2. 第 3-6 個月導入 xSyphon LP（看實際成效後）
3. 第 6-12 個月升級到 Evo full stack（如他們想全面替換）

## 典型成交週期
- Discovery → POC：3-6 週
- POC → 合約：4-8 週
- 合約 → live：2-3 週
- **總計**：3-5 個月

## ARR 範圍
- Connect subscription：$60k-$200k/年
- + per-volume fee：依量
- 估計年化（單獨 Connect）：**$80k - $300k**
- + cross-sell xSyphon LP：+$50k - $500k

## 常見死局
- 對方剛簽 oneZero / PrimeXM 三年合約（lock-in 期過後再回頭）
- COO / Head of Trading 離職、新人上任：等 3-6 個月
- 對方規模 < $500M daily（CP 不夠 sweet）
