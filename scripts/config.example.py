"""Mail Merge Config — EXAMPLE

複製此檔為 `config.py` 後填入真實資料。
`config.py` 已被 .gitignore，不會 commit。

格式：純 Python dict，編輯時 IDE 會幫你抓語法錯。
"""

# ===== 你的個人資訊 =====
SENDER = {
    "name_tc": "[你的繁中姓名]",          # 例：陳大文
    "name_en": "[Your English Name]",     # 例：Tai-Man Chan
    "title_en": "Business Development",
    "email_from": "[your.email@xsyphon.com]",
    "phone": "+852-XXXX-XXXX",
    "calendly_link": "https://calendly.com/[your-handle]/cgse-bullion-15min",
    # 簽名 block（會塞到每封 email 結尾）
    "signature_block": (
        "{name_en} ({name_tc})\n"
        "{title_en} | xSyphon\n"
        "{email_from}\n"
        "{phone}\n"
        "xsyphon.com"
    ),
}

# ===== 5 家 prospects =====
# 發送前必須填入 contact_name + contact_email
# 留空者腳本仍會生成 .txt 但 To: 欄位會是 [PENDING — fill in before sending]
PROSPECTS = [
    {
        "id": "acetop",
        "company_tc": "領峰貴金屬",
        "company_en": "Acetop Precious Metals",
        "cgse_no": "145",
        "contact_name": "",           # 例：李總 / Mr. Lee
        "contact_title": "",          # 例：交易部主管
        "contact_email": "",          # 例：dealing@acetop.com
        "send_date": "2026-05-26",
        "track": "LP",
        "variant_id": "A",
    },
    {
        "id": "plotio",
        "company_tc": "百利好金融",
        "company_en": "Plotio Bullion",
        "cgse_no": "126",
        "contact_name": "",
        "contact_title": "",
        "contact_email": "",
        "send_date": "2026-05-28",
        "track": "LP",
        "variant_id": "B",
    },
    {
        "id": "royal-capital",
        "company_tc": "皇御金融",
        "company_en": "Royal Capital Precious Metals",
        "cgse_no": "076",
        "contact_name": "",
        "contact_title": "",
        "contact_email": "",
        "send_date": "2026-06-02",
        "track": "LP",
        "variant_id": "C",
        "icp_verify_deadline": "2026-06-01",  # 必須在此日期前驗證 ICP
    },
    {
        "id": "first-asia",
        "company_tc": "第一亞洲商人金融",
        "company_en": "First Asia Merchants Bullion",
        "cgse_no": "114",
        "contact_name": "",
        "contact_title": "",
        "contact_email": "",
        "send_date": "2026-06-04",
        "track": "LP",
        "variant_id": "D",
    },
    {
        "id": "goodwill",
        "company_tc": "信譽金行",
        "company_en": "Goodwill Gold Group",
        "cgse_no": "050",
        "contact_name": "",
        "contact_title": "",
        "contact_email": "",
        "send_date": "2026-06-09",
        "track": "WL",
        "variant_id": "Goodwill",
        "icp_verify_deadline": "2026-06-08",
    },
]
