x = [1, 6, 4, 3]
y = max(x)
missing_values = []

for i in range(min(x), y + 1):
    if i not in x:
        missing_values.append(i)

print(missing_values)