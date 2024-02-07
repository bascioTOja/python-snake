import pygame

from src.constants import GRID_WIDTH, GRID_HEIGHT, HEAD_COLOR, SNAKE_COLOR, SNAKE_SPEED
from src.enums.direction import Direction
from src.snake_part import SnakePart


class Snake:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.direction = Direction.RIGHT

        init_x = max(round(GRID_WIDTH * 0.3), 2)
        init_y = round(GRID_HEIGHT / 2)

        self.body = [SnakePart(init_x, init_y, self.direction, HEAD_COLOR), SnakePart(init_x - 1, init_y, self.direction, SNAKE_COLOR)]
        self.size = len(self.body)

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

    def draw(self, screen: pygame.Surface) -> None:
        for part in self.body:
            part.draw(screen)
