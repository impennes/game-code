import pygame

pygame.init()
screen = pygame.display.set_mode((600, 300))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # mouse with event loop
        if event.type == pygame.MOUSEMOTION:
            print(event.pos)
        if event.type == pygame.MOUSEBUTTONDOWN:
            print('az egér gombja lenyomva')

    # pygame.mouse
    # print('az egér pozíciója:', pygame.mouse.get_pos())
    # print('az egér gombajinak lenyomása:', pygame.mouse.get_pressed())
    pygame.display.update()

pygame.quit()