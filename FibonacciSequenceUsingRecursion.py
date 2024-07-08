# Fibonacci Sequence using recursion
def fibo(i):
    if i <= 1:
        return i
    else:
        return fibo(i-1)+fibo(i-2)


for i in range(10):
    print(fibo(i), end=" ")

