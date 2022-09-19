from collections import defaultdict
from re import S


cases = int(input())
for _ in range(cases):
    input()
    temp = input().split()
    stations = input().split()
    sdict = defaultdict(list)
    for i in range(len(stations)):
        if stations[i] not in sdict:
            sdict[stations[i]] = [i]
        else:
            if len(sdict[stations[i]]) == 1:
                sdict[stations[i]].append(i)
                sdict[stations[i]].sort()
            else:
                if i > sdict[stations[i]][1]:
                    sdict[stations[i]][1] = i
                if i < sdict[stations[i]][0]:
                    sdict[stations[i]][0] = i
    for _ in range(int(temp[1])):
        temp1 = input().split()
        form, to = sdict[temp1[0]], sdict[temp1[1]]

        if not form or not to or min(form) > max(to):
            print('NO')
        else:
            print('YES')
