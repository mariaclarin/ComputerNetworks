import socket, select

# IP of the server or the machine that you have
# where to send the messages or packets
HOST = ""
# direct the connection to  port 8888
PORT = 8008
DESTINATION_PORT = 8080


# this py for 30 march

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
            #ask the user to type whether they want 
            msg = input("What do you want to do? (GET, POST)\n")
            msg = msg.lower() #lower case string
            #if statement to get (request the file and open the requested file)
            if msg == "get":
                #ask user for the input for the file they want to get
                get = input("What file would you want to get? (e.g. '/index.html')\n")
                getmsg = "get " + get
                #encode and send it to another user
                s.sendto(getmsg.encode(), ((SEND, DESTINATION_PORT)))
                filecontent = []
                reading = True
                name = input("Enter new file name: ")
                name = name + ".html"
                while reading:
                    #The user will wait to get the message, if the time expire
                    #they will automatically ask for the file
                    incoming = select.select([s],[],[],5) 
                    try:
                        data, address = incoming[0][0].recvfrom(1024)
                        #decode the encoded message and remove entrailing characters
                        decode = data.decode("ascii")
                        decode = decode.rstrip()
                        #store message in the list
                        filecontent.append(decode)
                        #printout the message
                    except :
                        reading = False 
                    # get = get.replace("/", "", 1)
                    with open(name, "w") as fo:
                        # loop to read all the lines in the file
                        for line in filecontent:
                            # send it to the sender address, decoded to ascii
                            fo.write(f"{line}\n")
                        fo.seek(0)
                        # fo.close()
                    # reading = False

                    continue
                continue
                    # store decode to a file
            #if statement to post (see the request and send the messages)
            elif msg == "post":
                #receive message and decode it
                data, address = s.recvfrom(1024)
                decode = data.decode('ascii')
                get = decode.split(' ')
                #the file is on the second index
                gets = get[1]
                gets = gets.replace("/", "", 1)
                gets = gets.rstrip()
                with open(gets, "r") as fo:
                    # loop to read all the lines in the file
                    for line in fo:
                        # send it to the sender address, decoded to ascii
                        s.sendto(line.encode(), ((SEND, DESTINATION_PORT)))
                    fo.close()
                continue
        except Exception as e:
            print(e)
