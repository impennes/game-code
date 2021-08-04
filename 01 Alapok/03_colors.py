import pygame

pygame.init()
screen = pygame.display.set_mode((600, 300))
pygame.display.set_caption('Színek')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill('yellow')
    # screen.fill((125, 125, 0))
    pygame.display.update()

pygame.quit()