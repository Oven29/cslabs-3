import sys
import math
from typing import Optional, Set, List


class BiquadraticSolver:
    """
    Класс для решения биквадратного уравнения Ax^4 + Bx^2 + C = 0.
    """

    def __init__(self, A: float, B: float, C: float) -> None:
        """Инициализация с коэффициентами A, B, C."""
        self.A: float = A
        self.B: float = B
        self.C: float = C
        self.real_roots: Set[float] = set()

    def _calculate_roots(self) -> Optional[str]:
        """
        Внутренний метод для вычисления корней и заполнения self.real_roots.
        Возвращает строку с описанием специальных случаев (бесконечность/нет),
        или None, если выполнено стандартное вычисление.
        """
        self.real_roots.clear()

        if self.A == 0:
            if self.B == 0:
                if self.C == 0:
                    return "Бесконечно много решений."
                else:
                    return f"Уравнение {self.C} = 0 не имеет решений."

            x_squared: float = -self.C / self.B
            if x_squared >= 0:
                self.real_roots.add(math.sqrt(x_squared))
                self.real_roots.add(-math.sqrt(x_squared))
            return None

        D: float = self.B**2 - 4 * self.A * self.C

        if D < 0:
            return None

        sqrt_D: float = math.sqrt(D)
        y1: float = (-self.B + sqrt_D) / (2 * self.A)
        y2: float = (-self.B - sqrt_D) / (2 * self.A)

        if y1 >= 0:
            root1: float = math.sqrt(y1)
            self.real_roots.add(root1)
            self.real_roots.add(-root1)

        if y2 >= 0:
            root2: float = math.sqrt(y2)
            self.real_roots.add(root2)
            self.real_roots.add(-root2)

        return None

    def solve_and_print(self) -> None:
        """Вычисляет корни и выводит результат в консоль."""

        print("\n--- Решение уравнения ---")
        print(f"Уравнение: {self.A}x^4 + {self.B}x^2 + {self.C} = 0")

        D_display: float = self.B**2 - 4 * self.A * self.C

        result: Optional[str] = self._calculate_roots()

        if result:
            print(result)
        elif not self.real_roots:
            print(f"Дискриминант D (для y = x^2): D = {D_display}")
            print("Действительных корней нет.")
        else:
            print(f"Дискриминант D (для y = x^2): D = {D_display}")
            print("Действительные корни x:")
            sorted_roots: List[float] = sorted(list(self.real_roots))
            for root in sorted_roots:
                if abs(root) < 1e-9:
                    root = 0.0
                print(f"x = {root}")
            print(
                f"Общее количество действительных корней: {len(self.real_roots)}")


def safe_input_oop(prompt: str, param_value: Optional[str] = None) -> float:
    """
    Безопасный ввод коэффициента с клавиатуры или использование значения из
    командной строки, с повторной попыткой ввода при ошибке.
    Возвращает действительное число (float).
    """
    while True:
        if param_value is not None:
            input_str: str = str(param_value)
            print(f"{prompt} (из командной строки): {input_str}")
        else:
            input_str: str = input(prompt).strip()

        try:
            coefficient: float = float(input_str)
            return coefficient
        except ValueError:
            print(
                f"Ошибка: Некорректное значение '{input_str}'. Пожалуйста, введите действительное число.")
            param_value = None


def main() -> None:
    """
    Основная функция ООП-программы. Обрабатывает ввод и создает экземпляр
    класса BiquadraticSolver для решения.
    """
    args: List[str] = sys.argv[1:]

    A_param: Optional[str] = args[0] if len(args) > 0 else None
    B_param: Optional[str] = args[1] if len(args) > 1 else None
    C_param: Optional[str] = args[2] if len(args) > 2 else None

    print("=== Решение Биквадратного Уравнения (ООП Подход) ===")

    A: float = safe_input_oop("Введите коэффициент A: ", A_param)
    B: float = safe_input_oop("Введите коэффициент B: ", B_param)
    C: float = safe_input_oop("Введите коэффициент C: ", C_param)

    solver: BiquadraticSolver = BiquadraticSolver(A, B, C)
    solver.solve_and_print()


if __name__ == "__main__":
    main()
