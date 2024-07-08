num = int(input("Enter a number: "))

fib1, fib2 = 0, 1

while fib2 < num:
    fib1, fib2 = fib2, fib1 + fib2

if fib2 == num:
    print(f"{num} is a Fibonacci number.")
else:
    print(f"{num} is not a Fibonacci number.")