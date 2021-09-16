import pygame

BLUE = (0, 0, 255)
GRAY = (127, 127, 127)

pygame.init()
screen = pygame.display.set_mode((600, 300))
background = GRAY

# Négyszög rajzolása
# pygame.draw.rect(screen, BLUE, (10, 20, 100, 50), 5, 10)
rect_pos_x = 10
rect_pos_y = 20
rect = pygame.Rect(rect_pos_x, rect_pos_y, 100, 50)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    rect_pos_x += 0.01
    rect_pos_y += 0.01
    screen.fill(background)
    rect = pygame.Rect(rect_pos_x, rect_pos_y, 100, 50)
    pygame.draw.rect(screen, BLUE, rect)
    pygame.display.update()

pygame.quit()