import logging
import math

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def log_decorator(func):
    def log(op1, op2, operation, tolerance=1e-6):
        logger.debug(f'Введенные данные переменных и операции: {op1}, {op2}, {operation}')
        res = func(op1, op2, operation, tolerance)
        logging.info(f'Результат: {res}, точность {tolerance}')
        return res

    return log


@log_decorator
def calculate(a, b, operation, tolerance=1e-6):
    if operation == 'add':
        return a + b
    if operation == 'sub':
        return a - b
    if operation == 'div':
        if b == 0:
            raise ValueError("Division is not possible")
        return a / b
    if operation == 'mult':
        return round(a * b, convert_precision(tolerance))
    return a


def convert_precision(tolerance):
    return int(math.log10(1 / tolerance))


def main():
    a = float(input("Число a = "))
    b = float(input("Число b = "))
    operation = str(input("Введите операцию(add,sub,div,mult): "))
    tolerance = 1e-6
    print("Result:", calculate(a, b, operation, tolerance))


if __name__ == "__main__":
    main()
