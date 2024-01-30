import pygame

from src.enums.direction import Direction
from src.enums.exit_state import ExitState
from src.snake import Snake


class GameController:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.snake = Snake(self.screen)
        self.exit_state = ExitState.CONTINUE

    def exit(self) -> None:
        self.exit_state = ExitState.EXIT

    def events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit()
            elif event.type == pygame.KEYDOWN:
                self.keydown_events(event)

    def keydown_events(self, event) -> None:
        if event.key == pygame.K_UP:
            self.snake.set_direction(Direction.UP)
        elif event.key == pygame.K_DOWN:
            self.snake.set_direction(Direction.DOWN)
        elif event.key == pygame.K_LEFT:
            self.snake.set_direction(Direction.LEFT)
        elif event.key == pygame.K_RIGHT:
            self.snake.set_direction(Direction.RIGHT)

    def process_game_iteration(self) -> ExitState:
        self.events()

        return self.exit_state
