from typing import Self


class Vector:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def clone(self):
        return Vector(self.x, self.y)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other: Self):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y

        return False
