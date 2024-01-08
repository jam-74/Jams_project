import pygame
import subprocess  # Import the subprocess module
from settings import *
from player import Player
from sprites import Generic

class CameraGroup(pygame.sprite.Group):
    def __init__(self, *sprites):
        super().__init__(*sprites)
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()

    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - SCREEN_WIDTH / 2
        self.offset.y = player.rect.centery - SCREEN_HEIGHT / 2

        for layer in LAYERS.values():
            for sprite in self.sprites():
                if hasattr(sprite, 'z') and sprite.z == layer:
                    offset_rect = sprite.rect.copy()
                    offset_rect.center -= self.offset
                    self.display_surface.blit(sprite.image, offset_rect)

class Level:
    def __init__(self):
        # Get the display surface
        self.display_surface = pygame.display.get_surface()

        # Initialize sprite groups
        self.all_sprites = CameraGroup()

        # Define the teleportation area in the bottom-left corner
        teleport_area_rect = pygame.Rect(0, SCREEN_HEIGHT - 100, 100, 100)
        new_background_path = "graphics/world/ground.png"  # File path to the new background

        # Create a teleportation area
        self.teleport_area = TeleportArea(teleport_area_rect, new_background_path, [self.all_sprites])

        # Define the collision rectangle
        collision_rect = pygame.Rect(0, 0, 1157, 875)

        # Create the player instance with the collision_rect
        self.player = Player((640, 360), self.all_sprites, collision_rect)

        # Create a generic sprite for the ground
        self.ground_sprite = Generic(
            pos=(0, 0),
            surf=pygame.image.load("graphics/world/ground.png").convert_alpha(),
            groups=self.all_sprites,
            z=LAYERS['ground']
        )

        # Flag to track if the background has been changed
        self.background_changed = False

    def run(self, dt):
        self.display_surface.fill("black")

        # Check if the player teleports using the teleport_area
        new_background = self.teleport_area.teleport(self.player)

        if new_background:
            # Load the new background
            self.load_new_background(new_background)

        self.all_sprites.custom_draw(self.player)
        self.all_sprites.update(dt)

    def load_new_background(self, new_background_path):
        if not self.background_changed:
            # Load the new background image
            new_background = pygame.image.load(new_background_path).convert_alpha()
            self.display_surface.blit(new_background, (0, 0))
            self.ground_sprite.kill()  # Remove the old ground sprite

            self.player.set_position(100, SCREEN_HEIGHT - 100) 

            self.background_changed = True
            subprocess.Popen(['python', 'level2.py']) 
            pygame.quit()

class TeleportArea(pygame.sprite.Sprite):
    def __init__(self, rect, new_background_path, groups):
        super().__init__(groups)
        self.rect = rect
        self.new_background_path = new_background_path
        self.activated = False  # Flag to track if the area has been activated

    def teleport(self, player):
        # Check if the player's rectangle collides with the teleport area's rectangle
        if self.rect.colliderect(player.rect) and not self.activated:
            self.activated = True
            # Update the player's position (adjust this as needed)
            player.set_position(100, SCREEN_HEIGHT - 100)  # Set the new player position
            return self.new_background_path
        return None

# Start the game loop here
