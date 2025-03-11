# Лабораторная работа 2
:small_orange_diamond: Условия для дерева вариант №3: Root = 3; height = 4, left_leaf = root+2, right_leaf = root*3
## Задание
С использованием борда https://replit.com/@zhukov/prog-4-lr2-1#main.py сравнить реализации (рекурсивной и нерекурсивной) построения бинарного дерева с точки зрения эффективности работы алгоритма (время выполнения) двумя способами: 

:small_orange_diamond:"timeit" с помощью модуля timeit;
:small_orange_diamond: "complex-profiling" с помощью создания специальной оболочки для тестирования (matplotlib, setup_data, timeit).

Для второго способа следует переписать содержимое функции setup_data так, чтобы генерировались не списки чисел (в борде пример генерации данных для сравнения работы функции-факториала), а списки пар чисел (кортеж или словарь, представляющих root и height), также необходимо определить оптимальные значения параметров: количество «прогонов» тестов и длина списка с параметрами для построения деревьев.

## Timeit

### Комментарий к заданию: Использовалась программа с лабораторной 1. Далее в программе эксель создавалась сводная таблица показаний, с помощью который далее строились графики и сраванивали рекурсивный и нерекурсивный способ
### Терминал
:small_orange_diamond: Рекурсия
![rectimeit](https://github.com/BlohinaValeria/Programming-2nd-course/blob/main/2%20семестр/Лабораторная%202/recurs_timeit.png)
:small_orange_diamond: Нерекурсия
![rectimeit](https://github.com/BlohinaValeria/Programming-2nd-course/blob/main/2%20семестр/Лабораторная%202/not_recurs_timeit.png)

### График:
![LAB1_rec](https://github.com/BlohinaValeria/Programming-2nd-course/blob/main/2%20семестр/Лабораторная%202/timeit.png)
[Перейти](https://github.com/BlohinaValeria/Programming-2nd-course/blob/main/2%20семестр/Лабораторная%202/Графики.xlsx)

## Complex-profiling
### Комментарий к заданию: Использовалась программа с лабораторной 1 и борд. Программа борда исправлена под построение бинарного дерева
### Терминал
![all](https://github.com/BlohinaValeria/Programming-2nd-course/blob/main/2%20семестр/Лабораторная%202/3_10_term.png)

### График:
![all](https://github.com/BlohinaValeria/Programming-2nd-course/blob/main/2%20семестр/Лабораторная%202/all.png)

## Complex-profiling
### Комментарий к заданию: Тесты проверяют не только функции борда, но и построение бинарного дерева из лабораторной 1
### Результат
![test](https://github.com/BlohinaValeria/Programming-2nd-course/blob/main/2%20семестр/Лабораторная%202/test.png)

