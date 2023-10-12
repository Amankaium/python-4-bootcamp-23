nums = [5, 3, 7]
res = [num ** 2 for num in nums]
# print(res)

res_dict = {num: num ** 3 for num in nums}
# print(res_dict)

info = {"address": "Isanova 103", "floors": 7, "has_parking": True}
converted = [info[key] for key in info]
print(converted)

# Из списка чисел получить ещё один список чисел,
# где значения больше на 1:
# например, из [5, 3, 7] получить [6, 4, 8]
nums_1 = [num + 1 for num in nums]
# print(nums_1)

nums_2 = [num + 1 for num in nums if num >= 5]
# print(nums_2)

m = [[4, 2, 3], [7, 6, 3]]
nums_m = [num for lst in m for num in lst]
# print(nums_m)

m = [
        [3, 7, 8, 6],
        [4, 2, 9, 3],
        [5, 1, 7, 0]
    ]

m_1 = [[m[i][j] + 1 for j in range(len(m[i]))] for i in range(len(m))]
print(m_1)
