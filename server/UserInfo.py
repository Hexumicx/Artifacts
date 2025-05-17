import requests
import json


def get_user_info(user_id: str = "Hexumicx"):
    url = f"https://api.artifactsmmo.com/accounts/{user_id}/characters"
    headers = {"Accept": "application/json"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return None


def get_char_info(char: str = "Wix1"):
    user_info = get_user_info()
    if user_info is None:
        print("Failed to retrieve user info.")
        return None

    char_info = [data for data in user_info.get("data") if data.get("name") == char][0]
    return char_info


def get_inventory(user_id: str = "Hexumicx", char: str = "Wix1", item_id: str = None):

    user_info = get_user_info(user_id)
    if user_info is None:
        print("Failed to retrieve user info.")
        return None

    char_info = [data for data in user_info.get(
        "data") if data.get("name") == char][0]
    inventory = char_info.get("inventory", [])
    inventory_total = char_info.get("inventory_max_items", 0)

    item_count = 0
    target_item_count = 0
    for item in inventory:
        if item.get("code") == item_id:
            target_item_count += item.get("quantity", 0)
        item_count += item.get("quantity", 0)

    return item_count, inventory_total, item_count == inventory_total, target_item_count

def get_location(user_id: str = "Hexumicx", char: str = "Wix1"):
    char_info = get_user_info(char)
    if char_info is None:
        print("Failed to retrieve user info.")
        return None

    x = char_info.get("x")
    y = char_info.get("y")
    return x, y

if __name__ == "__main__":
    print(get_char_info("Wix1"))
