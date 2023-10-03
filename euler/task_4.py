mad_max = 1

for i in range(1, 100):
    for j in range(1, 100):
        # print(i, j)
        mult = i * j
        if str(mult) == str(mult)[::-1]:
            if mult > mad_max:
                mad_max = mult
print(mad_max)
