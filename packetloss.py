import random

msg = input("What do you want to do? (GET, POST)\n")
msg = msg.lower()
flag = False

if msg == "get":
    while flag == False:
        if random.random() < 0.25:
            msg = input("What do you want to do? (GET, POST)\n")
            msg = msg.lower()
        else:
            flag = True


if msg == "post":
    while flag == False:
        if random.random() < 0.25:
            msg = input("What do you want to do? (GET, POST)\n")
            msg = msg.lower()
        else:
            flag = True