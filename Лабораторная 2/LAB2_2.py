import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)


def log_decorator(func):
    '''Внутри декоратора определяется функция.func— это функция, которую мы хотим декорировать. Она передается в декоратор log_decorator в качестве аргумента.'''

    def log(op1, op2, operation):
        logger.debug(f'Введенные данные переменных и операции: {op1}, {op2}, {operation}')
        res = func(op1,op2, operation)
        logging.info(f'Результат: {res}')
        return res

    return log


@log_decorator
def calculate(a, b, operation):
    if operation == 'add':
        return a + b
    if operation == 'sub':
        return a - b
    if operation == 'div':
        if b == 0:
            raise ValueError("Division is not possible")
        return a / b
    if operation == 'mult':
        return a * b


def main():
    a = float(input("Число a = "))
    b = float(input("Число b = "))
    operation = str(input("Введите операцию(add,sub,div,mult): "))

    print("Result:", calculate(a, b, operation))


if __name__ == "__main__":
    main()
