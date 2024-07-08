items = int(input("enter the number of items that your want to input in array: "))
target = int(input("enter the targeted value: "))
x = []
for i in range(items):
    x.append(int(input("enter the items:")))
x.sort()
print(x)
for j in range(len(x)):
    if x[j]  == target:
        print(j)
    else:
        print("-1 -1")

# -----------------------------------------------------------------------------------------------------#


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
    print("First Occurrence =", first,
          "\nLast Occurrence =", last)
else:
    print("Not Found")
