import requests
import base64
import json
import sys

# User Constants
TOKEN = "YOUR_GITHUB_PAT_HERE"
REPO = "uyang-03/n8n-autotypein"
OLD_FILE = "autotypein_v1.5.json"
NEW_FILE = "autotypein_v1.51.json"
VERSION = "V1.51"
BASE_URL = f"https://api.github.com/repos/{REPO}"

HEADERS = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def get_file_sha(path):
    r = requests.get(f"{BASE_URL}/contents/{path}", headers=HEADERS)
    if r.status_code == 200:
        return r.json()['sha']
    return None

def update_repo():
    # 1. Read local JSON content
    with open(r'C:\Users\yuyan\.gemini\antigravity\scratch\n8n_workflow_final.json', 'r', encoding='utf-8') as f:
        content = f.read()
    
    encoded_content = base64.b64encode(content.encode('utf-8')).decode('utf-8')

    # 2. Create or Update file
    print(f"Updating {NEW_FILE}...")
    new_file_sha = get_file_sha(NEW_FILE)
    
    data = {
        "message": f"Update n8n workflow to {VERSION} (scrubbed)",
        "content": encoded_content,
        "branch": "main"
    }
    
    if new_file_sha:
        data["sha"] = new_file_sha

    r = requests.put(f"{BASE_URL}/contents/{NEW_FILE}", headers=HEADERS, json=data)
    if r.status_code not in [200, 201]:
        print(f"Failed to update file: {r.text}")
        return
    
    new_commit_sha = r.json()['commit']['sha']
    print(f"Created {NEW_FILE}, commit: {new_commit_sha}")

    # 3. Delete OLD file
    old_sha = get_file_sha(OLD_FILE)
    if old_sha:
        print(f"Deleting {OLD_FILE}...")
        data = {
            "message": f"Remove old version {OLD_FILE}",
            "sha": old_sha,
            "branch": "main"
        }
        r = requests.delete(f"{BASE_URL}/contents/{OLD_FILE}", headers=HEADERS, json=data)
        if r.status_code == 200:
            print(f"Deleted {OLD_FILE}")
            new_commit_sha = r.json()['commit']['sha']
        else:
            print(f"Failed to delete old file: {r.text}")

    # 4. Create Tag
    print(f"Creating tag {VERSION}...")
    # First create a git tag object (optional but good practice) or just a ref
    # We'll just create a ref (lightweight tag)
    tag_data = {
        "ref": f"refs/tags/{VERSION}",
        "sha": new_commit_sha
    }
    r = requests.post(f"{BASE_URL}/git/refs", headers=HEADERS, json=tag_data)
    if r.status_code == 201:
        print(f"Successfully created tag {VERSION}")
    else:
        print(f"Failed to create tag: {r.text}")

if __name__ == "__main__":
    update_repo()
