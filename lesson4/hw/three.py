num = int(input())  # 542 # 5

# 1
hundreds =  num // 100  # 5
tens = (num % 100) // 10 # 4
digits = num % 10 # 2

# 2
sum_3 = hundreds + tens + digits

# 3
mult_3 = hundreds * tens * digits

# 4
print(sum_3)
print(mult_3)
