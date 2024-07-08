li = [15, 6, 7, 10, 12, 20, 10, 28, 10]
x = int(input("enter a number"))
count = 0
for i in li:
    if i == x:
        count = count + 1
print(count)