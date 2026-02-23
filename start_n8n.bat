@echo off
echo ================================================
echo   n8n 自動化系統啟動腳本 (通用版)
echo   開啟後請前往 http://localhost:5678
echo ================================================
echo.

REM 確認 Node.js 已安裝
where node >nul 2>&1
if %errorlevel% neq 0 (
    echo [錯誤] 找不到 Node.js！請先到 https://nodejs.org 安裝 LTS 版本。
    pause
    exit /b 1
)

echo [啟動中...] 使用 npx 啟動 n8n，首次執行可能需要下載，請稍候...
echo.
npx n8n

pause
