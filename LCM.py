num1 = 12
num2 = 24

# Choose the greater number
if num1 > num2:
    greater = num1
else:
    greater = num2

while True:
    if greater % num1 == 0 and greater % num2 == 0:
        lcm = greater
        break
    greater += 1

print("The L.C.M. is", lcm)
