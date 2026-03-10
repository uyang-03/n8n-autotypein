# ⚙️ 個人化設定範本 (config-template.md)

> **說明**：請將下方的 `YOUR_XXX_HERE` 全部換成你自己的實際值，再貼回 `autotypein_v1.6.json` 中對應的位置。
> 也可以把這份檔案保存在本機，作為設定備忘錄（請勿上傳到 GitHub）。

---

## 🔑 Step 1：取得 Google Folder ID

1. 打開你的 Google Drive，進入該資料夾
2. 查看瀏覽器網址列，例如：
   `https://drive.google.com/drive/u/0/folders/1AbCdEfGhIjKlMnOpQ`
3. 最後那一段 `1AbCdEfGhIjKlMnOpQ` 就是 **Folder ID**

## 📊 Step 2：取得 Google Spreadsheet ID

1. 打開你的 Google Sheets
2. 查看瀏覽器網址列，例如：
   `https://docs.google.com/spreadsheets/d/1XyZAbCdEfGhIjKl/edit`
3. 中間那一段 `1XyZAbCdEfGhIjKl` 就是 **Spreadsheet ID**

---

## 📋 我的設定值（請自行填入）

| 設定項目 | 我的 ID | 說明 |
| :--- | :--- | :--- |
| **Google Sheets Spreadsheet ID** | `（請填入）` | 寫入試算表的 ID |
| **Asia KOL 主資料夾 ID** | `（請填入）` | Asia KOL 品牌的 Google Drive 根資料夾 |
| **Fans Feed 主資料夾 ID** | `（請填入）` | Fans Feed 品牌的 Google Drive 根資料夾 |
| **i-Buzz 預設主資料夾 ID** | `（請填入）` | i-Buzz 品牌的 Google Drive 根資料夾 |
| **建立本週三主資料夾的父資料夾 ID** | `（請填入）` | 所有週次資料夾的存放位置 |
| **搜尋主資料夾用的根資料夾 ID** | `（請填入）` | 搜尋週次資料夾時的搜尋根目錄 |

---

## 🔧 Step 3：如何在 JSON 中替換

填完上方表格後，在 `autotypein_v1.6.json` 裡用「尋找/取代」功能：

- 用文字編輯器（如 VS Code）打開 `autotypein_v1.6.json`
- 使用 `Ctrl + H`（取代）功能
- 搜尋：`YOUR_FOLDER_ID_HERE`（注意：不同節點的資料夾 ID 可能不同，請逐一確認）
- 搜尋：`YOUR_SPREADSHEET_ID_HERE`
- 憑證 ID（`YOUR_CREDENTIAL_ID_HERE`）則在 n8n 匯入後，在介面上重新設定即可，**不需要手動填入**。

---

## 📌 注意事項

- 憑證資訊（`YOUR_CREDENTIAL_ID_HERE`, `YOUR_CREDENTIAL_NAME_HERE`）**不需要**在 JSON 裡手動填入
- 這些會在 n8n 介面内，當你重新設定 OAuth 授權時自動連結
- 有任何疑問請參考 `docs/google_auth_setup_guide.md`
