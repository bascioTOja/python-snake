import pygame

from src.constants import MAX_MAP_WIDTH, MAX_MAP_HEIGHT, TILE_SIZE
from src.enums.direction import Direction
from src.enums.exit_state import ExitState
from src.map import Map
from src.snake import Snake


class GameController:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.map = Map(MAX_MAP_WIDTH, MAX_MAP_HEIGHT, TILE_SIZE)
        self.snake = Snake(self.screen)
        self.exit_state = ExitState.CONTINUE

    def exit(self) -> None:
        self.exit_state = ExitState.EXIT

    def events(self, dt: float) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit()
            elif event.type == pygame.KEYDOWN:
                self.keydown_events(event)

        self.snake.move(dt)

    def keydown_events(self, event) -> None:
        if event.key == pygame.K_UP or event.key == pygame.K_w:
            self.snake.set_direction(Direction.UP)
        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
            self.snake.set_direction(Direction.DOWN)
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.snake.set_direction(Direction.LEFT)
        elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.snake.set_direction(Direction.RIGHT)

    def draw(self) -> None:
        self.map.draw(self.screen)
        self.snake.draw(self.screen)

    def process_game_iteration(self, dt: float) -> ExitState:
        self.events(dt)
        self.draw()

        return self.exit_state
