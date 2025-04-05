import requests
from dotenv import load_dotenv
import os
import time

load_dotenv()
API_KEY = os.getenv("API_KEY")

def gather(char="Wix1"):
    url = f"https://api.artifactsmmo.com/my/{char}/action/gathering"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {API_KEY}",
    }
    response = requests.post(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
    
    return data

while True:
    data = gather()
    print(data)
    time.sleep(25)
