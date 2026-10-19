# UX-Deck

> **專注於多專案跨平台一致性與差異化體驗的 UX 技能庫 (Design System & Skills Deck)**  
> 統一設計底層規範（8pt 網格、語意色彩、WCAG AA 對比、流暢動效），同時為各關聯專案打造專屬且優雅精緻的獨特視覺風格。

---

## 🎯 專案定位與設計理念

本倉庫是九大關聯兄弟端點的 **視覺體驗中樞 (UX Deck)** 與 **Antigravity 技能發布庫 (Skills Hub)**，與外部 ../skills 自動保持同步：

```
                                              +-------------------------+
                                              |      UX-Deck Tokens     |
                                              | 8pt Grid · Shadows · AA |
                                              +-------------------------+
                                                           |
    +-------------+------------+------------+------+-------+------+------------+------------+------------+
    |             |            |            |      |       |      |            |            |            |
    v             v            v            v      v       v      v            v            v            v
[mkdocs-life] [AlertMgr]  [YTAudio]  [mkdocs-inv] [TW-Cov] [TV-HUD] [Synology]  [InvestorConf]    [VIX]
 人文生活誌    SaaS情報     影音播放器   大盤配置   個股調研  電視彈窗  私有雲DevOps  法說會逐字稿   全球波動率雷達
 (Pages)      (Pages)      (Pages)      (Pages)    (Pages)   (TV)     (NAS)        (Pages)       (Pages)
```

### 核心哲學：一致底層，獨特個性 (Consistent Foundation, Differentiated Soul)
- **一致性 (Consistency)**：所有專案共享相同間距規範、圓角梯度、陰影深度層級、流暢的 Bézier 曲線動效，以及對比度無障礙標準。
- **差異化 (Differentiation)**：依據不同載體（文件/日誌、生產力儀表板、多媒體播放器、大盤金融、台股個股調研、客廳大螢幕、私人雲端 DevOps、法人說明會與全球波動率黑天鵝預警）塑造最適化視覺風格與操作心智模型。

---

## 📊 兄弟專案設計與動物意象矩陣 (Design & Animal Mascot Matrix)

| 專案名稱 | 載體型態 | 主題定位 | 動物意象 (Mascot Icon) | 主色調 / 色彩語意 | 關鍵 UX 元件 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **[mkdocs-life](#1-skill-ux-mkdocs-life)** | GitHub Pages (MkDocs) | 溫潤人文雜誌 (Warm Editorial) | **幾何林鹿 🦌 (Mindful Deer)**<br>#icon-deer-life | 鼠尾草綠 (#0d9488)、暖紙米白 (#faf8f5)、磚橘 (#e07a5f) | 故事卡片、反思引言塊、生命里程碑時間軸 |
| **[GoogleAlertManager](#2-skill-ux-google-alert-manager)** | GitHub Pages (Web App) | SaaS 情報過濾 (Signal Intelligence) | **破曉警報鳥 🐦 (Alert Bird)**<br>#icon-falcon-radar | 活力警報橘 (#ea580c)、日落橘 (#f97316)、冷灰純白 | 快速分類篩選膠囊、未讀脈衝點、單鍵收藏/封存 |
| **[YoutubeAudio.Fetch](#3-skill-ux-youtube-audio-fetch)** | GitHub Pages (Web App) | 工作室多媒體聲波 (Studio Soundwave) | **聲波座頭鯨 🐋 (Sonic Whale)**<br>#icon-whale-sonic | 幻紫 (#8b5cf6)、聲波青綠 (#06b6d4)、純白底 (#ffffff) | 雙欄集數導覽、YouTube影格與即時逐字稿同步、立體聲波播放面板 |
| **[mkdocs-investment](#4-skill-ux-mkdocs-investment)** | GitHub Pages (MkDocs) | 大盤資產配置 (Fintech Slate) | **幾何狂牛 🐂 / 守護熊 🐻**<br>#icon-bull-fintech / #icon-bear-defense | 皇室藍 (#2563eb)、大盤紅漲綠跌、安全防禦指標 | KPI 指標看板、等寬對齊數據表、多頭/避險多維圖表 |
| **[My-TW-Coverage](#5-skill-ux-tw-coverage)** | GitHub Pages (MkDocs) | 台股個股深度調研 (Equity Radar) | **拍拍翅萌萌鴞 🦉 (Flapping Owlet)**<br>#icon-owl-coverage | 台灣冷杉綠 (#059669)、調研琥珀金 (#d97706)、紅漲綠跌 | BUY/HOLD 投資評級膠囊、目標價試算、PER/ROE/EPS 估值雷達 |
| **[HomeAssistant](#6-skill-ux-homeassistant-tv)** | Android TV (Popup/HUD) | 10英呎客廳毛玻璃 (Frosted Glass HUD) | **客廳小管家 柴柴 🐕 (Faithful Shiba)**<br>#icon-sentinel-tv | 天際青輝光 (#0284c7)、毛玻璃深幕 (rgba(10,12,18,0.92)) | 3–4米超清晰大字階、電視遙控 D-pad 焦點框、生活事件自動倒數光條 |
| **[wenchiehlee.quickconnect.to](#7-skill-ux-synology-nas)** | Synology NAS (Web Station) | 私人雲端 DevOps 堡壘 (Cyber Slate) | **裝甲穿山甲 🛡️ / 守護貓 🐱**<br>#icon-pangolin-shield | 群暉藍 (#0284c7)、黑曜賽博岩板 (#0f172a)、霓虹盾光 (#38bdf8) | 原生導航膠囊、Docker 容器狀態 HUD、Tailscale 私有通道徽章 |
| **InvestorConference** | GitHub Pages (Vite/TS) | 法說領航庫 (IR Intelligence) | **領航雄鷹 🦅 (Sovereign Eagle)**<br>#icon-eagle-ir | 領航翡翠綠 (#22a553)、薄荷翠底 (#f0fdf4)、深墨翠字 (#166534) | 季度法說會矩陣、音檔逐字稿同步播放器、中英 IR 簡報下載鈕、MOPS 直連 |
| **VIX** | GitHub Pages (Plotly App) | 全球波動率雷達 (Crash Sentinel) | **幾何黑天鵝 🦢 (Black Swan)**<br>#icon-swan-vix | 恐慌赤紅 (#ef4444)、警戒暖橘 (#f97316)、平靜綠 (#10b981)、曜石墨 | 即時波動率與恐慌指數 KPI、市場情緒光譜儀、歷史重大黑天鵝股災回測 |
---

## 📦 技能庫架構 (Skills Structure)

本倉庫技能遵循規範（與 `../skills/common/skill-investment-decision-coach` 相同之 `skill-*` 命名前綴），已同步至 `../skills/common/` 與本機 `.agents/skills`：

```text
UX-Deck/
├── tokens/
│   ├── design-tokens.json                 # 跨工具可消費之語意 Token 定義 (含圖示與動物象徵)
│   ├── tokens.css                         # 全域共享 CSS 變數基礎與微動態動畫
│   └── icons/
│       └── animal-icons.svg               # 24x24 向量動物意象與精修圖示主 Sprite
├── skills/
│   ├── skill-ux-design-system/            # 核心主設計系統規範與差異化矩陣
│   │   ├── SKILL.md
│   │   ├── references/design-matrix.md
│   │   └── references/animal-iconography.md # 動物意象與圖示精修設計規範

│   ├── skill-ux-mkdocs-life/              # mkdocs-life 專用技能
│   │   ├── SKILL.md
│   │   ├── resources/mkdocs-life.css
│   │   └── examples/mkdocs.yml
│   ├── skill-ux-google-alert-manager/     # GoogleAlertManager 專用技能
│   │   ├── SKILL.md
│   │   ├── resources/alert-manager-theme.css
│   │   └── examples/alert-card-component.html
│   ├── skill-ux-youtube-audio-fetch/      # YoutubeAudio.Fetch 專用技能
│   │   ├── SKILL.md
│   │   ├── resources/media-player-theme.css
│   │   └── examples/player-interface.html
│   ├── skill-ux-mkdocs-investment/        # mkdocs-investment 專用技能
│   │   ├── SKILL.md
│   │   ├── resources/mkdocs-investment.css
│   │   └── examples/kpi-widget.html
│   ├── skill-ux-tw-coverage/              # My-TW-Coverage 台股個股調研專用技能
│   │   └── SKILL.md
│   └── skill-ux-homeassistant-tv/         # HomeAssistant Android TV 專用技能
│       ├── SKILL.md
│       ├── resources/tv-popup.css
│       └── examples/tv-notification-card.yaml
└── scripts/
    ├── sync_skills.py                     # Python 跨平台高效同步工具 (MD5 增量、驗證、自訂路徑)
    └── sync-skills.ps1                    # PowerShell 快捷相容包裝腳本
```

---

## 🚀 技能同步流程 (Python Sync Engine)

本倉庫提供具備高度彈性的跨平台 Python 同步引擎 [sync_skills.py](file:///C:/Users/WJLEE/SynologyDrive/NAS/github.com/UX-Deck/scripts/sync_skills.py)：
- **MD5 增量同步**：僅寫入異動或新增檔案，避免無謂磁碟 I/O。
- **YAML Frontmatter 格式驗證**：自動校驗每個技能的 `name` 與 `description`。
- **遺留目錄清理**：自動清除舊版未帶前綴的目錄。

### 常用指令

```bash
# 1. 預覽變更 (Dry Run，不更動磁碟)
python ./scripts/sync_skills.py --dry-run

# 2. 執行同步至 ../skills/common (並同步更新本機 .agents/skills)
python ./scripts/sync_skills.py

# 3. 顯示完整檔案比對細節 (Verbose)
python ./scripts/sync_skills.py -v

# 4. 自訂目標目錄 (彈性同步至任何專案或共用目錄)
python ./scripts/sync_skills.py --target "../my-other-workspace/skills"

# 5. 強制覆蓋所有檔案
python ./scripts/sync_skills.py --force
```

---

## 🎨 各專案落地指引 (How to Apply)

### 1. `GoogleAlertManager` (SaaS 情報過濾) — ✅ 已落地完成
- **部署指南**：[deploy/google-alert-manager/DEPLOYMENT.md](file:///C:/Users/WJLEE/SynologyDrive/NAS/github.com/UX-Deck/deploy/google-alert-manager/DEPLOYMENT.md)
- **吉祥物意象**：精密雷達隼 🦅 (`#icon-falcon-radar`)，象徵高空雷達偵察與雜訊剃除。
- **亮點**：常駐頂部品牌欄、跨專案藥丸按鈕導航、Docsify 即時利多/利空分析結論 Callout 容器與 SaaS 表格升級。

### 2. `mkdocs-life` (溫潤人文日誌) — ✅ 已落地完成
- **部署指南**：[deploy/mkdocs-life/DEPLOYMENT.md](file:///C:/Users/WJLEE/SynologyDrive/NAS/github.com/UX-Deck/deploy/mkdocs-life/DEPLOYMENT.md)
- **吉祥物意象**：幾何林鹿 🦌 (`#icon-deer-life`)，象徵從容沉思與生活記錄。
- **亮點**：`life-theme.css` 暖白紙感排版、卡片網格、頂部靈鹿徽章與跨專案導航按鈕。

### 3. `YoutubeAudio.Fetch` (大氣深邃媒體) — ✅ 已落地完成
- **部署指南**：[deploy/youtube-audio-fetch/DEPLOYMENT.md](file:///C:/Users/WJLEE/SynologyDrive/NAS/github.com/UX-Deck/deploy/youtube-audio-fetch/DEPLOYMENT.md)
- **吉祥物意象**：流暢聲波鯨 🐋 (`#icon-whale-sonic`)，象徵深海聽覺共鳴與音頻光芒。
- **亮點**：常駐頂部海洋微光品牌列、即時逐字稿同步、跨專案快捷導航。

### 4. `My-TW-Coverage` (台股個股深度調研) — ✅ 已落地完成
- **部署指南**：[deploy/tw-coverage/DEPLOYMENT.md](file:///C:/Users/WJLEE/SynologyDrive/NAS/github.com/UX-Deck/deploy/tw-coverage/DEPLOYMENT.md)
- **吉祥物意象**：拍拍翅萌萌鴞 🦉 (`#icon-owl-coverage`)，象徵犀利個股洞見。
- **亮點**：頂部浮動萌鴞品牌欄、index.html 統一配色徽章、圓角搜尋偏移防重疊、隱藏冗餘 corner。

### 5. `HomeAssistant` (Android TV 10-Foot HUD) — ✅ 已實機上線
- **實體部署套件**：專屬部署目錄位於 [deploy/android-tv/](file:///C:/Users/WJLEE/SynologyDrive/NAS/github.com/UX-Deck/deploy/android-tv/)，內含完整指南 [DEPLOYMENT.md](file:///C:/Users/WJLEE/SynologyDrive/NAS/github.com/UX-Deck/deploy/android-tv/DEPLOYMENT.md)。
- **吉祥物意象**：客廳守護柴柴 🐕 (`#icon-sentinel-tv`)。
- **實機落地**：更新客廳 1F 電視 PiPup 通知至右上角 10-Foot 曜石毛玻璃 HUD，行程提醒與家電狀態全部自動同步。

---

## 📄 License
MIT License.
