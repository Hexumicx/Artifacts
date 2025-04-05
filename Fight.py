from dotenv import load_dotenv
import os
import requests
import time
import json
from UserInfo import get_user_info

def fight(char="Wix1"):
    API_KEY = os.getenv("API_KEY")
    url = f"https://api.artifactsmmo.com/my/{char}/action/fight"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {API_KEY}",
    }
    response = requests.post(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: {response.status_code}")
        return None
    
def rest(char="Wix1"):
    API_KEY = os.getenv("API_KEY")
    url = f"https://api.artifactsmmo.com/my/{char}/action/rest"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {API_KEY}",
    }
    response = requests.post(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: {response.status_code}")
        return None
    
if __name__ == "__main__":
    load_dotenv()
    while True:
        userinfo = get_user_info()
        if userinfo is None:
            print("Failed to retrieve user info.")
            break
        health = userinfo.get("data")[0].get("hp", 100)
        print(f"Current health: {health}")
        if health <= 40:
            print("Health is low, resting...")
            data = rest()
        else:
            print("Health is sufficient, fighting...")
            data = fight()
        try:
            cooldown = data.get("data").get("cooldown").get("total_seconds", 60)
        except:
            cooldown = 60
        print(f"Cooldown time: {cooldown} seconds")
        time.sleep(cooldown)
        os.system('cls' if os.name == 'nt' else 'clear')