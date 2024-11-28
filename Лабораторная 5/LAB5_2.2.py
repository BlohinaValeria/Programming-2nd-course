class BatchCalculatorContextManager:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, 'r')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

    def read_operations(self):
        for line in self.file:
            line = line.strip()
            if line:
                yield line


def calculate(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '/':
        if b == 0:
            raise ValueError("Division is not possible")
        return a / b
    elif operation == '*':
        return a * b
    else:
        raise ValueError("Unknown operation")


def main():
    filename = 'operations.txt'
    with BatchCalculatorContextManager(filename) as bcm:
        for operation in bcm.read_operations():
            parts = operation.split()
            if len(parts) == 3:
                a = float(parts[0])
                operation_type = parts[1]
                b = float(parts[2])
                result = calculate(a, b, operation_type)
                print(f"Результат вычислений: {operation} = {result}")
            else:
                print(f"Invalid operation format: {operation}")


if __name__ == "__main__":
    main()
