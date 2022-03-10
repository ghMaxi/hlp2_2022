import socket
from constants import *


def send_file(file, print_function=print):
    print_function(f'sending {file.name}')
    # подключение к серверу
    client_socket = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect(server_address)
        data = file.read()
        print(len(data))
        client_socket.send(data)
        print_function(f'sent {file.name}')
    except socket.error as e:
        print_function(f"Client Error: {e}")
