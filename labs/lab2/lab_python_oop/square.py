from lab_python_oop.rectangle import Rectangle


class Square(Rectangle):
    FIGURE_TYPE = "Квадрат"

    def __init__(self, side: float, color: str) -> None:
        super().__init__(side, side, color)
        self._side = side

    def __repr__(self) -> str:
        return f"{self.get_figure_type()} {self._color.color} цвета со стороной {self._side} площадью {self.square()}."
