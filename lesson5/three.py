# найти сумму и произведение четырёхзначного числа
num = input()  # 3542 # 5
# 1
thousand = int(num[0])
hundreds = int(num[1])
tens = int(num[2])
digits = int(num[3])
# 2
sum_3 = thousand + hundreds + tens + digits
# 3
mult_3 = thousand * hundreds * tens * digits
# 4
print(sum_3)
print(mult_3)

