import socket
from random import randint
from network import address
from _thread import start_new_thread


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    server_socket.bind(address)
except socket.error as e:
    str(e)
server_socket.listen(2)

print("Waiting for a connection, Server Started")
coordinate_dict = {}


def client_function(target_socket, client_id):
    print("Connected to: ", client_id)
    x = randint(10, 790)
    y = randint(10, 590)
    coordinate_dict[client_id] = [x, y]
    target_socket.send(f"ok: {client_id}".encode())
    while True:
        try:
            data = target_socket.recv(2048)
            if not data:
                print("Disconnected")
                break
            elif data.decode()[:6] == "update":
                move_direction = eval(data.decode()[7:])
                position_list = coordinate_dict[client_id]
                position_list[0] += move_direction[0]
                position_list[1] += move_direction[1]
                print(coordinate_dict)
                target_socket.send(
                    str(coordinate_dict).encode())
        except Exception as e:
            print(str(e))
            break
    del coordinate_dict[client_id]
    target_socket.close()



while True:
    client_socket, client_address = server_socket.accept()
    start_new_thread(client_function, (client_socket, client_address[1]))




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
from _thread import start_new_thread
while True:
    conn, addr = server_socket.accept()
    print("Connected to:", addr)
    start_new_thread(client_thread, (conn, client_id))
    client_id += 1
