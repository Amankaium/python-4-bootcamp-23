matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix[0] # [1, 2, 3]
matrix[2][1]

my_sum = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        my_sum += matrix[i][j] # my_sum = my_sum + matrix[i][j] # 1 + 2 

print(my_sum)
