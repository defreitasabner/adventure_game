import pygame
from pygame.surface import Surface

from constants import colors

class Actor:
    def __init__(self, initial_position: tuple[int]) -> None:
        self.__rect = pygame.Rect((initial_position), (32, 32))

    def draw(self, screen: Surface) -> None:
        pygame.draw.rect(screen, colors.GREEN, self.__rect)

    def event_handler(self) -> None:
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            self.__rect.move_ip(-1, 0)
        elif key[pygame.K_d]:
            self.__rect.move_ip(1, 0)
        elif key[pygame.K_w]:
            self.__rect.move_ip(0, -1)
        elif key[pygame.K_s]:
            self.__rect.move_ip(0, 1)