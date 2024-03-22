import pygame, utility, sprites
from .scene import Scene

class Level(Scene):

    def __init__(self):
        super().__init__()

        # Create a custom event for adding a new enemy and cloud
        pygame.time.set_timer(utility.ADDENEMY, 250)
        pygame.time.set_timer(utility.ADDCLOUD, 1000)

        # Create the player
        self.player = sprites.Player()

        # Create groups to hold enemy sprites and all sprites
        # - enemies is used for collision detection and position updates
        # - clouds is used for position updates
        # - all_sprites is used for rendering
        self.enemies = pygame.sprite.Group()
        self.clouds = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)

    def update(self, pressed_keys):
        super().update(pressed_keys)

        # Update the player sprite based on keypresses
        self.player.update(pressed_keys)
        
        # Update the enemies positions
        self.enemies.update()

        # Update the cloud positions
        self.clouds.update()

        # Fill the background with sky blue
        Scene.screen.fill((135, 206, 250))
        
        # Draw all sprites
        for entity in self.all_sprites:
            Scene.screen.blit(entity.surf, entity.rect)

        # Detect Collisions
        if pygame.sprite.spritecollideany(self.player, self.enemies):
            self.player.kill()
            pygame.event.post(pygame.event.Event(utility.OUTROSCENE))


    def check_event(self, event):
        # Add a new enemy?
        if event.type == utility.ADDENEMY:
            # Create the new enemy and add it to the sprite groups
            new_enemy = sprites.Enemy()
            self.enemies.add(new_enemy)
            self.all_sprites.add(new_enemy)

        # Add a new cloud?
        if event.type == utility.ADDCLOUD:
            # Create the new cloud and add it to the sprite groups
            new_cloud = sprites.Cloud()
            self.clouds.add(new_cloud)
            self.all_sprites.add(new_cloud)










        
