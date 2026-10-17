# HomeAssistant on Android TV: 10-Foot Frosted HUD 部署指南

本指南提供將 **UX-Deck 10-Foot Frosted HUD** 部署至真實客廳 **Android TV (Google TV)** 與 **Home Assistant** 的完整步驟。

---

## 📐 10 英呎電視介面設計準則

| 設計維度 | 規範標準 | 理由與效益 |
| :--- | :--- | :--- |
| **觀看距離** | 3 ~ 4 公尺客廳沙發視角 | 文字最小 20px，標題 26px~32px，高對比白字配深色毛玻璃 |
| **停駐位置** | 螢幕右上角 (`top: 48px, right: 56px`) | 完全避開中央電影主體畫面與下方字幕條（無碰撞干擾） |
| **遙控器 D-pad** | 亮青色焦點外框 (`border: 2px solid #38bdf8`) | 高可見度發光 Focus 動效，支援電視遙控器左右切換與 OK 鍵 |
| **自動關閉進度條** | 底部動態倒數收合條 (預設 8 秒) | 讓觀影者一目了然通知剩餘停留時間 |
| **象徵吉祥物** | 客廳守護犬 🐕 (`#icon-sentinel-tv`) | 守護家庭安全，具備呼吸光暈微動態 |

---

## 🚀 部署步驟 (Deployment Steps)

### 步驟 1：部署靜態資源至 Home Assistant

將本專案 `deploy/android-tv/www/` 內的所有檔案複製到 Home Assistant 的 `/config/www/ux-deck/` 目錄：

```bash
# 透過 SSH 或 Samba 將資源放置於 HA www 目錄
mkdir -p /config/www/ux-deck/
cp ./deploy/android-tv/www/tv-popup.css /config/www/ux-deck/
cp ./deploy/android-tv/www/animal-icons.svg /config/www/ux-deck/
```

> **驗證連結**：在瀏覽器造訪 `http://<YOUR_HA_IP>:8123/local/ux-deck/tv-popup.css`，確認可正常載入。

---

### 步驟 2：啟用客廳電視主題 (Theme)

1. 將 [themes/tv_frosted_hud.yaml](./themes/tv_frosted_hud.yaml) 複製至 Home Assistant 的 `/config/themes/` 目錄。
2. 確認 `configuration.yaml` 中包含主題支援：
   ```yaml
   frontend:
     themes: !include_dir_merge_named themes
   ```
3. 在 Home Assistant 中前往 **開發者工具** -> **YAML** -> 點擊 **重新載入主題**。

---

### 步驟 3：部署電視彈窗通知自動化 (Automations)

1. 將 [automations/tv_notifications.yaml](./automations/tv_notifications.yaml) 內的規則合併至您的 `/config/automations.yaml`。
2. 替換您的門鈴、相機與家電實體名稱（例如 `binary_sensor.front_door_doorbell`、`camera.front_door`）。
3. 支援兩大電視推播方案：
   - **方案 A (最通用 - Notifications for Android TV)**：在電視安裝 `Notifications for Android TV` App，HA 配置 `notify.android_tv`，支援原生系統層覆蓋通知。
   - **方案 B (進階相機串流 - PiPup)**：在電視透過 ADB 安裝 `PiPup`，支援直接在電視任意畫面中彈出 HTML 或監視器 live 快照。

---

### 步驟 4：客廳電視專屬大看板 (Lovelace Dashboard)

若電視端使用 **Fully Kiosk Browser**、**Wallpanel** 或 **Home Assistant Android TV App**：
1. 建立一個新 Dashboard 或將 [dashboards/tv_dashboard.yaml](./dashboards/tv_dashboard.yaml) 匯入。
2. 將主題設定為 `tv_frosted_hud`。
3. 享受專為電視遙控器方向鍵設計的大卡片與即時監控視野。

---

## 🎮 本地互動式模擬器 (Local Simulator)

在將配置推送至實體電視前，您可以在本機直接啟動互動式電視模擬器：

- 開啟檔案：[simulator.html](./simulator.html)
- 支援按鍵操作：
  - **鍵盤方向鍵 ◀ / ▶**：切換遙控器焦點按鈕。
  - **Enter 鍵**：觸發選中動作（如開門、通話、關閉）。
  - **按鍵 1 / 2 / 3**：即時測試門鈴訪客、周邊警報、家電完成 3 種真實情境。
  - **Esc 鍵**：手動關閉當前通知。
