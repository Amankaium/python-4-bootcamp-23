# Задача 2: Генератор списка
# Напишите функцию generate_even_numbers(n),
# которая принимает целое число n и возвращает список
# всех четных чисел от 1 до n, используя генератор списка.

def generate_even_numbers(n):
    lst = [i for i in range(1, n) if i % 2 == 0]
    return lst

print(generate_even_numbers(7))
