import socket
from constants import *
from random import randint
from _thread import start_new_thread
client_dict = dict()


def service_client(client_socket, client_id):
    while True:
        try:
            request = client_socket.recv(buffer_size)
            if request[:len(update_request)] == update_request:
                move_data = eval(request[len(update_request):].decode())
                coord = client_dict[client_id][0]
                coord[0] += move_data[0]
                coord[1] += move_data[1]
                client_socket.send(str(client_dict).encode())
            else:
                raise Exception("Incorrect request")
        except Exception as e:
            print("Client error:", e)
            break
    print(f'{client_id} disconnected')
    del client_dict[client_id]


def main():
    server_socket = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM)
    try:
        server_socket.bind(server_address)
    except socket.error as e:
        print("Server Error:", str(e))
        return
    server_socket.listen(2)
    print("Server is listening")

    client_id = 0
    while True:
        client_socket, client_address = server_socket.accept()
        client_id += 1
        coords = [randint(0, width - box_size),
                  randint(0, height - box_size)]
        print(client_address)
        color = eval(client_socket.recv(buffer_size).decode())
        client_dict[client_id] = (coords, color)
        start_new_thread(service_client, (client_socket, client_id))


if __name__ == "__main__":
    main()
