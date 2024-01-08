import pygame, sys
import time
import subprocess
import os

os.environ['SDL_VIDEO_WINDOW_POS'] = '950,150'  # Replace 'x' and 'y' with the desired window position

# Initialize Pygame
pygame.init()

# textbox_ingame.py

# Read player_name from the file
with open('player_name.txt', 'r') as file:
    player_name = file.read()

# Now you can use the player_name variable in this script
print("Player Name:", player_name)

# Create display window
SCREEN_WIDTH = 528
SCREEN_HEIGHT = 200
BACKGROUND_COLOUR = (166,131,90)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("(｡•̀ᴗ-)✧")

# Load the image
text_box_image = pygame.image.load("ts_assets/text_box.png").convert_alpha()

# Define the new size
new_width = 800  # Replace with the desired width
new_height = 500  # Replace with the desired height

# Scale the image to the new size
text_box_image = pygame.transform.scale(text_box_image, (new_width, new_height))

screen.fill(BACKGROUND_COLOUR)

# Define the position for the image
x = -80  # X-coordinate
y = -140  # Y-coordinate

# Create a font
font = pygame.font.Font(None, 26)
text_color = (255, 255, 255)

# Create a list of text messages
text_messages = [
    "ALMAS: hey- thanks for coming. I really need help.",
    player_name+": no worries. So, what’s the problem?",
    "ALMAS: so... I have to complete this coding class",
    "ALMAS: and the homework is due... in about an hour.",
    "ALMAS: I didn’t pay attention, but I need help please.",
    player_name+": Almas!",
    "ALMAS: I'm sorry! I know- can you please help-",
    player_name+": I expect something out of it.",
    "ALMAS: oh- yeah... sure! I'll give you a battery.",
    "ALMAS: you told me how you've been trying to build",
    "-a computer from scratch, i can give you a few parts.",
    player_name+": Sure! I’ll do it!",
    ""
]

# Initialize text index and typewriter effect variables
text_index = 0
current_char = 0
typing_speed = 15  # Characters per second


# Define the position for the text
text_x = 50
text_y = 60

# Define the last line index
last_line_index = len(text_messages) - 1

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

    # Blit the image onto the screen at the specified position
    screen.blit(text_box_image, (x, y))

    current_message = text_messages[text_index]

    if current_char < len(current_message):
        # Render and display the text with a typewriter effect
        text_surface = font.render(current_message[:current_char + 1], True, text_color)
        text_rect = text_surface.get_rect(topleft=(text_x, text_y))
        screen.blit(text_surface, text_rect)

        current_char += 1

    # Update the display
    pygame.display.update()

    time.sleep(1 / typing_speed)

# Quit Pygame
pygame.quit()
sys.exit()
