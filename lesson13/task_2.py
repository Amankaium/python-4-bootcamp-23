# создайте функцию,
# которая принимает
# список чисел
# и возвращает словарь,
# в котором ключом является
# само число, а значением
# это же число в
# третьей степени
# Пример:
# nums = [5, 3, 2]
# pow_dict(nums)
# возвращает:
# {5: 125, 3: 27, 2: 8}

def pow_dict(nums_list):
    res_dict = {}
    for num in nums_list:
        a = num ** 3
        res_dict[num] = a
    return res_dict

nums = [5, 3, 2]
print(pow_dict(nums))
