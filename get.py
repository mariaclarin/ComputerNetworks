import socket, select
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
    print("Welcome to L4AC's CompNet project")
    SEND = input("What is your destination IP? ")
    # while loop - wont stop until we tell them to
    while True:
        try:
            # messagerec, address = s.recvfrom(1024)
            # decoded = messagerec.decode('ascii')
            msg = input("What do you want to do? (GET, POST)\n")
            msg = msg.lower()
            if msg == "get":
                get = input("What file would you want to get? (e.g. '/index.html')\n")
                getmsg = "get " + get
                s.sendto(getmsg.encode(), ((SEND, PORT)))
                filecontent = []
                reading = True
                while reading:
                    incoming = select.select([s],[],[],5)
                    try:
                        data, address = s.recvfrom(1024)
                        decode = data.decode("ascii")
                        decode = decode.rstrip()
                        filecontent.append(decode)
                        print(decode)
                    except IndexError:
                        reading = False 
                    get = get.replace("/", "", 1)
                    with open(get, "w") as fo:
                        # loop to read all the lines in the file
                        for line in filecontent:
                            # send it to the sender address, decoded to ascii
                            fo.write(f"{line}\n")
                        # fo.seek(0)
                        fo.close()
                    # store decode to a file
            elif msg == "post":
                data, address = s.recvfrom(1024)
                decode = data.decode('ascii')
                get = decode.split(' ')
                gets = get[1]
                gets = gets.replace("/", "", 1)
                gets = gets.rstrip()
                with open(gets, "r") as fo:
                    # loop to read all the lines in the file
                    for line in fo:
                        # send it to the sender address, decoded to ascii
                        s.sendto(line.encode(), ((SEND, PORT)))
                    fo.seek(0)
                continue
        except Exception as e:
            print(e)

        # # to recieve from the socket
        # data, address = s.recvfrom(1024)
        # # decode the data recieved into ascii
        # decode = data.decode('ascii')
        # # split the decode or message with '', store in an array
        # word_list = decode.split(' ')
    
        # # set whatever the first word is to lowercase
        # word_list[0] = word_list[0].lower()
        
        # # run this if the first word is 'get'
        # if word_list[0] == "get":
        #     # replace the / with nothing, do it once
        #     # optional?
        #     word_list[1] = word_list[1].replace("/", "", 1)
        #     # remove trailing characters, to remove "\n"
        #     word_list[1] = word_list[1].rstrip()
        #     # open the file (supposed form the message index.html)
        #     with open(word_list[1], "r") as fo:
        #         # loop to read all the lines in the file
        #         for line in fo:
        #             # send it to the sender address, decoded to ascii
        #             s.sendto(line.encode(), ((address[0], PORT)))
        #         fo.seek(0)

        # # run this if the first word is 'post'
        # elif word_list[0] == 'post':
        #     pass