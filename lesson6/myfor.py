# lst = [4, 9, 7]

# вывод элементов списка
# for i in range(0, 3, 1):
#     print(lst[i])

# # вывод чисел
# for j in range(1, 11, 1):
#     print(j)

# # вывод нечётных чисел
# for j in range(1, 11, 2):
#     print(j)


# # вывод чисел
# for k in range(1, 11):
#     print(k)

# # вывод чисел
# for i in range(11):
#     print(i)

lst = [4, 9, 7, "hello", False, -5, 0, 335]

# вывод элементов списка через индекс
for i in range(len(lst)):
    print(lst[i])

# вывод элементов списка через поэлементное обращение
for element in lst:
    print(element)
