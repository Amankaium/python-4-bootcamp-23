lst = [4, 9, 7, "hello", False, -5, 0, 335]

for i, elem in enumerate(lst):
    print(i, elem) # индекс, элемент

# каждое число в списке
# надо возвести в степень,
# равную индексу
lst = [4, 9, 7, 6, 3]

for k, num in enumerate(lst):
    # k # индекс # 1
    # num # элемент # 9
    print(num ** k) # 9 ** 1
