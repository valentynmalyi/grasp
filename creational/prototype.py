from __future__ import annotations

from copy import deepcopy


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"


class PointPrototype:
    def clone(self, **kwargs) -> Point:
        raise NotImplemented()


class XPointPrototype(PointPrototype):
    def clone(self, y: int) -> Point:
        return Point(
            x=0,
            y=y,
        )


class YPointPrototype(PointPrototype):
    def __init__(self):
        self.point = Point(
            x=1,
            y=0,
        )

    def clone(self, x: int) -> Point:
        point = deepcopy(self.point)
        point.x = x
        return point


def main():
    point = YPointPrototype().clone(x=4)
    print(point)


if __name__ == '__main__':
    main()
