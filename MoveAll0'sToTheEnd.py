nums = [0, 1, 0, 3, 12]
x = []
y = []
for i in nums:
    if i == 0:
        x.append(i)
    else:
        y.append(i)

y.extend(x)
print(y)
