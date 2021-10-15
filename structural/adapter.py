from time import sleep


class C1:
    def __init__(self, element: int):
        self.element = element

    def get_answer(self, n):
        sleep(2)
        return n + self.element


class C2:
    def __init__(self, n: int):
        self.n = n

    def add_number(self, m):
        return self.n + m


c1 = C1(element=5)
print(c1.get_answer(n=4))

c2 = C2(n=5)
print(c2.add_number(m=4))


class C2Adapter:
    def __init__(self, element: int):
        self.c2 = C2(n=element)

    def get_answer(self, n: int):
        return self.c2.add_number(m=n)


c3 = C2Adapter(element=5)
print(c3.get_answer(n=4))

# Но лучше написать интьерфейс
