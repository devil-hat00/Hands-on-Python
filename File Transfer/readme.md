# 📁 Python File Transfer App
A lightweight and straightforward file transfer tool built using Python’s socket programming. It enables fast sending and receiving of files between two systems over a local network — no frameworks, no dependencies, just pure Python.

🚀 Features
Send and receive any file type
Uses simple socket communication
Works over LAN (Wi-Fi / Ethernet)
Lightweight and easy to run
Beginner-friendly and extendable

🛠️ How It Works
This project contains two scripts:
server.py → Receives the file
client.py → Sends the file to the server
The client connects to the server using an IP address and port, then streams the file in chunks.

📦 Installation
Ensure Python is installed (3.x recommended).
Download or clone the project folder.
git clone https://github.com/your-username/file-transfer-app
Navigate inside the folder.

▶️ Usage
Step 1: Start the Server
Run this on the system that will receive the file:
python server.py
Step 2: Run the Client
Run this on the system that will send the file:
python client.py

Then enter the filename you want to transfer.

🌐 LAN Usage
To transfer across two different devices:
Replace HOST = "127.0.0.1" in client.py with the server's local IP.
Ensure both devices are on the same network.
Find your local IP using:

ipconfig   # Windows  
ifconfig   # Linux/Mac  

🔮 Future Enhancements
GUI version (Tkinter/PyQt)
Multiple file transfer support
Encryption (AES/SSL)
Progress bar
Auto device discovery
