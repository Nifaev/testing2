import math

from main.figure import Figure


class Triangle(Figure):
    side_a = float()
    side_b = float()
    side_c = float()

    def __init__(self, a, b, c):
        if max(a, b, c) >= min(a, b, c) + a + b + c - max(a, b, c) - min(a, b, c):
            raise ValueError

        self.side_a = a
        self.side_b = b
        self.side_c = c

    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

    def area(self):
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c))

    def is_right(self):
        hypotenuse = max(self.side_a, self.side_b, self.side_c)
        cathetus1 = min(self.side_a, self.side_b, self.side_c)
        cathetus2 = self.perimeter() - hypotenuse - cathetus1

        return cathetus1 ** 2 + cathetus2 ** 2 == hypotenuse ** 2

    def is_regular(self):
        return self.side_a == self.side_b == self.side_c

    def is_isosceles(self):
        return self.side_a == self.side_b or self.side_b == self.side_c or self.side_a == self.side_c
