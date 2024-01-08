import pygame
from settings import *
from level import Level

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("CODEMON(｡•̀ᴗ-)✧")
        self.clock = pygame.time.Clock()
        self.level = Level()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            dt = self.clock.tick(60) / 1000.0

            self.level.run(dt)

            pygame.display.flip()

        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()


