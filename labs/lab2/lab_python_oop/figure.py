import abc


class GeometricFigure(abc.ABC):
    """
    Абстрактный базовый класс для всех геометрических фигур.
    """
    FIGURE_TYPE = "Геометрическая фигура"

    @abc.abstractmethod
    def square(self) -> float:
        pass

    def get_figure_type(self) -> str:
        return self.FIGURE_TYPE
