x = "python"
l = []
flag = True
for i in x:
    if i not in l:
        l.append(i)
    else:
        flag = False
        break
if flag:
    print("Given word is Unique")
else:
    print("Given word is not Unique")