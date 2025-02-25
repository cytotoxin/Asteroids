import pygame
from constants import *

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
BLACK = (0, 0, 0)

# Set up the clock
clock = pygame.time.Clock()
dt = 0

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill the screen with black
    screen.fill(BLACK)
    pygame.display.flip()
    
    # Update delta time
    dt = clock.tick(60) / 1000.0

pygame.quit()


