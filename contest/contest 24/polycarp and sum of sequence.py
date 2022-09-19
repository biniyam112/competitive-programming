cases = int(input())
for _ in range(cases):
    nums = input().split()
    nums = [int(x) for x in nums]
    answer = [nums[0], nums[1]]
    for i in nums:
        if sum(answer)+i == nums[-1]:
            answer.append(i)
    answer = [str(x) for x in answer]
    print(' '.join(answer))
