import pygame
import numpy as np
from pygame.surface import Surface

from constants import colors

class Actor:
    def __init__(self, initial_position: tuple[int], size = 32) -> None:
        self.__rect = pygame.Rect((initial_position), (size, size))
        self.__velocity = 1

    def draw(self, screen: Surface) -> None:
        pygame.draw.rect(screen, colors.GREEN, self.__rect)

    def movement_request(self) -> None:
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            self.__rect.move_ip(-self.__velocity, 0)
        elif key[pygame.K_d]:
            self.__rect.move_ip(self.__velocity, 0)
        elif key[pygame.K_w]:
            self.__rect.move_ip(0, -self.__velocity)
        elif key[pygame.K_s]:
            self.__rect.move_ip(0, self.__velocity)

    def current_position(self):
        return self.__rect.center