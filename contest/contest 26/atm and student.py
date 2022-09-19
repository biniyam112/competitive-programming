cases = int(input())
for _ in range(cases):
    print('\n\n', '---------------------------')
    max_idx = (-1, -1)
    temp = input().split()
    presum = int(temp[1])
    trans = input().split()
    trans = [int(x) for x in trans]
    cur_sum = presum
    i = 0
    j = 0
    while j < len(trans):
        cur_sum += trans[j]
        if cur_sum >= 0:
            cases = int(input())
for _ in range(cases):
    # print('\n\n', '----------------------')
    max_idx = (-1, -1)
    temp = input().split()
    presum = int(temp[1])
    trans = input().split()
    trans = [int(x) for x in trans]
    cur_sum = presum
    i = 0
    j = 0
    while j < len(trans):
        if cur_sum + trans[j] >= 0:
            cur_sum += trans[j]
            # assign max sum
            if max_idx == (-1, -1) or j-i > max_idx[1]-max_idx[0]:
                max_idx = (i, j)
            j += 1
        else:
            while cur_sum < 0:
                cur_sum -= trans[i]
                i += 1
    if max_idx == (-1, -1):
        print(-1)
    else:
        print(max_idx[0]+1, max_idx[1]+1)
        cur_sum += trans[j]
        if max_idx == (-1, -1) or j-i > max_idx[1]-max_idx[0]:
            max_idx = (i, j)
            j += 1
        else:
            cur_sum -= trans[i]
            i += 1
    if max_idx == (-1, -1):
        print(-1)
    else:
        print(max_idx[0]+1, max_idx[1]+1)
