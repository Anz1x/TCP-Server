#A TCP server coded with Python
# IF YOU ARE RUNNING SERVER.PY ON THIS HOST THEN RUN THIS ON A DIFFERENT MACHINE SINCE THIS IS THE CLIENT LIKE A VM OR ANOTHER DEVICE

#████████╗░█████╗░██████╗░  ░██████╗███████╗██████╗░██╗░░░██╗███████╗██████╗░
#╚══██╔══╝██╔══██╗██╔══██╗  ██╔════╝██╔════╝██╔══██╗██║░░░██║██╔════╝██╔══██╗
#░░░██║░░░██║░░╚═╝██████╔╝  ╚█████╗░█████╗░░██████╔╝╚██╗░██╔╝█████╗░░██████╔╝
#░░░██║░░░██║░░██╗██╔═══╝░  ░╚═══██╗██╔══╝░░██╔══██╗░╚████╔╝░██╔══╝░░██╔══██╗
#░░░██║░░░╚█████╔╝██║░░░░░  ██████╔╝███████╗██║░░██║░░╚██╔╝░░███████╗██║░░██║
#░░░╚═╝░░░░╚════╝░╚═╝░░░░░  ╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝

import socket
import json

# Socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

with open("settings.json", "r") as file:
    settings = json.load(file)
    host = settings["host"]
    port = settings["port"]
    message = settings["message"]

# Binding to socket
try:
    server_socket.bind((host, port))
except:
    print("Failed to bind")

# Starting the listener and the amount of devices it can connect to at the same time
server_socket.listen(5)

while True:
    # Starting the connection
    try:
        client_socket,address = server_socket.accept()

        print("Established a connection with %s" % str(address))
    except:
        print("Connection failed")
    
    try:
        # Encoding the message
        client_socket.send(message.encode("ascii"))
    except:
        print("\nMessaged failed to deliver to the client")

    client_socket.close()