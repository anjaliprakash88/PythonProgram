n = int(input("enter a number: "))
for i in range(1, 100):
    if i % n == 0:
        print(i, end=" ")