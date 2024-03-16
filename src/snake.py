import pygame

from src.constants import SNAKE_SPEED
from src.enums.direction import Direction
from src.fruit import Fruit
from src.map import Map
from src.vector import Vector
from src.snake_part import SnakePart


class Snake:
    def __init__(self, game_map: Map):
        self.map = game_map
        self.moves = []
        self.direction = Direction.RIGHT
        self.speed = 10 / SNAKE_SPEED
        self.move_timer = self.speed

        init_x = max(round(self.map.amount_tiles * 0.3), 2)
        init_y = round(self.map.amount_tiles / 2)

        self.body = [SnakePart(Vector(init_x, init_y), True),
                     SnakePart(Vector(init_x - 1, init_y), False)]

    def append_move(self, direction: Direction) -> None:
        last_move = self.moves[-1] if len(self.moves) else self.direction

        if not last_move.is_same_axis(direction):
            self.moves.append(direction)

    def get_move(self):
        return self.moves.pop(0) if len(self.moves) else self.direction

    def move(self, dt: float) -> None:
        if self.move_timer > 0:
            self.move_timer -= dt
            return

        self.move_timer = self.speed
        self.direction = self.get_move()

        self.body[0].change_to_body()
        self.body.insert(0, SnakePart(self.body[0].position + self.direction.get_vector(), True))
        self.body.pop()

    def try_eat_fruit(self, fruit: Fruit) -> bool:
        if self.body[0].position == fruit.position:
            self.grow()
            return True
        return False

    def grow(self) -> None:
        self.body.append(SnakePart(self.body[-1].position.clone(), False))

    def check_self_collision(self) -> bool:
        return any(
            part.position == self.body[0].position
            for part in self.body[1:]
        )

    def check_border_collision(self) -> bool:
        head = self.body[0]
        return head.position.x < 0 or head.position.x >= self.map.amount_tiles or head.position.y < 0 or head.position.y >= self.map.amount_tiles

    def check_collisions(self) -> bool:
        return self.check_self_collision() or self.check_border_collision()

    def draw(self, screen: pygame.Surface) -> None:
        for part in self.body:
            part.draw(screen)
