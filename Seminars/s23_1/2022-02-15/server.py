import socket
from random import randint
from network import *
from _thread import start_new_thread


client_dict = {}


def client_function(client_socket, client_id):
    while True:
        data = client_socket.recv(2048)
        print(f"from client {data}")
        client_socket.send(b'ok')


def main():
    server_socket = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM)
    try:
        server_socket.bind(address)
    except socket.error as e:
        print(str(e))
        return
    server_socket.listen(2)
    print("Server listening to requests")

    while True:
        client_socket, client_address = server_socket.accept()
        client_dict[client_address[1]] = [
            randint(box_size, width - box_size),
            randint(box_size, height - box_size)]
        start_new_thread(client_function, (client_socket, client_address[1]))


if __name__ == "__main__":
    main()
