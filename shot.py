import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, SHOT_RADIUS):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen):
        pygame.draw.circle(screen, 
                           (255, 255, 255), 
                           (int(self.position.x), int(self.position.y)), 
                           int(SHOT_RADIUS),
                           2)
        
    def update(self, dt):
        self.position += self.velocity * dt