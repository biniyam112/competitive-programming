cases = int(input())
for _ in range(cases):
    output = 0
    count = int(input())
    nums = input().split()
    nums = [int(x) for x in nums]
    items = {}
    total = sum(nums)
    mean = total / count
    for i in nums:
        pair = total - mean*(count-2) - i
        if pair in items:
                output += items[pair]
        if i in items:
            items[i] += 1
        else:
            items[i] = 1
    print(output)