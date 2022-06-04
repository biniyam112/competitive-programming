size = input().split(' ')
size = [int(x) for x in size]
coveredays = []
drange = []

for i in range(size[1]):
    drange.append([int(x) for x in input().split(' ')])

drange.sort()

for i in drange:
    if  coveredays and coveredays[-1] >= i[0]:
        i[0] = coveredays[-1]+1
    for j in range(i[0],i[1]+1):
        coveredays.append(j)


if size[0] == len(coveredays):
    print('NO')
else:
    print('YES')