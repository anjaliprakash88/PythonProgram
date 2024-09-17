try:
    x = int(input("Enter the first number"))
    y = int(input("Enter the second number"))
    z = x/y
except ZeroDivisionError:
    print("Division by zero is not allowed. Please enter a non-zero denominator.")
except ValueError:
    print("Please enter valid integer numbers.")
