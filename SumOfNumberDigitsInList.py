test_list = [12, 67, 98, 34]
res = []
for i in test_list:
    sum = 0
    for j in str(i):
        sum = sum + int(j)
    res.append(sum)


print(res)