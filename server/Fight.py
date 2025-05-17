from dotenv import load_dotenv
import os
import requests
import time
import json

from UserInfo import get_user_info, get_char_info
from cooldown import resolve_cooldown
from Move import move
from Bank import Bank

def fight(char: str = "Wix1"):
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


def rest(char: str = "Wix1"):
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


def fight_rest(char: str = "Wix1"):
    while True:
        charinfo = get_char_info(char)
        if charinfo is None:
            print("Failed to retrieve user info.")
            break
        health = charinfo.get("hp", 100)
        print(f"Current health: {health}")
        if health <= 70:
            print("Health is low, resting...")
            data = rest(char=char)
            resolve_cooldown(data)
        else:
            print("Health is sufficient, fighting...")
            data = fight(char=char)
            resolve_cooldown(data)


def fight_loop(char: str = "Wix1"):
    char_info = get_char_info(char)
    initial_location = char_info.get("x"), char_info.get("y")
    data = move(char=char, x=Bank.location[0], y=Bank.location[1])  # Move to Bank location
    resolve_cooldown(data)
    Bank.deposit_all(character=char) # Self-resolve cooldown
    data = move(char=char, x=initial_location[0], y=initial_location[1])  # Move back to initial location
    resolve_cooldown(data)  # Self-resolve cooldown
    while True:
        fight_rest(char=char)
        # Assume Inventory full
        data = move(char=char, x=Bank.location[0], y=Bank.location[1])  # Move to Bank location
        resolve_cooldown(data)
        Bank.deposit_all(char=char)  # Deposit all items to the Bank
        data = move(char=char, x=initial_location[0], y=initial_location[1])
        resolve_cooldown(data)  # Move back to the initial location

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
            cooldown = data.get("data").get(
                "cooldown").get("total_seconds", 60)
        except:
            cooldown = 60
        print(f"Cooldown time: {cooldown} seconds")
        time.sleep(cooldown)
        os.system('cls' if os.name == 'nt' else 'clear')
