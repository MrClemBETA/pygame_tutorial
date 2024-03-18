# Simple pygame program

# Import and initialize the pygame library
import pygame
from game import Game

# Initialize pygame
pygame.init()

# Setup for sounds, defaults are good
pygame.mixer.init()

# Create the game
game = Game()
    
# Done! Time to quit.
pygame.mixer.music.stop()
pygame.mixer.quit()
pygame.quit()










