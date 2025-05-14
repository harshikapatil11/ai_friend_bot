import json
import random

def get_personality_for_user(user_number):
    with open("app/db/personality_store.json") as f:
        data = json.load(f)
    return data.get(user_number, data["default"])

def all_users():
    with open("app/db/personality_store.json") as f:
        data = json.load(f)
    return [u for u in data.keys() if u != "default"]

def get_random_prompt():
    return random.choice([
        "Had your lunch?",
        "Hope your day went well!",
        "Take some time to relax, okay?"
    ])
