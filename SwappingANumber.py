a, b = 2, 4
b, a = a, b
print(a)
print(b)


x1 = int(input("enter any 2 number: "))
x2 = int(input())
x3 = x1
x1 = x2
x2 = x3
print(x1)
print(x2)


a = int(input("enter any 2 number: "))
b = int(input())
a = a + b
b = a - b
a = a - b
print(a)
print(b)