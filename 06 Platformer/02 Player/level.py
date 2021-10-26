import pygame
from settings import *
from player import Player


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
        self.player = pygame.sprite.GroupSingle()

        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if cell == 'P':
                    player_sprite = Player((x, y))
                    self.player.add(player_sprite)
                elif cell != ' ':
                    tile = Tile((x, y), tile_size, cell)
                    self.tiles.add(tile)

    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0

    def run(self):
        self.player.update()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.tiles.draw(self.diplay_surface)
        self.player.draw(self.diplay_surface)