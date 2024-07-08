# for row in range(7):
#     for col in range(5):
#         if (row == 0) or (col == 0) or (row == 6) or (row == 4 and col != 1) or (row == 5 and col == 4):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print("")
#
# print("*", " ", "*", " ", "*", " ", "*", " ", "*")
# print("*")
# print("*")
# print("*", " ", "   ", "*", " ", "*", " ", "*")
# print("*", " ", "   ", " ", " ", " ", " ", "*")
# print("*", " ", "*", " ", "*", " ", "*", " ", "*")

a=10
for i in range(0,1):
    for j in range(0,a+1):
        print("*",end=" ")
    print()
for i in range(0,5):
    for j in range(0,1):
        print("*",end=" ")
    print()
for i in range(0,1):
    for j in range(0,a+1):
        if j==1 or j==2 or j==3 or j==4:
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()
for i in range(0,5):
    for j in range(0,2):
        print("*",end="                   ")
    print()
for i in range(0,1):
    for j in range(0,a+1):
        print("*",end=" ")
    print()


