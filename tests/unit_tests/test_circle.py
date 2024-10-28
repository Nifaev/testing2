import math
import pytest
from main.circle import Circle


def test_circle_init():
    circle = Circle(0.5)
    assert circle.radius == 0.5


def test_circle_perimeter():
    circle = Circle(2)
    assert circle.perimeter() == 2 * math.pi * 2


def test_circle_area():
    circle = Circle(3)
    assert circle.area() == math.pi * 3 * 3

