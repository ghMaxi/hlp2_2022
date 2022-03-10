from threading import Thread, Lock
from os.path import exists
import socket
from constants import *


def send(filename):
    lock = Lock()
    lock.acquire()
    thread = Thread(
        target=send_file,
        args=(filename, lock))
    thread.start()
    return lock


def send_file(filename, lock: Lock):
    print(f"sending {filename} in thread")
    if not exists(filename):
        print(f"{filename} does not exist")
        return
    with open(filename, 'rb') as file:
        send_data = file.read()
    client_socket = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(server_address)
    client_socket.send(len(send_data).to_bytes(SIZE_BYTES, 'big'))
    client_socket.send(send_data)
    print('data sent, waiting for ok')
    try:
        data = client_socket.recv(2048)
        print(data)
    except Exception as e:
        print(e)
    lock.release()
