
P = float(input("Enter the principal amount: "))
r = float(input("Enter the annual interest rate : "))
n = int(input("Enter the number of times interest"))
t = int(input("Enter the number of years: "))

A = P * (1 + r/n)**(n*t)

interest = A - P

print(interest)
