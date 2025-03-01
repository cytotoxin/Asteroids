import pygame

from circleshape import CircleShape
from constants import *
from shot import Shot


# Player class
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    # Draw the player
    def draw(self, screen):
        pygame.draw.polygon(screen, 
                            (255, 255, 255), 
                            self.triangle()
                            )
        
    # Rotate the player
    def rotate(self, dt):
        return self.rotation + PLAYER_TURN_SPEED * dt
    
    # Update the player
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotation = self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotation = self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE] and self.timer <= 0:
            self.shoot()

        # Decrease the timer by dt
        if self.timer > 0:
            self.timer -= dt

    # Move the player
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    # Shoot
    def shoot(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        shot.velocity = forward * PLAYER_SHOOT_SPEED
        shot.add(*Shot.containers)
        self.timer = PLAYER_SHOOT_COOLDOWN