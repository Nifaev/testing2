import math

from main.circle import Circle
from main.rectangle import Rectangle
from main.triangle import Triangle


class Geometry:
    def __init__(self):
        self.figures = list()

    def add_figure(self, figure):
        self.figures.append(figure)

    def total_area(self):
        return sum(figure.area() for figure in self.figures)

    def total_perimeter(self):
        return sum(figure.perimeter() for figure in self.figures)

    # написать метод, который будет принимать на вход произвольную фигуру (из тех, что реализованы)
    # и проверять, помещается ли эта фигура целиком в каждую фигуру из списка figures
    def fit_into_figure(self, input_figure):
        result = []

        for figure in self.figures:
            # Если input_figure - прямоугольник
            if type(input_figure) is type(Rectangle(2, 4)):
                # Если текущая figure - круг
                if type(figure) is type(Circle(1)):
                    '''
                    То прямоугольник можно поместить в окружность,
                    если половина его диагонали меньше или равна радиусу окружности
                    '''
                    diag = math.sqrt(input_figure.width ** 2 + input_figure.height ** 2)
                    result.append(diag / 2 <= figure.radius)

                # Если текущая фигура - прямоугольник
                if type(figure) is type(Rectangle(1, 2)):
                    '''
                    То прямоугольник можно поместить в прямоугольник, если
                    длина и ширина входящего прямоугольника меньше или равны
                    длины и ширины исходного прямоугольника
                    '''
                    result.append(input_figure.width <= figure.width and
                                  input_figure.height <= figure.height)

                # Если текущая фигура - треугольник
                if type(figure) is type(Triangle(3, 4, 5)):
                    '''
                    Единственное, что смог придумать:
                    Если прямоугольник можно вписать во вписанную
                    в треугольник окружность - то прямоугольник
                    поместится в треугольник
                    Считаем радиус вписанной окружности - площадь / полупериметр
                    '''
                    r = figure.area() / (figure.perimeter() / 2)
                    diag = math.sqrt(input_figure.width ** 2 + input_figure.height ** 2)
                    result.append(diag / 2 <= r)

            # Если input_figure - круг
            if type(input_figure) is type(Circle(1)):
                # Если текущая фигура - круг
                if type(figure) is type(Circle(1)):
                    result.append(input_figure.radius <= figure.radius)

                # Если текущая фигура - прямоугольник
                if type(figure) is type(Rectangle(1, 2)):
                    ''' 
                    Окружность можно поместить (не вписать!!!) в прямоугольник
                    Если ее диаметр меньше или равен наименьшему из длины и ширины 
                    прямоугольника
                    '''
                    result.append(input_figure.radius * 2 <= min(figure.width, figure.height))

                # Если текущая фигура - треугольник
                if type(figure) is type(Triangle(3, 4, 5)):
                    '''
                    Окружность можно поместить в треугольник, если ее радиус
                    меньше или равен радиусу вписанной в треугольник окружности
                    '''
                    r = figure.area() / (figure.perimeter() / 2)
                    result.append(input_figure.radius <= r)

            # Если input_figure - треугольник
            if type(input_figure) is type(Triangle(3, 4, 5)):
                # Если текущая фигура - прямоугольник:
                if type(figure) is type(Rectangle(1, 2)):
                    '''
                    Проверяем для первой стороны прямоугольника:
                    Сначала для первой стороны треугольника:
                    Если сторона треугольника меньше или равна стороне прямоугольника,
                    при этом высота треугольника, проведенная к данной стороне,
                    меньше или равна второй стороне прямоуогольника
                    и остальные стороны треугольника меньше или равны диагонали прямоугольника
                    то треугольник можно поместить в прямоугольник.
                    Иначе проверяем для остальных сторон треугольника.
                    Иначе - для второй стороны прямоугольника
                    '''
                    res = False
                    diag = math.sqrt(figure.width ** 2 + figure.height ** 2)
                    if input_figure.side_a <= figure.width:
                        h = (2 * input_figure.area()) / input_figure.side_a
                        res = h <= figure.height and input_figure.side_b <= diag and input_figure.side_c <= diag
                    if not res and input_figure.side_b <= figure.width:
                        h = (2 * input_figure.area()) / input_figure.side_b
                        res = h <= figure.height and input_figure.side_a <= diag and input_figure.side_c <= diag
                    if not res and input_figure.side_c <= figure.width:
                        h = (2 * input_figure.area()) / input_figure.side_c
                        res = h <= figure.height and input_figure.side_b <= diag and input_figure.side_a <= diag

                    if not res and input_figure.side_a <= figure.height:
                        h = (2 * input_figure.area()) / input_figure.side_a
                        res = h <= figure.width and input_figure.side_b <= diag and input_figure.side_c <= diag
                    if not res and input_figure.side_b <= figure.height:
                        h = (2 * input_figure.area()) / input_figure.side_b
                        res = h <= figure.width and input_figure.side_a <= diag and input_figure.side_c <= diag
                    if not res and input_figure.side_c <= figure.height:
                        h = (2 * input_figure.area()) / input_figure.side_c
                        res = h <= figure.width and input_figure.side_b <= diag and input_figure.side_a <= diag

                    result.append(res)

                # Если текущая фигура - круг
                if type(figure) is type(Circle(1)):
                    '''
                    Треугольник можно поместить в круг, если радиус описанной
                    вокруг него окружности меньше или равен радиусу окружности
                    '''
                    r = (input_figure.side_a * input_figure.side_b * input_figure.side_c) / (4 * input_figure.area())
                    result.append(r <= figure.radius)

                # Если текущая фигура - треугольник
                if type(figure) is type(Triangle(3, 4, 5)):
                    '''
                    Треугольник можно разместить в треугольнике
                    если радиус описанной окружности будет меньше или равен радиусу 
                    второй описанной окружности
                    '''
                    r1 = (input_figure.side_a * input_figure.side_b * input_figure.side_c) / (4 * input_figure.area())
                    r2 = (figure.side_a * figure.side_b * figure.side_c) / (4 * figure.area())
                    result.append(r1 <= r2)

        return result
