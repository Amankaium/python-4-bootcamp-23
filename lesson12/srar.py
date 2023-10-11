# Напишите функцию, которая принимает список чисел 
# и возвращает среднее арифметическое этих чисел
# Пример:
# calc_average([5, 6, 10]) # должно вернуть число 7

def calc_average(nums_list):
    average = sum(nums_list) / len(nums_list) # 7
    return average # 7

a = calc_average([5, 6, 10]) # 7
print(a)

nums_1 = [1, 2, 3]
b = calc_average(nums_1)