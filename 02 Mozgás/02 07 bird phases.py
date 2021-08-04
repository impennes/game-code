import pygame

pygame.init()
screen_width = 1280
screen_height = 620
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

bird_phases = ['0', 'bird1.png', 'bird2.png', 'bird4.png', 'bird3.png', '5']

bird = pygame.image.load(bird_phases[1])
bird_rect = bird.get_rect(midleft=(0, screen_height / 2))
bird_speed = 5
index = 0
delta = 1
szamlalo = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((140, 137, 246))

    if szamlalo % 7 == 0:
        if index == 4:
            delta = -1
        elif index == 1:
            delta = 1
        index += delta
    szamlalo += 1

    bird = pygame.image.load(bird_phases[index])
    if bird_rect.right < screen_width:
        bird_rect.move_ip(bird_speed, 0)
    screen.blit(bird, bird_rect)
    pygame.display.update()
    clock.tick(120)

pygame.quit()