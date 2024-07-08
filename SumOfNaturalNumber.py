n = int(input("enter a number: "))
sum = 0
if n < 0:
    print("please enter +ve number")
else:
    while n > 0:
        sum = sum + n
        n = n - 1
    print(sum)