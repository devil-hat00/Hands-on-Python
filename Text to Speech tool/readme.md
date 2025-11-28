# 🗣️ Wednesday – AI Voice Assistant for Windows

Wednesday is a Python-powered desktop voice assistant that listens, speaks, automates tasks, controls apps, plots graphs, sends WhatsApp messages, manages reminders, and handles your PC hands-free.
Designed to feel like a real AI companion, Wednesday operates using simple natural voice commands.


⭐ Features

🎙️ Voice Interaction

1.Speech recognition (STT)
2.Text to speech (TTS)
3.Natural conversational replies
4.Wake-style detection (“Hello Wednesday”)

🧠 Smart Abilities

1.Add, list, and clear reminders
2.Scheduled WhatsApp messages
3.Instant WhatsApp messages
4.Current time & date queries
5.Jokes & fallback responses

💻 System Control

1.Open apps (Notepad, Calculator, Paint, CMD, Chrome…)
2.Open user folders (Downloads, Desktop, Documents…)
3.Close applications
4.Close all browsers
5.Shutdown, restart, lock, or sleep the PC

🌐 Internet Control

1.Open websites
2.Google search
3.Play YouTube videos

📊 Graph Plotting

1.Bar graph
2.Line graph
3.Sine wave graph

🛠️ Installation

Clone the repository:

git clone https://github.com/yourusername/Wednesday-AI-Assistant
cd Wednesday-AI-Assistant


Install required libraries:

pip install -r requirements.txt


⚠️ Note:
You must have PyAudio installed for microphone features.
If PyAudio fails on Windows, install it using:
pip install pipwin
pipwin install pyaudio

▶️ Usage

Run the assistant:

python wednesday.py


Once running, just speak commands like:

“Open YouTube”

“Play Imagine Dragons songs”

“Send message to mom saying I’ll be late”

“Set reminder at 6 PM to drink water”

“Plot sine graph”

“Shutdown my system”

📝 Requirements
speechrecognition
pyttsx3
pywhatkit
matplotlib
numpy
psutil
pyaudio

🔧 Configuration

Update your WhatsApp contacts in wednesday.py:

contacts = {
    "mom": "+91XXXXXXXXXX",
    "dad": "+91XXXXXXXXXX",
    "rahul": "+91XXXXXXXXXX",
    "brother": "+91XXXXXXXXXX"
}

🤝 Contributing

Pull requests are welcome!
For major changes, open an issue to discuss what you want to improve.

📜 License

This project is open-source under the MIT License.
