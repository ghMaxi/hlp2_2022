import pygame
import socket


class Application:
    def __init__(self):
        self.name = 'maxibox'
        self.field_info = ''
        self.id = -1
        self.is_active = True
        self.socket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)
        self.address = ("127.0.0.1", 5555)
        try:
            self.socket.connect(self.address)
            info = self.socket.recv(2048).decode()
            if info != "connected":
                raise socket.error()
            self.socket.send(self.name.encode())
            self.id = int(self.socket.recv(2048).decode())
        except socket.error as e:
            print(type(e), e)
            self.is_active = False

    def update(self, fps):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_active = False
        pressed_keys = pygame.key.get_pressed()
        move_direction = (
                pressed_keys[pygame.K_LEFT] - pressed_keys[pygame.K_RIGHT],
                pressed_keys[pygame.K_UP] - pressed_keys[pygame.K_DOWN])
        try:
            self.socket.send(f"update {move_direction}".encode())
            self.field_info = self.socket.recv(2048).decode()
        except socket.error as e:
            print(type(e), e)
            self.is_active = False


    def draw(self, screen):
        screen.fill((255, 255, 255))
        field_dict = eval(self.field_info)
        for id, coord in field_dict.items():
            rect = (coord[0] - 10, coord[1] - 10, 20, 20)
            pygame.draw.rect(screen, (0, 0, 0), rect)
        pygame.display.flip()
