import requests
from dotenv import load_dotenv
import os
import time
import json

from Bank import Bank
from UserInfo import get_user_info, get_inventory
from Move import move
from Fight import fight, rest
from Gather import gather, gather_loop
from cooldown import resolve_cooldown

load_dotenv()

bank_location = (4, 1)
gather_location = (2, 0)

item_code = "copper_ore"
char = "Wix1" 

while True:
    inventory_cur, inventory_total, inventory_full, target_count = get_inventory(
        item_id=item_code)
    print(f"Current inventory: {inventory_cur}/{inventory_total}")
    if inventory_full:
        data = move(char=char, location=bank_location)
        if data is None:
            print("Failed to move to bank location.")
        else:
            resolve_cooldown(data)

        data = Bank.deposit(char, item_code, target_count)
        if data is None:
            print("Failed to deposit items.")
            break
        else:
            resolve_cooldown(data)
    else:
        data = move(char=char, location=gather_location)

        if data is None:
            print("Failed to move to gather location.")
        else:
            resolve_cooldown(data)

        data = gather_loop()
