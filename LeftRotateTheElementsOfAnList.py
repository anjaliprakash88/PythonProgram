arr = [1, 2, 3, 4, 5]
n = len(arr)
k = 3
for j in range(k):
    first_element = arr[0]
    for i in range(n - 1):
        arr[i] = arr[i + 1]
    arr[n - 1] = first_element
print(arr)



