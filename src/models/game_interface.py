from typing import List

import pygame
from pygame.surface import Surface

from scenario import Scenario
from actor import Actor

class GameInterface:
    def __init__(self, scenario: Scenario, actors: List[Actor]) -> None:
        self.__scenario = scenario
        self.__actors = actors

    def draw(self, screen: Surface):
        self.__scenario.draw(screen)
        self.__scenario.draw_grid(screen)
        for actor in self.__actors:
            actor.draw(screen)

    def event_handler(self):
        for actor in self.__actors:
            if self.__scenario.allow_movement(actor.movement_request()):
                actor.move()
            else:
                actor.colide()