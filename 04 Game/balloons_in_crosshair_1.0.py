import pygame
import random

WIDTH = 1280
HEIGHT = 620
BALLOON_SPEED = 4
FONT_COLOR = (27, 131, 142)
GAME_TIME = 8000

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Balloons in crosshair')
clock = pygame.time.Clock()

bg_surf = pygame.image.load('img/sky.png').convert_alpha()
bg_surf = pygame.transform.rotozoom(bg_surf, 0, 1.3)
bg_rect = bg_surf.get_rect(bottomleft=(0, HEIGHT))

balloon_surf = pygame.image.load('img/balloon.png').convert_alpha()
balloons_rect = []
balloons_timer = pygame.USEREVENT + 1
pygame.time.set_timer(balloons_timer, 1000)

crosshair_surf = pygame.image.load('img/crosshair.png').convert_alpha()
crosshair_surf = pygame.transform.rotozoom(crosshair_surf, 0, 0.7)
crosshair_rect = crosshair_surf.get_rect(center=(WIDTH / 2, HEIGHT / 2))

game_font = pygame.font.SysFont('arial', 30, bold=True)

start_time = pygame.time.get_ticks()
score = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            crosshair_rect = crosshair_surf.get_rect(center=event.pos)
        # lufik létrehozása megadott időközönként
        if event.type == balloons_timer:
            balloons_rect.append(balloon_surf.get_rect(center=(random.randint(50, WIDTH-50), HEIGHT-50)))

    screen.blit(bg_surf, bg_rect)

    for index, balloon_rect in enumerate(balloons_rect):
        # lufik emelkedése
        balloons_rect[index].top -= BALLOON_SPEED
        # lufik oldalirányí mozgása
        mov_y = random.randint(0, 3)
        if mov_y == 0:
            balloons_rect[index].left -= 2
        else:
            balloons_rect[index].left += 2
        # lufik törlése a képernyő elhagyásakor
        if balloons_rect[index].bottom <= -10:
            del balloons_rect[index]
        # találat viszgálata
        if balloon_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed(num_buttons=3)[0]:
            del balloons_rect[index]
            score += 1

        screen.blit(balloon_surf, balloon_rect)
    screen.blit(crosshair_surf, crosshair_rect)

    # pontszám megjelenítése
    score_surf = game_font.render('score: ' + str(score), True, FONT_COLOR)
    score_rect = score_surf.get_rect(topleft=(10, 10))
    screen.blit(score_surf, score_rect)

    # a hátralévő játékidő számítása és megjelenítése
    time_left = int((start_time + GAME_TIME - pygame.time.get_ticks()) / 1000)
    time_left_surf = game_font.render('time left: ' + str(time_left), True, FONT_COLOR)
    time_left_rect = time_left_surf.get_rect(topleft=(10, 50))
    screen.blit(time_left_surf, time_left_rect)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
