import pygame
from utility import SCREEN_WIDTH, SCREEN_HEIGHT
from pygame.locals import (RLEACCEL, K_UP, K_DOWN, K_LEFT, K_RIGHT)

pygame.mixer.init()
move_up_sound = pygame.mixer.Sound("sounds/Rising_putter.ogg")
move_down_sound = pygame.mixer.Sound("sounds/Falling_putter.ogg")
collision_sound = pygame.mixer.Sound("sounds/Collision.ogg")

# Define a Player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("imgs/jet.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT/2)
        )
        
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
            move_up_sound.play()
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
            move_down_sound.play()
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
            
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

    def kill(self):
        collision_sound.play()
        super().kill()










            
