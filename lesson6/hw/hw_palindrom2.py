num = 1
for i in range(1, 1000):
    for g in range(1, 1000):
        mult = i * g
        if str(mult) == str(mult)[::-1]:
            if mult > num:
                num = mult
print(num)