import socket
from constants import *


def client_function(file, server_address, print_function=print):
    send_bytes = file.read()
    print_function(f'send {file.name}')
    file.close()

    # настройка сети
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect(server_address)
        client_socket.send(send_bytes)
    except socket.error as e:
        print_function(str(e))
