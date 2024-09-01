# app/utils.py

from twilio.rest import Client
from .config import Config

def send_sms(to_number, message_body):
    client = Client(Config.TWILIO_ACCOUNT_SID, Config.TWILIO_AUTH_TOKEN)

    message = client.messages.create(
        body=message_body,
        from_=Config.TWILIO_PHONE_NUMBER,
        to=to_number
    )

    return message.sid

# Example usage
# send_sms("+1234567890", "Your interview is scheduled for tomorrow at 10 AM.")


