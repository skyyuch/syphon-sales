# 異議處理庫

> 客戶常見質疑與標準回應。每次遇到新異議要補進來。

## 牌照 / 合規類

### Q: 毛里裘斯牌照「夠不夠」？
**A**: xSyphon 持 FSC GB25204632，合規 MiFID II / UK FCA 框架。對機構業務（非散戶）完全足夠。如客戶有更高牌照需求（如歐盟散戶分發），可在他們的本地實體下 booking，xSyphon 作為 LP。

### Q: KYC / AML 流程要多久？
**A**: 1-2 個工作天完成 KYC，整體 onboarding 5-10 個工作天 from signed agreement.

---

## 技術類

### Q: Sub-100ns / 5ms 是 marketing 數字嗎？
**A**: 
- Syphonix sub-100ns 是 **engine benchmark**（co-located 環境下從 order receipt 到 fill confirmation 的 median）
- xSyphon 5ms 是 **cloud round-trip**
- 兩個指標不直接可比，可申請完整 latency profile

### Q: 不想換 MT5 / 既有橋接商
**A**: Syphon Connect 是 FIX-native plug-in，不用換。並存於現有 stack，2-3 週上線。支援 OneZero / PrimeXM / Centroid / Gold-i / Tools for Brokers。

### Q: AI 黑箱風險？
**A**: 
- 2,500+ 參數可配置
- 每個 agent 決策完整 audit trail
- Human-in-loop 可設置哪些決策需要人工 approve
- 模型可使用 OpenAI / Anthropic / Google，也可帶自己的 .onnx / .bin

### Q: Co-location 要求？
**A**: 達到 sub-100ns 需要 co-located 部署（LD4/NY4/TY3/SG1）。非 co-located 客戶會運作在 microsecond 級別。

---

## 商業 / 定價類

### Q: 最低 volume 要求？
**A**:
- xSyphon: M ADV 起，FX 最小 ticket 1,000 units，金最小 1 oz
- Syphonix（Evo/Connect 主要目標）: 日均 $500M+ FX flow

### Q: 為什麼比 oneZero / PrimeXM 貴？
**A**: 我們不是 EMS，是 AI-native 執行棧。oneZero 是路由 + 監控，我們是路由 + **學習 + 自適應**。執行品質改善（fill rate、spread、reject rate）通常 1-2 個月內回本。

### Q: Lock-in 風險？
**A**: 
- 標準 FIX 4.4 接入，技術上隨時可下架
- Syphon Connect 因為不換 stack，下架成本最低（只是回到原狀）
- 合約一般 12 個月

---

## 競品對比類

### Q: 為什麼不選 LMAX / Saxo Prime？
**A**:
- 中小型 broker 通常拿不到 LMAX/Saxo 的直接報價（門檻太高）
- 我們 5-10 天 onboarding，他們 3-6 個月
- XAU/CNH 是我們獨家
- 對方規模大，但服務反應慢、客製化少

### Q: B2Broker / Match-Trade 不是也做全套？
**A**:
- 他們是「broker 啟動套件」，我們是「AI-native 執行基礎設施」
- 我們的 Sub-100ns 與 1.2M events/sec 不在同一級別
- 適合場景不同：他們服務「新手 broker」，我們服務「想升級執行品質的中大型 broker」

---

## 風控 / 風險類

### Q: B-Book 風險如何控制？
**A**: 
- AI flow toxicity scoring 自動決定 A/B Book 路由
- NOP / margin / tail risk 都是 **inline pre-trade check**（不是 post-trade report）
- 自動 hedging 可設閾值觸發
- Circuit breaker 可配置 per instrument / client / session

### Q: 客戶被 hack 我們有責任嗎？
**A**: 標準 SLA 包含 99.98% uptime；客戶端安全（API key 管理、IP 白名單）有最佳實踐文件。具體合約條款請走法務。

---

---

## CGSE 金商特有異議（2026-05-21 新增）

> 香港金銀業貿易場 E-Trading 行員的決策節奏 + 文化與 FX broker 不同，需要不同處理。
> 對應 playbook：`playbooks/cgse-bullion-dealer.md`、discovery script：`templates/pitch/cgse-bullion-discovery-call-tc-v1.md`

### Q: 我們已經用同一家金 LP 多年，關係很穩定，不想換
**A**:
- 完全理解，**不是要您換** —— 是補一個獨家產品（XAU/CNH）上去
- 新增不影響既有關係，您現有的金 LP 完全保留
- 看 IB / 客戶反應，再決定要不要深化第二個產品
- **這是金商最高頻異議**，必須第一句話 pre-empt「不是替換」

### Q: XAU/CNH 我沒看到客戶 / IB 在問
**A**:
- 中國離岸人民幣資產配置近三年複合增長 ~25-30%（**這是宏觀趨勢，不是 broker-specific 需求**）
- IB 沒主動問通常是**「沒產品所以沒辦法賣」**，不是「沒需求」
- 我們可以提供繁中 1-pager 給您的 IB 試水，看 IB 的反饋，不需要立即決定接 LP
- 對應素材：`content/collateral/xau-cnh-for-cgse-bullion-1pager-tc-v1.md`

### Q: 我們是傳統金商，不接受 AI / 黑箱
**A**:
- xSyphon **是 LP 不是系統**，核心服務是給您報價 + 深度 + 結算
- AI 是後台用來決定 maker priority，**您完全看不到**
- 文件上沒有「AI 黑箱」字眼，您給合規看的合約就是**傳統 LP 合約**
- （**注意**：對傳統金商，刻意不講 Syphonix 系統，純講 LP）

### Q: 我們電話量太小，你們看不上
**A**:
- xSyphon 最低 M ADV（million daily volume），CGSE E-Trading 行員平均量級都符合
- 我們有中小金商的**快速通道**：5-10 工作天 onboarding，傳統金 LP 通常 1-3 個月
- 不需要承諾最低 commitment，按實際成交量結算

### Q: 我們自己也對外提供 LP / Prime services
**A**:
- 🚩 **這是 ICP 排除信號**（依 `knowledge-base/products/cross-sell-matrix.md` 排除規則）
- xSyphon 對對方是競品，不要 push
- 仍可探索 **Syphonix（純系統）對話**（Connect / Evo），系統不是 LP，不直接競爭
- Call 後標記為「ICP 排除」，未來改 Syphonix-only outreach

### Q: 毛里裘斯牌照我們不太熟，CGSE 認可這個牌照嗎
**A**:
- FSC 等同 Tier 2 牌照，合規 MiFID II / UK FCA 框架
- CGSE 行員與外部 LP 之間是**機構業務關係**（非散戶分發），FSC 合規足夠
- 文件 1 週內可給您的合規 review
- 如需更高牌照層級的 booking，可在貴司本地實體下 booking，xSyphon 作為上游 LP

### Q: 一個合約接 metals + FX + Crypto？我們不做 FX 也不做 Crypto
**A**:
- 完全沒問題，一個 FIX session 只接金也可以，**未來想擴 FX / Crypto 時不用重簽合約**
- 對於目前已確定方向（純金）的金商，可以先把這個彈性放著
- 對於 1-2 年內可能擴 FX 的金商，這個架構可以省一輪 onboarding

### Q: 我們的客戶都是繁中，你們有繁中支援嗎
**A**:
- 業務溝通、合約、KYC 文件**全套支援繁體中文**
- 中文 1-pager / 中文 IB-facing 素材可直接 forward 給客戶
- 中文 discovery / demo 為預設語言
- 對應素材：`content/collateral/xau-cnh-for-cgse-bullion-1pager-tc-v1.md`（中英雙語）

### Q: 我們是 CGSE 行員，你們了解金商的特殊性嗎
**A**:
- 我們的 BD 團隊以亞洲金商為 segment 重點，了解 CGSE E-Trading 行員結構（編號制、Loco London / 99 金 / 公斤金條合約分類）
- 我們有針對 CGSE segment 的專屬 playbook + 對應素材（不是 FX broker 通用方案套用過來）
- 也願意去 CGSE 行業活動 / 與貴司會員代表交流，深化對 segment 的理解

---

## 待補
- [ ] 跨境支付與結算問題（涉及 PSP 客戶）
- [ ] 公司穩定性 / 財務狀況問題（如果客戶問）
- [ ] 客戶資料隱私 / GDPR
- [ ] CGSE 場內合約（人民幣公斤金條）vs xSyphon XAU/CNH OTC 的差異化解釋（leverage、結算、客戶資格）
