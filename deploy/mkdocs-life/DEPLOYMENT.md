# mkdocs-life 部署指南 (Warm Editorial & Mindful Journal)

## 吉祥物意象
- **吉祥物**：林鹿寧靜冥想 (Scandinavian Forest Deer 🦌)
- **Symbol ID**：`#icon-deer-life`
- **定位**：優雅從容、沉思反饋、暖白紙感 editorial 閱讀美學

## 部署內容
1. **主題樣式檔**：`docs/stylesheets/life-theme.css`（暖白紙感、卡片網格、時間軸、引用區塊）
2. **範本覆寫**：`docs/overrides/main.html`（注入 Announcement 頂部導航鈕與靈鹿徽章）
3. **配置文件**：`mkdocs.yml`（在 `extra_css:` 中啟用 `stylesheets/life-theme.css`）

## 驗證方式
- 本地構建：`mkdocs serve` 或 `mkdocs build`
- 遠端部署：推送至 `main` 分支後透過 GitHub Actions 自動部署至 GitHub Pages。
