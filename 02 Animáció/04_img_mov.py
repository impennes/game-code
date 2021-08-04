import pygame

pygame.init()
WIDTH, HEIGHT = 1280, 620
# SCREEN_SIZE = (1280, 620)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

bird_surf = pygame.image.load('img/bird1.png')
bird_x, bird_y = 0, 300
BIRD_SPEED = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((140, 137, 246))

    if bird_x <= WIDTH - 150:
        bird_x += BIRD_SPEED
    screen.blit(bird_surf, (bird_x, bird_y))

    pygame.display.update()
    clock.tick(60)

pygame.quit()