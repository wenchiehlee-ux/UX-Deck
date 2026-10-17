import os
import json
import requests

env_path = r"C:\Users\WJLEE\SynologyDrive\NAS\github.com\HomeAssistant\.env"
token = ""
if os.path.exists(env_path):
    with open(env_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("HA_TOKEN1="):
                token = line.split("=", 1)[1].strip()

if not token:
    print("No HA token found")
    exit(1)

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

# Payload matching Home Assistant's automations
payload_data = {
    "duration": 60,
    "position": 0,
    "title": "客廳守護系統 🐕",
    "titleColor": "#38BDF8",
    "titleSize": 18,
    "message": "UX-Deck 10-Foot HUD 部署成功！客廳大螢幕守護中。",
    "messageColor": "#FFFFFF",
    "messageSize": 14,
    "backgroundColor": "#EE0A0C12",
    "media": {
        "image": {
            "uri": "https://img.icons8.com/fluency/96/dog.png",
            "width": 64
        }
    }
}

payload = {
    "payload_json": json.dumps(payload_data, ensure_ascii=False)
}

url = "http://192.168.31.101:8123/api/services/rest_command/pipup_notify_1f"
print("Calling HA service:", url)
r = requests.post(url, headers=headers, json=payload, timeout=8)
print("Response:", r.status_code, r.text)
