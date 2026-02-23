# Google Cloud OAuth2 設定指南 (For Local n8n)

因為您的 n8n 是在地端運行 (Localhost)，原本雲端版的憑證無法直接共用。您需要建立自己專用的 Google Cloud 憑證才能讓 Google Sheets 相關節點正常運作。

請依照以下步驟操作，全程約需 5-10 分鐘。

## 第一步：建立 Google Cloud 專案與啟用 API

1. 前往 [Google Cloud Console](https://console.cloud.google.com/)。
2. 點擊左上角的專案選單，選擇 **"New Project" (建立專案)**。
    - **Project Name**: 輸入 `n8n-local` (或您喜歡的名字)。
    - 點擊 **Create**。
3. 確認已選取剛建立的專案。
4. 在左側選單點擊 **"APIs & Services" (API 和服務) > "Library" (程式庫)**。
5. 搜尋 **"Google Sheets API"**，點擊進入並選擇 **"Enable" (啟用)**。
    - *(如果您的 Workflow 還有用到 Google Drive，建議也搜尋並啟用 Google Drive API)*。

## 第二步：設定 OAuth 同意畫面 (Consent Screen)

1. 在左側選單點擊 **"APIs & Services" > "OAuth consent screen" (OAuth 同意畫面)**。
2. User Type 選擇 **"External" (外部)**，點擊 **Create**。
3. 填寫基本資訊：
    - **App name**: `n8n Local`
    - **User support email**: 選擇您的 Email。
    - **Developer contact information**: 輸入您的 Email。
    - 點擊 **Save and Continue**。
4. Scops (範圍) 頁面可以直接點擊 **Save and Continue** 略過。
5. Test Users (測試使用者) 頁面：
    - 點擊 **Add Users**。
    - **輸入您要用來登入 Google Sheets 的 Gmail 地址** (非常重要，否則測試模式下會無法登入)。
    - 點擊 **Save and Continue**。

## 第三步：建立憑證 (Credentials)

1. 在左側選單點擊 **"Credentials" (憑證)**。
2. 點擊上方 **"+ CREATE CREDENTIALS" > "OAuth client ID"**。
3. Application type 選擇 **"Web application"**。
4. Name 輸入 `n8n Local Credential`。
5. **Authorized redirect URIs** (已授權的重新導向 URI) **【最關鍵的一步】**：
    - 點擊 **ADD URI**。
    - 輸入：`http://localhost:5678/rest/oauth2-credential/callback`
    - *(這是 n8n 接收 Google 授權回應的標準地址)*
6. 點擊 **Create**。
7. 畫面會彈出 **Your Client ID** 和 **Your Client Secret**。
    - ⚠️ **請將這兩組字串複製下來，稍後會用到。**

## 第四步：在 n8n 中設定憑證

1. 回到您的本地 n8n 介面 ([http://localhost:5678](http://localhost:5678))。
2. 點擊左側選單的 **Credentials**。
3. 點擊右上角 **Add credential**。
4. 搜尋並選擇 **"Google Sheets OAuth2 API"**。
5. 填入資訊：
    - **Client ID**: 貼上剛才複製的 Client ID。
    - **Client Secret**: 貼上剛才複製的 Client Secret。
6. 點擊下方的 **"Sign in with Google"** 按鈕。
7. 在跳出的 Google 視窗中選擇您的帳號，並允許授權。
    - *注意：因為是未驗證的 App，Google 可能會顯示警告，點擊 "Show Advanced" > "Go to n8n Local (unsafe)" 繼續即可。*
8. 顯示 "Connected" 後，點擊右上角 **Save**。

## 第五步：修復 Workflow 節點

1. 回到您的 Workflow (Untitled-2)。
2. 分別點擊那三個有紅色驚嘆號的節點：
    - `複製 Template`
    - `新增tab`
    - `寫入當月分頁`
3. 在節點設定中，找到 **Credential** 選項。
4. 選擇您剛剛建立的 `Google Sheets account` 憑證。
5. 節點應該會恢復正常 (紅色驚嘆號消失)。
