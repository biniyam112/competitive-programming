count = int(input())
nums = input().split()
nums = [int(x) for x in nums]
i = 0
j = 1
maxIncrease = 1
while j < len(nums):
    if nums[j] > nums[j-1]:
        j += 1
    else:
        maxIncrease = max(maxIncrease, j-i)
        i = j
        j = i+1
maxIncrease = max(maxIncrease, j-i)

print(maxIncrease)
