def count(str1, str2):
    set_str1 = set(str1)
    set_str2 = set(str2)
    matched = set_str1 & set_str2
    print(str(matched))
    print(str(len(matched)))



str1 = input("enter the first string")
str2 = input("enter the second string")
count(str1, str2)