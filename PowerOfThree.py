# Given an integer n, return true if it is a power of three. Otherwise, return false.
# An integer n is a power of three, if there exists an integer x such that n == 3x.
x = int(input("enter the number: "))
flag = False
for i in range(1, x+1):
    if 3**i == x:
        flag = True
        break

if flag:
    print("True")
else:
    print("False")
