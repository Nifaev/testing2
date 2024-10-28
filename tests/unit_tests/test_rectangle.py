import pytest
from main.rectangle import Rectangle


def test_rectangle_init():
    rect = Rectangle(10, 5)
    assert rect.width == 10 and rect.height == 5


def test_rectangle_perimeter():
    rect = Rectangle(10, 5)
    assert rect.perimeter() == (10 + 5) * 2


def test_rectangle_area():
    rect = Rectangle(10, 5)
    assert rect.area() == 10 * 5


def test_rectangle_is_not_regular():
    rect = Rectangle(10, 5)
    assert not rect.is_regular()


def test_rectangle_is_regular():
    rect = Rectangle(5, 5)
    assert rect.is_regular()
