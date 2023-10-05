# Пользователь вводит число,
# необходимо складывать пока не будет введено 0
n = int(input())
my_mult = 1 
my_sum = 0
# nums = [] # список, массив

while True: 
    if n == 0:
        break
    my_sum += n 
    # nums.append(n)
    my_mult *= n 
    n = int(input())

print(my_sum)
# print(sum(nums))
# print(len(nums))
print(my_mult)