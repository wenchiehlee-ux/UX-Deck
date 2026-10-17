#!/usr/bin/env python3
"""Send 10-foot Frosted HUD popup to 1F Android TV via PiPup with exact showcase mascot icon."""

import sys
import os
import requests

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

def send_tv_popup(
    title: str = "客廳小柴看家 🐕",
    message: str = "家裡一切安好，柴柴幫您守護中 🐾 (顯示 10 分鐘)",
    duration: int = 600, # 10 minutes
    image_width: int = 80, # Compact 10-foot HUD proportion
    bg_color: str = "#ee0a0c12", # Dark frosted translucent slate
    title_color: str = "#38bdf8", # Focus Cyan
    message_color: str = "#ffffff",
    image_path: str = None
):
    tv_ip = "192.168.31.232"
    url = f"http://{tv_ip}:7979/notify"
    
    if image_path is None:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        image_path = os.path.join(base_dir, "sentinel_mascot_clean.png")
        if not os.path.exists(image_path):
            image_path = os.path.join(base_dir, "sentinel_icon.png")

    # Pass text and layout options via URL query params for UTF-8 preservation in NanoHTTPD
    params = {
        "title": title,
        "message": message,
        "duration": str(duration),
        "imageWidth": str(image_width),
        "titleColor": title_color,
        "messageColor": message_color,
        "backgroundColor": bg_color
    }

    print(f"[*] Sending 10-foot HUD popup to 1F TV: {url}")
    print(f"[*] Title: {title}")
    print(f"[*] Message: {message}")
    print(f"[*] Duration: {duration}s ({duration // 60}m), Icon Width: {image_width}px")
    print(f"[*] Icon: {image_path}")

    with open(image_path, "rb") as f:
        files = {"image": ("sentinel_mascot.png", f, "image/png")}
        resp = requests.post(url, params=params, files=files, timeout=10)
        print(f"[OK] 1F TV Response (HTTP {resp.status_code})")
        return resp.status_code == 200

if __name__ == "__main__":
    dur = 600
    if len(sys.argv) > 1:
        try:
            dur = int(sys.argv[1])
        except ValueError:
            pass
    send_tv_popup(duration=dur)
