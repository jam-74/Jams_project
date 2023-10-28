import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 280
SCREEN_HEIGHT = 120
FONT_SIZE = 36
FONT_COLOR = (255, 255, 255)
BACKGROUND_COLOR = (0, 0, 0)
MAX_INPUT_LENGTH = 10  # Maximum allowed input length

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Name Input")

# Create a font
font = pygame.font.Font(None, FONT_SIZE)

input_text = ""
valid_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.unicode in valid_letters and len(input_text) < MAX_INPUT_LENGTH:
                input_text += event.unicode

    screen.fill(BACKGROUND_COLOR)

    text_surface = font.render(input_text, True, FONT_COLOR)
    text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

    screen.blit(text_surface, text_rect)

    pygame.display.update()

    
# Assign the entered text to a variable (up to 10 characters)
player_name = input_text


# Use the entered text as needed
print("Name is:", player_name)
# main.py

# Save player_name to a file
with open('player_name.txt', 'w') as file:
    file.write(player_name)


pygame.display.update()