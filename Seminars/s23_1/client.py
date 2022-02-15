import socket
from network import *
import pygame


def main():
    # server connection
    client_socket = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect(address)
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

        # updates
        try:
            client_socket.send(update_request_code)
            answer = client_socket.recv(2048)
            print(answer)
        except socket.error as e:
            print(str(e))
            input("ERROR: press enter to quit")
            return


        # drawing
        screen.fill(white)
        pygame.display.flip()

        clock.tick(60)


if __name__ == "__main__":
    main()
