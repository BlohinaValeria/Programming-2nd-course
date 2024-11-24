# Функция fib_memory вычисляет n-е число Фибоначчи, используя собственное кэширование результатов
# в виде словаря memory
# Функция fib_d вычисляет n-е число Фибоначчи, используя декоратор @cache из модуля functools.
# После кода представлена программа просчета чисел Фибоначчи на четность и нечетность
from functools import cache


def fib_memory(n):
    memory = {}

    def fib(n):
        if n in memory:
            return memory[n]
        if n <= 1:
            return n
        result = fib(n - 1) + fib(n - 2)
        memory[n] = result
        return result

    return fib(10)

def fib_lab(n, f_lst = [0, 1]):
    if n == 0:
        return []
    if n == 1:
        return [f_lst[0]]
    if n == 2:
        return f_lst
    else:
        last_n = f_lst[-2] + f_lst[-1]
        return fib_lab(n-1, f_lst =f_lst + [last_n])  # упаковываем список
assert fib_lab(2) == [0, 1]
print(fib_lab(9))

@cache
def fib_d(n):
    if n <= 1:
        return n
    return fib_d(n - 1) + fib_d(n - 2)


for i in range(9):
    print(f"fib_d({i}): {fib_d(i)}")

"""Возвращает список чисел ряда фибоначчи на основе
# >>> fib_lab(3)
# [0, 1, 1, 2, 3]
# >>>fib_lab(0)
# []
# >>>fib_lab(1)
# [0]
# >>>fib_lab(2)
[0, 1]

:params n;
return 

if n == 0:
return []
if n == 1:
    return [f_lst[0]]

if n == 2:
    return f_lst
else:
    last_n = f_lst[-2] + f_lst[-1]
    return sorted(fib_lab(n-1, f_lst =f_lst + [last_n])) # упаковываем список

    assert fib_lab(2) == [0, 1]

print(fib_lab(13))"""

#@cache
#def fib_lst(n: int, numbers: str = None):
#    if numbers == 'even':
#        return [0, 2]
#   elif numbers == 'odd':
#      return [1, 1, 3]
#    else:
#        return [0, 1, 1, 2, 3]

#print(fib_lst(5))'