import requests
from dotenv import load_dotenv
import os
import time


def move(char: str = "Wix1", x: int = 0, y: int = 0):

    load_dotenv()
    API_KEY = os.getenv("API_KEY")
    url = f"https://api.artifactsmmo.com/my/{char}/action/move"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {API_KEY}",
    }
    payload = {
        "x": x,
        "y": y
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: {response.status_code}")
        return None


if __name__ == "__main__":
    char = "Wix1"  # Replace with your character name
    location = (2, 0)  # Replace with the desired coordinates
    result = move(char, location)
    if result:
        print(result)
    else:
        print("Failed to move character.")
    cooldown = result.get("data").get("cooldown").get("total_seconds", 60)
    time.sleep(cooldown)
