# Discovery Call — Questions Framework v1

**Goal**: 30 分鐘內，搞清楚對方現況、痛點、決策流程、能否成單。
**Format**: 不照本宣科，依對方類型靈活取捨。

---

## Opening（前 3 分鐘）
- 自我介紹（15 秒）：「我做 xSyphon 流動性 + Syphonix 執行系統 BD」
- 對方介紹（30 秒）
- Set agenda：「我想用 20 分鐘了解你們現況，留 10 分鐘看是否值得深聊」

---

## 必問題（無論客戶類型）

### 1. 規模與業務型態
- 日均 FX volume 大概多少？
- A-book / B-book 比例？
- 主要客戶來源（哪些區域、零售/機構）？
- 目前有幾個 desk / 多少人在 trading & ops？

### 2. 現有技術棧
- 平台是 MT4、MT5、還是自研？
- 用哪家 bridge / hub？（OneZero / PrimeXM / Centroid / Gold-i / 自研）
- LP 是哪幾家？大致 mix（Tier 1 銀行 vs PoP vs ECN）？
- Pricing engine 是 in-house 還是 bridge 自帶？

### 3. 痛點探索
- 過去 12 個月最大的執行品質投訴是什麼？
- Fill rate / spread / rejection 你們追蹤嗎？目前數字大概多少？
- A/B book 決策是怎麼做的（規則、人工、模型）？
- Risk management 是 post-trade 還是 pre-trade？

### 4. 決策流程
- 像這類系統決策通常誰最後拍板？
- 預算週期？（季度 / 年度）
- 既有合約 lock-in 嗎？什麼時候到期？

---

## 加分題（時間充裕時）

- 你們有沒有想過要做更窄的 spread？卡在哪裡？
- 如果 ops team 人手減半，能做到嗎？什麼阻擋你？
- 你最理想的 LP 提供商長什麼樣？
- 過去評估過哪些競品？為什麼沒選？

---

## 紅旗信號（出現要警覺）
- 對方答不出 fill rate / rejection rate → 不是 quant-driven，可能不是好客戶
- 對方一直問價格 → 還沒看到價值
- 對方說「我們再評估」+ 拒絕安排下次會議 → 沒興趣，別追了
- 對方問題都聚焦在「我能不能用最便宜的方案」→ 不適合 Syphonix

---

## 結束（最後 5 分鐘）
- 重複我聽到的痛點（確認理解）
- 對應推薦 1 個產品方向（不要一次推三個）
- 約下一步：「我能不能下週發一份 tailored proposal + 安排 30 分鐘 deep dive？」
- 確認 follow-up 對象 & email

---

## Call 後 24 小時內
1. 寫 follow-up email（summarize discussion + 下一步）
2. 更新 `crm/prospects/<company>.md`（互動紀錄 + 下一步）
3. 若有新異議 / 新洞察，更新 `knowledge-base/faq/objection-handling.md`
