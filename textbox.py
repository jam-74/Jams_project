import pygame
import sys
import time
import subprocess

# Initialize Pygame
pygame.init()

# Read player_name from the file
with open('player_name.txt', 'r') as file:
    player_name = file.read()

# Now you can use the player_name variable in this script
print("Player Name:", player_name)

# Create display window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("CODEMON(｡•̀ᴗ-)✧")

# Load the image
text_box_image = pygame.image.load("ts_assets/text_box.png").convert_alpha()

# Define the new size
new_width = 1300  # Replace with the desired width
new_height = 700  # Replace with the desired height

# Scale the image to the new size
text_box_image = pygame.transform.scale(text_box_image, (new_width, new_height))

# Define the position for the image
x = -150  # X-coordinate
y = 130  # Y-coordinate

# Create a font
font = pygame.font.Font(None, 36)
text_color = (255, 255, 255)

# Create a list of text messages
text_messages = [
    player_name+": hm..? what time is it?.",
    "[phone ringing]",
    player_name+": hello?",
    "ALMAS: hey- " +player_name+ "? could you come over?",
    "ALMAS: I need help with a serious deadline. It's urgent",
    player_name+": why what’s wrong?",
    "ALMAS: it doesn’t matter. Just come over pleaseee.",
    player_name+": alright… I’ll be there in 10 mins.",
    "[phone hangs up]",
]

# Initialize text index and typewriter effect variables
text_index = 0
current_char = 0
typing_speed = 10  # Characters per second

# Define the position for the text
text_x = 60
text_y = 420

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

            # Check if it's the last line and open another program
            if text_index == last_line_index:
                subprocess.Popen(["python", "code/thread.py"])  # Replace with your other program's name
                pygame.quit()  # Close the current Pygame window
                sys.exit()  # Exit the current script

    # Clear the screen
    #screen.fill((0, 0, 0))  # Fill with a background color if needed

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
