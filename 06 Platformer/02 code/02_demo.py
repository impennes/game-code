import pygame


class Level():
    def __init__(self):
        self.player = pygame.sprite.GroupSingle()
        self.tiles = pygame.sprite.Group()
        for _ in range(10):
            tile = Tile()
            self.tiles.add(tile)
        self.player.add(Player())

class Tile(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()


level = Level()
print(level)
print(level.tiles)
print(level.player.sprite)

# for tile in level.tiles:
#     print(tile)