cases = int(input())
for _ in range(cases):
    temp = input().split()
    frnds = input().split()
    frnds = [int(x)-1 for x in frnds]
    pre = input().split()
    pre = [int(x) for x in pre]
    cost = 0
    frnds.sort(reverse=True)
    pre.sort()
    i = 0
    for frnd in frnds:
        if i == len(pre):
            cost += pre[frnd]
        if pre[frnd] > pre[i]:
            cost += pre[i]
            i += 1
        else:
            cost += pre[frnd]
    print(cost)
