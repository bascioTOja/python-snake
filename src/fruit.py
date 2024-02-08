import pygame

from src.constants import TILE_SIZE, MAP_MARGIN


class Fruit():
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(
            screen,
            self.color,
            (self.x * TILE_SIZE + MAP_MARGIN, self.y * TILE_SIZE + MAP_MARGIN, TILE_SIZE, TILE_SIZE)
        )
