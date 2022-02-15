import socket
from _thread import *
from constants import PORT as port
import sys

address = ("127.0.0.1", port)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server_socket.bind(address)
except socket.error as e:
    str(e)

server_socket.listen(2)
print("Waiting for a connection, Server Started")


def threaded_client(client_socket: socket, id: int):
    client_socket.send(str(id).encode())
    reply = ""
    while True:
        try:
            data = client_socket.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                client_messages.append(reply)
                print("Received: ", reply)
                print("Sending : ", str(client_messages))
            client_socket.sendall(str.encode(str(client_messages)))
        except:
            break

    print("Lost connection")
    client_socket.close()


client_id = 0
client_messages = []
while True:
    conn, addr = server_socket.accept()
    print("Connected to:", addr)
    start_new_thread(threaded_client, (conn, client_id))
    client_id += 1


