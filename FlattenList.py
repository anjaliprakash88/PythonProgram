x = [[1, 2, 3, 4], ['a', 'b', 'c'], [5, 6, 7]]
res = []
for i in x:
    for j in i:
        res.append(j)
print(res)