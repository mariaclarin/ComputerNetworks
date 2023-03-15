import socket
import os
from pathlib import Path

HOST = "192.168.196.174"
PORT = 1412

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))

    while True:
        data, addr = s.recvfrom(1024)
        decode = data.decode('ascii')
        word_list = decode.split(' ')
        word_list[0] = word_list[0].lower()
        if word_list[0] == "get":
            path = Path(f'.{word_list[1]}')
            if path.is_file():
                word_list[1] = word_list[1].replace("/", "", 1)
                s.sendto(os.system(f'cat {word_list[1]}'), addr)
        elif word_list[1] == 'post':
            pass