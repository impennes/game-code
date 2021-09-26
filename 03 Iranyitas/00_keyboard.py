import pygame

WIDTH, HEIGHT = 600, 300

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # keyboard input with event loop
        # if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        #     print('SPACE DOWN')

    # keyboard input with pygame.key
    # print(pygame.key.get_pressed())
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        print(keys[pygame.K_SPACE])

    pygame.display.update()
    clock.tick(1)

pygame.quit()