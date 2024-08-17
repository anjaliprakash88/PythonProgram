arr = [1, 2, 2, 8, 3, 5, 2, 2, 1]
frequency = {}

for element in arr:
    if element in frequency:
        frequency[element] += 1
    else:
        frequency[element] = 1

print("----------------------------------------")
print("Element     | Frequency")
print("----------------------------------------")
for key, value in frequency.items():
    print(key, "          |",      value)
print("----------------------------------------")
