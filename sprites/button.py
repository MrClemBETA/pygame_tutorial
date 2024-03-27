import pygame, utility

class Button(pygame.sprite.Sprite):
    
    def __init__(self, image, pos, text_input, base_color, hovering_color):
        self.image = image
        self.pos = pos
        self.font = pygame.font.Font("assets/font.ttf", 35)
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.pos[0], self.pos[1]))
        self.text_rect = self.text.get_rect(center=(self.pos[0], self.pos[1]))

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def check_for_input(self):
        return self.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]

    def change_color(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)

    def set_event(self, event):
        self.event = event

    def run_event(self):
        try:
            pygame.event.post(pygame.event.Event(self.event))
        except:
            print("No event set for the " + self.text_input + " button")






    
