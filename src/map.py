import pygame


class Map:
    def __init__(self,
                 screen: pygame.Surface,
                 width: int,
                 height: int,
                 tile_size: int,
                 position: tuple = (0, 0),
                 background_color: tuple = (255, 255, 255),
                 tile_border_color: tuple = (0, 0, 0)
                 ):

        self.screen = screen
        self.width = width
        self.height = height
        self.tile_size = tile_size
        self.tiles_in_width = round(self.width / self.tile_size)
        self.tiles_in_height = round(self.height / self.tile_size)
        self.position = position
        self.background_color = background_color
        self.tile_border_color = tile_border_color

    def draw(self) -> None:
        pygame.draw.rect(self.screen, self.background_color,
                         (self.position[0], self.position[1], self.width, self.height))
        # TODO: Draw like a checkerboard
        for y in range(self.tiles_in_height):
            for x in range(self.tiles_in_width):
                pygame.draw.rect(
                    self.screen, self.tile_border_color,
                    ((x * self.tile_size) + self.position[0], (y * self.tile_size) + self.position[1], self.tile_size, self.tile_size),
                    2
                )

