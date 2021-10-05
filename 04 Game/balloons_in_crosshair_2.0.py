import pygame
from random import randint

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

score = 0
game_font = pygame.font.SysFont('arial', 30, bold=True)
title_surf = game_font.render('BALLOON IN CROSSHAIR', True, FONT_COLOR)
title_rect = title_surf.get_rect(center=(WIDTH / 2, 200))
run_surf = game_font.render('Press space to run', True, FONT_COLOR)
run_rect = run_surf.get_rect(center=(WIDTH / 2, HEIGHT - 150))

start_time = pygame.time.get_ticks()
running = True
game_active = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            crosshair_rect = crosshair_surf.get_rect(center=event.pos)
        # lufik létrehozása megadott időpontban
        if event.type == balloons_timer:
            balloons_rect.append(balloon_surf.get_rect(center=(randint(50, WIDTH - 50), HEIGHT)))

    screen.blit(bg_surf, bg_rect)

    if game_active:
        time_left = int((start_time + GAME_TIME - pygame.time.get_ticks()) / 1000)
        if time_left < 0:
            game_active = False

        for index, balloon_rect in enumerate(balloons_rect):
            # lufik emelkedése
            balloons_rect[index].top -= BALLOON_SPEED
            # lufik oldalirányú mougása
            mov_y = randint(0, 3)
            if mov_y == 1:
                balloons_rect[index].left -= 2
            else:
                balloons_rect[index].left += 2
            # lufik törlése a képernyő elhagyásakor
            if balloons_rect[index].bottom <= -10:
                del balloons_rect[index]
            # találat vizsgálata
            if balloon_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed(num_buttons=3)[0]:
                del balloons_rect[index]
                score += 1
            # lufik és célkereszt megjelenítése
            screen.blit(balloon_surf, balloon_rect)
            screen.blit(crosshair_surf, crosshair_rect)

        # pontszám és játékidő meghelenítése
        score_surf = game_font.render('score: ' + str(score), True, FONT_COLOR)
        score_rect = score_surf.get_rect(topleft=(10, 10))
        screen.blit(score_surf, score_rect)

        time_left_surf = game_font.render('time left: ' + str(time_left), True, FONT_COLOR)
        time_left_rect = time_left_surf.get_rect(topleft=(10, 50))
        screen.blit(time_left_surf, time_left_rect)

    # nyitó- / záróképernyő
    else:
        screen.blit(title_surf, title_rect)
        screen.blit(balloon_surf, balloon_surf.get_rect(center=(WIDTH / 2, HEIGHT / 2)))
        screen.blit(crosshair_surf, crosshair_surf.get_rect(center=(WIDTH / 2, HEIGHT / 2)))
        screen.blit(run_surf, run_rect)

        # pontszám megjelenítése csak ha nagyobb, mint nulla
        if score:
            final_score_surf = game_font.render('SCORE: ' + str(score), True, FONT_COLOR)
            final_score_rect = final_score_surf.get_rect(center=(WIDTH / 2, HEIGHT - 220))
            screen.blit(final_score_surf, final_score_rect)

        # játék indítása
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            score = 0
            balloons_rect = []
            start_time = pygame.time.get_ticks()
            game_active = True

    pygame.display.update()
    clock.tick(60)

pygame.quit()
