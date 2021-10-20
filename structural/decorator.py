class Printer:
    def __init__(self, text: str):
        self.text = text

    def __str__(self):
        return self.text


class Bracket1Mixin:
    def __str__(self: Printer):
        return f"({super().__str__()})"


class Bracket2Mixin:
    def __str__(self: Printer):
        return f"[{super().__str__()}]"


class MyTextPrinter(Bracket1Mixin, Bracket2Mixin, Printer):
    pass


print(MyTextPrinter('123'))
