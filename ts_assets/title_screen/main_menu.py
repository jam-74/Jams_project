import pygame
import subprocess


#create display window
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("CODEMON(｡•̀ᴗ-)✧")
#----------------------------------------

#load images
start_img = pygame.image.load("ts_assets/title_screen/click_to_continue.png").convert_alpha()
exit_img = pygame.image.load("ts_assets/title_screen/title_name.png").convert_alpha()


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

       



#create button instances
start_button = Button(470, 600, start_img, 0.2)
exit_button = Button(300, 7, exit_img, 0.95)

#-----------------------------------------
#game loop
run = True
start_clicked = False
while run:
    
    screen.fill((0, 0, 0))

    if not start_clicked:  # Check if start_button hasn't been clicked
        if start_button.draw(screen):
            print("START")
            start_clicked = True
            if start_clicked:
                subprocess.Popen(["python", "ts_assets/level_select/lvl1_select.py"])  # Run main.py
                pygame.quit()  # Close the current pygame window
                sys.exit()     # Exit the main_menu.py script

    exit_button.draw(screen)

    #event handler
    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()