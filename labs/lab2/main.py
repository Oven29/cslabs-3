import numpy as np
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square


def main() -> None:
    N: float = 18.0  # Номер варианта

    print(f"--- Тестирование классов. Номер варианта {N=} ---")
    print("-" * 50)

    rect: Rectangle = Rectangle(N, N, "синего")
    print(f"Объект Rectangle:\n{rect!r}")

    circ: Circle = Circle(N, "зеленого")
    print("-" * 50)
    print(f"Объект Circle:\n{circ!r}")

    sq: Square = Square(N, "красного")
    print("-" * 50)
    print(f"Объект Square:\n{sq!r}")

    print("-" * 50)

    print("--- Тестирование внешнего пакета (numpy) ---")

    a: np.ndarray = np.array([rect.square(), circ.square(), sq.square()])
    print(f"Массив площадей фигур (numpy array):\n{a}")

    mean_square: float = np.mean(a)
    print(
        f"Средняя площадь фигур, вычисленная с помощью numpy.mean(): {mean_square:.2f}")

    std_dev: float = np.std(a)
    print(f"Стандартное отклонение площадей: {std_dev:.2f}")
    print("-" * 50)


if __name__ == "__main__":
    main()
