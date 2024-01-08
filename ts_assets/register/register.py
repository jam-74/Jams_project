import pygame
import threading
import subprocess
import sys


# Initialize Pygame
pygame.init()

# Create display window
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

def run_program1():
    subprocess.Popen(["python", "ts_assets/register/screen.py"])  # Replace with the actual command to run program1
# Create two threads to run the programs concurrently
thread1 = threading.Thread(target=run_program1)
thread1.start()
thread1.join()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("CODEMON(｡•̀ᴗ-)✧")

# Load images
background_img = pygame.image.load("ts_assets/register/register_screen.png").convert_alpha()
register_nc_img = pygame.image.load("ts_assets/register/register_nc.png").convert_alpha()
register_clickable_img = pygame.image.load("ts_assets/register/register_clickable.png").convert_alpha()
lvl1_img = pygame.image.load("ts_assets/register/lvl1_nc.png").convert_alpha()
cancel_img = pygame.image.load("ts_assets/register/cancel_clickable.png").convert_alpha()



#button class
class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def check_click(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            return pygame.mouse.get_pressed()[0] == 1 and not self.clicked
        return False

    def draw(self, surface):
        action = self.check_click()
        if action:
            self.clicked = True

        surface.blit(self.image, (self.rect.x, self.rect.y))
        return action

# Create button instances
cancel_button = Button(900, 600, cancel_img, 0.2)
register_clickable_button = Button(600, 600, register_clickable_img, 0.2)
lvl1_button = Button(400, 0, lvl1_img, 0.5)
register_nc_button = Button(250, 500, register_nc_img, 0.9)
background_button = Button(50, -250, background_img, 0.6)

# Game loop
run = True
cancel_clicked = False
register_clickable_clicked = False

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if not cancel_clicked:
        if cancel_button.draw(screen):
            print("START")
            cancel_clicked = True
            if cancel_clicked:
                subprocess.Popen(["python", "ts_assets/level_select/lvl1_select.py"])
                
                pygame.quit()
                sys.exit()

    if not register_clickable_clicked:
        if register_clickable_button.draw(screen):
            print("START")
            register_clickable_clicked = True
            if register_clickable_clicked:
                subprocess.Popen(["python", "textbox.py"])
                pygame.quit()
                sys.exit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

    background_button.draw(screen)
    register_clickable_button.draw(screen)
    lvl1_button.draw(screen)
    register_nc_button.draw(screen)
    cancel_button.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

