/**
 * 專業版 v17 (Incremental Merge - 增量合併)：
 * 
 * 修正重點：
 * 依照您的要求，不再「全欄重整」，而是只處理「最新加入的那一筆資料」。
 * 這樣可以確保上面的舊資料完全不動，只把最新的這筆「黏」上去。
 * 
 * 邏輯：
 * 1. 抓取最後一列 (最新資料)。
 * 2. 往上檢查：上一列是不是跟我是同一個日期？
 * 3. 如果是 -> 找出上面那團日期的「頭」在哪裡。
 * 4. 只針對這一段 (頭 ~ 尾) 執行合併。
 */
function handleDataChange(e) {
    const ss = SpreadsheetApp.getActiveSpreadsheet();
    const sheet = ss.getActiveSheet();
    const lastRow = sheet.getLastRow();
    const headerRows = 1;

    if (lastRow <= headerRows) return;

    // --- PART 1: 核取方塊 (D-H欄) ---
    const checkStartRow = Math.max(headerRows + 1, lastRow - 9);
    const checkNumRows = lastRow - checkStartRow + 1;
    const targetColStart = 4; // D
    const targetColEnd = 8;   // H
    const rangeCheckbox = sheet.getRange(checkStartRow, targetColStart, checkNumRows, targetColEnd - targetColStart + 1);
    const valuesCheckbox = rangeCheckbox.getValues();
    const checkboxRule = SpreadsheetApp.newDataValidation().requireCheckbox().build();

    for (let i = 0; i < valuesCheckbox.length; i++) {
        for (let j = 0; j < valuesCheckbox[i].length; j++) {
            let val = valuesCheckbox[i][j];
            if (typeof val === "boolean" || String(val).toUpperCase() === "TRUE" || String(val).toUpperCase() === "FALSE") {
                const cell = rangeCheckbox.getCell(i + 1, j + 1);
                if (!cell.getDataValidation()) {
                    cell.setDataValidation(checkboxRule);
                    cell.setValue(String(val).toUpperCase() === "TRUE");
                }
            }
        }
    }

    // --- PART 2: A 欄 增量合併 (只處理最後一筆) ---
    mergeSpecificRowGroup(sheet, lastRow);
}

/**
 * 針對特定的一列，往上尋找相同日期的群組並合併
 */
function mergeSpecificRowGroup(sheet, targetRow) {
    if (targetRow <= 1) return;

    // 1. 取得目標格子的值 (最新那筆)
    const targetRange = sheet.getRange(targetRow, 1);
    const targetValue = targetRange.getDisplayValue(); // 使用顯示值比對

    if (targetValue === "") return; // 空值不處理

    // 2. 往上檢查上一列 (targetRow - 1)
    const prevRow = targetRow - 1;
    if (prevRow < 1) return;

    const prevRange = sheet.getRange(prevRow, 1);

    // 檢查上一列是否被合併過
    const mergedRanges = prevRange.getMergedRanges();
    let prevValue = "";
    let groupStartRow = prevRow;

    if (mergedRanges.length > 0) {
        // 如果上一列已經是合併儲存格的一部份
        const mr = mergedRanges[0];
        prevValue = mr.getDisplayValue(); // 拿合併儲存格的值
        groupStartRow = mr.getRow(); // 這一團的起始列
    } else {
        // 如果上一列沒被合併，直接拿值
        prevValue = prevRange.getDisplayValue();
    }

    // 3. 比對：如果日期一樣，就執行合併
    if (prevValue === targetValue) {
        // 定義新合併範圍：從「上一團的頭」到「現在這列(腳)」
        const newNumRows = targetRow - groupStartRow + 1;
        const rangeToMerge = sheet.getRange(groupStartRow, 1, newNumRows, 1);

        // 執行合併 (Google 會自動擴展現有的合併範圍)
        rangeToMerge.mergeVertically();
        rangeToMerge.setVerticalAlignment("middle");
        rangeToMerge.setHorizontalAlignment("center");

        console.log(`已將第 ${targetRow} 列合併至群組 (起始列: ${groupStartRow})`);
    } else {
        console.log("日期不同，無需合併");
    }
}

/**
 * 🛠️ 測試按鈕 (會針對您目前選取的列進行「向上合併」測試)
 */
function debugMerge() {
    const ss = SpreadsheetApp.getActiveSpreadsheet();
    const sheet = ss.getActiveSheet();
    const cell = sheet.getActiveCell();

    if (cell.getColumn() !== 1) {
        SpreadsheetApp.getUi().alert("請選取 A 欄的某一格來測試");
        return;
    }

    try {
        mergeSpecificRowGroup(sheet, cell.getRow());
        SpreadsheetApp.getUi().alert("✅ 增量合併執行完畢！");
    } catch (e) {
        SpreadsheetApp.getUi().alert("❌ 錯誤：" + e.message);
    }
}
