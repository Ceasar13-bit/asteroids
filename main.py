import pygame
from constants import *
from player import Player

def main():
    pygame.init
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    fps = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        player.draw(screen)
        player.update(dt)
        pygame.display.flip()
        dt = fps.tick(60) / 1000


if __name__ == "__main__":
    main()