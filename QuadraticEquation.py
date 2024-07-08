import math

a = float(input("Enter a number: "))
b = float(input("Enter a number: "))
c = float(input("enter a number: "))
if a != 0:
    d = (b*b)-(4*a*c)
    if d == 0.0:
        print("root are real & equal")
        r = -b/2*a
        print("The root are", r, "and", r)
    elif d > 0.0:
        print("root are real & distinct")
        r1 = (-b + (math.sqrt(d))) / (2*a)
        r2 = (-b - (math.sqrt(d))) / (2 * a)
        print("The root1 is: ", r1)
        print("The root2 is: ", r2)
    else:
        print("the root is imaginary")
        rp = -b / 2 * a
        ip = math.sqrt(-d)/ (2*a)
        print("The Root1 is: ", rp, "+i", ip)
        print("The Root2 is: ", rp, "+i", ip)
else:
    print("Not a quadratic equation")


