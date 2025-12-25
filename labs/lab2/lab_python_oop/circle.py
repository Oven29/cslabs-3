import math
from lab_python_oop.figure import GeometricFigure
from lab_python_oop.color import FigureColor


class Circle(GeometricFigure):
    """
    Класс "Круг", наследуется от GeometricFigure.
    """
    FIGURE_TYPE = "Круг"

    def __init__(self, radius: float, color: str) -> None:
        self._radius = radius
        self._color = FigureColor(color)

    def square(self) -> float:
        return math.pi * (self._radius ** 2)

    def __repr__(self) -> str:
        return f"{self.get_figure_type()} {self._color.color} цвета радиусом {self._radius} площадью {self.square()}."

