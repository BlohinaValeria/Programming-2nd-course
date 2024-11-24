def strfunc(inp_string, offset):
  res_list = []
  for ch in inp_string:
    res_list.append(chr(ord(ch) + offset))
  res_string = ''.join(res_list)
  return res_string
my_str = "winter is coming"  # Исходная строка
res_str = strfunc(my_str, 13)
lst = []
for ch in res_str:
  lst.append(ord(ch))
print(lst)
# выходная строка преобразована в список __кодов__- символов:

# [132, 118, 123, 129, 114, 127, 45,
# 118, 128, 45, 112, 124, 122, 118, 123, 116]