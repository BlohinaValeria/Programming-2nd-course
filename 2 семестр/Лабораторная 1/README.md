# Лабораторная работа 1.Построение бинарного дерева
:small_orange_diamond: Условия для дерева вариант №3: Root = 3; height = 4, left_leaf = root+2, right_leaf = root*3
## Задание
Разработайте программу на языке Python, которая будет строить бинарное дерево (дерево, в каждом узле которого может быть только два потомка). Отображение результата в виде словаря (как базовый вариант решения задания). Далее исследовать другие структуры, в том числе доступные в модуле collections в качестве контейнеров для хранения структуры бинарного дерева. 
Необходимо реализовать рекурсивный и нерекурсивный вариант gen_bin_tree
Алгоритм построения дерева должен учитывать параметры, переданные в качестве аргументов функции. Пример: 
def gen_bin_tree(height=<number>, root=<number>):
    pass

## Комментарий к заданию:
:small_orange_diamond:Проблем с реализацией не было

## Результат рекурсивного способа:
![LAB1_rec](https://github.com/BlohinaValeria/Programming-2nd-course/blob/main/2%20семестр/Лабораторная%201/LR_Gen_bin.png)

## Результат тестов рекурсивного способа:
![LAB1_rec_test](https://github.com/BlohinaValeria/Programming-2nd-course/blob/main/2%20семестр/Лабораторная%201/LR_Gen_bin_test.png)

## Результат нерекурсивного способа:
![LAB1_not_rec](https://github.com/BlohinaValeria/Programming-2nd-course/blob/main/2%20семестр/Лабораторная%201/LR_Gen_bin_not.png)

## Результат тестов нерекурсивного способа:
![LAB1_rec_test](https://github.com/BlohinaValeria/Programming-2nd-course/blob/main/2%20семестр/Лабораторная%201/LR_Gen_bin_not_test.png)
