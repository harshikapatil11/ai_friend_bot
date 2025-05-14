# app/gpt_engine.py

import openai
from flask import current_app

def generate_response(user_input, prompt):
    openai.api_key = current_app.config["OPENAI_API_KEY"]
    response = openai.ChatCompletion.create(
        model="gpt-4",  # or your desired model
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message.content.strip()
