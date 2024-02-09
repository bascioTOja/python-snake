from typing import Tuple

import pygame

from src.constants import TILE_SIZE, MAP_MARGIN
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

    def move(self, move_direction: Direction) -> Direction:
        if self.direction == Direction.STOP:
            self.direction = move_direction
            return self.direction

        if move_direction == Direction.UP:
            self.y = self.y - 1
        elif move_direction == Direction.DOWN:
            self.y = self.y + 1
        elif move_direction == Direction.LEFT:
            self.x = self.x - 1
        elif move_direction == Direction.RIGHT:
            self.x = self.x + 1

        old_direction = self.direction
        self.direction = move_direction

        return old_direction

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

    def __str__(self) -> str:
        return f'({self.x}, {self.y} - {self.direction})'
