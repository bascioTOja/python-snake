import pygame

from src.enums.direction import Direction


class Snake:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.direction = Direction.RIGHT
        self.size = 2
        self.pos = (5, 5)

    def set_direction(self, direction: Direction) -> None:
        self.direction = direction

    def move(self) -> None:
        if self.direction == Direction.UP:
            self.pos = (self.pos[0], self.pos[1] - 1)
        elif self.direction == Direction.DOWN:
            self.pos = (self.pos[0], self.pos[1] + 1)
        elif self.direction == Direction.LEFT:
            self.pos = (self.pos[0] - 1, self.pos[1])
        elif self.direction == Direction.RIGHT:
            self.pos = (self.pos[0] + 1, self.pos[1])

    def draw(self):
        pass
