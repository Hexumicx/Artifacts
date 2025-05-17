import requests
from dotenv import load_dotenv
import os
import time

from cooldown import resolve_cooldown
from UserInfo import get_user_info, get_char_info
from Move import move
from Bank import Bank

load_dotenv()
API_KEY = os.getenv("API_KEY")


def _gather(char: str = "Wix1"):
    url = f"https://api.artifactsmmo.com/my/{char}/action/gathering"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {API_KEY}",
    }
    response = requests.post(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
    else:
        print(f"Error: {response.status_code}")
        return None
    return data

def gather(char: str = "Wix1"):
    while True:
        data = _gather(char)
        if data is None: 
            break
        resolve_cooldown(data)

def gather_loop(char: str = "Wix1", drop: bool = True):
    userinfo = get_char_info(char)
    initial_location = userinfo.get("x"), userinfo.get("y")
    data = move(char=char, x=Bank.location[0], y=Bank.location[1]) # Move to Bank location
    resolve_cooldown(data)
    Bank.deposit_all(character=char)
    data = move(char=char, x=initial_location[0], y=initial_location[1]) # Move back to initial location
    resolve_cooldown(data)
    while True:
        gather(char=char)
        # Assume inventory is full
        data = move(char=char, x=Bank.location[0], y=Bank.location[1]) # Move to Bank location
        resolve_cooldown(data)
        Bank.deposit_all(character=char) 
        data = move(char=char, x=initial_location[0], y=initial_location[1]) # Move back to initial location
        resolve_cooldown(data)
        

if __name__ == "__main__":
    char = "Wix1"  # Replace with your character name
    gather_loop(char)
