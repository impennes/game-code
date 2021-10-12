import pygame.sprite

WIDTH = 1280
HEIGHT = 620
BG_COLOR = (255, 255, 255)
NINJA_SPEED = 5
GRAVITY = 0.8
JUMP_SPEED = -8

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Ninja jump')
clock = pygame.time.Clock()

ninja_surf = pygame.image.load('img/Idle__000 1.png').convert_alpha()
ninja_rect = ninja_surf.get_rect(midbottom=(WIDTH/2, HEIGHT-100))
ground = HEIGHT-95

platform_surf = pygame.image.load('img/platform.png').convert_alpha()
platform_rect = platform_surf.get_rect(topleft=(HEIGHT/2-50, ground))

direction_y = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BG_COLOR)
    screen.blit(platform_surf, platform_rect)


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and ninja_rect.left > NINJA_SPEED:
        ninja_rect.centerx -= NINJA_SPEED
    if keys[pygame.K_RIGHT] and ninja_rect.right < WIDTH - NINJA_SPEED:
        ninja_rect.centerx += NINJA_SPEED

    direction_y += GRAVITY
    if keys[pygame.K_SPACE]:
        direction_y = JUMP_SPEED

    ninja_rect.centery += direction_y
    if ninja_rect.colliderect(platform_rect):
        ninja_rect.bottom = ground


    screen.blit(ninja_surf, ninja_rect)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
