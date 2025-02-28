import pygame
from circleshape import CircleShape


# Asteroid class
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    # Draw the asteroid
    def draw(self, screen):
        pygame.draw.circle(screen, 
                           (255, 255, 255), 
                           (int(self.position.x), int(self.position.y)), 
                           self.radius,
                           2)
    # Update the asteroid
    def update(self, dt):
        self.position += self.velocity * dt