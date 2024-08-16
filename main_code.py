import pygame
import constants

from planet_registry import PlanetRegistry

pygame.init()
screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT),
                                 pygame.FULLSCREEN | pygame.DOUBLEBUF)
screen_center = constants.WIDTH // 2, constants.HEIGHT // 2
preg = PlanetRegistry()
current_planet: int = 0

running = True

preg.planets[current_planet].display(screen)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            current_planet = (current_planet + 1) % len(preg.planets)
            preg.planets[current_planet].display(screen)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            current_planet -= 1
            if current_planet < 0:
                current_planet = len(preg.planets) - 1
            preg.planets[current_planet].display(screen)
        pygame.display.update()


