import os
import requests

env_path = r"C:\Users\WJLEE\SynologyDrive\NAS\github.com\HomeAssistant\.env"
token = ""
if os.path.exists(env_path):
    with open(env_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("HA_TOKEN1="):
                token = line.split("=", 1)[1].strip()

if token:
    headers = {"Authorization": f"Bearer {token}"}
    try:
        r = requests.get("http://192.168.31.101:8123/api/states", headers=headers, timeout=5)
        if r.status_code == 200:
            for e in r.json():
                eid = e["entity_id"].lower()
                if "tv" in eid or "android" in eid or "pipup" in eid:
                    print(f"{e['entity_id']}: state={e['state']}")
    except Exception as ex:
        print("Error:", ex)
