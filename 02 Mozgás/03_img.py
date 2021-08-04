import pygame

pygame.init()
screen = pygame.display.set_mode((800, 400))

bird_surf = pygame.image.load('img/bird1.png').convert_alpha()
bird_x = 0
bird_y = 200

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((140, 137, 246))
    screen.blit(bird_surf, (bird_x, bird_y))
    pygame.display.update()

pygame.quit()