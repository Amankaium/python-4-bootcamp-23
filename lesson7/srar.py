# найти среднее арифметическое списка чисел
nums = [-5, 81, 32, -62, -2, 34, 52]

# 1
s = 0
for n in nums:
    s += n
print(s / len(nums))

# 2
print(sum(nums) / len(nums))
