import socket
from constants import *
from random import randint
from _thread import start_new_thread

client_dict = {}
client_id = 0


def client_function(client_socket, cid):
    while True:
        try:
            data = client_socket.recv(buffer_size)
            if data:
                if data[:6] == update_bytes:
                    move_data = eval(data[7:].decode())
                    client_dict[cid] = (
                        client_dict[cid][0] + move_data[0],
                        client_dict[cid][1] + move_data[1])
                    client_socket.send(str(client_dict).encode())
            else:
                print(f"{cid} disconnected")
                break
        except Exception as e:
            print(str(e))
            break
    del client_dict[cid]


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server_socket.bind(server_address)
    except socket.error as e:
        print(str(e))
        return
    server_socket.listen(2)
    print("Сервер ждёт подключений")
    while True:
        client_socket, client_address = server_socket.accept()
        global client_id
        client_id += 1
        client_socket.send(
            str(client_id).encode())
        x = randint(0, width - box_size)
        y = randint(0, height - box_size)
        client_dict[client_id] = x, y
        start_new_thread(
            client_function,
            (client_socket, client_id))


if __name__ == "__main__":
    main()
