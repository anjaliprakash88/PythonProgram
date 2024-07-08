# Shuffle decks of cards
import random, itertools
deck = list(itertools.product(range(1, 14), ["spade", "club", "hearts", "Diamond0"]))
random.shuffle(deck)
for i in range(5):
    print(deck[i][0], "of", deck[i][1])