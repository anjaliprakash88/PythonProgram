x = input("enter any word/number:")
x1 = x.upper()
x2 = x1[::-1]
if x1 == x2:
    print("given", x, "is a palindrome")
else:
    print("given", x, "is not a palindrome")