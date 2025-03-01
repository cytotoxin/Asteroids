import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
BLACK = (0, 0, 0)

# Set up the clock
clock = pygame.time.Clock()
dt = 0

# Create groups for updatable and drawable objects
updatables = pygame.sprite.Group()
drawables = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
asteroidfield = pygame.sprite.Group()
Shots = pygame.sprite.Group()
Player.containers = (updatables, drawables)
Asteroid.containers = (updatables, drawables, asteroids)
AsteroidField.containers = (updatables)
Shot.containers = (updatables, drawables, Shots)


#Initialize the player
player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)

# Initialize the AsteroidField
asteroid_field = AsteroidField()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill the screen with black
    screen.fill(BLACK)

    # Update the updateables
    updatables.update(dt)

    # Check for collisions
    for obj in asteroids:
        if player.collides_with(obj):
            print("Game Over!")
            running = False
            break

    # Check for collisions between shots and asteroids
    for shot in Shots:
        for asteroid in asteroids:
            if shot.collides_with(asteroid):
                asteroid.split()
                shot.kill()

    # Draw the drawables
    for drawable in drawables:
        drawable.draw(screen)

    # Update the display
    pygame.display.flip()
    
    # Update delta time
    dt = clock.tick(60) / 1000.0

    

pygame.quit()


