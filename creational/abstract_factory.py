from abc import ABC, abstractmethod
from typing import Type


class Point:
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z


class Triangle:
    def __init__(self, a: Point, b: Point, c: Point):
        self.A = a
        self.B = b
        self.C = c


class Quadrilateral:
    def __init__(self, a: Point, b: Point, c: Point, d: Point):
        self.A = a
        self.B = b
        self.C = c
        self.D = d


class RightTriangle(Triangle, ABC):
    def __init__(self, a: int, b: int):
        super().__init__(Point(0, 0, 0), self.get_second_point(a), self.get_third_point(b))

    @staticmethod
    @abstractmethod
    def get_second_point(a: int) -> Point:
        raise NotImplementedError()

    @staticmethod
    @abstractmethod
    def get_third_point(a: int) -> Point:
        raise NotImplementedError()


class Rectangle(Quadrilateral):
    def __init__(self, a: int, b: int):
        super().__init__(Point(0, 0, 0), self.get_second_point(a), self.get_third_point(b), self.get_fourth_point(a, b))

    @staticmethod
    @abstractmethod
    def get_second_point(a: int) -> Point:
        raise NotImplementedError()

    @staticmethod
    @abstractmethod
    def get_third_point(a: int) -> Point:
        raise NotImplementedError()

    @staticmethod
    @abstractmethod
    def get_fourth_point(a: int, b: int) -> Point:
        raise NotImplementedError()


class XOY:
    @staticmethod
    def get_second_point(a: int) -> Point:
        return Point(a, 0, 0)

    @staticmethod
    def get_third_point(a: int) -> Point:
        return Point(0, a, 0)

    @staticmethod
    def get_fourth_point(a: int, b: int) -> Point:
        return Point(a, b, 0)


class XOZ:
    @staticmethod
    def get_second_point(a: int) -> Point:
        return Point(a, 0, 0)

    @staticmethod
    def get_third_point(a: int) -> Point:
        return Point(0, 0, a)

    @staticmethod
    def get_fourth_point(a: int, b: int) -> Point:
        return Point(a, 0, b)


class YOZ:
    @staticmethod
    def get_second_point(a: int) -> Point:
        return Point(0, a, 0)

    @staticmethod
    def get_third_point(a: int) -> Point:
        return Point(0, 0, a)

    @staticmethod
    def get_fourth_point(a: int, b: int) -> Point:
        return Point(0, a, b)


class XOYRightTriangle(XOY, RightTriangle):
    pass


class XOZRightTriangle(XOZ, RightTriangle):
    pass


class YOZRightTriangle(YOZ, RightTriangle):
    pass


class XOYRectangle(XOY, Rectangle):
    pass


class XOZRectangle(XOZ, Rectangle):
    pass


class YOZRectangle(YOZ, Rectangle):
    pass


class AbstractFactoryPlane(ABC):
    rectangle: Type[Rectangle]
    right_triangle: Type[RightTriangle]

    @classmethod
    def create_right_triangle(cls, a: int, b: int) -> RightTriangle:
        return cls.right_triangle(a, b)

    @classmethod
    def create_rectangle(cls, a: int, b: int) -> Rectangle:
        return cls.rectangle(a, b)


class XOYPlane(AbstractFactoryPlane):
    rectangle = XOZRectangle
    right_triangle = XOYRightTriangle


class XOZPlane(AbstractFactoryPlane):
    rectangle = XOZRectangle
    right_triangle = XOYRightTriangle


class YOZPlane(AbstractFactoryPlane):
    rectangle = XOZRectangle
    right_triangle = XOYRightTriangle
