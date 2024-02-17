import pygame

from src.constants import BORDER_COLOR, MAP_MARGIN, TILES_COLOR, SECOND_TILES_COLOR, BORDER_WIDTH, MAP_SIZE_TILES


class Map:
    def __init__(self,
                 width: int,
                 height: int,
                 tile_size: int,
                 ):

        self.width = width
        self.height = height
        self.tile_size = tile_size
        self.position = (MAP_MARGIN, MAP_MARGIN)

    def draw(self, screen: pygame.Surface) -> None:
        # Border
        pygame.draw.rect(
            screen,
            BORDER_COLOR,
            (self.position[0] - BORDER_WIDTH,
             self.position[1] - BORDER_WIDTH,
             self.width + BORDER_WIDTH * 2,
             self.height + BORDER_WIDTH * 2)
        )

        # Tiles
        for y in range(MAP_SIZE_TILES):
            use_second_color = y % 2
            for x in range(MAP_SIZE_TILES):
                pygame.draw.rect(
                    screen,
                    TILES_COLOR if use_second_color else SECOND_TILES_COLOR,
                    ((x * self.tile_size) + self.position[0],
                     (y * self.tile_size) + self.position[1],
                     self.tile_size,
                     self.tile_size),
                )
                use_second_color = not use_second_color
