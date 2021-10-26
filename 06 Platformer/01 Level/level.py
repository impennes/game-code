import pygame
from settings import *

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

level = Level(level_map, screen)
bg_surf = pygame.image.load('img/BG.png').convert_alpha()
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