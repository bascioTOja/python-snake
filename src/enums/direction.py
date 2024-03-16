from enum import IntEnum, auto

from src.vector import Vector


class Direction(IntEnum):
    UP = auto()
    RIGHT = auto()
    DOWN = auto()
    LEFT = auto()

    def get_vector(self) -> Vector:
        return vectors.get(self)

    def is_same_axis(self, direction: 'Direction') -> bool:
        self_vector = self.get_vector()
        other_vector = direction.get_vector()
        return self_vector.x == other_vector.x or self_vector.y == other_vector.y


vectors: dict[Direction, Vector] = {
    Direction.UP: Vector(0, -1),
    Direction.RIGHT: Vector(1, 0),
    Direction.DOWN: Vector(0, 1),
    Direction.LEFT: Vector(-1, 0)
}
