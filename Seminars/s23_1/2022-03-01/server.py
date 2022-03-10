import socket
from _thread import start_new_thread
from constants import *


def server_thread(printer=print):
    server_socket = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM)
    try:
        server_socket.bind(server_address)
    except socket.error as e:
        printer(f'Server error {e}')
        return
    server_socket.listen(2)
    printer("Server listening to requests")

    client_id = 1
    while True:
        client_socket, _ = server_socket.accept()
        start_new_thread(client_function,
                         (client_socket, client_id, printer))
        client_id += 1


def client_function(client_socket, client_id, printer=print):
    printer(f'id {client_id} connected')
    data = client_socket.recv(buffer_size)
    with open(f"newfile{client_id}.png", mode='wb') as file:
        while data:
            file.write(data)
            try:
                data = client_socket.recv(buffer_size)
            except socket.error as e:
                data = None
                printer(f'Client error: {e}')
    printer(f'id {client_id} disconnected')
