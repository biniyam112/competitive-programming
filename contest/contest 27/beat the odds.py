cases = int(input())
for _ in range(cases):
    n = int(input())
    nums = input().split()
    nums = [int(x) for x in nums]
    n = len(nums)
    ec = 0
    oc = 0
    for num in nums:
        if num % 2 == 0:
            ec += 1
        else:
            oc += 1
    print(min(ec, oc))
    # i = 0
    # counter = 0
    # while i < n:
    #     if i+1 >= n:
    #         counter += 1
    #         break
    #     if nums[i] % 2 == nums[i+1] % 2:
    #         i += 2
    #         continue
    #     elif i + 2 == n:
    #         counter += 2
    #         break
    #     else:
    #         i += 3
    #         counter += 1
    # print(counter)
