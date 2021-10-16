from __future__ import annotations


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    class Builder:

        def __init__(self):
            self.point = Point(0, 0)

        def up(self, a: int) -> Point.Builder:
            self.point.y += a
            return self

        def right(self, a: int) -> Point.Builder:
            self.point.x += a
            return self

        def build(self) -> Point:
            return self.point


print(Point.Builder().up(5).right(4).build())
