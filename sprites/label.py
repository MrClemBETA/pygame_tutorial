import pygame

class Label(pygame.sprite.Sprite):
    def __init__(self, pos, text_input, base_color, text_size):
        self.pos = pos
        self.text_input = text_input
        self.base_color = base_color
        self.text_size = text_size
        self.font = pygame.font.Font("assets/font.ttf", self.text_size)
        self.text = self.font.render(self.text_input, True, self.base_color)
        self.rect = self.text.get_rect(center=self.pos)

    def update(self, screen):
        screen.blit(self.text, self.rect)
