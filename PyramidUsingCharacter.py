# for i in range(65, 70):
#     for j in range(65, i+1):
#         print(chr(j), end=' ')
#     print()


n = int(input("enter number of rows"))
x = ord("A")
for i in range(1, n+1):
    for j in range(1, i+1):
        print(chr(x), end=' ')
        x = x + 1
    print()