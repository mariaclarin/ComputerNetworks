import socket
import os
from pathlib import Path

# IP of the server or the machine
HOST = input("Enter destination IP: ")
PORT = 8888

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))

    while True:
        data = s.recvfrom(1024)
        print(data)
        text = data[0]
        decode = text.decode('ascii')
        print(decode)
        word_list = decode.split(' ')
        word_list[0] = word_list[0].lower()
        if word_list[0] == "get":
            path = Path(f'.{word_list[1]}')
            if path.is_file():
                word_list[1] = word_list[1].replace("/", "", 1)
                s.sendto(os.system(f'cat {word_list[1]}'), data[1])
        elif word_list[0] == 'post':
            pass