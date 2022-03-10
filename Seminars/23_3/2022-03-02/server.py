import socket
from constants import *
from _thread import start_new_thread


def service_client(client_socket, client_id, print_function=print):
    print_function(f'{client_id} connected')
    file = open(f'newfile{client_id}.png', mode='wb')
    while True:
        try:
            file_data = client_socket.recv(buffer_size)
            file.write(file_data)
            if not file_data:
                break
        except Exception as e:
            print_function(f"Client error: {e}")
            break
    file.close()
    print_function(f'{client_id} disconnected')


def main(print_function=print):
    server_socket = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM)
    try:
        server_socket.bind(
            server_address)
    except socket.error as e:
        print_function(f"Server Error: {e}")
        return
    server_socket.listen(2)
    print_function("Server is listening")

    client_id = 0
    while True:
        client_socket, client_address = server_socket.accept()
        client_id += 1
        start_new_thread(
            service_client,
            (client_socket,
             client_id,
             print_function))


if __name__ == "__main__":
    main()
