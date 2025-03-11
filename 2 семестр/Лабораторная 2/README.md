# Лабораторная работа 2
:small_orange_diamond: Условия для дерева вариант №3: Root = 3; height = 4, left_leaf = root+2, right_leaf = root*3
## Задание
С использованием борда https://replit.com/@zhukov/prog-4-lr2-1#main.py сравнить реализации (рекурсивной и нерекурсивной) построения бинарного дерева с точки зрения эффективности работы алгоритма (время выполнения) двумя способами: 
1."timeit" с помощью модуля timeit;
2."complex-profiling" с помощью создания специальной оболочки для тестирования (matplotlib, setup_data, timeit).
Для второго способа следует переписать содержимое функции setup_data так, чтобы генерировались не списки чисел (в борде пример генерации данных для сравнения работы функции-факториала), а списки пар чисел (кортеж или словарь, представляющих root и height), также необходимо определить оптимальные значения параметров: количество «прогонов» тестов и длина списка с параметрами для построения деревьев.

## Timeit
### Комментарий к заданию:
:small_orange_diamond:

### Результат рекурсивного способа:
![LAB1_rec](https://github.com/BlohinaValeria/Programming-2nd-course/blob/main/2%20семестр/Лабораторная%201/LR_Gen_bin.png)

### Результат тестов рекурсивного способа:
![LAB1_rec_test](https://github.com/BlohinaValeria/Programming-2nd-course/blob/main/2%20семестр/Лабораторная%201/LR_Gen_bin_test.png)

### Результат нерекурсивного способа:
![LAB1_not_rec](https://github.com/BlohinaValeria/Programming-2nd-course/blob/main/2%20семестр/Лабораторная%201/LR_Gen_bin_not.png)

### Результат тестов нерекурсивного способа:
![LAB1_rec_test](https://github.com/BlohinaValeria/Programming-2nd-course/blob/main/2%20семестр/Лабораторная%201/LR_Gen_bin_not_test.png)

