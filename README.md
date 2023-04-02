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

## How it works

## Features
1. POST
2. GET 
3. Packet Loss Simulation
4. RTT Timer
5. Multithreading
6. Three-way Handshake

## Sequence Diagrams
Visual representations of the interaction between the two peers for our project for possible scenarios in sequence diagram form: </br>
1. Scenario 1: All packages received with no issues.
<img src="https://cdn.discordapp.com/attachments/1090244781155823697/1090290956328247367/Blank_diagram_3.png"> 

2. Scenario 2: No response from other peer thus premature timeout occurs.
<img src="https://cdn.discordapp.com/attachments/1090244781155823697/1092098536558047232/case_2.png">

3. Scenario 3:
<img src="">

4. Scenario 4:
<img src="">

5. Scenario 5:
<img src="">

6. Scenario 6:
<img src="">

7. Scenario 7:
<img src="">

8. Scenario 8:
<img src="">

9. Scenario 9:
<img src="">

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
## Result Documentation
## Future Improvements
## Contributors
