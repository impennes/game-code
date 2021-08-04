import pygame

BLUE = (0, 0, 255)
GRAY = (127, 127, 127)

pygame.init()
screen = pygame.display.set_mode((600, 300))
background = GRAY

rect_pos_x = 10
rect_pos_y = 20
rect = pygame.Rect(rect_pos_x, rect_pos_y, 100, 50)

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    rect_pos_x += 10
    rect_pos_y += 5
    screen.fill(background)
    rect = pygame.Rect(rect_pos_x, rect_pos_y, 100, 50)
    pygame.draw.rect(screen, BLUE, rect)
    pygame.display.update()
    clock.tick(60)

pygame.quit()