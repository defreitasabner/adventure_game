import pygame
import numpy as np
from pygame.surface import Surface

from constants import colors

class Actor:
    def __init__(self, initial_position: tuple[int], size = 32) -> None:
        self.__rect = pygame.Rect((initial_position), (size, size))
        self.__velocity = 1
        self.__intended_movement = initial_position

    def draw(self, screen: Surface) -> None:
        pygame.draw.rect(screen, colors.GREEN, self.__rect)

    def movement_request(self) -> None:
        key = pygame.key.get_pressed()
        intended_position = self.__rect.center
        if key[pygame.K_a]:
            intended_movement = np.array(self.__rect.center) - np.array([self.__velocity, 0])
            intended_position = tuple(intended_movement - np.array([self.__rect.width // 2, 0]))
            self.__intended_movement = tuple(intended_movement)
        elif key[pygame.K_d]:
            intended_movement = np.array(self.__rect.center) + np.array([self.__velocity, 0])
            intended_position = tuple(intended_movement + np.array([self.__rect.width // 2, 0]))
            self.__intended_movement = tuple(intended_movement)
        elif key[pygame.K_w]:
            intended_movement = np.array(self.__rect.center) - np.array([0, self.__velocity])
            intended_position = tuple(intended_movement - np.array([0, self.__rect.height // 2]))
            self.__intended_movement = tuple(intended_movement)
        elif key[pygame.K_s]:
            intended_movement = np.array(self.__rect.center) + np.array([0, self.__velocity])
            intended_position = tuple(intended_movement + np.array([0, self.__rect.height // 2]))
            self.__intended_movement = tuple(intended_movement)
        return intended_position

    def move(self):
        self.__rect.center = self.__intended_movement

    def colide(self):
        self.__intended_movement = self.__rect.center

    def current_position(self):
        return self.__rect.center
    
    # def movement_request(self) -> None:
    #     key = pygame.key.get_pressed()
    #     if key[pygame.K_a]:
    #         self.__rect.move_ip(-self.__velocity, 0)
    #     elif key[pygame.K_d]:
    #         self.__rect.move_ip(self.__velocity, 0)
    #     elif key[pygame.K_w]:
    #         self.__rect.move_ip(0, -self.__velocity)
    #     elif key[pygame.K_s]:
    #         self.__rect.move_ip(0, self.__velocity)