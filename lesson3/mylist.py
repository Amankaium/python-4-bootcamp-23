# list, array, массив, список
numbers = [4, 8, 3, 20, 7]

# обращание к элементам списка
print(numbers[0])
print(numbers[1])
print(numbers[3])

# добавление элементов
print(numbers)
numbers.append(33)
print(numbers)

# другой список
names = ["John", "Smith", "Steve"]

# тип данных
print(names)
print(type(names))
print(names[1]) # Smith
print(type(names[1]))
print("He is " + names[1])

# смешанный список
my_list = [34, 7.4, False, "hello", [5, 2], None]

# кол-во элементов, длина списка
print(len(my_list))

# пустой
b = []
print(b)
b.append(8)
print(b)