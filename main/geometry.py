class Geometry:
    def __init__(self):
        self.figures = list()

    def add_figure(self, figure):
        self.figures.append(figure)

    def total_area(self):
        return sum(figure.area() for figure in self.figures)

    def total_perimeter(self):
        return sum(figure.perimeter() for figure in self.figures)
    