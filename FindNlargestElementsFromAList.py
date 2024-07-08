x = [1, 34, 56, 78, 90, 43, 12, 45, 35]
k = int(input("enter a number"))
if k == len(x):
    print("we cannot find n largest numbers in th list")
else:
    x.sort()
    print(x[-k:])