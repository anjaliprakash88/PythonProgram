# You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative
# integers.

nums = [-1, 1]
pos = []
neg = []
res = []
for i in nums:
    if i > 0:
        pos.append(i)
    else:
        neg.append(i)
for i in range(len(pos)):
    res.append(pos[i])
    res.append(neg[i])

print(res)
