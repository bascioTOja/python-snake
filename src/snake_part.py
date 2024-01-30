import pygame


class SnakePart:
    def __init__(self, screen: pygame.Surface, pos: tuple):
        self.screen = screen
        self.pos = pos
        self.color = (105, 180, 200)  # TODO: Maybe random color
