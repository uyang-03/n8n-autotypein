# n8n-autotypein 自動化系統

自動化抓取 i-Buzz 每週觀點文章，並寫入 Google Sheets 的完整解決方案。

## 📁 檔案說明

| 檔案 | 用途 |
| :--- | :--- |
| `autotypein_v1.6.json` | **n8n 工作流程主體**（直接匯入使用） |
| `smart_chip_script.js` | **Google Apps Script**（貼入試算表使用） |
| `config-template.md` | **個人化設定範本**（填入你的 ID，不要上傳到 GitHub） |
| `start_n8n.bat` | **Windows 一鍵啟動腳本** |
| `docs/` | 說明文件資料夾（操作手冊、結案報告等） |

---

## 🚀 首次使用完整設定流程

### 步驟 1：安裝 Node.js

前往 [https://nodejs.org](https://nodejs.org) 下載並安裝 **LTS 版本**。

> ✅ 安裝完後在終端機輸入 `node -v` 確認版本號出現即代表成功。

### 步驟 2：安裝 n8n

在 PowerShell 或命令提示字元中執行：

```powershell
npm install -g n8n
```

> ⚠️ **若出現 `ECONNRESET` 網路錯誤**，請依序嘗試：
>
> 1. 重新執行一次（有時只是網路短暫不穩）
> 2. 清除快取後再試：`npm cache clean --force`，再執行 `npm install -g n8n`
> 3. 如果仍然失敗，改用以下指令繞過嚴格的連線驗證：
>
>    ```powershell
>    npm install -g n8n --legacy-peer-deps
>    ```
>
> 4. 若一直無法下載，可能是你的網路環境有 Proxy，請確認或關閉後再試。

### 步驟 3：填入你的個人設定 (⚠️ 最重要的步驟)

1. 複製一份 `config-template.md`，重新命名為 `config-私人設定.md`（或任意名稱），**不要上傳到 GitHub**。
2. 參考範本說明，取得以下資訊並記錄下來：
   - **Google Drive 資料夾 ID**（Asia KOL / Fans Feed / i-Buzz 各一個）
   - **Google Sheets Spreadsheet ID**
3. 用 VS Code 打開 `autotypein_v1.6.json`，使用 **`Ctrl + H`（取代）** 功能：
   - 將所有 `YOUR_SPREADSHEET_ID_HERE` 換成你的試算表 ID
   - 將不同位置的 `YOUR_FOLDER_ID_HERE` 換成對應的資料夾 ID
   - ⚠️ 注意：不同節點可能需要不同的資料夾 ID，請逐一確認

> 📖 詳細取得 ID 的步驟請見 `config-template.md`

### 步驟 4：啟動 n8n

**方法一（Windows 推薦）**：直接雙擊 `start_n8n.bat` 啟動。

**方法二（手動）**：

```powershell
npx n8n
```

開啟瀏覽器，前往 `http://localhost:5678`。

> ⚠️ 每次電腦重新開機後，都需要重新啟動 n8n。

### 步驟 5：匯入工作流程

1. 在 n8n 介面，點選左側 **Workflows** → **Add Workflow**。
2. 點右上角 **`...`** → **Import from File**。
3. 選擇已修改好的 `autotypein_v1.6.json` 檔案（即步驟 3 填好 ID 的版本）。

### 步驟 6：設定 Google 授權憑證 (⚠️ 必要步驟)

> 憑證因安全性不會隨工作流程轉移，需要在新電腦重新授權。

工作流程匯入後，含有紅色警告的節點需要重新連接憑證：

- **Google Sheets OAuth2**：用於寫入試算表
- **Google Drive OAuth2**：用於搜尋雲端資料夾

點進紅色節點，選擇或新增你的 Google 帳號授權即可。

詳細申請步驟請參考 `docs/google_auth_setup_guide.md`。

### 步驟 7：設定 Google Sheets Apps Script

1. 打開目標 Google 試算表。
2. 點選選單 **擴充功能** → **Apps Script**。
3. 將 `smart_chip_script.js` 的全部內容貼入。
4. 儲存後，點選 **觸發器** → 新增觸發器：
   - 函式：`handleDataChange`
   - 事件類型：**試算表變更時 (On change)**

### 步驟 8：啟用工作流程

回到 n8n，將工作流程右上角的開關切換為 **Active（啟用）**。

---

## 📂 說明文件

詳細文件請見 `docs/` 資料夾：

- `project_report.md` — 系統架構與運作邏輯結案報告
- `n8n_operation_manual.md` — n8n 地端版操作手冊
- `migration_guide.md` — 詳細遷移注意事項
- `walkthrough.md` — 開發過程技術導覽
- `google_auth_setup_guide.md` — Google API 授權設定教學
