from __future__ import annotations


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"


class PointBuilder:

    def __init__(self):
        self.point = Point(0, 0)

    def up(self, a: int) -> PointBuilder:
        self.point.y += a
        return self

    def right(self, a: int) -> PointBuilder:
        self.point.x += a
        return self

    def build(self) -> Point:
        return self.point


def main():
    builder = PointBuilder()
    point = builder.up(5).right(4).build()
    print(point)


if __name__ == '__main__':
    main()
