vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
char = input("enter any alphabets:")
if char in vowels:
    print("given", char, "is vowel")
else:
    print("given", char, "is not vowel")