from main.figure import Figure


class Rectangle(Figure):
    width = float()
    height = float()

    def __init__(self, width, height):
        self.height = height
        self.width = width

    def perimeter(self):
        return (self.height + self.width) * 2

    def area(self):
        return self.width * self.height

    def is_regular(self):
        return self.width == self.height
