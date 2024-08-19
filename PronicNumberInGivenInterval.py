def is_pronic(i):
    for j in range(1, i + 1):
        if j * (j + 1) == i:
            return True
    return False


for i in range(1, 100):
    if is_pronic(i):
        print(i, end=" ")


# from math import *
# a = int(input("enter the starting limit : "))
# b = int(input("enter the ending limit :"))
# s=[]
# def pronic(a,b):
#     for i in range(a,b+1):
#         c = int(sqrt(i))
#         d = c * (c+1)
#         if i == d:
#             s.append(i)
# pronic(a,b)
# if s:
#     for i in s:
#         print(f"{i} is pronic number")
# else:
#     print("there is no pronic number in this range")