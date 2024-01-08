import pygame
from settings import *
from support import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group, collision_rect):
        super().__init__(group)
        self.collision_rect = collision_rect

        # Load player animations and set initial state
        self.load_animations()
        self.status = 'down'
        self.frame_index = 0

        # Initialize general setup
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center=pos)
        self.z = LAYERS['main']

        # Movement attributes
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200

    def set_position(self, x, y):
        self.pos = pygame.math.Vector2(x, y)
        self.rect.centerx = x
        self.rect.centery = y

    def load_animations(self):
        # Load player animations from files
        animation_names = ['up', 'down', 'left', 'right',
                           'right_idle', 'left_idle', 'up_idle', 'down_idle',
                           'right_hoe', 'left_hoe', 'up_hoe', 'down_hoe',
                           'right_axe', 'left_axe', 'up_axe', 'down_axe',
                           'right_water', 'left_water', 'up_water', 'down_water']

        self.animations = {name: import_folder(f'graphics/character/{name}') for name in animation_names}

    def animate(self, dt):
        # Update animation frames
        self.frame_index += 4 * dt
        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0

        self.image = self.animations[self.status][int(self.frame_index)]

    def input(self):
        # Handle player input for movement
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.status = "up"
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
            self.status = "down"
        else:
            self.direction.y = 0

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.status = "right"
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.status = "left"
        else:
            self.direction.x = 0

    def move(self, dt):
        # Update player movement
        new_pos = self.pos + self.direction * self.speed * dt

        # Check for collisions with the collision_rect
        if self.collision_rect.collidepoint(new_pos.x, new_pos.y):
            self.pos = new_pos
            self.rect.centerx = self.pos.x
            self.rect.centery = self.pos.y

    def update(self, dt):
        # Update player state
        self.input()
        self.move(dt)
        self.animate(dt)
