def two_sum(lst: list[int], target: int) -> tuple[int, int]:
  """
  Возвращает кортеж из двух индексов элементов списка lst, таких что сумма элементов по этим индексам равна переменной target.
  Элемент по индексу может быть выбран один раз, но значения в списке могут повторяться.
  Алгоритм на двух циклах, сложность O(n^2).
  """
  min1= len(lst)
  min2 = len(lst)
  for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
      if lst[i] + lst[j] == target and i < min1 and j < min2:
        min1 = i
        min2 = j
        return (i, j)
  return None

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 8
result = two_sum(lst, target)
print('Если сумма элементов по индексам i и j равна target:',result)
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 34
result = two_sum(lst, target)
print('Подходящие индексы не найдены:',result)