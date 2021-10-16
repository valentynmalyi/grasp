from abc import ABC, abstractmethod


class Color:
    def __init__(self, r: int, g: int, b: int):
        self.r = r
        self.g = g
        self.b = b

    def __str__(self):
        return f"Color(r={self.r}, g={self.g}, b={self.b})"


class BlueColor(Color):
    def __init__(self):
        super().__init__(0, 0, 255)


class RedColor(Color):
    def __init__(self):
        super().__init__(255, 0, 0)


class YellowColor(Color):
    def __init__(self):
        super().__init__(255, 255, 0)


class Car(ABC):
    def __init__(self, color: Color):
        self.color = color

    @abstractmethod
    def print(self) -> None:
        raise NotImplementedError()


class Bmw(Car):
    def print(self) -> None:
        print(f"BMW of color: {self.color}")


class Audi(Car):
    def print(self) -> None:
        print(f"Audi of color: {self.color}")


Bmw(RedColor()).print()
