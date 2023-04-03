import socket, select, re, random, json, time

# IP of the server or the machine that you have
# where to send the messages or packets



# this py for 1 april

# set s variable as socket.socket
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    HOST = input("Enter your machine IP: ")
    PORT = int(input("Enter your machine PORT: "))
    # associate socket with the adderss
    s.bind((HOST, PORT))
    print("Welcome to L4AC's CompNet project")
    print("=================================")
    SEND = input("What is your destination IP? ")
    DESTINATION_PORT = int(input("What is your destination port? "))
    print("=================================")
    print("Connected to", SEND, "on port", DESTINATION_PORT)
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
                t1 = time.time()
                filecontent = []
                reading = True
                name = input("Enter new file name: ")
                name = name + ".html"
                print("loading...")
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
                        # print("try decode")
                        #printout the message
                    except :
                        reading = False
                    er_check = filecontent[0]
                    er_check2 = re.search("\[Errno.*", er_check)
                    if er_check2:
                        print(er_check)
                        filecontent.clear()
                        break
                    else:
                        with open(name, "w") as fo:
                            # loop to read all the lines in the file
                            for line in filecontent:
                                # send it to the sender address, decoded to ascii
                                fo.write(f"{line}\n")
                            fo.seek(0)
                        # print("with")
                    continue
                if len(filecontent) == 0:
                    print("File is not received")
                else:
                    et1 = time.time()
                    print("Time exe1 :", (et1-t1))
                    with open ("database.json") as file:
                        listJSON = json.load(file)
                    
                    jsondict = {
                        "target IP" : SEND,
                        "target PORT" : DESTINATION_PORT,
                        "file name" : name,
                        "file content" : filecontent
                    }
                    listJSON.append(jsondict)
                    with open ("database.json", 'w') as file:
                        json.dump(listJSON, file, indent = 4, separators=(',',': '))
                    print("File received. Saved as", name)
                continue
            #if statement to post (see the request and send the messages)
            elif msg == "post":
                #receive message and decode it
                flag = False
                while flag == False:
                    if random.random() < 0.25:
                        print("packetloss is there lol")
                        msg = input("What do you want to do? (GET, POST)\n")
                        msg = msg.lower()
                    else:
                        flag = True
                        continue
                data, address = s.recvfrom(1024)
                decode = data.decode('ascii')
                get = decode.split(' ')
                # print(get)
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
            errors  = str(e)
            s.sendto(errors.encode(), ((SEND, DESTINATION_PORT)))
