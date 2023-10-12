# создайте функцию, которая принимает список чисел
# и возвращает список, в котором эти же числа во второй степени
# Пример:
# nums = [5, 3, 7]
# modify(nums)
# возвращает:
# [25, 9, 49]

def modify(nums_list):
    res_list = []
    for num in nums_list:
        a = num ** 2
        res_list.append(a)
    return res_list

nums = [5, 3, 7]
print(modify(nums)) # возвращает [25, 9, 49]
