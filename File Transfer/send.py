import socket
import os

HOST = "127.0.0.1"   # IPv4 of Receiver Device
PORT = 5001

filename = input("Enter filename to send: ")

if not os.path.exists(filename):
    print("File not found!")
    exit()

client = socket.socket()
client.connect((HOST, PORT))
print("[+] Connected to server")

# Send file name first
client.send(filename.encode())

with open(filename, "rb") as f:
    data = f.read(1024)
    while data:
        client.send(data)
        data = f.read(1024)

print("[+] File sent successfully.")
client.close()
