import pygame


class UI:
    def __init__(self, surface):
        self.display_surface = surface
        self.heart_surf = pygame.image.load('../img/heart.png').convert_alpha()
        self.crate_surf = pygame.image.load('../img/crate.png').convert_alpha()
        self.font = pygame.font.Font('../img/font/ARCADEPI.ttf', 30)

    def show_health(self, h_current):
        heart_rect = self.heart_surf.get_rect(topleft=(20, 20))
        for index in range(h_current):
            heart_rect.x += 50 * index
            self.display_surface.blit(self.heart_surf, heart_rect)

    def show_create(self, c_max, c_current):
        crate_rect = self.crate_surf.get_rect(topleft=(20, 80))
        self.display_surface.blit(self.crate_surf, crate_rect)

        crate_txt_surf = self.font.render(f'{c_max} / {c_current}', False, '#33323d')
        crate_txt_rect = crate_txt_surf.get_rect(topleft=(80, 80))
        self.display_surface.blit(crate_txt_surf, crate_txt_rect)


