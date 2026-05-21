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

## 待補
- [ ] 跨境支付與結算問題（涉及 PSP 客戶）
- [ ] 公司穩定性 / 財務狀況問題（如果客戶問）
- [ ] 客戶資料隱私 / GDPR
