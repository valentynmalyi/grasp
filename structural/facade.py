class Calc:
    def __init__(self, n: int):
        self.n = n

    def add_one(self):
        self.n += 1
        return self.n


class CalcFacade:
    def __init__(self, n: int):
        self.calc = Calc(n)

    def add_five(self):
        self.calc.add_one()
        self.calc.add_one()
        self.calc.add_one()
        self.calc.add_one()
        self.calc.add_one()

    def add_tree(self):
        self.calc.add_one()
        self.calc.add_one()
        self.calc.add_one()

    def get_value(self):
        return self.calc.n


c = CalcFacade(2)
c.add_tree()
c.add_five()
print(c.get_value())
