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
                    pygame.draw.rect(screen, colors.BLACK, (temp_x, temp_y, self.__cell_width, self.__cell_height))
                else:
                    pygame.draw.rect(screen, colors.WHITE, (temp_x, temp_y, self.__cell_width, self.__cell_height))
                temp_x += self.__cell_width
            temp_x = 0
            temp_y += self.__cell_height

    def allow_movement(self, intend_position: tuple[int]) -> tuple[int]:
        if type(intend_position) == tuple:
            intend_pos_on_matrix = self.__convert_pixel_position_to_matrix_position(intend_position)
            if self.__matrix[intend_pos_on_matrix[0], intend_pos_on_matrix[1]] == 0:
                return True
            else:
                return False

    def __convert_pixel_position_to_matrix_position(self, pixel_position: tuple[int]) -> tuple[int]:
        x = pixel_position[0]
        y = pixel_position[1]
        row = x // self.__cell_width
        column = y // self.__cell_height
        return (row, column)
    
    def __convert_matrix_position_to_matrix_position(self, matrix_position: tuple[int]) -> tuple[int]:
        x = ((matrix_position[1] + 1) * self.cell_width) - (self.cell_width // 2)
        y = ((matrix_position[0] + 1) * self.cell_height) - (self.cell_height // 2)
        return (x, y)
