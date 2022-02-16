import socket
from constants import *
import pygame


def main():
    # настройка сети
    client_socket = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect(server_address)
        my_id = eval(
            client_socket.recv(
                buffer_size).decode())
    except socket.error as e:
        print(str(e))
        return

    # запуск pygame
    pygame.init()
    screen = pygame.display.set_mode( (width, height) )
    is_active = True
    while is_active:
        # обработка событий и ввода
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_active = False
        keys = pygame.key.get_pressed()
        move_x = keys[pygame.K_d] - keys[pygame.K_a]
        move_y = keys[pygame.K_s] - keys[pygame.K_w]
        print(move_x, move_y)

        # коммуникация с сервером
        try:
            client_socket.send(f'update ({move_x}, {move_y})'.encode())
            object_data = eval(client_socket.recv(buffer_size).decode())
        except socket.error as e:
            print(str(e))
            object_data = {}
            is_active = False

        # отрисовка объектов
        screen.fill(bg_color)
        for value in object_data.values():
            rect = value[0], value[1], box_size, box_size
            pygame.draw.rect(screen, white, rect)
        rect = object_data[my_id][0],\
               object_data[my_id][1], box_size, box_size
        pygame.draw.rect(screen, green, rect)
        pygame.display.flip()


if __name__ == "__main__":
    main()
