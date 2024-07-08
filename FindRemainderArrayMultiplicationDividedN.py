arr =[100, 10, 5, 25, 35, 14]
n = 11
sum = 1
for i in arr:
    sum = sum * i
res = sum % 11
print(res)