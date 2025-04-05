import requests
import json

def get_user_info(user_id="Hexumicx"):
    url = f"https://api.artifactsmmo.com/accounts/{user_id}/characters"
    headers = {"Accept": "application/json"}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None
    
if __name__ == "__main__":
    user_info = get_user_info()
    if user_info:
        print(json.dumps(user_info, indent=4))
    else:
        print("Failed to retrieve user info.")