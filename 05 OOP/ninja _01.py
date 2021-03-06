import pygame.sprite

WIDTH = 1280
HEIGHT = 620
BG_COLOR = (255, 255, 255)


class Ninja(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('img/Idle__000 1.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom=(WIDTH / 2, HEIGHT - 100))
        self.speed = 5

    def ninja_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.x_movement(self.speed)
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.x_movement(-self.speed)

    def x_movement(self, dx):
        self.rect.x += dx

    def update(self):
        self.ninja_input()


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Fruit Ninja')
clock = pygame.time.Clock()

# létrehoz egy ninja nevű konténert
ninja = pygame.sprite.GroupSingle()
# a konténerhez adja a Ninja osztály egy példányát
ninja.add(Ninja())

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BG_COLOR)

    ninja.draw(screen)
    ninja.update()

    pygame.display.update()
    clock.tick(60)

pygame.quit()
