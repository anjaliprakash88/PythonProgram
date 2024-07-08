# Sum of Natural Numbers Using Recursion
def naturalNumber(n):
    if n == 1:
        return n
    else:
        return n + naturalNumber(n-1)


n = int(input("enter a number: "))
if n <= 0:
    print("enter a +ve number....")
else:
    print("sum of n natural number is ", naturalNumber(n))