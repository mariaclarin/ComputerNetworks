import socket
import json

# Define the host IP and port number
HOST = 'localhost'
PORT = 8888

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))

# Define the buffer size and timeout
BUFFER_SIZE = 1024
TIMEOUT = 10

# Define the file name and storage location for received files
RECEIVED_FILE = "received.html"
STORAGE_LOCATION = "storage.json"

# Define the GET and POST methods
GET_METHOD = "GET"
POST_METHOD = "POST"

# Define the response codes
OK_RESPONSE = "HTTP/1.1 200 OK\n\n"
NOT_FOUND_RESPONSE = "HTTP/1.1 404 Not Found\n\n"
BAD_REQUEST_RESPONSE = "HTTP/1.1 400 Bad Request\n\n"

# Define the function to handle GET requests
def handle_get_request():
    try:
        # Receive the file from the source peer
        data, addr = sock.recvfrom(BUFFER_SIZE)
        with open(RECEIVED_FILE, "wb") as f:
            f.write(data)
        # Send the OK response to the source peer
        sock.sendto(OK_RESPONSE.encode(), addr)
    except:
        # If there is an error, send the NOT_FOUND response to the source peer
        sock.sendto(NOT_FOUND_RESPONSE.encode(), addr)

# Define the function to handle POST requests
def handle_post_request():
    try:
        # Receive the JSON data from the source peer
        data, addr = sock.recvfrom(BUFFER_SIZE)
        json_data = json.loads(data)
        # Store the JSON data in the storage location
        with open(STORAGE_LOCATION, "a") as f:
            f.write(json.dumps(json_data))
        # Send the OK response to the source peer
        sock.sendto(OK_RESPONSE.encode(), addr)
    except:
        # If there is an error, send the BAD_REQUEST response to the source peer
        sock.sendto(BAD_REQUEST_RESPONSE.encode(), addr)

# Start the main loop
while True:
    # Set the socket timeout
    sock.settimeout(TIMEOUT)
    try:
        # Receive the request method from the source peer
        data, addr = sock.recvfrom(BUFFER_SIZE)
        request_method = data.decode()
        # Handle the GET or POST request based on the method
        if request_method == GET_METHOD:
            handle_get_request()
        elif request_method == POST_METHOD:
            handle_post_request()
        else:
            # If the method is not recognized, send the BAD_REQUEST response to the source peer
            sock.sendto(BAD_REQUEST_RESPONSE.encode(), addr)
    except socket.timeout:
        # If there is a timeout, restart the loop
        continue