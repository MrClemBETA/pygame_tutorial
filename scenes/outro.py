import pygame, utility
from .scene import Scene
from pygame.locals import (KEYDOWN, K_r)

class Outro(Scene):

    def __init__(self):
        super().__init__()
        Scene.screen.fill("green")

    def check_event(self, event):
        if event.type == KEYDOWN:
            if event.key == K_r:
                pygame.event.post(pygame.event.Event(utility.INTROSCENE))
