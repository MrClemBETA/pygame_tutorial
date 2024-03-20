import pygame
from utility import SCREEN_WIDTH, SCREEN_HEIGHT

class Scene:

    # Set up the drawing window
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

    def __init__(self):
        pass

    def update(self, pressed_keys):
        pass

    def check_event(self, event):
        pass
