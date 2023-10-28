import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FONT_SIZE = 36
FONT_COLOR = (255, 255, 255)
BACKGROUND_COLOR = (0, 0, 0)
TEXT = "[welcome (player_name) to the world of Codemon. A world of adventure and opportunities where you learn how to code and how to navigate this new and unusual world.] [ You wake up one day to the sound of a phone ringing. Your friend frantically calling you to come over to their house urgently.]"

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Typewriter Effect")

# Create a font
font = pygame.font.Font(None, FONT_SIZE)

text = ""
current_char = 0
typing_speed = 20  # Characters per second

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND_COLOR)

    if current_char < len(TEXT):
        text += TEXT[current_char]
        current_char += 1

    text_surface = font.render(text, True, FONT_COLOR)
    text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

    screen.blit(text_surface, text_rect)
    pygame.display.update()

    clock.tick(typing_speed)

pygame.quit()
sys.exit()
