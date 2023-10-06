# lst = [5, 0, -1, [3, 5], 'hello', {"code": "python"}]
# for e in lst:
#     print(e)

# матрица, двумерный список
m = [
        [3, 7, 8, 6],
        [4, 2, 9, 3],
        [5, 1, 7, 0]
    ]

# [3, 7, 8, 6, 4, ..., 0]
nums = []

# print(m[1][2])
# print(m[2][1])

for r in m:
    # print(r)
    for num in r:
        # print(num)
        nums.append(num)

for i in range(len(m)):
    # print(m[i]) # lst
    for j in range(len(m[i])):
        # print(m[i][j])
        nums.append(m[i][j])

