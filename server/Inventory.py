import requests
from dotenv import load_dotenv
import os
import time
import json

def sell_item(item_id, count, char="Wix1"):
    load_dotenv()
    API_KEY = os.getenv("API_KEY")
    url = f"https://api.artifactsmmo.com/my/{char}/action/npc/sell"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {API_KEY}",
    }
    payload = {
        "code": item_id,
        "quantity": count
    }
    response = requests.post(url, headers=headers, json=payload)
    print(response.text)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: {response.status_code}")
        return None

def delete_item(item_id, count, char="Wix1"):
    load_dotenv()
    API_KEY = os.getenv("API_KEY")
    url = f"https://api.artifactsmmo.com/my/{char}/action/delete"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {API_KEY}",
    }
    payload = {
        "code": item_id,
        "quantity": count
    }
    response = requests.post(url, headers=headers, json=payload)
    print(response.text)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: {response.status_code}")
        return None

if __name__ == "__main__":
    item_id = "egg"  
    count = 25  
    result = delete_item(item_id, count)
    if result:
        print(json.dumps(result, indent=4))
    else:
        print("Failed to sell item.")