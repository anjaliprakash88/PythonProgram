matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix+matrix2)

import numpy as np
m1= np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m2 = np.matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(np.concatenate((m1, m2)))