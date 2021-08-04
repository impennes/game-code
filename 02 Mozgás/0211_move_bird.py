# pygame.image.load(os.path.join('pictures', 'background.png'))
import pygame

pygame.init()
WIDTH = 1280
HEIGHT = 620
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

bird = pygame.image.load('bird1.png')
bird_rect = bird.get_rect(center=(150, 300))
bird_x = 0
bird_y = 0
SPEED = 4

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and bird_rect.left >= 0:
        bird = pygame.image.load('bird1back.png')
        bird_x = -SPEED
    elif keys[pygame.K_RIGHT] and bird_rect.right <= WIDTH:
        bird = pygame.image.load('bird1.png')
        bird_x = SPEED
    else:
        bird_x = 0
    if keys[pygame.K_UP] and bird_rect.top >= 0:
        bird_y = -SPEED
    elif keys[pygame.K_DOWN] and bird_rect.bottom <= HEIGHT:
        bird_y = SPEED
    else:
        bird_y = 0

    screen.fill((140, 137, 246))

#    if bird_rect.right <= WIDTH:
    bird_rect.move_ip(bird_x, bird_y)
    screen.blit(bird, bird_rect)

    pygame.display.update()
    clock.tick(120)

pygame.quit()