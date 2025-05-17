import os
import requests
from dotenv import load_dotenv
from UserInfo import get_user_info, get_char_info
from cooldown import resolve_cooldown

load_dotenv()

class Bank:
    location = (4, 1)  # Default location for the bank

    @staticmethod
    def withdraw(character, code, amount):
        url = f"https://api.artifactsmmo.com/my/{character}/action/bank/withdraw"
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'Bearer {os.getenv("API_KEY")}',
        }
        payload = {
            'code': code,
            'quantity': amount
        }
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}")
            return None

    @staticmethod
    def deposit(character, code, amount):
        url = f"https://api.artifactsmmo.com/my/{character}/action/bank/deposit"
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'Bearer {os.getenv("API_KEY")}',
        }
        payload = {
            'code': code,
            'quantity': amount
        }
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}")
            return None
        
    @staticmethod
    def deposit_all(character):
        charinfo = get_char_info(character)
        inventory = charinfo.get("inventory", [])
        for item in inventory:
            code = item.get("code")
            quantity = item.get("quantity")
            if quantity > 0:
                data = Bank.deposit(character, code, quantity)
                resolve_cooldown(data)
        return 1
    
if __name__ == "__main__":
    character = "Wix1"
    Bank.deposit_all(character)