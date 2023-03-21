import socket

HOST=""
PORT = 80

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr  = s.accept()
    print(f"Client: {addr}")