# app/routes.py
from flask import Blueprint, request

main = Blueprint("main", __name__)

@main.route("/webhook", methods=["POST"])
def webhook():
    from .gpt_engine import generate_response  # Import here to avoid circular import
    from .twilio_client import send_whatsapp_message
    from .utils import get_personality_for_user

    data = request.form
    user_message = data.get("Body")
    user_number = data.get("From")

    personality_prompt = get_personality_for_user(user_number)
    gpt_reply = generate_response(user_message, personality_prompt)
    send_whatsapp_message(user_number, gpt_reply)

    return "OK", 200