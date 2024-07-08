n = int(input("enter number of rows"))
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=' ')
    print()

def pyr(rows):
    for i in range(1, rows + 1):
        for j in range(1, i+1):
            print(j, end=' ')
        print()

rows = int(input("enter no.of rows"))
pyr(rows)