import pygame
from settings import *
from player import Player
from tiles import Tile, TerrainTile, Crate, OtherTile
from enemy import Enemy


class Level:
    def __init__(self, level_data, surface):
        self.diplay_surface = surface
        self.world_shift = 0
        self.player = pygame.sprite.GroupSingle()
        self.terrain_tiles = pygame.sprite.Group()
        self.crates = pygame.sprite.Group()
        self.other_tiles = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.constraints = pygame.sprite.Group()
        self.max_hearts = 0
        self.current_hearts = 0
        self.max_crates = 0
        self.current_crates = 0
        self.setup_level(level_data)

    def setup_level(self, layout):
        for row_index, row in enumerate(layout):
            for col_index, tile_type in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if tile_type == 'P':
                    player_sprite = Player((x, y))
                    self.player.add(player_sprite)
                elif tile_type == 'T':
                    tile = Crate(tile_size, x, y)
                    self.crates.add(tile)
                elif tile_type == 'E':
                    self.enemies.add(Enemy(tile_size, x, y))
                elif tile_type == 'C':
                    constraint = Tile(tile_size, x, y)
                    self.constraints.add(constraint)
                elif tile_type in others:
                    tile = OtherTile(tile_size, x, y, tile_type)
                    self.other_tiles.add(tile)
                elif tile_type != ' ':
                    tile = TerrainTile(tile_size, x, y, tile_type)
                    self.terrain_tiles.add(tile)

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < screen_width / 4 and direction_x < 0:
            self.world_shift = 8
            player.speed = 0
        elif player_x > screen_width - (screen_width / 4) and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 8

    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.terrain_tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.terrain_tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0

    def enemy_collision_reverse(self):
        for enemy in self.enemies.sprites():
            if pygame.sprite.spritecollide(enemy, self.constraints, False):
                enemy.reverse()

    def run(self):
        self.player.update()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.terrain_tiles.update(self.world_shift)
        self.terrain_tiles.draw(self.diplay_surface)
        self.crates.update(self.world_shift)
        self.crates.draw(self.diplay_surface)
        self.other_tiles.update(self.world_shift)
        self.other_tiles.draw(self.diplay_surface)
        self.enemies.draw(self.diplay_surface)
        self.constraints.update(self.world_shift)
        self.enemy_collision_reverse()
        self.enemies.update(self.world_shift)
        self.scroll_x()
        self.player.draw(self.diplay_surface)