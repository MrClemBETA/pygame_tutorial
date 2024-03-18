from scene import Scene


ADDENEMY = pygame.USEREVENT + 1
ADDCLOUD = pygame.USEREVENT + 2

class Level(Scene):

    def __init__(self, screen):
        super().__init__(screen)

        # Create a custom event for adding a new enemy and cloud
        pygame.time.set_timer(ADDENEMY, 250)
        pygame.time.set_timer(ADDCLOUD, 1000)

        # Create the player
        player = Player((SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

        # Create groups to hold enemy sprites and all sprites
        # - enemies is used for collision detection and position updates
        # - clouds is used for position updates
        # - all_sprites is used for rendering
        enemies = pygame.sprite.Group()
        clouds = pygame.sprite.Group()
        all_sprites = pygame.sprite.Group()
        all_sprites.add(player)

    def update(self, pressed_keys):
        super().update()

        # Update the player sprite based on keypresses
        player.update(pressed_keys)
        
        # Update the enemies positions
        enemies.update()

        # Update the cloud positions
        clouds.update()

        # Fill the background with sky blue
        screen.fill((135, 206, 250))
        
        # Draw all sprites
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        # Detect Collisions
        if pygame.sprite.spritecollideany(player, enemies):
            player.kill()
            running = False


    def handle_event(self, event):
        # Add a new enemy?
        if event.type == ADDENEMY:
            # Create the new enemy and add it to the sprite groups
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

        # Add a new cloud?
        if event.type == ADDCLOUD:
            # Create the new cloud and add it to the sprite groups
            new_cloud = Cloud()
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)










        
