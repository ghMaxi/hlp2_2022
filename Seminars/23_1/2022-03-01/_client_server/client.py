import socket
from network import *
import pygame


def main():
    # server connection
    client_socket = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect(address)
        client_socket.send(str(my_color).encode())
    except socket.error as e:
        print(str(e))
        input("ERROR: press enter to quit")
        return

    # pygame loop
    screen = pygame.display.set_mode( (width, height) )
    game_active = True
    clock = pygame.time.Clock()
    object_dict = {}
    while game_active:
        # events and input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_active = False
        keys = pygame.key.get_pressed()
        move_x = keys[pygame.K_d] - keys[pygame.K_a]
        move_y = keys[pygame.K_s] - keys[pygame.K_w]

        # updates
        try:
            request = update_request_code + f'({move_x},{move_y})'.encode()
            client_socket.send(request)
            answer = client_socket.recv(2048)
        except socket.error as e:
            print(str(e))
            input("ERROR: press enter to quit")
            return
        object_dict, color_dict = eval(answer.decode())

        # drawing
        screen.fill(white)
        for object_id, coord in object_dict.items():
            rect = (coord[0] - box_size / 2,
                    coord[1] - box_size / 2,
                    box_size, box_size)
            pygame.draw.rect(screen, color_dict[object_id], rect)
        pygame.display.flip()

        clock.tick(60)


if __name__ == "__main__":
    main()
