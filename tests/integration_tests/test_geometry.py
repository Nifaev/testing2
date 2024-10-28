import math
import pytest
from main.circle import Circle
from main.geometry import Geometry
from main.rectangle import Rectangle
from main.triangle import Triangle


def test_geometry_init():
    g = Geometry()
    assert len(g.figures) == 0


def test_geometry_add_circle():
    g = Geometry()
    g.add_figure(Circle(2))
    assert len(g.figures) == 1 and type(g.figures[0]) is type(Circle(2))


def test_geometry_add_triangle():
    g = Geometry()
    g.add_figure(Triangle(2, 2, 2))
    assert len(g.figures) == 1 and type(g.figures[0]) is type(Triangle(2, 2, 2))


def test_geometry_add_rectangle():
    g = Geometry()
    g.add_figure(Rectangle(2, 4))
    assert len(g.figures) == 1 and type(g.figures[0]) is type(Rectangle(2, 4))


def test_geometry_add_three_figures():
    g = Geometry()
    g.add_figure(Circle(2))
    g.add_figure(Rectangle(2, 4))
    g.add_figure(Triangle(2, 2, 2))
    assert len(g.figures) == 3


def test_geometry_total_area_two_figures():
    g = Geometry()
    g.add_figure(Circle(2))
    g.add_figure(Triangle(2, 2, 2))
    total_area = math.pi * 2 * 2
    total_area += math.sqrt(3)
    assert pytest.approx(g.total_area()) == total_area


def test_geometry_total_perimeter_two_figures():
    g = Geometry()
    g.add_figure(Circle(3))
    g.add_figure(Rectangle(2, 4))
    total_p = math.pi * 2 * 3
    total_p += (2 + 4) * 2
    assert pytest.approx(g.total_perimeter()) == total_p
