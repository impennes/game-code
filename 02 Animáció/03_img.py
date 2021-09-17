import pygame

WIDTH, HEIGHT = 1280, 620
BG_COLOR = (140, 137, 246)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# convert: PyGame könnyebben kezeli a képet, így gyorsabban fut
bird_surf = pygame.image.load('img/bird1.png').convert_alpha()
bird_x = 0
bird_y = 200

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BG_COLOR)
    screen.blit(bird_surf, (bird_x, bird_y))
    pygame.display.update()

pygame.quit()