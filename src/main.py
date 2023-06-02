import pygame

from constants import settings, colors
from models.scenario import Scenario
from models.matrix_generator import MatrixGenerator
from models.actor import Actor

pygame.init()

screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
clock = pygame.time.Clock()

matrix_generator = MatrixGenerator()
scenario = Scenario(size = 20, matrix = matrix_generator.generate_simple_arena(20))

actor = Actor((settings.SCREEN_WIDTH // 2, settings.SCREEN_HEIGHT // 2))

running = True
while running:

    screen.fill(colors.BLACK)

    scenario.draw(screen)
    scenario.draw_grid(screen)

    actor.draw(screen)
    actor.movement_request()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()