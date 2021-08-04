import pygame
from pygame.locals import *
# https://pygame.readthedocs.io/en/latest/1_intro/intro.html

pygame.init()

BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((640, 240))
background = GRAY

key_dict = {K_x:BLACK, K_r:RED, K_g:GREEN, K_b:BLUE, K_w:WHITE}

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key in key_dict:
                background = key_dict[event.key]
                caption = 'background color = ' + str(background)
                pygame.display.set_caption(caption)

    screen.fill(background)
    pygame.display.update()

pygame.quit()