n = int(input("enter a number: "))
x = n
while x >=10:
    sum = 0
    while x > 0:
        rem = x % 10
        sum = sum + rem ** 2
        x = x // 10
    x = sum
if sum == 1:
    print(n, "is a Happy Number")
else:
    print(n, "is not a happy number")


