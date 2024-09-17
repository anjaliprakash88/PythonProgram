nums = [1, 2, 5, 7, 7, 8]
res = []
for i in range(len(nums)):
    count = 0
    for j in range(len(nums)):
        if nums[i] == nums[j]:
            count = count + 1
    if count == 1:
        res.append(nums[i])
print(res)

