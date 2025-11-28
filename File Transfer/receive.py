import socket

HOST = "0.0.0.0"   
PORT = 5001       

server = socket.socket()
server.bind((HOST, PORT))
server.listen(1)

print(f"[+] Listening on {HOST}:{PORT} ...")
conn, addr = server.accept()
print(f"[+] Connected with {addr}")


filename = conn.recv(1024).decode()
print(f"[+] Receiving: {filename}")

with open(filename, "wb") as f:
    while True:
        data = conn.recv(1024)
        if not data:
            break
        f.write(data)

print("[+] File received successfully.")
conn.close()
server.close()
