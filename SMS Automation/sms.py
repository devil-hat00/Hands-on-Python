from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

ACCOUNT_SID = os.getenv("TWILIO_SID")
AUTH_TOKEN = os.getenv("TWILIO_TOKEN")
TWILIO_NUMBER = os.getenv("TWILIO_NUMBER")
RECEIVER_NUMBER = os.getenv("RECEIVER_NUMBER")

client = Client(ACCOUNT_SID, AUTH_TOKEN)

message = client.messages.create(
    body="Hello, this is a message sent from Python using Twilio!",
    from_=TWILIO_NUMBER,
    to=RECEIVER_NUMBER
)

print("Message SID:", message.sid)
