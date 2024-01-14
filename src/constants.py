"""
Module to keep all the constants commonly used by other modules.

Can be imported from anywhere.
"""
FRAME_RATE = 60

STR_GAME_TITLE = 'Python - Snake'

MAIN_WIN_WIDTH = 1000
MAIN_WIN_HEIGHT = 800

MAP_MARGIN = 20

MAX_MAP_WIDTH = MAIN_WIN_HEIGHT - MAP_MARGIN
MAX_MAP_HEIGHT = MAIN_WIN_HEIGHT - MAP_MARGIN

TILE_SIZE = 39

GRID_WIDTH = MAX_MAP_WIDTH / TILE_SIZE
GRID_HEIGHT = MAX_MAP_HEIGHT / TILE_SIZE

SNAKE_SPEED = 10