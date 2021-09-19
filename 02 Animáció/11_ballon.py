import pygame

WIDTH = 1280
HEIGHT = 620
SPEED = 4

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

ballon_surf = pygame.image.load('img/ballon.png')
ballon_rect = ballon_surf.get_rect(center=(WIDTH-100, HEIGHT/2))


bird_fw_1 = pygame.image.load('img/bird1.png')
bird_fw_2 = pygame.image.load('img/bird2.png')
bird_fw_3 = pygame.image.load('img/bird3.png')
bird_fw_4 = pygame.image.load('img/bird4.png')
birds_fw = [bird_fw_1, bird_fw_2, bird_fw_3, bird_fw_4]
bird_b_1 = pygame.image.load('img/bird1back.png')
bird_b_2 = pygame.image.load('img/bird2back.png')
bird_b_3 = pygame.image.load('img/bird3back.png')
bird_b_4 = pygame.image.load('img/bird4back.png')
birds_b = [bird_b_1, bird_b_2, bird_b_3, bird_b_4]


bird_x = WIDTH / 2
bird_y = HEIGHT / 2
bird_index = 0

ballon_out = False
counter = 0
forward = True
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and bird_rect.left >= 0:
        forward = False
        bird_x += -SPEED
    elif keys[pygame.K_RIGHT] and bird_rect.right <= WIDTH:
        forward = True
        bird_x += SPEED
    if keys[pygame.K_UP] and bird_rect.top >= 0:
        bird_y += -SPEED
    elif keys[pygame.K_DOWN] and bird_rect.bottom <= HEIGHT:
        bird_y += SPEED

    screen.fill((140, 137, 246))
    if not ballon_out:
        screen.blit(ballon_surf, ballon_rect)
    bird_rect = birds_fw[bird_index].get_rect(center=(bird_x, bird_y))

    counter += 1
    if counter % 7 == 0:
        bird_index += 1
    if bird_index > len(birds_fw) - 1:
        bird_index = 0
    if forward:
        screen.blit(birds_fw[bird_index], bird_rect)
    else:
        screen.blit(birds_b[bird_index], bird_rect)

    if ballon_rect.colliderect(bird_rect):
        ballon_out = True

    pygame.display.update()
    clock.tick(60)

pygame.quit()