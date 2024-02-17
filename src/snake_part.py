from typing import Tuple
import pygame

from src.constants import TILE_SIZE, MAP_MARGIN
from src.enums.direction import Direction


class SnakePart:
    def __init__(self, x: int, y: int, color: Tuple[int, int, int]):
        self.x = x
        self.y = y
        self.color = color

    def move_by_direction(self, move_direction: Direction) -> Tuple[int, int]:
        old_position = (self.x, self.y)

        if move_direction == Direction.UP:
            self.y = self.y - 1
        elif move_direction == Direction.DOWN:
            self.y = self.y + 1
        elif move_direction == Direction.LEFT:
            self.x = self.x - 1
        elif move_direction == Direction.RIGHT:
            self.x = self.x + 1

        return old_position

    def move(self, move_position: Tuple[int, int]) -> Tuple[int, int]:
        old_position = (self.x, self.y)
        self.x, self.y = move_position

        return old_position

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(
            screen,
            self.color,
            ((self.x * TILE_SIZE) + MAP_MARGIN, (self.y * TILE_SIZE) + MAP_MARGIN, TILE_SIZE, TILE_SIZE)
        )
        pygame.draw.rect(
            screen,
            (0, 0, 0),
            ((self.x * TILE_SIZE) + MAP_MARGIN, (self.y * TILE_SIZE) + MAP_MARGIN, TILE_SIZE, TILE_SIZE),
            2
        )
