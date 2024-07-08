x = [8, 5, 7, 3, 2]
k = 10
count = 0
for i in range(len(x)):
    for j in range(i+1, len(x)):
        if x[i] + x[j] == k:
            count = count + 1

print(count)
