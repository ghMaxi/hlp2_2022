# source: https://www.techwithtim.net/tutorials/python-online-game-tutorial/sending-receiving-information/

import socket
OFFLINE_ID = -1
SERVER = "127.0.0.1"
PORT = 5555


class NetworkClient:
    def __init__(self, server, port):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.address = (server, port)
        self.id = self.connect()

    @property
    def is_connected(self):
        return self.id != OFFLINE_ID

    def connect(self):
        try:
            self.client.connect(self.address)
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(type(e), e)
            return OFFLINE_ID

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(type(e), e)
