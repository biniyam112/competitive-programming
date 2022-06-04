from collections import defaultdict


temp = input().split()
r = int(temp[0])
h = int(temp[1])
routers = []
hotspots = []


#? children
spots = defaultdict(list)
for i in range(r):
    temp = input().split()
    temp = [int(x) for x in temp]
    #? capacity and bandwidth
    routers.append([temp[0],temp[1]])
    # ? children 
    spots[i] = []
for i in range(h):
    temp = input().split()
    temp = [int(x) for x in temp]
    spots[temp[1]].append(i+r)
    hotspots.append([temp[0],temp[1]])

    
maxband = 0
def dp(index,band):
    if index < r:
        if routers[index][0] - len(spots[index]) > 0:
            band = routers[index][1]//len(spots[index])+1
            return max(band,[dp(x,band) for x in spots[index]])
        else:
            return band 

for i in range(r):
    maxband = max(maxband,dp(i,0))
print(maxband)
    
    


