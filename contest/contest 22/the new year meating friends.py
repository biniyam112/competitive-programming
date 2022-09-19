dist = input().split()
dist = [int(x) for x in dist]
dist.sort()
minDis = 0
for i in dist:
    minDis += abs(i-dist[1])
print(minDis)
