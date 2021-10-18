from typing import List


class Number:
    def __init__(self, n):
        self.n = n


class Composite(Number):
    def __init__(self, n):
        super().__init__(n)
        self.leaves: List[Composite] = []

    def sum(self) -> int:
        s = self.n
        for number in self.leaves:
            s += number.sum()
        return s


n1 = Composite(1)
n2 = Composite(2)
n3 = Composite(3)
n4 = Composite(4)
n4.leaves.extend([n1, n2, n3])
n5 = Composite(5)
n6 = Composite(6)
n6.leaves.extend([n5, n4])
print(n6.sum())
