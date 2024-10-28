import pytest
import math
from main.triangle import Triangle


def test_triangle_init_success():
    tr = Triangle(2, 2, 3)
    assert tr.side_a == 2 and tr.side_b == 2 and tr.side_c == 3


def test_triangle_init_failure():
    with pytest.raises(ValueError):
        Triangle(1, 2, 3)


def test_triangle_perimeter():
    tr = Triangle(2, 2, 2)
    assert tr.perimeter() == 2 + 2 + 2


def test_triangle_area():
    tr = Triangle(2, 2, 2)
    assert tr.area() == math.sqrt(3)


def test_triangle_is_right():
    tr = Triangle(3, 4, 5)
    assert tr.is_right()


def test_triangle_is_not_right():
    tr = Triangle(2, 2, 2)
    assert not tr.is_right()


def test_triangle_is_regular():
    tr = Triangle(5, 5, 5)
    assert tr.is_regular()


def test_triangle_is_not_regular():
    tr = Triangle(3, 4, 5)
    assert not tr.is_regular()


def test_triangle_is_isosceles():
    tr = Triangle(3, 3, 4)
    assert tr.is_isosceles()


def test_triangle_is_not_isosceles():
    tr = Triangle(3, 5, 4)
    assert not tr.is_isosceles()
