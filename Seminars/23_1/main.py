import socket
from network import address
import pygame

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_name = ""
try:
    client_socket.connect(address)
    answer = client_socket.recv(2048)
    server_name = answer[4:]
except socket.error as e:
    print(str(e))

screen = pygame.display.set_mode( (800, 600) )
clock = pygame.time.Clock()
x = 0
y = 0
while True:
    # отработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    keys = pygame.key.get_pressed()
    x = keys[pygame.K_a] - keys[pygame.K_d]
    y = keys[pygame.K_w] - keys[pygame.K_s]
    # счётчик fps
    clock.tick(60)
    data_dict = {}
    try:
        client_socket.send(f'update ({x}, {y})'.encode())
        answer = client_socket.recv(2048)
        data_dict = eval(answer.decode())
    except socket.error as e:
        print(str(e))

    # отрисовка
    screen.fill( (255, 255, 255) )
    for value in data_dict.values():
        rect = (value[0] - 10, value[1] - 10, 20, 20)
        pygame.draw.rect(screen, (0,0,0), rect)
    pygame.display.flip()
