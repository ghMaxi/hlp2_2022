import socket
from random import randint
from network import *
from _thread import start_new_thread


client_dict = {}
color_dict = {}


def client_function(client_socket, client_id):
    while True:
        try:
            data = client_socket.recv(2048)
            if not data:
                raise socket.error("Client disconnected")
            if data[:len(update_request_code)] != update_request_code:
                raise socket.error("Wrong request")
        except socket.error as e:
            print("Client func error:", e)
            break

        move_info = eval(data[len(update_request_code):].decode())
        client_dict[client_id][0] += move_info[0]
        client_dict[client_id][1] += move_info[1]
        client_info = str((client_dict, color_dict)).encode()
        client_socket.send(client_info)

    print(f'{client_id} disconnected')
    del client_dict[client_id]
    del color_dict[client_id]



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

    client_id = 0
    while True:
        client_socket, client_address = server_socket.accept()
        client_dict[client_id] = [
            randint(box_size, width - box_size),
            randint(box_size, height - box_size)]
        color_dict[client_id] = eval(client_socket.recv(2048).decode())
        start_new_thread(client_function, (client_socket, client_id))
        client_id += 1


if __name__ == "__main__":
    main()
