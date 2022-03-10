import socket
from constants import *
import pygame


def main():
    # подключение к серверу
    client_socket = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect(server_address)
        client_socket.send(str(my_color).encode())
    except socket.error as e:
        print("Client Error:", str(e))
        return

    # окно pyGame
    screen = pygame.display.set_mode(  (width, height)  )
    is_active = True
    while is_active:
        # обработка событий и ввода
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_active = False
        keys = pygame.key.get_pressed()
        move_x = keys[pygame.K_d] - keys[pygame.K_a]
        move_y = keys[pygame.K_s] - keys[pygame.K_w]

        object_dict = {}
        try:
            client_socket.send(update_request+f'({move_x},{move_y})'.encode())
            object_dict = eval(
                client_socket.recv(buffer_size).decode())
        except socket.error as e:
            print("Client Error2:", str(e))
            is_active = False

        # отрисовка
        screen.fill(white)
        for object_id, data in object_dict.items():
            coord, color = data
            rect = coord[0], coord[1], box_size, box_size
            pygame.draw.rect(screen, color, rect)
        pygame.display.flip()


if __name__ == "__main__":
    main()
