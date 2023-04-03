# Peer-to-Peer Protocol with UDP 👥💻🤝💻👥
## Introduction
This project is a class project for computer network courses which touches several things we have learned in classes. The name of this project is reliable UDP protocol with socket programming. Basically as a class, we need to create a P2P protocol on top of the UDP using socket programming that works like HTTP 1.1 GET and POST methods such that an html file can be obtained if the ‘GET’ method is used in and a JSON data can be stored in a storage medium (e.g., file or database) in the target peer if the ‘POST’ method is used. 

## Table of Contents
- [Purpose and Structure](#purpose-and-structure)
- [How it works](#how-it-works)
- [Features](#features)
- [Sequence Diagrams](#sequence-diagrams)
- [Libraries and Requirements](#libraries-and-requirements)
- [Downloading Files](#downloading-files)
- [Installation](#installation)
- [Program Run](#program-run)
- [Testing](#testing)
- [Result Documentation](#result-documentation)
- [Future Improvements](#future-improvements)
- [Contributors](#contributors)
## Purpose and Structure
The purpose of this project is to provide a reliable and efficient P2P protocol for data transfer and storage, using the UDP protocol and socket programming in Python. The project consists of the design and implementation of the protocol, the development of a demo application, testing and validation, and documentation.

## How it works
In this program, we have successfully established a Peer to Peer connection on top of a UDP (a transport layer protocol) where two VMs are connected together without the help of a third-party server. All the user needs is to run two separate virtual machines at the same time and establish a connection with the help of the provided files (get.py) in our repository to run the program. 

When the program first runs, the user will be prompted to specify their IP destination address and desired port destination number on both virtual machines. The program will then attempt to establish a connection with the entered IP and port number from both machines. If the connection is successful, something like “Connected to xxx.xxx.xx.xxx on port xxxx” will appear. The program will then ask if the user wants to do GET or POST. The user will then have to enter one of the above options to continue as seen in the snippet below.
<img src="https://media.discordapp.net/attachments/1085112329018015744/1092101333873610832/image.png">

If the user wrote GET, the program will ask the user to enter a file they want to request from the other machine. Once the user reply with a file name they requested for, the program will ask the user to enter a new name for the later received file before having it saved on their machine. After the user has successfully submitted a new name, the user must respond with a POST within a 5 second timer on the other virtual machine. If there is no response within said timer, the user will be prompted to do another GET or POST option.

If the file name requested exists on the other machine, it will state that it has been received and saved as the new file name entered previously. If the entered file name does not exist, an error will be displayed indicating the file has not been received successfully. The program will also display the RTT (Round Trip Time) regardless a file has been received successfully or not. Finally, the program will show if there is packet loss through an emulation using the random module. Below is a snippet of how the final program looks like.
<img src="https://media.discordapp.net/attachments/1085112329018015744/1092135335129010277/image.png">

## Features
1. POST
    - The data is sent to the server via the POST method. It is typically used for uploading data or any other file to the server, such as when filling out a form, etc. 
2. GET 
    - To ask the server to GET the data or information by utilizing the GET technique.
3. Packet Loss Emulation
    - users can validate the existence of packet loss (given a random percentage) in a packet loss emulated environment/channel.
4. RTT Timer
    - A Round Trip Time (RTT) timer that starts when the first peer sends a request and ends when the second peer responds. Used to check the connection response time.
5. Multithreading
    - Simultaneously running several threads by quickly transferring CPU control between them (called context switching). 
6. Three-way Handshake
    - The first VM sends a GET command to request a file from the second VM. The second VM responds with a POST command to accept the request and initiate the file transfer. The file transfer takes place with the exchange of data packets between the two VMs.

## Sequence Diagrams
Visual representations of the interaction between the two peers for our project for possible scenarios in sequence diagram form: </br>
1. Scenario 1: All packages received with no issues.
<img src="https://cdn.discordapp.com/attachments/1090244781155823697/1090290956328247367/Blank_diagram_3.png"> 

2. Scenario 2: No response from other peer thus premature timeout occurs.
<img src="https://cdn.discordapp.com/attachments/1090244781155823697/1092098536558047232/case_2.png">

3. Scenario 3:
<img src="https://cdn.discordapp.com/attachments/1090244781155823697/1090526112003674142/Sequence_Diagram_Case_3.png">

4. Scenario 4:
<img src="https://cdn.discordapp.com/attachments/1090244781155823697/1092092831146979408/Sequence_diagram_case_8.png">

5. Scenario 5:
<img src="https://media.discordapp.net/attachments/1090244781155823697/1090308053880033392/Sequence_diagram_case_5.png">

6. Scenario 6:
<img src="https://media.discordapp.net/attachments/1090244781155823697/1090308123216068639/Sequence_diagram_case_6_.png">

7. Scenario 7:
<img src="https://cdn.discordapp.com/attachments/1090244781155823697/1090526160791814197/Sequence_Diagram_Case_7.png">

8. Scenario 8:
<img src="https://cdn.discordapp.com/attachments/1090244781155823697/1092092831146979408/Sequence_diagram_case_8.png">

9. Scenario 9:
<img src="https://media.discordapp.net/attachments/1090244781155823697/1092107534128644096/Sequence_diagram_case_9.png">

## Libraries
Here is the list of libraries used for the project (Python):
1. socket (Python Standard Library)
    - to create and interact with sockets that send and receive data over the internet or other network protocols.
2. json (3.10.0 used)
    - methods for encoding and decoding data in JSON format
3. select (Python Standard Library)
    - mechanism for monitoring multiple I/O channels to determine when data is available to read or write,
4. re (2.2.1 used)
    - support for regular expressions
5. random (Python Standard Library)
    - generating random numbers and sequences, used for randomizing packet loss rates.

## Tools, Languages, and File Formats
![](https://img.shields.io/badge/Language-Python-blue)
![](https://img.shields.io/badge/Language-HTML-blue)
![](https://img.shields.io/badge/File%20Format-JSON-green)
![](https://img.shields.io/badge/Tools-GitHub-red)
![](https://img.shields.io/badge/Tools-Virtual%20Studio%20Code-red)
![](https://img.shields.io/badge/Tools-Virtual%20Box-red)

## Downloading Files
**Git Download Zip**
1. Click the '<> Code' dropdown button located on the repository page 
2. Select 'Download Zip' 
3. Unzip the downloaded package in your local Download directory

**Git Clone**
1. Initialize Git in terminal
```bash
git init
```
2. Clone the repository url
```bash
git clone https://github.com/mariaclarin/ComputerNetworks
```
**Git Desktop**
1. Click the '<> Code' dropdown button located on the repository page 
2. Click 'Open with GitHub Desktop'
3. Choose a local path to store the files
4. Click clone

**Note:** Clone the repository in both machines.

## Virtual Machine Installation

To use the preconfigured virtual machines for testing, follow these steps:

1. Download the virtual machine files (.ova) from [here](https://drive.google.com/drive/folders/1wj_-Vg8t6ctcz3UzJpr5EPx1WFFFeakV?usp=sharing). The virtual machines are preconfigured with Kali Linux and Ubuntu as the base machines, and are ready for testing.
2. Add the downloaded virtual machine files into Oracle VirtualBox.
3. Open a UDP port in the virtual machine network settings.
4. Connect both virtual machines via NAT network.
5. Get the IP address of each virtual machine by typing the "ip a" command in the terminal of each virtual machine.
6. Test and ensure that the connection is established with the "ping" command.
7. Your virtual machines are now ready to use for testing.

**Note:** the password for both VMs is will1289

## Testing
Connect the 2 Virtual Machine (VM):
1. Open the tool properties. 
2. Go to the port forwarding section.
3. Add a new port.
4. Change the protocol to User Datagram Protocol (UDP).
5. Change the host and guest ports.
6. Input the host IP address for the first VM and the guest IP address for the second VM.
7. Change the VM network to NAT Network.
8. Start both VMs and open their terminal.
9. Run the iperf command on both VM.
10. On the first VM, type: "host ip= iperf -s -p <port number> -u".
11. On the second VM, type: "client ip= iperf -c <host ip address> -u -p <port number> -b 10m".

GET & POST
- If Virtual Machine (VM) have two IP address:
1. Establish a connection between both VMs.
2. Run the get.py program on both VMs.
3. Enter the IP address and port number on both VMs.
4. On the first VM, input the "GET" command.
5. Enter the name of the desired file to retrieve.
6. Specify a new name for the file
7. On the second VM, input the "POST" command within 5 seconds after completing step 4 to complete the file transfer. Note that if the command is not entered within the allotted time, the process will time out.

- If Virtual Machine (VM) have one IP address:
1. Establish a connection between both VMs.
2. Run the get.py program on the first VM and get2.py on the second VM.
3. Enter the IP address and port number on both VMs.
4. On the first VM, input the "GET" command.
5. Enter the name of the desired file to retrieve.
6. Specify a new name for the file
7. On the second VM, input the "POST" command within 5 seconds after completing step 4 to complete the file transfer. Note that if the command is not entered within the allotted time, the process will time out. 

Packet Loss
- If Virtual Machine (VM) have two IP address:
1. Establish a connection between both VMs.
2. Run the packetloss2.py program on both VMs.
3. Enter the IP address and port number on both VMs.
4. If packet loss (probability 0.25%) does not occur, cancel the program using the control+c command until packet loss is detected.
5. Once packet loss is detected, try running the program again as you would with the get.py file to confirm proper functionality.

- If Virtual Machine (VM) have one IP address:
1. Establish a connection between both VMs.
2. Run the packetloss2.py program on the first VM and packetloss3.py on the second VM.
3. Enter the IP address and port number on both VMs.
4. If packet loss (probability 0.25%) does not occur, cancel the program using the control+c command until packet loss is detected.
5. Once packet loss is detected, try running the program again as you would with the get.py and get2.py file to confirm proper functionality.
       
Problems Encountered and Solution
1. Incorrect port input prevented the program from running. The issue was resolved by identifying and using the correct port number.
2. Incorrect commands. The issue was resolved by restarting and avoiding typos.
3. Unable to clone repository due to VM's unconnected network.
4. Unconnected network. This was resolved by checking the network connection of the VMs and port. 

## Result Documentation
Images of the results can be checked in the Test Results folder. Currently, there are 5 successful tests conducted.
1. get.py success
The file requested has been received successfully. 
2. RTT success
The RTT has been measured successfully as shown in the Time exe1 result.
3. Packetloss success:
Packetloss has been emulated successfully shown with “packetloss is there lol.”
4. No response or time out:
Result of test if other peer does not respond with POST within the 5 second timer.
5. File not found error: 
Result of test when file searched for is not found and thus not sent/received. 


## Future Improvements
## Contributors
**Special thanks to Mr ARDIMAS ANDI PURWITA, S.T., M.T., Ph.D.**
