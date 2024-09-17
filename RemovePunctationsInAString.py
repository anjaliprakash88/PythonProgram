punc = """!@#$%^&*()_+=
-=}{]]|\:;"'<>,.?/"""
word = input("Enter a Word: ")
empty = ""
for i in word:
    if i not in punc:
        empty += i
print(empty)
