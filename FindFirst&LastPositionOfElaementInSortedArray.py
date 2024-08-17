
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
n = len(arr)
x = 8

first = -1
last = -1

for i in range(n):
    if x != arr[i]:
        continue
    if first == -1:
        first = i
    last = i

if first != -1:
    print("First Occurrence =", first, "\nLast Occurrence =", last)
else:
    print("Not Found")
