import pygame
import time


WIDTH, HEIGHT = 1280, 620
BG_COLOR = (140, 137, 246)
FONT_COLOR = (255, 255, 255)

pygame.init()
time_start = time.time()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


game_font = pygame.font.Font(None, 60)
text_surf = game_font.render('GAME', True, FONT_COLOR)
text_rect = text_surf.get_rect(center=(WIDTH / 2, HEIGHT / 2))

points = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            points += 1

    game_time = str(int(round(time.time() - time_start, 0)))
    time_surf = game_font.render('SEC: ' + game_time, True, FONT_COLOR)
    time_rect = time_surf.get_rect(topleft=(10, 10))

    point_surf = game_font.render('SCORE: ' + str(points), True, FONT_COLOR)
    points_rect = point_surf.get_rect(topright=(WIDTH - 10, 10))

    screen.fill(BG_COLOR)
    screen.blit(time_surf, time_rect)
    screen.blit(point_surf, points_rect)
    screen.blit(text_surf, text_rect)
    pygame.display.update()
    clock.tick(60)

pygame.quit()