import pygame
from pygame.surface import Surface
import numpy as np
from numpy import ndarray

from constants import settings, colors

class Scenario():
    def __init__(self, size: int = 25, matrix: ndarray | None = None) -> None:
        self.__cell_width = settings.SCREEN_WIDTH // size
        self.__cell_height = settings.SCREEN_HEIGHT // size
        if type(matrix) == ndarray:
            self.__matrix = matrix
        else:
            self.__matrix: ndarray = np.array([np.zeros(size, dtype=int) for _ in range(size)])

    def draw_grid(self, screen: Surface) -> None:
        temp_x = 0
        temp_y = 0
        for _ in range(self.__matrix.shape[0]):
            temp_x += self.__cell_width
            temp_y += self.__cell_height
            pygame.draw.line(screen, colors.WHITE, (0, temp_y), (settings.SCREEN_WIDTH, temp_y))
            pygame.draw.line(screen, colors.WHITE, (temp_x, 0), (temp_x, settings.SCREEN_HEIGHT))

    def draw(self, screen: Surface) -> None:
        temp_x = 0
        temp_y = 0
        for i in range(self.__matrix.shape[0]):
            for j in range(self.__matrix.shape[1]):
                if self.__matrix[i][j] == 1:
                    pygame.draw.rect(screen, colors.RED, (temp_x, temp_y, self.__cell_width, self.__cell_height))
                else:
                    pygame.draw.rect(screen, colors.BLUE, (temp_x, temp_y, self.__cell_width, self.__cell_height))
                temp_x += self.__cell_width
            temp_x = 0
            temp_y += self.__cell_height
