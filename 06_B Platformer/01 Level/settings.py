import pygame

level_map_1 = [
'                            ',
'                            ',
'                            ',
' XXyz  XXX            XX    ',
' XX                         ',
' XXXX         XX         XX ',
' XXXX       XX              ',
' XX    X  XXXX    XX  XX    ',
'       X  XXXX    XX  XXX   ',
'    XXXX  XXXXXX  XX  XXXX  ',
'XXXXXXXX  XXXXXX  XX  XXXX  ']

level_map = [
'                            ',
'                            ',
'                            ',
'                            ',
'                            ',
'                            ',
'                            ',
'             noop           ',
'                            ',
'bbbbbbc    abbb   XX  XXX   ',
'eeeeeef   aheeee  XX  XXXX  ']




tile_size = 64
screen_width = 1200
screen_height = len(level_map) * tile_size


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size, type):
        super().__init__()
        if type == 'X':
            self.image = pygame.Surface((size, size))
            self.image.fill('grey')
        else:
            # self.image = pygame.image.load('img/terrain/Idle__000 1.png')
            self.image = pygame.image.load(f'img/terrain/{type}.png').convert_alpha()
            # self.image = pygame.transform.scale(self.image, (tile_size, tile_size))
        self.rect = self.image.get_rect(topleft=pos)


class Level:
    def __init__(self, level_data, surface):
        self.diplay_surface = surface
        self.setup_level(level_data)

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                if cell != ' ':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    tile = Tile((x, y), tile_size, cell)
                    self.tiles.add(tile)

    def run(self):
        self.tiles.draw(self.diplay_surface)