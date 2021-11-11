import pygame


class Level():
    def __init__(self):
        self.tiles = pygame.sprite.Group()
        for _ in range(10):
            tile = Tile()
            self.tiles.add(tile)


class Tile(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()


level = Level()
print(level)
print(level.tiles)
print(level.tiles.spritedict)

for tile in level.tiles:
    print(tile)