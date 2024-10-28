import math
import pytest
from main.circle import Circle
from main.geometry import Geometry
from main.rectangle import Rectangle
from main.triangle import Triangle


def test_geometry_total_area_all_figures():
    g = Geometry()
    g.add_figure(Circle(2))
    g.add_figure(Rectangle(2, 4))
    g.add_figure(Triangle(2, 2, 2))
    total_area = math.pi * 2 * 2
    total_area += math.sqrt(3)
    total_area += 2 * 4
    assert pytest.approx(g.total_area()) == total_area


def test_geometry_total_perimeter_all_figures():
    g = Geometry()
    g.add_figure(Circle(3))
    g.add_figure(Rectangle(2, 4))
    g.add_figure(Triangle(2, 3, 2))
    total_p = math.pi * 2 * 3
    total_p += 2 + 3 + 2
    total_p += (2 + 4) * 2
    assert pytest.approx(g.total_perimeter()) == total_p
