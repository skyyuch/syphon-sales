# xSyphon — iFX EXPO Cyprus 2026 microsite

A self-contained, zero-dependency interactive microsite for the xSyphon booth.
Visitors scan a QR with their phone; you run it full-screen on the iPad as a kiosk.
Dark "trading-desk" aesthetic matching xsyphon.com (near-black + neon green `#3ddc6c`).

## What's in here

| File | Purpose |
|------|---------|
| `index.html` | The microsite (all sections, inline CSS) |
| `app.js` | Live ticker, AI rotor, count-up, aggregation canvas, form handling |
| `config.js` | **Edit this only** — Formspree URL, Calendly URL, fallback email |
| `manifest.webmanifest` + `sw.js` | PWA: installable + works offline on the iPad |
| `assets/xsyphon-logo.png` | Logo (rendered white on dark via CSS invert) |
| `xsyphon.vcf` | "Save our contact" card for visitors' phones |
| `gen-qr.py` | Generates `qr.png` / `qr.svg` (brand-coloured) |
| `qr.png` / `qr.svg` | The booth QR code |
| `qr-card.html` | Printable A5 "Scan me" standee card |

## 3 things to fill in before you fly (5 min)

Open `config.js` and set:

1. **`formEndpoint`** — sign up free at [formspree.io](https://formspree.io), create a form, paste the URL it gives you (e.g. `https://formspree.io/f/abcdwxyz`). Until set, the lead form opens the visitor's email app as a fallback.
2. **`calendlyUrl`** — your booking link (Calendly / Cal.com), e.g. `https://calendly.com/you/cyprus-20min`.
3. **`fallbackEmail`** — change `desk@xsyphon.com` to the inbox you want offline/fallback leads to reach.

Also update the contact in `xsyphon.vcf` (email / add your name + phone) if you want the saved contact to be you personally.

## Deploy (get the public URL for the QR)

Recommended: **Cloudflare Pages** (free, fast, gives an `https://...pages.dev` URL).

**Option A — drag & drop (no Git, ~2 min):**
1. Go to Cloudflare Pages → *Create a project* → *Direct Upload*.
2. Drag the whole `cyprus-2026/` folder in.
3. You get a URL like `https://xsyphon-cyprus.pages.dev`.

**Option B — Vercel:** `npx vercel deploy --prod` from inside this folder (or use the dashboard's drag-drop). Either gives a public URL.

> The QR hides the URL from visitors, so a `*.pages.dev` address looks completely clean. If marketing can add a DNS CNAME in time, you can later point `cyprus.xsyphon.com` at the same deploy.

### Regenerate the QR with the real URL

After you have the deployed URL:

```bash
cd expo/cyprus-2026
../../.venv/bin/python gen-qr.py "https://xsyphon-cyprus.pages.dev"
```

Then open `qr-card.html` and Print → Save as PDF (A5) for the standee, or just show it on a screen.

## iPad kiosk setup (works even if venue Wi-Fi drops)

1. On the iPad, open the deployed URL in **Safari**.
2. Share → **Add to Home Screen**. This installs it as a full-screen app and the service worker caches everything for **offline** use.
3. Launch it from the Home Screen icon at the booth — no browser chrome, full screen.
4. (Optional) Settings → Display & Brightness → Auto-Lock → **Never** so it doesn't sleep.
5. (Optional) Settings → Accessibility → **Guided Access** to lock visitors into the one app.

## Booth checklist

- [ ] `config.js` filled (Formspree + Calendly + email)
- [ ] `xsyphon.vcf` updated with your details
- [ ] Site deployed, public URL working on your phone
- [ ] `gen-qr.py` re-run with the real URL; `qr-card.html` printed/loaded
- [ ] iPad: added to Home Screen, tested **in Airplane mode** (offline works)
- [ ] iPad: Auto-Lock off, Guided Access on
- [ ] Test a lead submission end-to-end (check it lands in your inbox)
- [ ] Test "Book a meeting" and "Add to contacts" buttons

## Data sources & accuracy

All copy and figures are taken from [xsyphon.com](https://xsyphon.com) and
[`knowledge-base/products/xsyphon.md`](../../knowledge-base/products/xsyphon.md):
`$1B+` daily notional, 12 Tier-1 PBs, 5ms execution, 99.7% fill, <1% rejection,
99.98% uptime, FSC GB25204632, XAU/CNH from 50 g.

Notes:
- Headline latency uses **5ms execution** (homepage / KB). The **0.8ms** figure is the
  Syphon OS routing-engine median and is shown only in the "Powered by Syphonix" section
  to avoid contradicting the headline.
- The live ticker and aggregation animation are **illustrative client-side simulations**,
  not a real market feed (disclosed in the footer). Do not present them as live pricing.
- No third-party / competitor logos are used (compliance + honesty). Trust is conveyed via
  the FSC license, infrastructure and zero-last-look badges.

## Edit anything

Single source of truth for copy is `index.html`. Colours are CSS variables at the top of
its `<style>` block. To force an offline cache refresh after edits, bump `CACHE` in `sw.js`.
