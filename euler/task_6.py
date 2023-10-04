n = 101

sum_sq = 0
sq_sum = 0

for i in range(1, n):
    sum_sq = sum_sq + i ** 2 # sum_sq += i ** 2
    sq_sum += i
    sq_sum = sq_sum + i

sq_sum = sq_sum ** 2
print(sq_sum - sum_sq)
