import pygame
from settings import *
from level import Level
from ui import UI

class Game:
    def __init__(self):
        self.game_active = True
        self.ui = UI(screen)
        self.current_health = 3

    def run(self):
        if self.game_active:
            self.ui.show_health(self.current_health)
            self.ui.show_create()

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

level = Level(level_map, screen)
bg_surf = pygame.image.load('../img/BG.png').convert_alpha()
bg_rect = bg_surf.get_rect(bottomleft=(0, screen_height))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # screen.fill('black')
    screen.blit(bg_surf, bg_rect)
    level.run()

    pygame.display.update()
    clock.tick(60)

pygame.quit()