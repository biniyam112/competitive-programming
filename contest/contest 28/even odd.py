cases = int(input())
for _ in range(cases):
    input()
    nums = input().split()
    nums = [int(x) for x in nums]
    even = set()
    odd = set()
    for i in range(len(nums)):
        if i % 2 == 0:
            if nums[i] % 2 == 0:
                even.add(0)
            if nums[i] % 2 != 0:
                even.add(1)
        if i % 2 != 0:
            if nums[i] % 2 == 0:
                odd.add(0)
            if nums[i] % 2 != 0:
                odd.add(1)
    if len(even) == 2 or len(odd) == 2:
        print('No')
    else:
        print('YES')
