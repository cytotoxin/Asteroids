import pygame
import random
from circleshape import CircleShape
from constants import *


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

    # Split the asteroid
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            # Create two new smaller asteroids
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

            # Set their velocities based on the random angles
            asteroid1.velocity = self.velocity.rotate(random_angle) * 1.2
            asteroid2.velocity = self.velocity.rotate(-random_angle) * 1.2

            # Add the new asteroids to the appropriate groups
            asteroid1.add(*Asteroid.containers)
            asteroid2.add(*Asteroid.containers)
            