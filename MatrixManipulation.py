# You are given a ‘n x n’ 2D matrix ‘matrix’. Rotate the matrix by 90 degrees (clockwise).

# Input:
# ‘matrix’ = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]’
# Output:
# [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
n = len(matrix)
for i in range(n):
    for j in range(i, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
for i in range(n):
    matrix[i].reverse()
print(matrix)

