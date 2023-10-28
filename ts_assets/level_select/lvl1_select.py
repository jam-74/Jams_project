import pygame
import subprocess

# Create display window
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("CODEMON(｡•̀ᴗ-)✧")
# ----------------------------------------

# Load images
lvl_bg_img = pygame.image.load("ts_assets/level_select/lvlselect_screen.png").convert_alpha()
lvl_locked_img = pygame.image.load("ts_assets/level_select/lvls_locked.png").convert_alpha()
lvl1_img = pygame.image.load("ts_assets/level_select/lvl1_clickable.png").convert_alpha()
lvls_img = pygame.image.load("ts_assets/level_select/lvl_select_nc.png").convert_alpha()

# Define new dimensions for the scaled images
bg_scale = 0.9
locked_scale = 0.5
level_scale = 0.5  # Add this line
levels_scale = 9.5

# Store original dimensions for reference
original_lvl1_width = lvl1_img.get_width()
original_lvl1_height = lvl1_img.get_height()

#-----------------
original_lvls_width = lvls_img.get_width()
original_lvls_height = lvls_img.get_height()
#------------------
original_lvl_locked_width = lvl_locked_img.get_width()
original_lvl_locked_height = lvl_locked_img.get_height()
#------------------
original_lvl_bg_width = lvl_bg_img.get_width()
original_lvl_bg_height = lvl_bg_img.get_height()



# Button class
class Button:
    def __init__(self, x, y, image, scale):
        # Scale the image with a tuple (width, height)
        self.image = pygame.transform.scale(image, scale)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False


    def check_click(self):
        pos = pygame.mouse.get_pos()
        return self.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0]

    def draw(self, surface):
        self.clicked = self.check_click()
        surface.blit(self.image, self.rect.topleft)
        return self.clicked


lvl1_button = Button(100, 100, lvl1_img, (int(original_lvl1_width * level_scale), int(original_lvl1_height * level_scale)))


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Check if lvl1_button is clicked
    if lvl1_button.draw(screen):
        print("Opening register.py")  # Add a message for testing
        subprocess.Popen(["python", "ts_assets/register/register.py"])
        pygame.quit()  # Close the current window
        sys.exit()  # Exit the script

    # Update the display
    pygame.display.update()

pygame.quit()



#---------------------------------------------------------

