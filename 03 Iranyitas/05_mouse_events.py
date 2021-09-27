import pygame

pygame.init()
screen = pygame.display.set_mode((600, 300))
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # mouse with event loop
        # if event.type == pygame.MOUSEMOTION:
        #     print(event.pos)
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     print('az egér gombja lenyomva')

    # pygame.mouse
    print('az egér pozíciója', pygame.mouse.get_pos())
    print('az egér gombja lenyomva', pygame.mouse.get_pressed())
    print(pygame.mouse.get_pressed()[0])
    pygame.display.update()
    clock.tick(30)

pygame.quit()