# Given a fixed-length array arr, duplicate each oocurrence of zero, shifting the remaining elements to right
# input: arr=[1, 0, 2, 3, 0, 4, 5]
# output:  [1, 0, 0, 2, 3, 0, 0, 4, 5]
#
x=[1, 0, 2, 3, 0, 4, 5]
z = len(x)
y=[]
for i in x:
    if i != 0:
        y.append(i)
    elif i == 0:
        y.append(i)
        y.append(0)

while z != len(y):
    y.pop()

print(y)

