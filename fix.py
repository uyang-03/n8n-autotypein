import json

path = r"c:\Users\yuyan\.gemini\antigravity\scratch\project_n8n_automation\github_repo\n8n_workflow_final.json"
with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Update positions
pos_map = {
    "抓取觀點文章頁面": [720, 176],
    "拆出當周新文章": [960, 176],
    "搜尋主資料夾": [48, 176],
    "判斷資料夾是否存在": [272, 176],
    "建立本週三主資料夾": [496, 276],
    "建立文章子資料夾": [1200, 0],
    "抓新文章雲端_v2": [1200, 176],
    "尋找已上稿資料夾": [1440, 176],
    "搬移至已上稿": [1680, 176],
    "Merge": [1200, 352],
    "寫入當月分頁": [1440, 352]
}

for node in data["nodes"]:
    if node["name"] in pos_map:
        node["position"] = pos_map[node["name"]]
        
    if node["name"] == "建立文章子資料夾":
        node["parameters"]["folderId"]["value"] = "{{ $('建立本週三主資料夾').isExecuted ? $('建立本週三主資料夾').first().json.id : $('搜尋主資料夾').first().json.files[0].id }}"

# Update connections
data["connections"] = {
    "每週一下午觸發": { "main": [ [ { "node": "搜尋主資料夾", "type": "main", "index": 0 } ] ] },
    "搜尋主資料夾": { "main": [ [ { "node": "判斷資料夾是否存在", "type": "main", "index": 0 } ] ] },
    "判斷資料夾是否存在": { "main": [ [ { "node": "抓取觀點文章頁面", "type": "main", "index": 0 } ], [ { "node": "建立本週三主資料夾", "type": "main", "index": 0 } ] ] },
    "建立本週三主資料夾": { "main": [ [ { "node": "抓取觀點文章頁面", "type": "main", "index": 0 } ] ] },
    "抓取觀點文章頁面": { "main": [ [ { "node": "拆出當周新文章", "type": "main", "index": 0 } ] ] },
    "拆出當周新文章": { "main": [ [ { "node": "抓新文章雲端_v2", "type": "main", "index": 0 }, { "node": "建立文章子資料夾", "type": "main", "index": 0 }, { "node": "Merge", "type": "main", "index": 0 } ] ] },
    "建立文章子資料夾": { "main": [ [] ] },
    "抓新文章雲端_v2": { "main": [ [ { "node": "尋找已上稿資料夾", "type": "main", "index": 0 }, { "node": "Merge", "type": "main", "index": 1 } ] ] },
    "尋找已上稿資料夾": { "main": [ [ { "node": "搬移至已上稿", "type": "main", "index": 0 } ] ] },
    "搬移至已上稿": { "main": [ [] ] },
    "Merge": { "main": [ [ { "node": "寫入當月分頁", "type": "main", "index": 0 } ] ] },
    "寫入當月分頁": { "main": [ [] ] }
}

with open(path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
