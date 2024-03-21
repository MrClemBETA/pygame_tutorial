import pygame, utility
from .scene import Scene
from pygame.locals import (KEYDOWN, K_l)

class Intro(Scene):

    def __init__(self):
        super().__init__()

        Scene.screen.fill("red")

    def check_event(self, event):
        if event.type == KEYDOWN:
            # Check the l key
            if event.key == K_l:
                pygame.event.post(pygame.event.Event(utility.LEVELSCENE))
