from typing import Tuple

import pygame

from src.constants import SNAKE_COLOR, TILE_SIZE, MAP_MARGIN
from src.enums.direction import Direction


class SnakePart:
    def __init__(self, x: int, y: int, direction: Direction, color: Tuple[int, int, int]):
        self.x = x
        self.y = y
        self.direction = direction
        self.offset_width = MAP_MARGIN
        self.offset_height = MAP_MARGIN
        self.color = color
        self.size = TILE_SIZE

    def draw(self, screen: pygame.Surface) -> None:

        pygame.draw.rect(
            screen,
            self.color,
            ((self.x * self.size) + self.offset_width, (self.y * self.size) + self.offset_height,self.size, self.size)
        )
        pygame.draw.rect(
            screen,
            (0, 0, 0),
            ((self.x * self.size) + self.offset_width, (self.y * self.size) + self.offset_height,self.size, self.size),
            2
        )
