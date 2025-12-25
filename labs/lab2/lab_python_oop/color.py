class FigureColor:
    def __init__(self, color_param: str) -> None:
        self._color = color_param

    @property
    def color(self) -> str:
        return self._color
