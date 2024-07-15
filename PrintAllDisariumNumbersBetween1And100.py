for i in range(1,101):
    length = len(str(i))
    Temp = i
    sum_of_digits = 0
    while Temp > 0:
        rem = Temp % 10
        sum_of_digits += rem ** length
        Temp //= 10
        length -= 1
    if sum_of_digits == i:
        print(i, end=" ")
