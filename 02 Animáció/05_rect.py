import pygame

WIDTH, HEIGHT = 500, 200
RED = (255, 0, 0)
GRAY = (150, 150, 150)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

rect = pygame.Rect(50, 60, 200, 80)
print(f'x={rect.x}, y={rect.y}, w={rect.w}, h={rect.h}')
print(f'left={rect.left}, top={rect.top}, right={rect.right}, bottom={rect.bottom}')
print(f'center={rect.center}')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(GRAY)
    pygame.draw.rect(screen, RED, rect)
    # pygame.display.update()
    pygame.display.flip()

pygame.quit()