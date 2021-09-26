# https://opengameart.org/content/20-crosshairs-for-re
import pygame
import random

WIDTH = 1280
HEIGHT = 620

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

ballon_surf = pygame.image.load('img/balloon.png').convert_alpha()
ballons_rect = []
for _ in range(5):
    ballon_rect = ballon_surf.get_rect(center=(random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)))
    ballons_rect.append(ballon_rect)

crosshair_surf = pygame.image.load('img/crosshair.png').convert_alpha()
crosshair_rect = crosshair_surf.get_rect(center=(WIDTH / 2, HEIGHT / 2))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            crosshair_rect = crosshair_surf.get_rect(center=event.pos)
        if event.type == pygame.MOUSEBUTTONDOWN:
            for index, ballon_rect in enumerate(ballons_rect):
                if ballon_rect.collidepoint(event.pos):
                    del ballons_rect[index]

    screen.fill((140, 137, 246))

    for ballon_rect in ballons_rect:
        screen.blit(ballon_surf, ballon_rect)
    screen.blit(crosshair_surf, crosshair_rect)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
