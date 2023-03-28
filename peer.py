import socket, select
import os
from pathlib import Path
import requests
from inputimeout import inputimeout

# IP of the server or the machine that you have
# where to send the messages or packets
HOST = ""
# direct the connection to  port 8888
PORT = 8080

# this py for 28 march

# set s variable as socket.socket
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    # associate socket with the adderss
    s.bind((HOST, PORT))
    SEND = input("What is your destination IP? ")

    # while loop - wont stop until we tell them to
    while True:
        incoming = select.select([s],[],[],5)
        try:
            msg, address = incoming[0][0].recvfrom(1024)
            print(msg)
        except IndexError:
            pass
        try:
            msg = inputimeout(prompt="Enter something: ", timeout=20)
            s.sendto(msg.encode(), (SEND, PORT))
        except:
            pass