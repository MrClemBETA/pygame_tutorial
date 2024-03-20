import pygame
from level import Level
from intro import Intro

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_ESCAPE, KEYDOWN, QUIT    
)

class Game:

    def __init__(self):
        # Load and play background music
        # Sound source: http://ccmixter.org/files/Apoxode/59262
        # License: https://creativecommons.org/licenses/by/3.0/
        pygame.mixer.music.load("Apoxode_-_Electric_1.mp3")
        pygame.mixer.music.play(loops=-1)

        # Create the clock for the frame rate
        self.clock = pygame.time.Clock()

        # Create the scene, temporarily it is Level
        self.scene = Intro()

        # Run until the user asks to quit
        self.running = True
        while self.running:
            self.update()


    def update(self):

        # Look at every event in the queue
        for event in pygame.event.get():
            # Did the user hit a key?
            if event.type == KEYDOWN:
                # Was it the Escape key? if so, stop the loop
                if event.key == K_ESCAPE:
                    self.running = False
            
            if event.type == QUIT:
                self.running = False

            # Execute the scene's event checker
            if self.scene.check_event(event) == "level":
                self.scene = Level()
                
        # Get the set of keys pressed and check for user input
        pressed_keys = pygame.key.get_pressed()

        # Execute the scene's update function
        if self.scene.update(pressed_keys) == False:
            self.running = False

        # Flip the display
        pygame.display.flip()

        # Tick the clock
        self.clock.tick(30)








        
