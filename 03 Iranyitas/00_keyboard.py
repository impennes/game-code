import pygame

pygame.init()
screen = pygame.display.set_mode((600, 300))
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # keyboard input with event loop
        if event.type == pygame.KEYDOWN and pygame.K_SPACE:
            print('SPACE down')

    # keyboard input with pygame.key
    # print(pygame.key.get_pressed())
    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]:
    #     print(type(keys))
    #     print(keys[pygame.K_SPACE])
    pygame.display.update()
    clock.tick(1)

pygame.quit()