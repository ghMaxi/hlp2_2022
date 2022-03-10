import socket
from constants import *


def client_thread(file, target_address, printer=print):
    printer(f'{target_address} << {file.name}')
    # server connection
    client_socket = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM)
    try:
        address, port = target_address.split(':')
        client_socket.connect((address, int(port)))
        client_socket.send(file.read())
    except socket.error as e:
        printer(f'Client error: {e}')
    file.close()
