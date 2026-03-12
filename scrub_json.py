import json
import re
import os

fpath = r'C:\Users\yuyan\.gemini\antigravity\scratch\n8n_workflow_final.json'

def scrub_workflow():
    if not os.path.exists(fpath):
        print(f"File not found: {fpath}")
        return

    with open(fpath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 1. Scrub Spreadsheet IDs (documentId)
    # 2. Scrub Folder IDs (folderId)
    # 3. Scrub Credential IDs
    # 4. Scrub IDs inside expressions (q parameters)

    for node in data.get('nodes', []):
        params = node.get('parameters', {})
        
        # documentId
        if 'documentId' in params:
            doc_id = params['documentId']
            if isinstance(doc_id, dict):
                # Replace value if it looks like a URL or ID
                doc_id['value'] = 'YOUR_SPREADSHEET_ID_HERE'
            elif isinstance(doc_id, str):
                params['documentId'] = 'YOUR_SPREADSHEET_ID_HERE'

        # folderId
        if 'folderId' in params:
            fol_id = params['folderId']
            if isinstance(fol_id, dict):
                fol_id['value'] = 'YOUR_FOLDER_ID_HERE'
            elif isinstance(fol_id, str):
                params['folderId'] = 'YOUR_FOLDER_ID_HERE'

        # credentials
        if 'credentials' in node:
            for cred_type in node['credentials']:
                node['credentials'][cred_type]['id'] = 'YOUR_CREDENTIAL_ID_HERE'
                if 'name' in node['credentials'][cred_type]:
                    node['credentials'][cred_type]['name'] = 'YOUR_CREDENTIAL_NAME_HERE'

        # queryParameters (Google Drive Search 'q')
        if 'queryParameters' in params:
            for p in params['queryParameters'].get('parameters', []):
                if p.get('name') == 'q' and 'value' in p:
                    # Replace long alphanumeric strings (typical IDs) with placeholder
                    p['value'] = re.sub(r'[0-9a-zA-Z_-]{25,}', 'YOUR_FOLDER_ID_HERE', p['value'])

    # 5. Remove instanceId from meta
    if 'meta' in data:
        data['meta'].pop('instanceId', None)

    with open(fpath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    
    print("Scrubbing complete.")

if __name__ == "__main__":
    scrub_workflow()
