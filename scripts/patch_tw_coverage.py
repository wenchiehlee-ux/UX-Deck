import os
import sys

idx_path = r"C:\Users\WJLEE\SynologyDrive\NAS\github.com\My-TW-Coverage\index.html"
with open(idx_path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Add JetBrains Mono & extra.css link in head
if "extra.css" not in html:
    insert_point = "</head>"
    new_head = (
        "  <!-- Google Fonts: JetBrains Mono for Institutional Tabular Alignment -->\n"
        '  <link rel="preconnect" href="https://fonts.googleapis.com">\n'
        '  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
        '  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700;800&display=swap" rel="stylesheet">\n'
        "  <!-- UX-Deck Unified Design System & TW-Coverage Theme -->\n"
        '  <link rel="stylesheet" href="extra.css">\n'
        + insert_point
    )
    html = html.replace(insert_point, new_head)
    print("Linked extra.css and JetBrains Mono in head.")

# 2. Add inline SVG sprite for owl-mascot right after <body> tag
if 'id="icon-owl-coverage"' not in html:
    body_tag = "<body>"
    with open(r"C:\Users\WJLEE\SynologyDrive\NAS\github.com\UX-Deck\deploy\tw-coverage\assets\owl-mascot.svg", "r", encoding="utf-8") as f:
        svg_content = f.read().strip()
    html = html.replace(body_tag, body_tag + "\n  " + svg_content)
    print("Embedded owl-mascot SVG sprite after <body>.")

# 3. Update app-nav branding to include owl mascot emoji/brand
old_logo = "content: 'TW Stock Database 📊';"
new_logo = "content: 'My-TW-Coverage 🦉 · 台股個股深度調研';"
if old_logo in html:
    html = html.replace(old_logo, new_logo)
    print("Updated navbar logo text.")

old_title = "<title>Taiwan Stock Coverage Database 📈</title>"
new_title = "<title>My-TW-Coverage · 台灣上市櫃公司個股深度調研 🦉</title>"
if old_title in html:
    html = html.replace(old_title, new_title)
    print("Updated page title.")

with open(idx_path, "w", encoding="utf-8") as f:
    f.write(html)

print("My-TW-Coverage index.html successfully updated!")
