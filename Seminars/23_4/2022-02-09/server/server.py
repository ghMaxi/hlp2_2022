import random
import socket
from _thread import start_new_thread


address = ("127.0.0.1", 5555)
server_socket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)
try:
    server_socket.bind(address)
except socket.error as e:
    str(e)
server_socket.listen(2)
print("Waiting for a connection, Server Started")

client_position_dict = {}


def client_thread(client_socket, client_id):
    client_socket.send("connected".encode())
    client_name = client_socket.recv(2048).decode()
    client_socket.send(str(client_id).encode())
    client_position_dict[client_id] = [
        random.randint(0, 580), random.randint(0, 430)]
    print(client_position_dict)
    while True:
        try:
            data = client_socket.recv(2048)
            if not data:
                print("Disconnected")
                break
            elif data.decode()[:6] == "update":
                move_direction = eval(data.decode()[7:])
                position_list = client_position_dict[client_id]
                position_list[0] += move_direction[0]
                position_list[1] += move_direction[1]
                client_socket.send(
                    str(client_position_dict).encode())
        except:
            break
    print(f"Lost connection with {client_id}: {client_name}")
    del client_position_dict[client_id]
    print(client_position_dict)
    client_socket.close()

client_id = 0
while True:
    conn, addr = server_socket.accept()
    print("Connected to:", addr)
    start_new_thread(client_thread, (conn, client_id))
    client_id += 1
