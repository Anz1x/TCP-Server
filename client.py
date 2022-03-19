#A TCP client coded with python 3.10.2.
# IF YOU ARE RUNNING SERVER.PY ON THIS HOST THEN RUN THIS ON A DIFFERENT MACHINE SINCE LIKE A VM OR AN ANOTHER DEVICE

#████████╗░█████╗░██████╗░  ░█████╗░██╗░░░░░██╗███████╗███╗░░██╗████████╗
#╚══██╔══╝██╔══██╗██╔══██╗  ██╔══██╗██║░░░░░██║██╔════╝████╗░██║╚══██╔══╝
#░░░██║░░░██║░░╚═╝██████╔╝  ██║░░╚═╝██║░░░░░██║█████╗░░██╔██╗██║░░░██║░░░
#░░░██║░░░██║░░██╗██╔═══╝░  ██║░░██╗██║░░░░░██║██╔══╝░░██║╚████║░░░██║░░░
#░░░██║░░░╚█████╔╝██║░░░░░  ╚█████╔╝███████╗██║███████╗██║░╚███║░░░██║░░░
#░░░╚═╝░░░░╚════╝░╚═╝░░░░░  ░╚════╝░╚══════╝╚═╝╚══════╝╚═╝░░╚══╝░░░╚═╝░░░

import socket
import json
import os

os.system("cls ; clear")

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
