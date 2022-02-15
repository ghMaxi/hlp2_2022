import pygame
from application import Application

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((600, 450))
    app = Application()
    clock = pygame.time.Clock()

    while app.is_active:
        app.update(clock.tick(60))
        app.draw(screen)
