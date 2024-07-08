x = [2, 7, 11, 15]
target = 9
y = len(x)
for i in range(len(x)):
    for j in range(i+1, y):
        if x[i] + x[j] == target:
            print(i, j)
