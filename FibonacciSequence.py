x = int(input("enter the limits"))
a = 0
b = 1
for i in range(x):
    print(a)
    nth = a + b
    a = b
    b = nth
