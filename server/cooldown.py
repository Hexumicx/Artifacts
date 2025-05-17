import time

def resolve_cooldown(data: dict) -> None:
    """
    Extracts the cooldown time from the API response data.

    Args:
        data (dict): The API response data.

    Returns:
        int: The cooldown time in seconds.
    """
    try:
        time.sleep(data.get("data", {}).get("cooldown", {}).get("remaining_seconds", 60))
    except:
        print("Error extracting cooldown time. Defaulting to 60 seconds.")
        time.sleep(5)
    