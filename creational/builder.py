from __future__ import annotations


class Point:
    def __init__(self):
        self.x = 0
        self.y = 0

    def __str__(self):
        return f"({self.x}, {self.y})"


class PointBuilder:
    def __init__(self):
        self.point = Point()

    def up(self, a: int) -> PointBuilder:
        self.point.y += a
        return self

    def right(self, a: int) -> PointBuilder:
        self.point.x += a
        return self

    def build(self) -> Point:
        return self.point


print(PointBuilder().up(5).right(4).build())
