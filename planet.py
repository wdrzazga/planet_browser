import pygame


class Planet:
    def __init__(self, name, info, path):
        self.path = path
        self.info = info
        self.name = name

    def display(self, screen):

        screen.fill((0, 0, 0))
        bitmap = pygame.image.load(self.path).convert_alpha()
        screen.blit(bitmap, (20, 20))
