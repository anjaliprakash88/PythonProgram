x = int(input("enter a  number: "))
temp = x
sum = 0
while temp > 0:
    rem = temp % 10
    sum += rem
    temp //= 10

if x%sum == 0:
    print("Harshad Number")
else:
    print("Not Harshad Number")


