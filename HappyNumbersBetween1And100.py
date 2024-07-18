for n in range(1, 101):
    x = n
    if x == 1 or x == 7:
        print(x)
    else:
        while x >= 10:
            sum = 0
            while x > 0:
                rem = x % 10
                sum = sum + rem ** 2
                x = x // 10
            x = sum
    if sum == 1:
        print(n)
