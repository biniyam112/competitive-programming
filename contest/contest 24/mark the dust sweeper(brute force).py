cases = int(input())
for _ in range(cases):
    size = int(input())
    nums = input().split()
    nums = [int(x) for x in nums]
    operations = 0
    while True:
        i = 0
        while i < len(nums)-1 and nums[i] == 0:
            i += 1
        j = i+1
        while j < len(nums)-1 and nums[j] != 0:
            j += 1
        if i == len(nums)-1 or j == len(nums)-1:
            break
        nums[i] -= 1
        nums[j] += 1
        operations += 1
    for i in range(len(nums)-1):
        operations += nums[i]
    print(operations)
