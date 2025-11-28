# 🤖 AI Chat Bot — Powered by Gemini
A modern, fast, and intelligent AI chatbot built with Python + Streamlit + Google Gemini API.
It features multi-chat history, gradient chat bubbles, timestamps, clean UI, and persistent conversations — all running locally at high speed.

# 🚀 Overview
This project is a fully functional AI chatbot interface similar to ChatGPT.
It lets users:
1.Start multiple chats
2.Switch between old conversations
3.Talk to a real AI model
4.View messages with styled chat bubbles
5.Auto-refresh messages instantly
6.All processing happens dynamically using Streamlit and Google’s Gemini API.

# 🌟 Features
🔹 Real AI (Gemini 2.0 Flash)
Super-fast and accurate replies using Google’s latest Gemini model.

🔹 Multiple Chat Sessions
Each chat is stored separately and numbered:
Chat 1
Chat 2
Chat 3
Switch between them anytime.
🔹 Beautiful Chat UI
Gradient message bubbles
Shadows and soft rounded corners
Timestamp for each message
Clean left/right alignment
🔹 Persistent Conversation State
Your conversations stay until you close the app.
🔹 Made by Tarun Branding
Signature credit is added in the sidebar professionally.

# 🖥️ Live Demo (Local)
Run on your PC using Streamlit:
streamlit run ai.py

# 📂 Project Structure
AI-Chat-Bot/
│── ai.py                 # Main app
│── README.md             # Project documentation
│── requirements.txt      # Libraries needed
└── assets/               # For images or screenshots (optional)

# 🧩 Tech Stack
Component	Technology
Frontend	Streamlit
Backend	Python
AI Model	Gemini 2.0 Flash
UI Styling	Inline HTML + CSS

# 🔧 Installation & Setup
1️⃣ Clone the Repo
git clone https://github.com/your-username/ai-chat-bot.git
cd ai-chat-bot

2️⃣ Create a Virtual Environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Add Your Gemini API Key

Get your key from:

👉 https://ai.google.dev/

Then update it inside:

key = "YOUR_API_KEY"

5️⃣ Run the App
streamlit run ai.py

# 🧠 How It Works
1. User sends a message
Streamlit captures input using a form.
2. Message stored in session_state
Keeps chat history alive even when UI reruns.
3. Gemini API generates reply
Using:
model = genai.GenerativeModel("gemini-2.0-flash")
4. Chat bubbles rendered
Using secured HTML with inline CSS.
5. Sidebar shows all chats
Switch instantly without losing data.

# 🔮 Future Enhancements
Here are upgrades you can add later:
🎤 Voice input
🔊 AI voice output (text-to-speech)
🌓 Dark/Light theme toggle
📁 Export chat (PDF / TXT / JSON)
❤️ Reaction buttons on messages
🧬 AI memory for personalization
🔐 User login + cloud sync
If you want, I can build any of these for you.

🤝 Contributing
PRs and feature suggestions are welcome.
Make sure your changes are clean and well-structured.

👨‍💻 Author
Tarun
Developer | AI Engineer
Built with passion and creativity.

⭐ Support

If you like the project, consider starring ⭐ the GitHub repo.
