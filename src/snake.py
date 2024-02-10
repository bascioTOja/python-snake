import pygame

from src.constants import GRID_WIDTH, GRID_HEIGHT, HEAD_COLOR, SNAKE_COLOR, SNAKE_SPEED
from src.enums.direction import Direction
from src.fruit import Fruit
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

    def set_direction(self, direction: Direction) -> None:
        # TODO: Make movement as queue
        self.direction = direction

    def move(self, dt: float) -> bool:
        if self.move_timer > 0:
            self.move_timer -= dt
            return False

        self.move_timer = self.speed
        move_direction = self.direction

        for part in self.body:
            move_direction = part.move(move_direction)
        return True

    def try_eat_fruit(self, fruit: Fruit) -> bool:
        if self.body[0].x == fruit.x and self.body[0].y == fruit.y:
            self.grow()
            return True
        return False

    def grow(self) -> None:
        self.body.append(SnakePart(self.body[-1].x, self.body[-1].y, Direction.STOP, SNAKE_COLOR))

    def check_self_collision(self) -> bool:
        return any(
            part.x == self.body[0].x and part.y == self.body[0].y
            for part in self.body[1:]
        )

    def check_border_collision(self) -> bool:
        head = self.body[0]
        return head.x < 0 or head.x >= GRID_WIDTH or head.y < 0 or head.y >= GRID_HEIGHT

    def check_collisions(self) -> bool:
        return self.check_self_collision() or self.check_border_collision()

    def draw(self, screen: pygame.Surface) -> None:
        for part in self.body:
            part.draw(screen)
