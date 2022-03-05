#A TCP client coded with python

#████████╗░█████╗░██████╗░  ░█████╗░██╗░░░░░██╗███████╗███╗░░██╗████████╗
#╚══██╔══╝██╔══██╗██╔══██╗  ██╔══██╗██║░░░░░██║██╔════╝████╗░██║╚══██╔══╝
#░░░██║░░░██║░░╚═╝██████╔╝  ██║░░╚═╝██║░░░░░██║█████╗░░██╔██╗██║░░░██║░░░
#░░░██║░░░██║░░██╗██╔═══╝░  ██║░░██╗██║░░░░░██║██╔══╝░░██║╚████║░░░██║░░░
#░░░██║░░░╚█████╔╝██║░░░░░  ╚█████╔╝███████╗██║███████╗██║░╚███║░░░██║░░░
#░░░╚═╝░░░░╚════╝░╚═╝░░░░░  ░╚════╝░╚══════╝╚═╝╚══════╝╚═╝░░╚══╝░░░╚═╝░░░

import socket
import json

# Socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

with open("settings.json", "r") as file:
    settings = json.load(file)
    host = settings["host"]
    port = settings["port"]

# Connecting to the server
client_socket.connect((host, port))

# The amount of data we receive
message = client_socket.recv(1024)

client_socket.close()

# Decoding the message
print(message.decode("ascii"))