import random
import pygame

from src.constants import MAX_MAP_WIDTH, MAX_MAP_HEIGHT, TILE_SIZE, APPLE_COLOR, GRID_HEIGHT, GRID_WIDTH
from src.enums.direction import Direction
from src.enums.exit_state import ExitState
from src.fruit import Fruit
from src.map import Map
from src.snake import Snake


class GameController:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.map = Map(MAX_MAP_WIDTH, MAX_MAP_HEIGHT, TILE_SIZE)
        self.snake = Snake(self.screen)
        self.exit_state = ExitState.CONTINUE
        self.fruit = self.generate_fruit()

    def exit(self) -> None:
        self.exit_state = ExitState.EXIT

    def events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit()
            elif event.type == pygame.KEYDOWN:
                self.keydown_events(event)

    def keydown_events(self, event) -> None:
        if event.key in [pygame.K_UP, pygame.K_w]:
            self.snake.append_move(Direction.UP)
        elif event.key in [pygame.K_DOWN, pygame.K_s]:
            self.snake.append_move(Direction.DOWN)
        elif event.key in [pygame.K_LEFT, pygame.K_a]:
            self.snake.append_move(Direction.LEFT)
        elif event.key in [pygame.K_RIGHT, pygame.K_d]:
            self.snake.append_move(Direction.RIGHT)

    def generate_fruit(self) -> Fruit:
        available_spaces = [(x, y) for x in range(round(GRID_WIDTH)) for y in range(round(GRID_HEIGHT)) if not any(part.x == x and part.y == y for part in self.snake.body)]

        if not available_spaces:
            # TODO: Rethink this
            raise Exception("No space left!")

        fruit_position = random.choice(available_spaces)

        return Fruit(fruit_position[0], fruit_position[1], APPLE_COLOR)

    def draw(self) -> None:
        self.map.draw(self.screen)
        self.snake.draw(self.screen)
        self.fruit.draw(self.screen)

    def process_game_iteration(self, dt: float) -> ExitState:
        self.events()

        self.snake.move(dt)
        if self.snake.try_eat_fruit(self.fruit):
            self.fruit = self.generate_fruit()

        if self.snake.check_collisions():
            self.exit_state = ExitState.RESTART

        self.draw()

        return self.exit_state
