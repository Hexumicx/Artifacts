from dotenv import load_dotenv
import os
from flask import Flask, jsonify, request
from flask_cors import CORS
import queue
import threading
import time
import requests

from Gather import gather
from Bank import Bank
from Fight import fight, fight_rest
from Move import move
from cooldown import resolve_cooldown
from character import Character

app = Flask(__name__)
CORS(app, origins="http://localhost:3000")
load_dotenv()

char_names = ["Wix1", "Wix2", "Wix3", "Wix4", "Wix5"]
char_queue = {name: Character(name) for name in char_names}

@app.route('/add', methods=['POST'])
def add_to_queue():
    input_data = request.json
    name = input_data.pop('name', 'Wix1')
    action = input_data.pop('action', None)
    args = input_data
    char_queue[name].add_action(action, args)
    return jsonify({"status": "Action added to queue"}), 200


app.run(port=3001)
