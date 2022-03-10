import socket
import time
from _thread import start_new_thread
from constants import *


server_socket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)
try:
    server_socket.bind(server_address)
except socket.error as e:
    str(e)
server_socket.listen(2)
print("Waiting for a connection, Server Started")


def client_thread(client_socket, client_id):
    while True:
        try:
            data = client_socket.recv(SIZE_BYTES)
            if not data:
                break
            file_size = int.from_bytes(data, 'big')
            with open(f'uploads/client_file_{client_id}.png', 'wb') as file:
                while file_size > 0:
                    data = client_socket.recv(2048)
                    file_size -= len(data)
                    file.write(data)
            client_socket.send(MESSAGE_DONE)
        except Exception as e:
            print(f'client_thread: {e}')
            break
    print(f"Lost connection with {client_id}")
    client_socket.close()


client_id = 0
while True:
    conn, addr = server_socket.accept()
    print("Connected to:", addr)
    start_new_thread(client_thread, (conn, client_id))
    client_id += 1
