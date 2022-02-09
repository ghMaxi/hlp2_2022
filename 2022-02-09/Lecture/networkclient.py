# source: https://www.techwithtim.net/tutorials/python-online-game-tutorial/sending-receiving-information/

import socket
from constants import PORT

SERVER = "127.0.0.1"

OFFLINE_ID = -1


class NetworkClient:
    def __init__(self, server, port):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.address = (server, port)
        self.id = OFFLINE_ID
        self.connect()

    @property
    def is_connected(self):
        return self.id != OFFLINE_ID

    def connect(self):
        try:
            self.socket.connect(self.address)
            self.id = self.socket.recv(2048).decode()
            print(f"from server: {self.id}")
        except socket.error as e:
            print(type(e), e)
            self.id = OFFLINE_ID

    def send(self, data):
        try:
            self.socket.send(str.encode(data))
            return self.socket.recv(2048).decode()
        except socket.error as e:
            print(type(e), e)


if __name__ == "__main__":
    client = NetworkClient(SERVER, PORT)
    while True:
        message = input("Input message to server: ")
        answer = client.send(f'{client.id}: {message}')
        print(f"from server: {answer}")
