'''
Calculates the result of the calculator
"Arguments:
    a (int, float): The first number.
    b (int, float): The second number.
    operation (str): The operation to be performed.
        - 'add' for addition,
        - 'sub' for subtraction,
        - 'div' for division,
        - 'mult' for multiplication.
    Returns:
    int, float: The result of the operation.

    Exceptions:
    ValueError: If the division operation and the second number is zero.
'''


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

    print(calculate(a, b, operation))


if __name__ == "__main__":
    main()
