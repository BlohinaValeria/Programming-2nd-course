import time


class Timer:
    def __enter__(self):
        self.start_time = time.perf_counter()  # Сохраняем время начала
        return self  # Возвращаем экземпляр для дальнейшего использования

    def __exit__(self, *args):
        self.end_time = time.perf_counter()  # Сохраняем время окончания
        self.elapsed_time = self.end_time - self.start_time  # Вычисляем затраченное время

    def get_elapsed_time(self):
        return self.elapsed_time  # Возвращаем затраченное время


def fib_gen(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    num_fib = 100000
    with Timer() as t:
        fib_sequence = list(fib_gen(num_fib))

    print(f"Затраченное время: {t.get_elapsed_time()} секунд")  # Выводим затраченное время

