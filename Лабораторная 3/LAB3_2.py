import math
from typing import List, Union


def calculate(action: str, *args: Union[int, float], tolerance: float = 1e-6) -> Union[int, float]:
    """
    Calculates the result of the calculator based on the provided action and arguments.
    Args:
        action (str): The operation to be performed. Supported actions:
            - 'add': Addition
            - 'sub': Subtraction
            - 'div': Division
            - 'mult': Multiplication
            - 'medium': Mean value
            - 'variance': Variance
            - 'std_deviation': Standard deviation
            - 'median': Median value
            - 'q2': Second quartile (same as median)
            - 'q1': First quartile
            - 'q3': Third quartile
            - 'interquartile_range': Interquartile range (q3 - q1)
        *args (Union[int, float]): Variable number of operands.
        tolerance (float, optional): Tolerance for floating-point calculations. Defaults to 1e-6.
    """
    if action == 'add':
        return sum(args)
    elif action == 'sub':
        if len(args) < 2:
            raise ValueError("Ошибка! Вычитание требует 2 операнды.")
        return args[0] - sum(args[1:])
    elif action == 'div':
        if len(args) < 2:
            raise ValueError("Ошибка! Деление требует 2 операнды.")
        if args[1] == 0:
            raise ValueError("Ошибка! деление на 0 невозможно.")
        return args[0] / args[1]
    elif action == 'mult':
        if len(args) == 0:
            raise ValueError("Ошибка! Умножение требует 2 операнды.")
        result = 1
        for arg in args:
            result *= arg
        return result
    elif action in ('medium', 'variance', 'std_deviation', 'median', 'q2', 'q1', 'q3', 'interquartile_range'):
        if len(args) == 0:
            raise ValueError("Ошибка! Требуется 2 операнды")
        sorted_args = sorted(args)
        n = len(sorted_args)
        if action == 'medium':
            return sum(sorted_args) / n
        elif action in ('variance', 'std_deviation'):
            mean = sum(sorted_args) / n
            variance = sum((arg - mean) ** 2 for arg in sorted_args) / n
            if action == 'variance':
                return variance  # вычисление дисперсии(среднее арифметическое квадратов их отклонений от среднего арифметического этого ряда)
            else:
                return math.sqrt(
                    variance)  # вычисление std_deviation - стандартное отклонение— квадратный корень из дисперсии этого ряда.
        elif action in ('median', 'q2'):
            return sorted_args[n // 2] if n % 2 else (sorted_args[n // 2 - 1] + sorted_args[n // 2]) / 2
        elif action == 'q1':
            return sorted_args[n // 4] if n % 4 == 0 else (sorted_args[n // 4 - 1] + sorted_args[n // 4]) / 2
        elif action == 'q3':
            return sorted_args[3 * n // 4] if n % 4 == 0 else (sorted_args[3 * n // 4 - 1] + sorted_args[
                3 * n // 4]) / 2
        elif action == 'interquartile_range':
            return sorted_args[3 * n // 4] - sorted_args[n // 4]
    else:
        raise ValueError(f"Unsupported action: {action}")


if __name__ == "__main__":
    while True:
        action = input(
            "Введите действие (add, sub, div, mult, medium, variance, std_deviation, median, q1, q3, interquartile_range): ")
        if action == "exit":
            break
        try:
            operands = list(map(float, input("Введите операнды через пробел: ").split()))
            result = calculate(action, *operands)
            print(f"Результат: {result}")
        except ValueError as e:
            print(f"Ошибка: {e}")
