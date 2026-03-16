import json
import re

path = r'c:\Users\yuyan\.gemini\antigravity\scratch\project_n8n_automation\github_repo\n8n_workflow_final.json'
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Fix IF node condition and Parent Folder ID
for node in data['nodes']:
    if node['name'] == '判斷資料夾是否存在':
        node['parameters']['conditions']['conditions'] = [{
            'id': 'check-found', 
            'leftValue': '={{ $json.files.length }}', 
            'rightValue': 0, 
            'operator': {'type': 'number', 'operation': 'larger'}
        }]
    if node['name'] == '建立文章子資料夾':
        node['parameters']['folderId']['value'] = "{{ $('建立本週三主資料夾').isExecuted ? $('建立本週三主資料夾').first().json.id : $('搜尋主資料夾').first().json.files[0].id }}"

# Save the original file back with the fixes if needed? 
# The user asked: "幫我把已修正後的final檔上傳到我的repo庫，並將之脫敏命名改為1.7版"
# I will save the fixed version to final.json as well, just to be safe.
with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

# Desensitize
def desensitize_node(n):
    if 'credentials' in n:
        for cred_type in n['credentials']:
            n['credentials'][cred_type]['id'] = 'YOUR_CREDENTIAL_ID'
    if n['name'] == '寫入當月分頁' and 'documentId' in n.get('parameters', {}):
        n['parameters']['documentId']['value'] = 'YOUR_SPREADSHEET_URL'
    if n['name'] == '抓新文章雲端_v2' or n['name'] == '尋找已上稿資料夾':
        if 'queryParameters' in n.get('parameters', {}) and 'parameters' in n['parameters']['queryParameters']:
            for param in n['parameters']['queryParameters']['parameters']:
                if param['name'] == 'q':
                    param['value'] = re.sub(r'[a-zA-Z0-9_-]{33}', 'YOUR_FOLDER_ID', param['value'])
    if n['name'] == '建立本週三主資料夾' and 'folderId' in n.get('parameters', {}):
        n['parameters']['folderId']['value'] = 'YOUR_PARENT_FOLDER_ID'
    if n['name'] == '搜尋主資料夾':
        if 'queryParameters' in n.get('parameters', {}) and 'parameters' in n['parameters']['queryParameters']:
            for param in n['parameters']['queryParameters']['parameters']:
                if param['name'] == 'q':
                    param['value'] = re.sub(r'[a-zA-Z0-9_-]{33}', 'YOUR_PARENT_FOLDER_ID', param['value'])

for node in data['nodes']:
    desensitize_node(node)

out_path = r'c:\Users\yuyan\.gemini\antigravity\scratch\project_n8n_automation\github_repo\n8n_workflow_v1.7.json'
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print('Done')
