# n8n Google Drive 整合除錯計畫

由於地端 n8n Google Drive 節點在檔案搜尋與地端憑證上有功能限制，我們改採直接呼叫 API 的方式來解決。

## 需要使用者協助事項

- **手動設定**: 由於先前自動匯入節點失敗，使用者需要手動設定 HTTP Request 節點。
- **憑證使用**: 確保 HTTP Request 節點使用的是 `Google Drive OAuth2 API` 憑證。

## 建議變更

### 工作流程架構 (Workflow Architecture)

- **替換項目**: 標準 Google Drive 節點 -> **HTTP Request 節點**
  - **方法**: GET
  - **網址**: `https://www.googleapis.com/drive/v3/files`
  - **查詢**: 使用 `q` 參數搭配 `name contains` (名稱包含) 與 `parents` (父資料夾) 進行篩選。
- **資料合併**: 使用 **Merge 節點** 將 API 搜尋結果與原始文章資料合併。

### 設定細節

- **目標資料夾**: `1tWsHVkYwLBaBAFhAj68K9OntLCCoQAt3` (i-Buzz消費者洞察)
- **搜尋語法**: `'<Folder_ID>' in parents and mimeType = 'application/vnd.google-apps.folder' and name contains '{{ $today.format('yyyyMMdd') }}'`
- **輸出欄位**: `files(id, name, webViewLink)`

### Google Sheets 自動化 (Apps Script)

- **目標**:
    1. D-H 欄位自動加入核取方塊。
    2. **A 欄位日期自動合併** (將相同日期的列群組起來)。
- **觸發時機**: `onChange` (變更時，用於偵測 n8n寫入事件)。
- **實作邏輯**:
  - 掃描 A 欄位，尋找連續且相同的日期數值。
  - 使用 `mergeVertically()` 進行垂直合併，將其視覺化分組。
  - **移除項目**: I 欄位的智慧方塊邏輯 (應使用者要求移除)。

## 驗證計畫

### 手動驗證流程

- **執行測試**: 使用範例文章執行一次工作流程。
- **檢查輸出**: 確認 HTTP Request 節點回傳的是一個 **Folder (資料夾)** 物件 (mimeType: `application/vnd.google-apps.folder`)。
- **檢查試算表**: 確認 "Cloud Link" 欄位填入的是有效的 Google Drive **資料夾** 連結。
