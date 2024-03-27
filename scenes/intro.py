import pygame, utility, sprites
from .scene import Scene
from pygame.locals import (KEYDOWN, K_l)

class Intro(Scene):

    def __init__(self):
        super().__init__()

        # Fill background
        Scene.screen.fill(utility.SKY_BLUE)

        # Create Title Label
        self.title = sprites.Label((utility.SCREEN_WIDTH / 2, utility.SCREEN_HEIGHT / 4),
                "Missile Dodger", "black", 40)

        # Create Buttons
        self.start_button = sprites.Button(None,
                (utility.SCREEN_WIDTH / 2, utility.SCREEN_HEIGHT / 2),
                "START", "black", "gray")
        self.start_button.set_event(utility.LEVELSCENE)

    def update(self, pressed_keys):
        self.start_button.change_color()
        self.start_button.update(Scene.screen)
        self.title.update(Scene.screen)
    
    def check_event(self, event):
        if self.start_button.check_for_input():
            self.start_button.run_event()
        



                
