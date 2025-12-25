from lab_python_oop.figure import GeometricFigure
from lab_python_oop.color import FigureColor


class Rectangle(GeometricFigure):
    FIGURE_TYPE = "Прямоугольник"

    def __init__(self, width: float, height: float, color: str) -> None:
        self._width = width
        self._height = height
        self._color = FigureColor(color)

    def square(self) -> float:
        return self._width * self._height

    def __repr__(self) -> str:
        return f"{self.get_figure_type()} {self._color.color} цвета шириной {self._width} и высотой {self._height} площадью {self.square()}."
