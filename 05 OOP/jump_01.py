import pygame.sprite

WIDTH = 1280
HEIGHT = 620
BG_COLOR = (255, 255, 255)
NINJA_VELOCITY = 5


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Ninja jump')
clock = pygame.time.Clock()

ninja_surf = pygame.image.load('img/Idle__000 1.png').convert_alpha()
ninja_rect = ninja_surf.get_rect(midbottom=(WIDTH/2, HEIGHT-100))

jump = False
jump_index = 10
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BG_COLOR)
    pygame.draw.line(screen, 'gray', (0, HEIGHT-95), (WIDTH, HEIGHT-95), 5)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and ninja_rect.left > NINJA_VELOCITY:
        ninja_rect.left -= NINJA_VELOCITY
    if keys[pygame.K_RIGHT] and ninja_rect.right < WIDTH - NINJA_VELOCITY:
        ninja_rect.right += NINJA_VELOCITY

    if keys[pygame.K_SPACE]:
        jump = True
    if jump:
        print(f'JUMP {jump_index=} {ninja_rect.bottom=}')
        if jump_index >= -10:
            direction = 1
            if jump_index < 0:
                direction = -1
            ninja_rect.bottom -= (jump_index ** 2) * 0.5 * direction
            jump_index -= 1
        else:
            jump = False
            jump_index = 10
            ninja_rect.bottom = HEIGHT-100

    screen.blit(ninja_surf, ninja_rect)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
