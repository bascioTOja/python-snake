import pygame
from src.enums.exit_state import ExitState
from src.game_controller import GameController


def main_loop(game_controller: GameController, screen: pygame.Surface, clock: pygame.time.Clock) -> ExitState:
    action: ExitState = ExitState.CONTINUE
    while action == ExitState.CONTINUE:
        screen.fill((0, 0, 0))
        action = game_controller.process_game_iteration()
        pygame.display.update()
        clock.tick(FRAME_RATE)
    return action


if __name__ == '__main__':
    import platform
    import contextlib

    from src.constants import (
        STR_GAME_TITLE,
        MAIN_WIN_WIDTH,
        MAIN_WIN_HEIGHT,
        FRAME_RATE,
    )

    pygame.init()

    pygame.display.set_caption(STR_GAME_TITLE)
    main_screen = pygame.display.set_mode((MAIN_WIN_WIDTH, MAIN_WIN_HEIGHT))

    # Make sure the game will display correctly on high DPI monitors on Windows.
    if platform.system() == "Windows":
        from ctypes import windll

        with contextlib.suppress(AttributeError):
            windll.user32.SetProcessDPIAware()

    game_manager = GameController(main_screen)

    exit_state = main_loop(game_manager, main_screen, pygame.time.Clock())

    pygame.quit()

    if (exit_state == ExitState.SAVE):
        # TODO: Save the scoreboard with the best scores
        pass
