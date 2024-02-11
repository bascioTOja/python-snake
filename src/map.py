import pygame

from src.constants import BORDER_COLOR, MAP_MARGIN, TILES_COLOR, SECOND_TILES_COLOR, BORDER_WIDTH


class Map:
    def __init__(self,
                 width: int,
                 height: int,
                 tile_size: int,
                 ):

        self.width = width
        self.height = height
        self.tile_size = tile_size
        self.tiles_in_width = round(self.width / self.tile_size)
        self.tiles_in_height = round(self.height / self.tile_size)
        self.position = (MAP_MARGIN, MAP_MARGIN)
        self.border_width = BORDER_WIDTH
        self.border_color = BORDER_COLOR
        self.tiles_color = TILES_COLOR
        self.second_tiles_color = SECOND_TILES_COLOR

    def draw(self, screen: pygame.Surface) -> None:
        # Border
        pygame.draw.rect(
            screen,
            self.border_color,
            (self.position[0] - self.border_width,
             self.position[1] - self.border_width,
             self.width + self.border_width * 2,
             self.height + self.border_width * 2)
        )

        # Tiles
        for y in range(self.tiles_in_height):
            use_second_color = y % 2
            for x in range(self.tiles_in_width):
                pygame.draw.rect(
                    screen, self.tiles_color if use_second_color else self.second_tiles_color,
                    ((x * self.tile_size) + self.position[0],
                     (y * self.tile_size) + self.position[1],
                     self.tile_size,
                     self.tile_size),
                )
                use_second_color = not use_second_color
