import socket
from constants import *
from _thread import start_new_thread


def client_function(
        client_socket,
        print_function=print):
    while True:
        try:
            data = client_socket.recv(1000000000)
            if data:
                with open("newfile.png", 'wb') as file:
                    file.write(data)
            else:
                print_function(f"{client_socket} disconnected")
                break
        except Exception as e:
            print_function(str(e))
            break


def main(print_function=print):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server_socket.bind(server_address)
    except socket.error as e:
        print_function(str(e))
        return
    server_socket.listen(2)
    print_function("Сервер ждёт подключений")
    while True:
        client_socket, client_address = server_socket.accept()
        start_new_thread(
            client_function,
            (client_socket, print_function))


if __name__ == "__main__":
    main()
