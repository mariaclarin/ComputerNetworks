import socket
import os
from pathlib import Path
import requests

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

    # while loop - wont stop until we tell them to
    while True:
        print("Press Enter to continue")
        # to recieve from the socket
        data, address = s.recvfrom(1024)
        # decode the data recieved into ascii
        decode = data.decode('ascii')
        # split the decode or message with '', store in an array
        word_list = decode.split(' ')

        # set whatever the first word is to lowercase
        word_list[0] = word_list[0].lower()
        
        # run this if the first word is 'get'
        if word_list[0] == "get":
            # replace the / with nothing, do it once
            # optional?
            # word_list[1] = word_list[1].replace("/", "", 1)
            # remove trailing characters, to remove "\n"
            word_list[1] = word_list[1].rstrip()
            # open the file (supposed form the message index.html)
            with open(word_list[1], "r") as fo:
                # loop to read all the lines in the file
                for line in fo:
                    # send it to the sender address, decoded to ascii
                    s.sendto(line.encode(), ((address[0], PORT)))
                fo.seek(0)

        # run this if the first word is 'post'
        elif word_list[0] == 'post':
            pass

        else:
            print(data)

        while True:
            messagerec, address = s.recvfrom(1024)
            if messagerec.len() != 0:
                print(messagerec)
            else:
                msg = input("")
                s.sendto(msg.encode(), (HOST, PORT))
                continue
                # kasi timer 10 sec if user blom kasi input
                # break the if else function


        msg = input("")
        s.sendto(msg.encode(), (HOST, PORT))
        messagerec, address = s.recvfrom(1024)
        print(messagerec)
