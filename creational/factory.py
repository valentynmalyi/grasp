from abc import ABC, abstractmethod


class CalculatorBase(ABC):
    @abstractmethod
    def add(self, a: int, b: int) -> int:
        raise NotImplemented()


class SimpleCalculator(CalculatorBase):
    def add(self, a: int, b: int) -> int:
        return a + b


class HttpCalculator(CalculatorBase):
    url = "example.com/sum/{a}/{b}"

    def add(self, a: int, b: int) -> int:
        return a + b


class CalculatorFactory:
    HTTP_LIMIT = 1000

    def __init__(self):
        self.simple = SimpleCalculator()
        self.http = HttpCalculator()

    def create_for_add(self, a: int, b: int) -> CalculatorBase:
        if self._is_use_http(a=a, b=b):
            return self.simple
        return self.http

    @classmethod
    def _is_use_http(cls, a: int, b: int) -> bool:
        return abs(a) > cls.HTTP_LIMIT or abs(b) > cls.HTTP_LIMIT



class MainCalculator(CalculatorBase):
    def __init__(self):
        self.factory = CalculatorFactory()

    def add(self, a: int, b: int) -> int:
        calculator = self.factory.create_for_add(a=a, b=b)
        return calculator.add(a=a, b=b)


def main():
    calculator = MainCalculator()
    assert calculator.add(1, 2) == 3


if __name__ == '__main__':
    main()
