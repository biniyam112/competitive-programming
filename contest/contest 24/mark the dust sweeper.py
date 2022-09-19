cases = int(input())
for _ in range(cases):
    size = int(input())
    nums = input().split()
    nums = [int(x) for x in nums]
    operations = 0
    zcount = 0
    numfound = nums[0] != 0
    for i in range(len(nums)-1):
        if nums[i] == 0 and numfound:
            zcount += 1
        elif nums[i] != 0:
            numfound = True
    for i in range(len(nums)-1):
        operations += nums[i]
    print(operations+zcount)
