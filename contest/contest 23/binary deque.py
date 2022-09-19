cases = int(input())


def recursion(output, target, nums, steps, count):
    if count == target:
        output.append(steps)
        return
    if count > target and steps <= min(output):
        index = 0
        if nums[0] == 1:
            while nums[index] == 1 and index < len(nums):
                index += 1
                steps += 1
                count -= 1
                if count == target:
                    output.append(steps)
                    return

        recursion(output, target, nums[index+1:], steps+1, count)
        index = len(nums)-1
        if nums[index] == 1:
            while nums[index] == 1 and index >= 0:
                index -= 1
                steps += 1
                count -= 1
                if count == target:
                    output.append(steps)
                    return
        recursion(output, target, nums[:index-1], steps+1, count)


for _ in range(cases):
    output = [float('inf')]
    target = input().split()
    target = int(target[1])
    nums = input().split()
    nums = [int(x) for x in nums]
    total = 0
    for x in nums:
        if x == 1:
            total += 1
    if target > total:
        print('-1')
    elif target == total:
        print('0')
    else:
        recursion(output, target, nums, 0, total)
        print(min(output))
