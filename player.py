import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_RATE, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
from bullet import Bullet

class Player(CircleShape):
    containers = ()
    TIMER = 0

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        
    
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        
        pygame.draw.polygon(screen,"white",self.triangle(), 2)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_RATE * dt
    
    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:    
            self.rotate(-dt)
        elif keys[pygame.K_d]:
            self.rotate(dt)
        elif keys[pygame.K_w]:
            self.move(dt)
        elif keys[pygame.K_s]:
            self.move(-dt)
        elif keys[pygame.K_SPACE]:
            if Player.TIMER <= 0:
                self.shoot()
                Player.TIMER = PLAYER_SHOOT_COOLDOWN
        Player.TIMER -= dt

            
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        shot = Bullet(*self.position)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        
    
    
        
