from posixpath import split


length = int(input())
num = input().split()
nums = [int(x) for x in num]
cost  = 0
zeros = 0

for i in range(len(nums)):
    if nums[i] == 0:
        zeros+=1
    elif nums[i] > 0:
        cost += abs(nums[i])-1
        nums[i] = 1
    else:
        cost += abs(nums[i])-1
        nums[i] = -1
if zeros > 0:
    print(cost+zeros)
else:
    prod = 1
    for num in nums:
        prod *= num
    if  prod < 0:
        cost+=2
    print(cost)