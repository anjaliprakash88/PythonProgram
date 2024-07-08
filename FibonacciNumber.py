n = int(input("Enter a positive integer N: "))
a = 0
b = 1
for i in range(2, n + 1):
    next_term = a + b
    a = b
    b = next_term
print(b)


n = int(input("enter a number :"))
a = 0
b = 1
i = 1
if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
   while n>=i:
       c = a+b
       a = b
       b = c
       i = i+1
   print(a)