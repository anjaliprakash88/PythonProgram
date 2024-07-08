# l1 = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
# x = []
# y = []
# for i in l1:
#     if i not in x:
#         x.append(i)
#     else:
#         print("True")
#
# print(y)


l1 = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
print(len(l1))
print(l1)
x = []
count = 0
for i in l1:
    if i not in x:
        x.append(i)
    else:
        count = count + 1

if count > 0:
    print("True")
