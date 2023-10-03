n = 4000000
res = 2
num_1 = 1
num_2 = 2
f = num_1 + num_2 # 3
while f < n:
    # print(f)
    num_1 = num_2       # 2 # 3 # 5
    num_2 = f           # 3 # 5 # 8
    f = num_1 + num_2   # 5 # 8 # 13

    if f > n:
        break

    if f % 2 == 0:
        res += f
print(res)