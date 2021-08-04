import pygame

pygame.init()
WIDTH, HEIGHT = 1280, 620
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

bird_surf = pygame.image.load('img/bird1.png')
bird_rect = bird_surf.get_rect(center=(150, 300))
BIRD_SPEED = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((140, 137, 246))

    if bird_rect.right <= WIDTH:
        bird_rect.left += BIRD_SPEED
    screen.blit(bird_surf, bird_rect)

    pygame.display.update()
    clock.tick(60)

pygame.quit()