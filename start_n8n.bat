@echo off
setlocal

:: 設定基礎工作目錄（以腳本所在位置為準）
set "BASE_DIR=%~dp0"
cd /d "%BASE_DIR%"

echo Starting n8n locally (Local Install)...
echo Current Directory: %BASE_DIR%
echo Please wait for the n8n editor to become accessible at http://localhost:5678

:: 定義關鍵工具腳本路徑（供後續擴充使用）
set "SCRUB_SCRIPT=%BASE_DIR%scrub_json.py"
set "GITHUB_SCRIPT=%BASE_DIR%github_update.py"

:: 直接用 node 執行 n8n 主程式
:: （避免 n8n.cmd 內部 endLocal 把工作目錄重置的問題）
set "N8N_MAIN=%BASE_DIR%node_modules\n8n\bin\n8n"

if exist "%N8N_MAIN%" (
    echo [OK] Found n8n main entry.
    node "%N8N_MAIN%"
) else (
    echo [ERROR] n8n not found at: %N8N_MAIN%
    echo Please run 'npm install' first.
    pause
    exit /b 1
)

pause
