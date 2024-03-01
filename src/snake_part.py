import pygame

from src.constants import TILE_SIZE, MAP_MARGIN, HEAD_COLOR, SNAKE_COLOR
from src.vector import Vector


class SnakePart:
    head_color = HEAD_COLOR
    body_color = SNAKE_COLOR

    def __init__(self, position: Vector, is_head: bool):
        self.position = position
        self.is_head = is_head

    def change_to_body(self):
        self.is_head = False

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(
            screen,
            self.head_color if self.is_head else self.body_color,
            ((self.position.x * TILE_SIZE) + MAP_MARGIN, (self.position.y * TILE_SIZE) + MAP_MARGIN, TILE_SIZE, TILE_SIZE)
        )
        pygame.draw.rect(
            screen,
            (0, 0, 0),
            ((self.position.x * TILE_SIZE) + MAP_MARGIN, (self.position.y * TILE_SIZE) + MAP_MARGIN, TILE_SIZE, TILE_SIZE),
            2
        )
