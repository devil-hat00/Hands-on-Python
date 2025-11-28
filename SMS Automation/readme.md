# Twilio SMS Sender (Python)
A simple and fast Python script to send SMS messages using the Twilio API.
Perfect for beginners exploring APIs or anyone who wants to automate messaging from Python.

🚀 Features
Send SMS to any verified number
Uses Twilio's official Python SDK
Clean and minimal code
Environment-variable based secure configuration
Fast setup — get running in < 2 minutes

🛠️ Tech Used
Python
Twilio REST API
dotenv (optional)

📦 Installation
1. Clone the repository
git clone https://github.com/your-username/twilio-sms-sender.git
cd twilio-sms-sender

2. Install dependencies
pip install twilio python-dotenv

🔐 Setup Environment Variables
Never hardcode your credentials.
Create a file named .env and add:
  TWILIO_SID=your_twilio_account_sid
  TWILIO_TOKEN=your_twilio_auth_token
  TWILIO_NUMBER=your_twilio_phone_number
  RECEIVER_NUMBER=receiver_phone_number

🧩 How It Works
Script loads Twilio credentials
Initializes a Twilio Client
Creates an SMS message request
Prints back a SID (proof message was queued)

⚠️ Important Notes
Trial accounts can only text verified numbers
Some Twilio numbers cannot send SMS to India
If your AUTH TOKEN is leaked, regenerate it immediately
Keep .env private (Gitignore it)


⭐ Show Your Support
If this project helped you, consider ⭐ starring the repo!
