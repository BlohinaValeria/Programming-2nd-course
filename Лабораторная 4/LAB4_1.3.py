def two_sum_hashed_all(lst: list[int], target: int) -> list[tuple[int, int]]:
  """
  Возвращает список всех кортежей из двух индексов элементов списка lst,
  таких что сумма элементов по этим индексам равна переменной target.
  Элемент по индексу может быть выбран один раз, но значения в списке могут повторяться.
  Алгоритм с использованием словаря, сложность O(n).
  """
  seen = {}
  result = []
  for i, num in enumerate(lst):
    if target - num in seen:
      result.append((seen[target - num], i))
    seen[num] = i
  return result

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 8
result = two_sum_hashed_all(lst, target)
print(result)
