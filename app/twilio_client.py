from twilio.rest import Client
from flask import current_app 

def send_sms(to, body):
    client = Client(current_app.config['TWILIO_ACCOUNT_SID'],
                    current_app.config['TWILIO_AUTH_TOKEN'])
    message = client.messages.create(
        to=to,
        from_=current_app.config['TWILIO_NUMBER'],
        body=body)