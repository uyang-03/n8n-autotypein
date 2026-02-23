# 地端 n8n 設定與疑難排解指南

## 1. 地端環境設定

我們成功在 Windows 環境下使用 `npx` 建立了地端 n8n 環境。

- **啟動腳本**: 建立了 `C:\Users\yuyan\.gemini\antigravity\scratch\start_n8n.bat`，可一鍵啟動。
- **存取網址**: [http://localhost:5678](http://localhost:5678)

## 4. Google Drive 整合 (透過 API 自動搜尋資料夾)

我們使用 n8n HTTP Request 節點與 Google Drive API v3 實作了強大的資料夾搜尋機制。

### 工作流程邏輯 (Workflow Logic)

1. **提取資料夾 ID**: 從原始 HTML 中定位父資料夾 ID (`1OaXcIEY0CXDTHL4TzBbfvwrMUeaXrzPD`)。
2. **API 搜尋查詢**:
    - 僅查詢資料夾: `mimeType = 'application/vnd.google-apps.folder'`
    - 指定搜尋父資料夾: `'<ID>' in parents`
    - 比對日期格式: `name contains '{{ $today.format('yyyyMMdd') }}'`
3. **動態對應 (Dynamic Mapping)**:
    - 若 `Brand` 為 "Asia KOL"，搜尋資料夾 `1CzGWmLOqeCkkjKnuxqVbDJup-PVFfU7H`
    - 若 `Brand` 為 "Fans Feed"，搜尋資料夾 `1czmLljMgsk1d33fQ_GTzpMl8GBuVsT14`
    - 預設 (Consumer Insights)，搜尋資料夾 `1tWsHVkYwLBaBAFhAj68K3OntLCCoQAt3`

## 5. Google Sheets 自動化 (Apps Script)

我們部署了專用的 Google Apps Script 來自動化資料輸入時的格式設定。

### 功能特性 (Features)

- **自動核取方塊 (D-H 欄)**: 將 `TRUE`/`FALSE` 文字轉換為互動式核取方塊。
- **智慧連結轉換 (I 欄)**:
  - 自動偵測 Google Drive 網址。
  - 將純文字網址轉換為可點擊且帶有預覽卡的 **Rich Text 連結**。
  - *注意：目前因 Google 平台對此帳號的限制，無法透過程式碼自動轉換為「檔案智慧方塊 (File Smart Chips)」。腳本提供了最佳替代方案 (Rich Link)，可透過 UI 一鍵手動轉換。*
- **日期自動合併 (A 欄)**:
  - 自動偵測 A 欄中連續相同的日期。
  - **邏輯**: 解除範圍合併 -> 自動填補空白儲存格 (資料修復) -> 重新合併相同群組。
  - 防止「合併衝突 (Merge Conflict)」錯誤並確保資料完整性。

### 程式碼 (v15 穩定版)

腳本使用「修復與合併 (Repair & Merge)」策略來處理 Google Sheets 的合併行為：

```javascript
function fixAndMergeDates(sheet) {
  // 1. 解除合併 (重置所有合併狀態)
  // 2. 自動填補 (將上方數值複製到因拆分而產生的空白格)
  // 3. 重新合併 (依據顯示值分組)
}
```

## 2. Google Cloud 憑證修復

導致 Workflow 無法執行的主要原因是地端實例缺少 OAuth2 憑證。

### 問題描述

- `Untitled-2.json` 顯示 Google Sheets 節點有憑證錯誤。
- 由於 Callback URL 不同，地端 n8n 無法直接共用雲端版本的憑證。

### 解決方案

1. **建立新專案**: 在 Google Cloud Console 中建立了 `n8n-local` 專案。
2. **設定 OAuth**:
    - **重新導向 URI**: 新增了 `http://localhost:5678/rest/oauth2-credential/callback`。
    - *修正*: 用戶最初將其填入 "JavaScript 來源 (Origins)"，已更正為 "重新導向 URI (Redirect URIs)"。
3. **完成驗證**: 使用新的 Client ID/Secret 成功將 n8n 連接至 Google 帳戶。

## 3. Workflow 驗證

用戶確認在套用新憑證後，`Untitled-2.json` 已可成功執行。

## 後續步驟 (選用)

- **Tunneling (通道)**: 如果您需要接收外部 Webhooks (例如來自 LINE 或建立 API 端點)，啟動 n8n 時需要加上 `--tunnel` 參數。
- **自動啟動**: 設定 n8n 隨 Windows 開機自動啟動。
