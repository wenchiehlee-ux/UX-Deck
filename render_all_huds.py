import os
import shutil
from playwright.sync_api import sync_playwright

scenarios = [
    {
        'id': 'doorbell',
        'title': '玄關訪客叮咚 🔔',
        'msg': '大門有人按門鈴，門鎖維持安全上鎖中 🐾',
        'accent': '#38bdf8',
        'icon_color': '#d97706',
        'progress': '65%'
    },
    {
        'id': 'washer_done',
        'title': '洗衣完成！ 🧺',
        'msg': '衣服已洗好，記得及時晾曬衣物喔 ✨',
        'accent': '#34d399',
        'icon_color': '#34d399',
        'progress': '100%'
    },
    {
        'id': 'washer_running',
        'title': '洗衣機運轉中 ⏱️',
        'msg': '運轉中... 預計 15:45 洗滌完成 🫧',
        'accent': '#38bdf8',
        'icon_color': '#38bdf8',
        'progress': '45%'
    },
    {
        'id': 'dryer_done',
        'title': '乾衣完成！ 👕',
        'msg': '烘衣行程已結束，請取出柔軟衣物 ✨',
        'accent': '#fb923c',
        'icon_color': '#fb923c',
        'progress': '100%'
    },
    {
        'id': 'calendar',
        'title': '今日行程提醒 📅',
        'msg': '今天整天：家庭聚餐、採買食材 ⏰',
        'accent': '#38bdf8',
        'icon_color': '#d97706',
        'progress': '30%'
    },
    {
        'id': 'battery_low',
        'title': '設備電量警告 🪫',
        'msg': '客廳夜燈電量低於 10%，請及時充電 ⚡',
        'accent': '#fbbf24',
        'icon_color': '#fbbf24',
        'progress': '10%'
    },
    {
        'id': 'delivery',
        'title': '外送到達！ 🛵',
        'msg': 'Foodpanda 外送員已抵達，請至門口取餐 🍱',
        'accent': '#fb923c',
        'icon_color': '#fb923c',
        'progress': '90%'
    }
]

os.makedirs('deploy/android-tv/huds', exist_ok=True)
os.makedirs('deploy/android-tv/www/huds', exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    for s in scenarios:
        html = f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Comfortaa:wght@600;700&family=Noto+Sans+TC:wght@400;500;700&family=Zen+Maru+Gothic:wght@500;700&display=swap" rel="stylesheet">
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      background: transparent !important;
      padding: 10px;
      margin: 0;
      width: fit-content;
      height: fit-content;
      overflow: hidden;
    }}
    .tv-hud-toast {{
      width: 520px;
      background: rgba(15, 23, 42, 0.40);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border: 1px solid {s['accent']}55;
      border-radius: 18px;
      padding: 1.3rem 1.5rem;
      display: flex;
      align-items: center;
      gap: 1.25rem;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6), 0 0 15px {s['accent']}25;
      font-family: 'Zen Maru Gothic', 'Comfortaa', 'Noto Sans TC', sans-serif;
      position: relative;
      overflow: hidden;
    }}
    .tv-hud-icon {{
      width: 52px;
      height: 52px;
      flex-shrink: 0;
      color: {s['icon_color']};
      filter: drop-shadow(0 0 10px {s['icon_color']}99);
    }}
    .tv-hud-content {{
      flex: 1;
      min-width: 0;
    }}
    .tv-hud-title {{
      font-size: 1.35rem;
      font-weight: 700;
      color: {s['accent']};
      margin-bottom: 0.35rem;
      display: flex;
      align-items: center;
      gap: 6px;
      font-family: 'Zen Maru Gothic', 'Comfortaa', sans-serif;
      letter-spacing: 0.01em;
    }}
    .tv-hud-message {{
      font-size: 1.15rem;
      color: #ffffff;
      line-height: 1.5;
      opacity: 0.98;
      font-family: 'Zen Maru Gothic', sans-serif;
      font-weight: 600;
      letter-spacing: 0.01em;
    }}
    .tv-progress {{
      position: absolute;
      bottom: 0;
      left: 0;
      height: 3px;
      width: {s['progress']};
      background: {s['accent']};
      box-shadow: 0 0 8px {s['accent']};
      border-radius: 0 0 0 14px;
    }}
  </style>
</head>
<body>
  <div class="tv-hud-toast" id="toast">
    <svg class="tv-hud-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
      <path d="M8.5 8.5c-.38 1.05-1.08 2.03-2.34 2.5-1.93.72-3.58-.3-3.66-1-.11-.99 1.18-6.53 4-7 1.92-.32 3.65.85 3.65 2.24A7.5 7.5 0 0 1 14 5.28c0-1.39 1.84-2.6 3.77-2.28 2.82.47 4.11 6.01 4 7-.08.7-1.73 1.72-3.66 1-1.26-.47-1.85-1.45-2.24-2.5" />
      <path d="M4.42 11.25A13.15 13.15 0 0 0 4 14.56C4 18.73 7.58 21 12 21s8-2.27 8-6.44a11.7 11.7 0 0 0-.49-3.31" />
      <path d="M8 14v.5" />
      <path d="M16 14v.5" />
      <path d="M11.25 16.25h1.5L12 17z" />
    </svg>
    <div class="tv-hud-content">
      <div class="tv-hud-title">{s['title']}</div>
      <div class="tv-hud-message">{s['msg']}</div>
    </div>
    <div class="tv-progress"></div>
  </div>
</body>
</html>"""
        page = browser.new_page()
        page.set_content(html, wait_until='networkidle')
        out_path = f"deploy/android-tv/huds/{s['id']}.png"
        page.locator('#toast').screenshot(path=out_path, omit_background=True)
        # Also copy to www/huds
        www_path = f"deploy/android-tv/www/huds/{s['id']}.png"
        shutil.copy2(out_path, www_path)
        if s['id'] == 'doorbell':
            shutil.copy2(out_path, "exact_card7_hud.png")
        page.close()
        print(f"Rendered {out_path} and copied to {www_path}")
    browser.close()
print("All scenarios rendered successfully!")
