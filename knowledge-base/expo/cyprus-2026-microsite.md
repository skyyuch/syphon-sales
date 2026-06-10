# iFX EXPO Cyprus 2026 — xSyphon 互動微網站（Booth 76）

> 展會攤位用互動微網站的技術參考。程式碼在獨立 repo，**不在 syphon-sales**。

## 基本資訊
- **Repo**：`git@github.com:skyyuch/Cyprus.git`（branch `main`）
- **場景**：iFX EXPO Cyprus 2026 · Booth 76（6/16–18）
- **本機路徑**：`scratch/cyprus-remote/`（在 syphon-sales 是 gitignore，僅本機工作副本）
- **Stack**：Vite + React + TypeScript + Tailwind；PWA（`vite-plugin-pwa`，可離線 kiosk）
- **定位**：攤位專用延伸頁（非縮小版官網）。訪客掃 QR → 10 秒抓重點 → 留資 / 約見。

## 視覺
- 配色對齊官網：近黑底 `#060807` / `#0d1410`，主色螢光綠 `#3ddc6c`，漲綠跌紅，XAU 用金 `#c9a96e`。
- 主要區塊：Hero（Booth 76）、即時報價 marquee、聚合視覺化 canvas、XAU/CNH 亮點卡、Why brokers switch、Powered by Syphonix、雙 CTA（留資 + Calendly + vCard）。
- 效能：靜態元素用 offscreen canvas 預繪、DPR 上限 1.5、減少 blur、避免 3D transform。

## 即時行情接法（核心）
- **協定**：GTS2 **Socket.IO v4**（`socket.io-client@4.1.3`）。非原生 WebSocket。
- **端點**（已用於 Cyprus，注意：公開 bundle 可見）：`https://webkd.gmtradeweb1.com:7036`，path `/socket.io/`，transports `['polling','websocket']`（要先 polling 握手再升級；直連 websocket 會 1006）。
- **流程**：`connect` → `emit('addme','Guest','Guest',128)` → 收 `init_prd_notify`（產品字典）→ 伺服器**自動狂推 `tick`**（不訂閱也有，guest firehose）。
- **字典 `init_prd_notify`**：`args[1]` = `{ "0": {uiCodeID, szShortName, aushBIG/aushGB(中文), uiDigit(小數位), uchZone}, ... }`。
- **`tick`**：`args[1]` = `{ "0": {uiCodeID, ask, bid, newP(最新), high, low, preclose, open} }`；漲跌 = `(newP-preclose)/preclose`。
- **節流**：tick 量大（~78/s），buffer 在 ref，`setInterval` 每 300ms 才 `setState`。
- **重連**：`reconnection:true`，斷線顯示 `RECONNECTING`（Cyprus 採 real-only，無模擬 fallback）。
- 實作檔：`src/useLiveQuotes.ts`（hook）；接進 `src/App.tsx` 取代原亂數模擬。

### 已映射商品 codeID（此端點）
| 顯示 | feed szShortName | codeID | 小數位 |
|------|------------------|--------|--------|
| EUR/USD | EURUSD | 3223601 | 5 |
| GBP/USD | GBPUSD | 3354673 | 5 |
| USD/JPY | USDJPY | 3289137 | 3 |
| AUD/USD | AUDUSD | 3485745 | 5 |
| USD/CNH | USDCNH | 3748145 | 5 |
| XAU/USD | XAUUSD | 3289648 | 2 |
| XAG/USD | XAGUSD | 3355184 | 3 |
| BTC/USD | BTCUSDT | 3552053 | 2 |
| ETH/USD | ETHUSDT | 3617589 | 1 |

> codeID 是該環境字典值，跨環境可能不同；正式做法是用 `init_prd_notify` 的 `szShortName`（正規化後）動態對應，不要硬編 codeID。`XAU/CNH` 此 feed 沒有 → 只做亮點卡、不放假價。

## 合規處理（已套用）
- LP 全部匿名化為 `LP-01…LP-12`，無第三方商標。
- KPI / latency / volume / fill 對齊官網與 `knowledge-base/products/xsyphon.md`；聚合動畫、KPI、測速標示 illustrative；報價為真即時。
- 頁尾：`xSyphon Ltd · FSC Mauritius License No. GB25204632 · MiFID II / UK FCA frameworks` + institutional-only + 風險聲明。
- **`.env` 含真實密鑰（CRS/CLOUD APIKEY 等）→ 永不入任何 repo**；純行情 guest 用不到。

## 交付 / 現場 checklist
- [ ] 部署：Cloudflare Pages / Vercel（免費，給 `*.pages.dev`）；之後可升 CNAME `cyprus.xsyphon.com`
- [ ] 用真實部署網址重產 QR（綠/黑配色，`booth/gen-qr.py`）+ 印 `qr-card.html` 立牌
- [ ] iPad：Safari →「加入主畫面」（PWA 離線備援）
- [ ] in-app 設定：Formspree endpoint、Calendly 連結、fallback email
- [ ] 更新 `public/xsyphon.vcf` 真實聯絡資訊
- [ ] 現場備穩定網路 / 4G（real-only，行情斷會顯示 RECONNECTING）
