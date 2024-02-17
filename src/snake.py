import pygame

from src.constants import GRID_WIDTH, GRID_HEIGHT, HEAD_COLOR, SNAKE_COLOR, SNAKE_SPEED
from src.enums.direction import Direction
from src.fruit import Fruit
from src.snake_part import SnakePart


def check_if_is_possible_move(direction: Direction, move_direction: Direction) -> bool:
    return (
            (direction != Direction.LEFT or move_direction != Direction.RIGHT)
            and (direction != Direction.RIGHT or move_direction != Direction.LEFT)
            and (direction != Direction.UP or move_direction != Direction.DOWN)
            and (direction != Direction.DOWN or move_direction != Direction.UP)
    )


class Snake:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.moves = []
        self.direction = Direction.RIGHT
        self.speed = 10 / SNAKE_SPEED
        self.move_timer = self.speed

        init_x = max(round(GRID_WIDTH * 0.3), 2)
        init_y = round(GRID_HEIGHT / 2)

        self.body = [SnakePart(init_x, init_y, HEAD_COLOR),
                     SnakePart(init_x - 1, init_y, SNAKE_COLOR)]

    def append_move(self, direction: Direction) -> None:
        last_move = self.moves[-1] if len(self.moves) else self.direction

        if check_if_is_possible_move(last_move, direction):
            self.moves.append(direction)

    def get_move(self):
        return self.moves.pop(0) if len(self.moves) else self.direction

    def move(self, dt: float) -> bool:
        if self.move_timer > 0:
            self.move_timer -= dt
            return False

        self.move_timer = self.speed
        self.direction = self.get_move()

        move_position = self.body[0].move_by_direction(self.direction)
        for part in self.body[1:]:
            move_position = part.move(move_position)

        return True

    def try_eat_fruit(self, fruit: Fruit) -> bool:
        if self.body[0].x == fruit.x and self.body[0].y == fruit.y:
            self.grow()
            return True
        return False

    def grow(self) -> None:
        self.body.append(SnakePart(self.body[-1].x, self.body[-1].y, SNAKE_COLOR))

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
