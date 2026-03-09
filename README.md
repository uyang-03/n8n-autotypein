# n8n-autotypein 自動化系統

自動化抓取 i-Buzz 每週觀點文章，並寫入 Google Sheets 的完整解決方案。

## 📁 檔案說明

| 檔案 | 用途 |
| :--- | :--- |
| `autotypein_v1.6.json` | **n8n 工作流程主體**（直接匯入使用） |
| `smart_chip_script.js` | **Google Apps Script**（貼入試算表使用） |
| `docs/` | 說明文件資料夾（操作手冊、結案報告等） |

---

## 🚀 在新電腦上快速啟動 (Migration Guide)

### 步驟 1：安裝 n8n 環境

確認已安裝 [Node.js (LTS)](https://nodejs.org/)，然後在終端機執行：

```bash
npm install -g n8n
```

### 步驟 2：啟動 n8n

```bash
npx n8n
```

開啟瀏覽器，前往 `http://localhost:5678`。

> ⚠️ **注意**：每次電腦重新開機後，都需要重新執行此指令才能啟動 n8n。

### 步驟 3：匯入工作流程

1. 在 n8n 介面，點選左側 **Workflows** → **Add Workflow**。
2. 點右上角 **`...`** → **Import from File**。
3. 選擇本倉庫的 `autotypein_v1.6.json` 檔案。

### 步驟 4：重新設定授權憑證 (⚠️ 必要步驟)

> 憑證因安全性不會隨工作流程轉移，需要在新電腦重新授權。

需要重新連接的服務：

- **Google Sheets OAuth2**：用於寫入試算表
- **Google Drive OAuth2**：用於搜尋雲端資料夾

在工作流程中，任何顯示紅色的節點都代表憑證失效，點進去重新選擇或新增憑證即可。

詳細申請步驟請參考 `docs/google_auth_setup_guide.md`。

### 步驟 5：設定 Google Sheets 腳本

1. 打開目標 Google 試算表。
2. 點選選單 **擴充功能** → **Apps Script**。
3. 將 `smart_chip_script.js` 的全部內容貼入。
4. 儲存後，點選 **觸發器** → 新增觸發器：
   - 函式：`handleDataChange`
   - 事件類型：**試算表變更時 (On change)**

### 步驟 6：啟用工作流程

回到 n8n，將工作流程右上角的開關切換為 **Active（啟用）**。

---

## ⚙️ 系統設定值

如果轉移到另一張試算表，請更新工作流程中的以下 ID：

| 設定 | 值 |
| :--- | :--- |
| Google Sheets ID | `YOUR_SPREADSHEET_ID_HERE` |
| Template Sheet ID | `YOUR_SHEET_ID_HERE` |
| Asia KOL Drive 資料夾 ID | `YOUR_FOLDER_ID_HERE` |
| Fans Feed Drive 資料夾 ID | `YOUR_FOLDER_ID_HERE` |
| i-Buzz 預設資料夾 ID | `YOUR_FOLDER_ID_HERE` |

---

## 📂 說明文件

詳細文件請見 `docs/` 資料夾：

- `project_report.md` — 系統架構與運作邏輯結案報告
- `n8n_operation_manual.md` — n8n 地端版操作手冊
- `migration_guide.md` — 詳細遷移注意事項
- `walkthrough.md` — 開發過程技術導覽
- `google_auth_setup_guide.md` — Google API 授權設定教學
