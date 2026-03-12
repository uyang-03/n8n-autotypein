# n8n AutoTypeIn 專案 (可移植版)

這是一個完整的 n8n 自動化工作流專案，支援跨電腦、跨平台的本機部署。包含自動化的資料處理腳本與 GitHub 同步工具。

## 🚀 快速開始 (適合已有環境者)

1. **下載專案**：
   ```bash
   git clone https://github.com/uyang-03/n8n-autotypein.git
   cd n8n-autotypein
   ```
2. **安裝依賴**：執行 `npm install`。
3. **啟動 n8n**：執行 `start_n8n.bat`。

---

## 🛠️ 首次安裝與完整設定流程 (新電腦必看)

### 步驟 1：環境準備
- **Node.js**: 建議 v20 LTS 版本（[下載](https://nodejs.org/)）。
- **Python**: 3.8+ 版本（[下載](https://www.python.org/)）。

### 步驟 2：核心組件安裝
在專案根目錄下開啟終端機，執行：
```powershell
npm install
```
這會根據專案內的 `package.json` 自動安裝正確版本的 n8n 及其依賴。

### 步驟 3：設定個人資料與憑證 (⚠️ 重要)
1. **Google Sheets ID**: 參考 `docs/` 下的說明文件，取得你的 Spreadsheet ID。
2. **授權認證**: 啟動 n8n 後，進入工作流中的 Google 節點，重新進行 OAuth2 授權（因為授權不隨檔案移動）。

### 步驟 4：設定 Apps Script (試算表端)
1. 將 `smart_chip_script.js` 貼入 Google 試算表的 Apps Script 編輯器。
2. 設定觸發器為「變更時 (On change)」。

---

## 📂 專案結構與工具說明
- `start_n8n.bat`: 優化後的一鍵啟動腳本。
- `n8n_workflow_final.json`: 最新版工作流配置檔。
- `scrub_json.py` / `github_update.py`: 核心資料處理與同步工具。
- `docs/`: 包含詳細的 Google 授權、遷移指引等說明文件。

## 🛠️ 維護與故障排除
- **路徑問題**: 啟動腳本已動態化路徑，若仍顯示 `Not Found`，請確認是否已執行 `npm install`。
- **雙重 node_modules**: 已在 `.gitignore` 排除，請避免手動手動搬移此目錄。

---
*Created by Antigravity AI Assistant.*
