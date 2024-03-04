import itertools
import pygame

from src.constants import BORDER_COLOR, MAP_MARGIN, TILES_COLOR, SECOND_TILES_COLOR, BORDER_WIDTH, \
    TILE_SIZE, MAP_AMOUNT_TILES


class Map:
    border_width = BORDER_WIDTH
    tile_size = TILE_SIZE
    amount_tiles = MAP_AMOUNT_TILES
    tile_color = TILES_COLOR
    second_tiles_color = SECOND_TILES_COLOR

    def __init__(self,
                 width: int,
                 height: int,
                 ):
        self.width = width
        self.height = height
        self.position = (MAP_MARGIN, MAP_MARGIN)

    def draw(self, screen: pygame.Surface) -> None:
        # Border
        pygame.draw.rect(
            screen,
            BORDER_COLOR,
            (self.position[0] - self.border_width,
             self.position[1] - self.border_width,
             self.width + self.border_width * 2,
             self.height + self.border_width * 2)
        )

        # Tiles
        for y, x in itertools.product(range(self.amount_tiles), range(self.amount_tiles)):
            pygame.draw.rect(
                screen,
                self.tile_color if (y % 2 != x % 2) else self.second_tiles_color,
                ((x * self.tile_size) + self.position[0],
                 (y * self.tile_size) + self.position[1],
                 self.tile_size,
                 self.tile_size),
            )
