import requests
import json

tv_ip = "192.168.31.232"
url = f"http://{tv_ip}:7979/notify"
image_path = r"C:\Users\WJLEE\SynologyDrive\NAS\github.com\UX-Deck\sentinel_icon.png"

data = {
    "duration": "600",
    "position": "0", # TopRight
    "title": "客廳守護系統 🐕",
    "titleColor": "#38bdf8",
    "titleSize": "18",
    "message": "UX-Deck 10-Foot HUD 部署成功！客廳大螢幕守護中。(顯示 10 分鐘)",
    "messageColor": "#ffffff",
    "messageSize": "14",
    "backgroundColor": "#ee0a0c12",
    "width": "120"
}

with open(image_path, "rb") as f:
    files = {
        "image": ("sentinel_icon.png", f, "image/png")
    }
    print(f"Sending multipart POST to {url}...")
    resp = requests.post(url, data=data, files=files, timeout=10)
    print("Response HTTP status:", resp.status_code)
    print("Response text:", resp.text)
