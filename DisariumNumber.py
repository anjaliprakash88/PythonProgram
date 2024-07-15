# Number = int(input("Enter the number to check Disarium number: "))
# length = len(str(Number))
# Temp = Number
# sum_of_digits = 0
# while Temp > 0:
#     rem = Temp % 10
#     sum_of_digits += rem ** length
#     Temp //= 10
#     length -= 1
# if sum_of_digits == Number:
#     print("Disarium Number")
# else:
#     print("Not a Disarium Number")


a = 88

b = str(a)
d = 0
for i in range(len(b)):
    c = int(b[i])
    d = d + c ** (i + 1)

if a == d:
    print("it is disarium number ")
else:
    print("it is not disarium number")
