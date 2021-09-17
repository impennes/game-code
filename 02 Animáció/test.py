import pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT))
rect = pygame.Rect(50, 60, 200, 80)
print(rect.left)


if rect.right == 800:
    ...

bird_surf = pygame.image.load('img/bird1.png').convert_alpha()
bird_x = 0
bird_y = 200
screen.blit(bird_surf, (bird_x, bird_y))
