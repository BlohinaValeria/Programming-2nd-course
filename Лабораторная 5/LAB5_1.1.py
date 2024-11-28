import random


class RandomNumberIterator:
    def __init__(self, params: list):
        if len(params) != 3:
            raise ValueError("Ошибка должно быть 3 параметра!")

        self.count = params[0]
        self.min = params[1]
        self.max = params[2]
        self.index = 0
        self._numbers = random.sample(range(self.min, self.max + 1), self.count)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self._numbers):
            raise StopIteration
        else:
            value = self._numbers[self.index]
            self.index += 1
            return value

    def get_params(self):
        return (self.count, self.min, self.max)


def main():
    print('Полученный список параметров')
    params = [10, 0, 105]
    iterator = RandomNumberIterator(params)
    result = list(iterator)
    print(result)


if __name__ == '__main__':
    main()
