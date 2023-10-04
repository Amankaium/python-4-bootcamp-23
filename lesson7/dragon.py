# найти максимумальное число из списка, некоторые числа в виде строки
nums = [-5, 81, 32, -62, -2, 34, 52, '32', '99', '3']

# 1
mad_max = nums[0]

for n in nums:
    if isinstance(n, str) and n.isdigit():
        n = int(n)
    if n > mad_max:
        mad_max = n

print(mad_max)

# 2
# print(max(nums))