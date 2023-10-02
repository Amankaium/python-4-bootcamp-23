# найти сумму и произведение n-значного числа
num = input()  # 38947333448376264583823 # str

sum_n = 0
mult_n = 1
i = 0
while i < len(num):
    digit = int(num[i]) # int
    sum_n = sum_n + digit
    mult_n = mult_n * digit
    i += 1

print(sum_n)
print(mult_n)
