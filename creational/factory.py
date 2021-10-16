class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class OXPoint(Point):
    def __init__(self, x: int):
        super().__init__(x, 0)


class OYPoint(Point):
    def __init__(self, y: int):
        super().__init__(0, y)


class PointFactory:
    @staticmethod
    def create(x: int, line: str):
        if line == 'x':
            return OXPoint(x=x)
        elif line == 'y':
            return OYPoint(y=x)
        raise Exception(f"Error line name '{line}'")
