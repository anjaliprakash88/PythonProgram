start = int(input("enter the start value"))
end = int(input("enter the ending value"))
for i in range(start, end+1):
    str_i = str(i)
    length = len(str_i)
    temp = int(str_i)
    sum = 0
    while temp > 0:
        rem = temp % 10
        sum = sum + rem ** length
        temp = temp // 10
    if sum == i:
        print(i)





