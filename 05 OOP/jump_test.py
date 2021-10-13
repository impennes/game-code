"""
end = int(input('Adj meg egy határértéket! '))
start = 10

up = True
index = start
while index < end:
    if index == 0:
        up = False
    if up:
        index -= 1
    else:
        index += 1
    print(f'{index=}  {index**2=}')
"""
"""Smooth Jumping"""

# imports
import pygame, sys

WIDTH, HEIGHT = 500, 350

pygame.init()

win = pygame.display.set_mode((WIDTH, HEIGHT), 32, 0)
clock = pygame.time.Clock()

player = pygame.Rect(30, 30, 32, 32)
player_speed = 5


def move(rect, x, y):
    rect.x += x
    rect.y += y


# Add gravity
def grav(rect, g_force=6):
    rect.y += g_force
    if rect.y + rect.h >= HEIGHT:
        rect.y = HEIGHT - rect.h


x, y = 0, 0

while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x = -player_speed
            if event.key == pygame.K_RIGHT:
                x = player_speed
            if event.key == pygame.K_UP:
                y = -20
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x = 0
            if event.key == pygame.K_RIGHT:
                x = 0
            if event.key == pygame.K_UP:
                y = 0

    # Draw
    win.fill((0, 0, 20))
    pygame.draw.rect(win, (255, 24, 10), player)

    # move
    move(player, x=x, y=y)
    grav(player)

    pygame.display.flip()
