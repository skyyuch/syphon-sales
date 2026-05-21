#!/usr/bin/env python3
"""mail_merge.py — CGSE Bullion Batch 1 → ready-to-send email files.

零外部依賴（純 stdlib）。讀 config.py，把 5 家 hydrated variants 替換成你的
個人資訊，輸出 .txt（複製貼 Gmail）+ .html（瀏覽器預覽）+ index.html（主控台）。

用法：
  cp config.example.py config.py
  # 編輯 config.py 填入聯絡資訊
  python3 mail_merge.py

輸出：scripts/output/cgse-batch1/
"""

from __future__ import annotations

import html as html_lib
import os
import sys
from pathlib import Path

# ===== Imports config =====
import importlib.util

SCRIPT_DIR = Path(__file__).resolve().parent
CONFIG_PATH = SCRIPT_DIR / "config.py"
EXAMPLE_PATH = SCRIPT_DIR / "config.example.py"

if CONFIG_PATH.exists():
    _config_path = CONFIG_PATH
    _output_subdir = "cgse-batch1"
elif EXAMPLE_PATH.exists():
    print("[INFO] config.py 不存在，fallback 用 config.example.py（output → output.example/）")
    print("       要產生 real 收件人版本：cp scripts/config.example.py scripts/config.py + 編輯")
    print()
    _config_path = EXAMPLE_PATH
    _output_subdir = "cgse-batch1"
else:
    print("[ERROR] 找不到 config.py 或 config.example.py。")
    sys.exit(1)

_spec = importlib.util.spec_from_file_location("mail_config", _config_path)
config = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(config)

SENDER = config.SENDER
PROSPECTS = config.PROSPECTS

_output_root = "output" if _config_path == CONFIG_PATH else "output.example"
OUTPUT_DIR = SCRIPT_DIR / _output_root / _output_subdir


# ===== Hydrated email variants (extracted from templates/email/*.md) =====
# 注意：這些 variants 與 templates/email/ 內的 markdown 為同源。
# 修改 markdown template 時，記得同步此處（或反之）。
# Placeholder 用 [雙方角括號]，會被 config 的真實值替換。

VARIANTS = {
    "A": {
        "track": "LP",
        "company_tc": "領峰貴金屬",
        "subject": "XAU/CNH bilateral 報價 — 給領峰多一個 IB 賣點",
        "body": """[CONTACT_NAME]您好，

我是 xSyphon 的 [SENDER_NAME_TC]。注意到貴司是 CGSE E-Trading 行員（編號 145），近幾年在零售金商品牌投入相對積極，IB 網絡覆蓋香港 + 中國 + 東南亞華人圈。

直接說重點：xSyphon 是毛里裘斯 FSC 持牌 LP（牌號 GB25204632），XAU/CNH（金/離岸人民幣）是我們的獨家 bilateral 報價，不是 cross 合成。據我們觀察，中國 IB 客戶近兩年對人民幣計價金的詢價明顯上升，但本地金商普遍拿不到深度。

如果貴司願意給 IB 多一個別人沒有的賣點，我可以 24 小時內準備一份 connectivity proposal —— 只需要您給個大概的 daily 金 volume + IB 結構。Onboarding 5-10 個工作天。

或 15 分鐘簡單聊聊：[CALENDLY_LINK]

順祝商祺，
[SENDER_NAME_TC]
""",
    },
    "B": {
        "track": "LP",
        "company_tc": "百利好金融",
        "subject": "XAU/CNH bilateral 報價 — 給百利好 IB 的差異化新產品",
        "body": """[CONTACT_NAME]您好，

我是 xSyphon 的 [SENDER_NAME_TC]。注意到貴司是 CGSE E-Trading 行員（編號 126），百利好品牌在香港地鐵 / 財經媒體的覆蓋很到位，IB 引介人網絡是核心增長引擎。

直接說重點：xSyphon 是毛里裘斯 FSC 持牌 LP（牌號 GB25204632），XAU/CNH（金/離岸人民幣）是我們的獨家 bilateral 報價，不是 cross 合成。亞洲時段（SG1 co-located）我們的深度比歐美 LP 更穩 —— 這是貴司 IB 客戶最活躍的時段。

如果貴司願意給 IB 多一個別人沒有的賣點，我可以 24 小時內準備一份 connectivity proposal —— 只需要您給個大概的 daily 金 volume + IB 結構。Onboarding 5-10 個工作天。

或 15 分鐘簡單聊聊：[CALENDLY_LINK]

順祝商祺，
[SENDER_NAME_TC]
""",
    },
    "C": {
        "track": "LP",
        "company_tc": "皇御金融",
        "subject": "金 + EM FX 統一報價 — 給皇御集團的 LP 打包方案",
        "body": """[CONTACT_NAME]您好，

我是 xSyphon 的 [SENDER_NAME_TC]。注意到貴司是 CGSE E-Trading 行員（編號 076），皇御集團涵蓋貴金屬 + 證券 + 期貨多元金融線。

集團型金商常見的痛點是金 / FX / 未來 Crypto CFD 各用一套 LP + 一套執行邏輯，運維成本高。xSyphon 一個 FIX session 可接 metals + EM FX + Crypto CFD：
- XAU/CNH bilateral（獨家，給中國 IB 客戶新賣點）
- EM FX（USD/CNH、USD/HKD 完整深度）
- 毛里裘斯 FSC 持牌（牌號 GB25204632）
- Onboarding 5-10 個工作天

先從 XAU/CNH 一個產品試接看 IB 反應，跑順了再擴展。15 分鐘討論可行性？

[CALENDLY_LINK]

順祝商祺，
[SENDER_NAME_TC]
""",
    },
    "D": {
        "track": "LP",
        "company_tc": "第一亞洲商人金融",
        "subject": "XAU/CNH bilateral — 一個獨家產品給貴司的 IB",
        "body": """[CONTACT_NAME]您好，

我是 xSyphon 的 [SENDER_NAME_TC]。看到貴司是 CGSE E-Trading 行員（編號 114），多年穩定運營純零售金業務。

我不是要建議您換現有金 LP —— 完全理解多年穩定關係的價值。直接說：xSyphon 有一個您現有 LP 拿不到的產品 —— XAU/CNH（金/離岸人民幣）bilateral 報價，毛里裘斯 FSC 持牌 LP（牌號 GB25204632）。

近兩年中國 IB 客戶人民幣計價金的詢價上升明顯，本地金商普遍沒這個產品。新增一個 LP 不影響您現有的關係，給 IB 多一個賣點而已。

要不要看一份 1-pager？我可以 email 過去您給 IB 試水，不需要先通話。

順祝商祺，
[SENDER_NAME_TC]
""",
    },
    "Goodwill": {
        "track": "WL",
        "company_tc": "信譽金行",
        "subject": "金商擴 FX 的最短路徑 — 給信譽金的 4-6 週方案",
        "body": """[CONTACT_NAME]您好，

我是 xSyphon / Syphonix 的 [SENDER_NAME_TC]。注意到貴司是 CGSE E-Trading 行員（編號 050），信譽金在香港地鐵 / 財經媒體的品牌覆蓋很到位，IB 網絡是核心引擎。

我們最近觀察到一個趨勢：CGSE 金商紛紛在嘗試擴 FX 業務。原因很直接 —— 黃金客戶量級成長遇天花板，FX 是天然延伸；同一批 IB / 同一批散戶，多賣一個產品就能放大 LTV。

但金商擴 FX 的共同挑戰我們聽過很多次：
- 沒 FX 技術（MT5 + 橋接 + 後台 + 風控自建至少 6-12 個月）
- 沒 FX LP（從零找 Tier-1 LP 並完成 KYC 通常 3-6 個月）
- 沒 FX 風控 know-how（金 risk ≠ FX risk）

Syphonix White Label + xSyphon LP 是一個合約搞定：
- 4-6 週上線全套 FX 平台（GUI、KYC/AML、後台、reporting）
- 內建 xSyphon LP（12+ Tier-1 聚合，毛里裘斯 FSC 持牌）
- 您的 IB 網絡立即可推 FX 給同一批客戶
- Brand-fronted 白標 —— 客戶看到的是「信譽金 FX」，不是別人品牌

如果信譽金目前沒有 FX 計劃，我們也可以先聊純 LP —— xSyphon 的 XAU/CNH bilateral 報價是 CGSE 金商拿不到的獨家產品，給 IB 多一個賣點。

15 分鐘聊一下哪個方向更貼合貴司的 1-2 年規劃？[CALENDLY_LINK]

順祝商祺，
[SENDER_NAME_TC]
""",
    },
}


# ===== Render functions =====


def render_signature() -> str:
    return SENDER["signature_block"].format(
        name_en=SENDER["name_en"],
        name_tc=SENDER["name_tc"],
        title_en=SENDER["title_en"],
        email_from=SENDER["email_from"],
        phone=SENDER["phone"],
    )


def fill_placeholders(text: str, prospect: dict) -> str:
    """Replace [CONTACT_NAME]、[SENDER_NAME_TC]、[CALENDLY_LINK]."""
    contact_name = prospect["contact_name"].strip() or f"[填入 {prospect['company_tc']} 決策人姓名]"
    return (
        text
        .replace("[CONTACT_NAME]", contact_name)
        .replace("[SENDER_NAME_TC]", SENDER["name_tc"])
        .replace("[CALENDLY_LINK]", SENDER["calendly_link"])
    )


def render_txt(prospect: dict, variant: dict) -> str:
    """RFC 822-flavored plaintext，含 To/From/Subject header（複製貼用）。"""
    to_line = prospect["contact_email"].strip() or "[PENDING — fill in before sending]"
    subject = variant["subject"]
    body = fill_placeholders(variant["body"], prospect).rstrip()
    signature = render_signature()

    blockers = []
    if not prospect["contact_name"].strip():
        blockers.append("contact_name")
    if not prospect["contact_email"].strip():
        blockers.append("contact_email")
    if "icp_verify_deadline" in prospect:
        blockers.append(f"ICP 驗證 deadline {prospect['icp_verify_deadline']}")

    header = f"""===== READY-TO-SEND EMAIL =====
Company        : {prospect['company_tc']} ({prospect['company_en']})
CGSE No.       : #{prospect['cgse_no']}
Track          : {prospect['track']}  |  Variant {prospect['variant_id']}
Planned send   : {prospect['send_date']}
Blockers       : {', '.join(blockers) if blockers else 'NONE - ready to send'}
================================

To: {to_line}
From: {SENDER['name_en']} <{SENDER['email_from']}>
Subject: {subject}

{body}

{signature}
"""
    return header


def render_html(prospect: dict, variant: dict) -> str:
    """瀏覽器預覽用 HTML，盡量擬真 Gmail / Outlook 樣式。"""
    subject = html_lib.escape(variant["subject"])
    body = fill_placeholders(variant["body"], prospect).rstrip()
    body_html = html_lib.escape(body).replace("\n", "<br>")
    signature = render_signature()
    signature_html = html_lib.escape(signature).replace("\n", "<br>")
    to_line = html_lib.escape(prospect["contact_email"].strip() or "[PENDING — fill in before sending]")

    blockers_html = ""
    blockers = []
    if not prospect["contact_name"].strip():
        blockers.append("contact_name")
    if not prospect["contact_email"].strip():
        blockers.append("contact_email")
    if "icp_verify_deadline" in prospect:
        blockers.append(f"ICP 驗證 deadline {prospect['icp_verify_deadline']}")
    if blockers:
        blockers_html = (
            f'<div class="blocker">⚠️ Blockers: {html_lib.escape(", ".join(blockers))}</div>'
        )
    else:
        blockers_html = '<div class="ready">✓ READY TO SEND</div>'

    return f"""<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="UTF-8">
<title>{subject}</title>
<style>
body {{
  font-family: -apple-system, BlinkMacSystemFont, "PingFang TC", "Noto Sans CJK TC",
               "Microsoft JhengHei", sans-serif;
  background: #F5F5F5; padding: 24px; margin: 0; color: #202124;
}}
.meta {{
  max-width: 720px; margin: 0 auto 16px; background: #fff;
  padding: 12px 20px; border-radius: 6px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);
  font-size: 13px; color: #5f6368;
}}
.meta .row {{ margin: 4px 0; }}
.meta .row strong {{ color: #202124; display: inline-block; width: 100px; }}
.blocker {{
  background: #FCE8E6; color: #C5221F; padding: 8px 12px; border-radius: 4px;
  margin-top: 8px; font-weight: 600;
}}
.ready {{
  background: #E6F4EA; color: #137333; padding: 8px 12px; border-radius: 4px;
  margin-top: 8px; font-weight: 600;
}}
.email {{
  max-width: 720px; margin: 0 auto; background: #fff;
  border-radius: 6px; box-shadow: 0 1px 3px rgba(0,0,0,0.1);
}}
.email .header {{
  padding: 16px 20px; border-bottom: 1px solid #E0E0E0;
}}
.email .subject {{
  font-size: 20px; font-weight: 500; color: #202124; margin-bottom: 8px;
}}
.email .from {{
  font-size: 13px; color: #5f6368;
}}
.email .from strong {{ color: #202124; }}
.email .body {{
  padding: 24px 20px; font-size: 14.5px; line-height: 1.7; color: #202124;
}}
.email .signature {{
  margin-top: 24px; padding-top: 16px; border-top: 1px dashed #E0E0E0;
  color: #5f6368; font-size: 13px; line-height: 1.6;
}}
.copy-hint {{
  max-width: 720px; margin: 16px auto 0; font-size: 12px; color: #888;
  text-align: center;
}}
</style>
</head>
<body>

<div class="meta">
  <div class="row"><strong>Company:</strong> {html_lib.escape(prospect['company_tc'])} ({html_lib.escape(prospect['company_en'])})</div>
  <div class="row"><strong>CGSE No.:</strong> #{html_lib.escape(prospect['cgse_no'])}</div>
  <div class="row"><strong>Track:</strong> {html_lib.escape(prospect['track'])} · Variant {html_lib.escape(prospect['variant_id'])}</div>
  <div class="row"><strong>Planned:</strong> {html_lib.escape(prospect['send_date'])}</div>
  {blockers_html}
</div>

<div class="email">
  <div class="header">
    <div class="subject">{subject}</div>
    <div class="from"><strong>From:</strong> {html_lib.escape(SENDER['name_en'])} &lt;{html_lib.escape(SENDER['email_from'])}&gt;</div>
    <div class="from"><strong>To:</strong> {to_line}</div>
  </div>
  <div class="body">
    {body_html}
    <div class="signature">{signature_html}</div>
  </div>
</div>

<div class="copy-hint">複製對應 .txt 內容貼到 Gmail compose · 預覽僅供確認長相</div>

</body>
</html>
"""


def render_index(rendered: list[tuple[dict, dict]]) -> str:
    """5 家總覽 + 連結。"""
    rows = []
    for prospect, variant in rendered:
        blockers = []
        if not prospect["contact_name"].strip():
            blockers.append("contact_name")
        if not prospect["contact_email"].strip():
            blockers.append("contact_email")
        status_cls = "blocker" if blockers else "ready"
        status_text = (
            f"Blockers: {', '.join(blockers)}" if blockers else "READY"
        )
        deadline = prospect.get("icp_verify_deadline", "—")
        rows.append(f"""
<tr>
  <td>{html_lib.escape(prospect['send_date'])}</td>
  <td><strong>{html_lib.escape(prospect['company_tc'])}</strong><br><span class="en">{html_lib.escape(prospect['company_en'])}</span></td>
  <td>#{html_lib.escape(prospect['cgse_no'])}</td>
  <td>{html_lib.escape(prospect['track'])} · {html_lib.escape(prospect['variant_id'])}</td>
  <td>{html_lib.escape(deadline)}</td>
  <td class="{status_cls}">{html_lib.escape(status_text)}</td>
  <td>
    <a href="{prospect['id']}-cold.html">預覽 HTML</a> ·
    <a href="{prospect['id']}-cold.txt">複製 TXT</a>
  </td>
</tr>""")
    rows_html = "\n".join(rows)

    return f"""<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="UTF-8">
<title>CGSE Bullion Batch 1 — Outbox 主控台</title>
<style>
body {{
  font-family: -apple-system, "PingFang TC", "Microsoft JhengHei", sans-serif;
  margin: 0; padding: 32px; background: #F8F9FA; color: #202124;
}}
h1 {{ margin: 0 0 8px; color: #1A2B4A; }}
.hint {{ color: #5f6368; margin-bottom: 24px; font-size: 14px; }}
table {{
  width: 100%; max-width: 1200px; border-collapse: collapse;
  background: #fff; box-shadow: 0 1px 4px rgba(0,0,0,0.08); border-radius: 6px; overflow: hidden;
}}
th, td {{ padding: 12px 14px; text-align: left; border-bottom: 1px solid #E8EAED; font-size: 13.5px; vertical-align: middle; }}
th {{ background: #1A2B4A; color: #fff; font-weight: 600; }}
.en {{ color: #5f6368; font-size: 12px; }}
.blocker {{ color: #C5221F; font-weight: 600; }}
.ready {{ color: #137333; font-weight: 600; }}
a {{ color: #1967D2; text-decoration: none; margin-right: 4px; }}
a:hover {{ text-decoration: underline; }}
.footer {{ margin-top: 24px; font-size: 12px; color: #888; }}
</style>
</head>
<body>

<h1>CGSE Bullion Batch 1 — Outbox</h1>
<p class="hint">
  Gmail 工作流：點 <strong>複製 TXT</strong> → 把純文字 body 貼到 Gmail compose →
  填收件人 → Send。<br>
  <strong>預覽 HTML</strong> 供你確認 email 排版 / 字體 / 換行是否 OK。
</p>

<table>
  <thead>
    <tr>
      <th>計畫發送</th>
      <th>公司</th>
      <th>CGSE</th>
      <th>Track / Variant</th>
      <th>ICP 驗證 deadline</th>
      <th>狀態</th>
      <th>檔案</th>
    </tr>
  </thead>
  <tbody>
    {rows_html}
  </tbody>
</table>

<div class="footer">
  Generated by <code>scripts/mail_merge.py</code> · 配合 <code>crm/campaigns/2026-05-cgse-bullion-batch1.md</code>
</div>

</body>
</html>
"""


# ===== Main =====


def main() -> int:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    rendered: list[tuple[dict, dict]] = []
    print(f"[INFO] Generating mail merge output → {OUTPUT_DIR}")
    print()

    for prospect in PROSPECTS:
        variant_id = prospect["variant_id"]
        if variant_id not in VARIANTS:
            print(f"[WARN] {prospect['id']}: variant_id={variant_id} 不在 VARIANTS 內，skip。")
            continue
        variant = VARIANTS[variant_id]

        txt_path = OUTPUT_DIR / f"{prospect['id']}-cold.txt"
        html_path = OUTPUT_DIR / f"{prospect['id']}-cold.html"

        txt_path.write_text(render_txt(prospect, variant), encoding="utf-8")
        html_path.write_text(render_html(prospect, variant), encoding="utf-8")

        blockers = []
        if not prospect["contact_name"].strip():
            blockers.append("name")
        if not prospect["contact_email"].strip():
            blockers.append("email")
        status = f"⚠️  missing {', '.join(blockers)}" if blockers else "✓ ready"
        print(f"  {prospect['id']:18} ({prospect['track']} · {variant_id})  {status}")

        rendered.append((prospect, variant))

    index_path = OUTPUT_DIR / "index.html"
    index_path.write_text(render_index(rendered), encoding="utf-8")

    print()
    print(f"[DONE] {len(rendered)} emails 生成完畢。")
    print(f"       打開主控台：open {index_path}")
    print()

    pending = [p for p in PROSPECTS if not p["contact_email"].strip()]
    if pending:
        print(f"[REMINDER] {len(pending)} 家還缺 contact_email：")
        for p in pending:
            print(f"           - {p['company_tc']} ({p['id']})")
        print("           完成 LinkedIn / Hunter.io research 後填入 config.py 重跑此腳本。")

    return 0


if __name__ == "__main__":
    sys.exit(main())
