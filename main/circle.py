import math

from main.figure import Figure


class Circle(Figure):
    radius = float()

    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius ** 2
