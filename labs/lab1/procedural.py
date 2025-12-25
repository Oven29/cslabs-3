import sys
import math
from typing import Optional, Set, List


def safe_input(prompt: str, param_value: Optional[str] = None) -> float:
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


def solve_biquadratic(A: float, B: float, C: float) -> None:
    """
    Решает биквадратное уравнение Ax^4 + Bx^2 + C = 0, находя ДЕЙСТВИТЕЛЬНЫЕ корни.
    Используется замена y = x^2 для сведения к квадратному уравнению Ay^2 + By + C = 0.
    """
    print("\n--- Решение уравнения ---")
    print(f"Уравнение: {A}x^4 + {B}x^2 + {C} = 0")

    if A == 0:
        if B == 0:
            if C == 0:
                print(
                    "Все коэффициенты равны 0. Уравнение имеет бесконечно много решений.")
            else:
                print(f"Уравнение {C} = 0 не имеет решений.")
            return

        x_squared: float = -C / B
        if x_squared < 0:
            print(
                "Уравнение сводится к квадратному, но x^2 < 0. Действительных корней нет.")
        elif x_squared == 0:
            print("Единственный действительный корень: x = 0")
        else:
            x1: float = math.sqrt(x_squared)
            x2: float = -math.sqrt(x_squared)
            print(f"Два действительных корня: x1 = {x1}, x2 = {x2}")
        return

    D: float = B**2 - 4 * A * C
    print(f"Дискриминант D (для y = x^2): D = B^2 - 4AC = {D}")

    if D < 0:
        print("Дискриминант D < 0. Действительных корней x нет.")
    else:
        sqrt_D: float = math.sqrt(D)
        y1: float = (-B + sqrt_D) / (2 * A)
        y2: float = (-B - sqrt_D) / (2 * A)

        real_roots: Set[float] = set()

        if y1 >= 0:
            root1: float = math.sqrt(y1)
            real_roots.add(root1)
            real_roots.add(-root1)

        if y2 >= 0:
            root2: float = math.sqrt(y2)
            real_roots.add(root2)
            real_roots.add(-root2)

        if not real_roots:
            print(
                f"Корни для y: y1 = {y1}, y2 = {y2}. Нет неотрицательных корней y. Действительных корней x нет.")
        else:
            print("Действительные корни x:")
            sorted_roots: List[float] = sorted(list(real_roots))
            for root in sorted_roots:
                if abs(root) < 1e-9:
                    root = 0.0
                print(f"x = {root}")
            print(f"Общее количество действительных корней: {len(real_roots)}")


def main() -> None:
    """
    Основная функция процедурной программы. Извлекает коэффициенты из аргументов
    командной строки, запрашивает ввод при необходимости и запускает решение.
    """
    args: List[str] = sys.argv[1:]

    A_param: Optional[str] = args[0] if len(args) > 0 else None
    B_param: Optional[str] = args[1] if len(args) > 1 else None
    C_param: Optional[str] = args[2] if len(args) > 2 else None

    print("=== Решение Биквадратного Уравнения (Процедурный Подход) ===")

    A: float = safe_input("Введите коэффициент A: ", A_param)
    B: float = safe_input("Введите коэффициент B: ", B_param)
    C: float = safe_input("Введите коэффициент C: ", C_param)

    solve_biquadratic(A, B, C)


if __name__ == "__main__":
    main()
