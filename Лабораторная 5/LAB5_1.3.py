def fib():
    x, y = 0, 1
    while True:
        yield x
        x, y = y, x + y

def second_fib(fib_gen):
    for num in fib_gen:
        yield num + 10


gen = fib()
second_gen = second_fib(gen)

k = int(input('Введите количество чисел Фибоначчи: '))

for i in range(k):
    print(f'Число Фибоначчи + 10: {next(second_gen)}')