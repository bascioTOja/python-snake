import sys

import pygame
import platform
import contextlib

from src.enums.exit_state import ExitState
from src.game_controller import GameController
from src.constants import (
    STR_GAME_TITLE,
    MAIN_WIN_SIZE,
    FRAME_RATE,
    BACKGROUND_COLOR,
)


def set_process_dpi_aware():
    from ctypes import windll

    with contextlib.suppress(AttributeError):
        windll.user32.SetProcessDPIAware()


def main_loop(game_controller: GameController, screen: pygame.Surface, clock: pygame.time.Clock) -> ExitState:
    action: ExitState = ExitState.CONTINUE
    while action == ExitState.CONTINUE:
        dt = clock.tick(FRAME_RATE) / 1000
        screen.fill(BACKGROUND_COLOR)
        action = game_controller.process_game_iteration(dt)
        pygame.display.update()

    return action


if __name__ == '__main__':
    pygame.init()

    pygame.display.set_caption(STR_GAME_TITLE)
    main_screen = pygame.display.set_mode((MAIN_WIN_SIZE, MAIN_WIN_SIZE))

    # Make sure the game will display correctly on high DPI monitors on Windows.
    if platform.system() == "Windows":
        set_process_dpi_aware()

    exit_state = ExitState.RESTART
    while exit_state != ExitState.EXIT:
        game_manager = GameController(main_screen)
        exit_state = main_loop(game_manager, main_screen, pygame.time.Clock())

    pygame.quit()
