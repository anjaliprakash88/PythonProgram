# You are given a dictionary ‘word_count’ where the keys are words and the values are the number of times those words appear in a text. Your task is to fi nd the word with the highest frequency and return it.

# Input: ‘word_count’ = {"apple": 4, "banana": 2, "cherry": 5}
# Output: "cherry"
# Explanation: "cherry" appears 5 times, which is the highest frequency.
word_count = {"apple": 4, "banana": 9, "cherry": 5}
max_word = " "
max_count = 0

for word, count in word_count.items():
    if count > max_count:
        max_word = word
        max_count = count

print(max_word)
