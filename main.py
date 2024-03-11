# Simple pygame program

# Import and initialize the pygame library
import pygame
from utility import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from enemy import Enemy
from cloud import Cloud

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, KEYDOWN, QUIT    
)

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Create the clock for the frame rate
clock = pygame.time.Clock()

# Create a custom event for adding a new enemy and cloud
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)
ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1000)

# Create the player
player = Player((SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

# Create groups to hold enemy sprites and all sprites
# - enemies is used for collision detection and position updates
# - clouds is used for position updates
# - all_sprites is used for rendering
enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Run until the user asks to quit
running = True
while running:
    
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            # Was it the Escape key? if so, stop the loop
            if event.key == K_ESCAPE:
                running = False
        
        if event.type == QUIT:
            running = False
            
        # Add a new enemy?
        if event.type == ADDENEMY:
            # Create the new enemy and add it to the sprite groups
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

        # Add a new cloud?
        if event.type == ADDCLOUD:
            # Create the new cloud and add it to the sprite groups
            new_cloud = Cloud()
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)
            
    # Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()
    
    # Update the player sprite based on keypresses
    player.update(pressed_keys)
    
    # Update the enemies positions
    enemies.update()

    # Update the cloud positions
    clouds.update()
            
    # Fill the background with sky blue
    screen.fill((135, 206, 250))
    
    # Draw all sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    # Detect Collisions
    if pygame.sprite.spritecollideany(player, enemies):
        player.kill()
        running = False
    
    # Flip the display
    pygame.display.flip()

    # Tick the clock
    clock.tick(30)
    
# Done! Time to quit.
pygame.quit()
