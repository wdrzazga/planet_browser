import pygame
import constants


class Planet:
    def __init__(self, name, info, path, moons=0):
        self.path = str(path)
        self.info = str(info)
        self.name = str(name)
        self.moons = int(moons)

    def display(self, screen):
        font = pygame.font.Font('resources/FacetLight.ttf', 40)
        font_small = pygame.font.Font('resources/FacetLight.ttf', 15)
        name_surface = font.render(self.name, True, constants.WHITE)
        info_surface = font_small.render(self.info, True, constants.WHITE)
        moons_surface = font_small.render(f'moons: {str(self.moons)}', True, constants.WHITE)
        name_rect = name_surface.get_rect(center=(2 * constants.WIDTH // 3, 30))
        info_rect = info_surface.get_rect(center=(constants.WIDTH // 2, 5 * constants.HEIGHT // 8))
        moons_rect = moons_surface.get_rect(center=(2 * constants.WIDTH // 3, 65))
        screen.fill((0, 0, 0))
        bitmap = pygame.image.load(self.path).convert_alpha()
        screen.blit(bitmap, (20, 20))
        screen.blit(name_surface, name_rect)
        screen.blit(info_surface, info_rect)
        screen.blit(moons_surface, moons_rect)
