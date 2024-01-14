import pygame
from src.enums.exit_state import ExitState


class GameController:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen

    def process_game_iteration(self) -> ExitState:
        print('Works!')

        return ExitState.EXIT
