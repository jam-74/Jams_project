import pygame
import subprocess

# Create display window
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("CODEMON(｡•̀ᴗ-)✧")

# Load and scale images
lvl_bg_img = pygame.image.load("ts_assets/level_select/lvlselect_screen.png").convert_alpha()
lvl_locked_img = pygame.image.load("ts_assets/level_select/lvls_locked.png").convert_alpha()
lvl1_img = pygame.image.load("ts_assets/level_select/lvl1_clickable.png").convert_alpha()
lvls_img = pygame.image.load("ts_assets/level_select/lvl_select_nc.png").convert_alpha()


bg_scale = 0.9
locked_scale = 0.55
level_scale = 0.55
levels_scale = 0.5


original_lvl1_width, original_lvl1_height = lvl1_img.get_size()
original_lvls_width, original_lvls_height = lvls_img.get_size()
original_lvl_locked_width, original_lvl_locked_height = lvl_locked_img.get_size()
original_lvl_bg_width, original_lvl_bg_height = lvl_bg_img.get_size()

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

# Create buttons for different images
lvl1_button = Button(200, 100, lvl1_img, (int(original_lvl1_width * level_scale), int(original_lvl1_height * level_scale)))
lvls_button = Button(400, 20, lvls_img, (int(original_lvls_width * levels_scale), int(original_lvls_height * levels_scale)))
locked_button = Button(200, 100, lvl_locked_img, (int(original_lvl_locked_width * locked_scale), int(original_lvl_locked_height * locked_scale)))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if lvl1_button.draw(screen):
        subprocess.Popen(["python", "ts_assets/register/register.py"])
        #if lvl_1 button clicked, it opens register.py
        pygame.quit()  
        sys.exit()  

    pygame.display.update()

pygame.quit()
