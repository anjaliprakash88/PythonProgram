# i = 1
# j = 4
# for row in range(0, 6):
#     for col in range(0, 6):
#         if row == 0 or row == 5:
#             print("*", end="")
#         elif row == i and col == j:
#             print("*", end="")
#             i = i + 1
#             j = j - 1
#         else:
#             print(end=" ")
#
#     print()


size = 7
for i in range(size):
    for j in range(size):
        if i == 0 or i == size - 1:
            print("*", end="")
        elif j == size - i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()