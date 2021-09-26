import pygame
from random import randint

WIDTH = 1280
HEIGHT = 620

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Balloons in crosshair')
clock = pygame.time.Clock()

ballon_surf = pygame.image.load('img/balloon.png').convert_alpha()
ballons_rect = []
balloons_timer = pygame.USEREVENT + 1
pygame.time.set_timer(balloons_timer, 1000)

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
        if event.type == balloons_timer:
            ballons_rect.append(ballon_surf.get_rect(center=(randint(50, WIDTH-50), randint(HEIGHT+20, HEIGHT+80))))


    screen.fill((140, 137, 246))

    for ballon_rect in ballons_rect:
        screen.blit(ballon_surf, ballon_rect)
    screen.blit(crosshair_surf, crosshair_rect)

    pygame.display.update()
    clock.tick(60)





pygame.quit()