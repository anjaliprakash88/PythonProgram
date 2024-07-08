x = input("enter the number")
length = len(x)
temp = int(x)
sum = 0
while temp > 0:
    rem = temp % 10
    sum = sum + rem ** length
    temp = temp // 10


if sum == int(x):
    print("Amstrong Number")
else:
    print("Not a amstrong Number")





