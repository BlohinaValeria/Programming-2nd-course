import random

class RandomNumberGenerator:
    def __init__(self, count, min_value, max_value):
        if count <= 0:
            raise ValueError("Кол-во элементов должно быть положительным!")
        self.count = count
        self.min = min_value
        self.max = max_value

    def gen(self):
        for i in range(self.count):
            yield random.randint(self.min, self.max) #альтернатива для этого for i является функция next

def main():
    print('Результат:')
    generator = RandomNumberGenerator(5, 0, 105)
    for number in generator.gen():
        print(number)

if __name__ == '__main__':
    main()