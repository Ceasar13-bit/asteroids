import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from bullet import Bullet

def main():
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Bullet.containers = (shots, updatable, drawable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid = AsteroidField()  
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    fps = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
          
        updatable.update(dt)

        screen.fill((0,0,0))
        for thing in drawable:
            thing.draw(screen)
        
        for thing in asteroids:
            if player.collision(thing):
                sys.exit("Game Over")
            
            for shot in shots:
                if thing.collision(shot):
                    thing.split()
                    shot.kill()
       
        pygame.display.flip()
        dt = fps.tick(60) / 1000


if __name__ == "__main__":
    main()