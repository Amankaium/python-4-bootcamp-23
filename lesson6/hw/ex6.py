num = 1

for i in range(99, 1000): # 900
    for j in range(99, 1000): # 900
        mult = i * j # 1
        if str(mult) == str(mult)[::-1]: # 1
            if mult > num: # 1
                num = mult # 1
print(num)

# 900 * 900