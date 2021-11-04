import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, size, x, y):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self, shift):
        self.rect.x += shift


class TerrainTile(Tile):
    def __init__(self, size, x, y, terrain_type):
        super().__init__(size, x, y)
        self.image = pygame.image.load(f'../img/terrain/{terrain_type}.png').convert_alpha()


class Crate(Tile):
    def __init__(self, size, x, y):
        super().__init__(size, x, y)
        self.image_list = []
        for index in range(1, 4):
            self.image_list.append(pygame.image.load(f'../img/crate/crate_{index}.png').convert_alpha())
        self.image_index = 0
        self.image = self.image_list[self.image_index]
        offset_y = y + size
        self.rect = self.image.get_rect(bottomleft=(x, offset_y))

    def update(self, shift):
        self.rect.x += shift

        self.image_index += 0.05
        if self.image_index > len(self.image_list):
            self.image_index = 0
        self.image = self.image_list[int(self.image_index)]