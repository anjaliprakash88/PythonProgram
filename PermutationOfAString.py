from itertools import permutations


def string_permutations(x):
    p = permutations(x)
    for i in p:
        print(''.join(i))


x = "ab"
string_permutations(x)
