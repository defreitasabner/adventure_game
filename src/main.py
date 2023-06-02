import pygame

from constants import settings, colors
from models.Scenario import Scenario

pygame.init()

screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
clock = pygame.time.Clock()

scenario = Scenario(size=25)

running = True
while running:

    screen.fill(colors.BLACK)

    scenario.draw(screen)
    scenario.draw_grid(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()