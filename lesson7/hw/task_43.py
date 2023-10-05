nums = [6, 2, 88, 23, 0, -5, 30, 9, 20, 10, 6, 56, -7]

nums_3 = []
nums_5 = []

for num in nums:
    if num == 0:
        continue

    if num % 3 == 0:
        nums_3.append(num)
    if num % 5 == 0:
        nums_5.append(num)

print(nums_3)
print(nums_5)

