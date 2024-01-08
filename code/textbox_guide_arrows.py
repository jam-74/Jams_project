import pygame
import sys
import time
import subprocess
import os

os.environ['SDL_VIDEO_WINDOW_POS'] = '150,150'  # Replace 'x' and 'y' with the desired window position

# Initialize Pygame
pygame.init()

# textbox_ingame.py

# Read player_name from the file
with open('player_name.txt', 'r') as file:
    player_name = file.read()

# Now you can use the player_name variable in this script
print("Player Name:", player_name)

# Create display window
SCREEN_WIDTH = 570
SCREEN_HEIGHT = 230
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("CODEMON(｡•̀ᴗ-)✧")

# Load the images
text_box_image = pygame.image.load("ts_assets/text_box.png").convert_alpha()
arrow_keys = pygame.image.load("ts_assets/arrow_keys.png").convert_alpha()

# Define the new size for text_box_image
new_width = 900  # Replace with the desired width
new_height = 600  # Replace with the desired height

# Define the new size for arrow_keys
new_width_a = 200  # Replace with the desired width
new_height_a = 200  # Replace with the desired height

# Scale the images to the new sizes
text_box_image = pygame.transform.scale(text_box_image, (new_width, new_height))
arrow_keys = pygame.transform.scale(arrow_keys, (new_width_a, new_height_a))

# Define the positions for the images
text_box_x = -100  # X-coordinate for text_box_image
text_box_y = -180  # Y-coordinate for text_box_image

arrow_keys_x = 10  # X-coordinate for arrow_keys
arrow_keys_y = 50  # Y-coordinate for arrow_keys

# Create a font
font = pygame.font.Font(None, 28)
text_color = (255, 255, 255)

# Create a list of text messages
text_messages = [
    "NARRATOR: press the arrow keys to walk to the exit.",
]

# Initialize text index and typewriter effect variables
text_index = 0
current_char = 0
typing_speed = 10  # Characters per second

# Define the position for the text
text_x = 40
text_y = 60

# Define the last line index
last_line_index = len(text_messages) - 1

# Record the start time
start_time = time.time()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            current_char = 0  # Reset the current character
            text_index = (text_index + 1) % len(text_messages)  # Switch to the next message

            if text_index == last_line_index:
                pygame.quit()  # Close the current Pygame window
                sys.exit()  # Exit the current script

    # Clear the screen
    # screen.fill((0, 0, 0))  # Fill with a background color if needed

    # Blit the images onto the screen at the specified positions
    screen.blit(text_box_image, (text_box_x, text_box_y))
    screen.blit(arrow_keys, (arrow_keys_x, arrow_keys_y))

    current_message = text_messages[text_index]

    if current_char < len(current_message):
        # Render and display the text with a typewriter effect
        text_surface = font.render(current_message[:current_char + 1], True, text_color)
        text_rect = text_surface.get_rect(topleft=(text_x, text_y))
        screen.blit(text_surface, text_rect)

        current_char += 1

    # Update the display
    pygame.display.update()

    # Check if 10 seconds have passed and exit if true
    if time.time() - start_time > 6:
        pygame.quit()
        sys.exit()

    time.sleep(1 / typing_speed)

# Quit Pygame (shouldn't reach this point due to sys.exit() above)
pygame.quit()
sys.exit()
