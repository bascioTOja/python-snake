import pygame

from src.constants import GRID_WIDTH, GRID_HEIGHT, HEAD_COLOR, SNAKE_COLOR, SNAKE_SPEED
from src.enums.direction import Direction
from src.snake_part import SnakePart


class Snake:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.direction = Direction.RIGHT
        self.speed = 10 / SNAKE_SPEED
        self.move_timer = self.speed

        init_x = max(round(GRID_WIDTH * 0.3), 2)
        init_y = round(GRID_HEIGHT / 2)

        self.body = [SnakePart(init_x, init_y, self.direction, HEAD_COLOR), SnakePart(init_x - 1, init_y, self.direction, SNAKE_COLOR)]
        self.size = len(self.body)

    def set_direction(self, direction: Direction) -> None:
        self.direction = direction

    def move(self, dt: float) -> None:
        if self.move_timer > 0:
            self.move_timer -= dt
            return

        self.move_timer = self.speed
        move_direction = self.direction
        print(move_direction)
        for part in self.body:
            move_direction = part.move(move_direction)

    def draw(self, screen: pygame.Surface) -> None:
        for part in self.body:
            part.draw(screen)
