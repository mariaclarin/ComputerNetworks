import socket
import os
from pathlib import Path
import requests

# IP of the server or the machine
HOST = input("Enter destination IP: ")
PORT = 8888

# this py for 23 march

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))

    while True:
        data, address = s.recvfrom(1024)
        # print(data)
        decode = data.decode('ascii')
        # print(decode)
        word_list = decode.split(' ')
        word_list[0] = word_list[0].lower()
        if word_list[0] == "get":
            # print(word_list)
            word_list[1] = word_list[1].replace("/", "", 1)
            word_list[1] = word_list[1].rstrip()

            with open(word_list[1], "r") as fo:
                for line in fo:
                    s.sendto(bytes(line, "ascii"), (address))
                fo.seek(0)
        elif word_list[0] == 'post':
            pass