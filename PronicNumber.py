n = int(input("enter a number: "))
flag = 0
for i in range(1, n + 1):
    if i * (i + 1) == n:
        flag = 1
        break

if flag:
    print(n, "is a pronic number")
else:
    print(n, "is not a pronic number")
