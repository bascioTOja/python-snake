import pygame

from src.constants import TILE_SIZE, MAP_MARGIN, APPLE_COLOR
from src.vector import Vector


class Fruit:
    color = APPLE_COLOR

    def __init__(self, position: Vector):
        self.position = position

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(
            screen,
            self.color,
            (self.position.x * TILE_SIZE + MAP_MARGIN, self.position.y * TILE_SIZE + MAP_MARGIN, TILE_SIZE, TILE_SIZE)
        )
