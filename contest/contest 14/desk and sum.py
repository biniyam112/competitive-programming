temp = input().split()
n = int(temp[0])
m = int(temp[1])
coordinates = []
for _ in range(n):
    temp = input().split()
    temp = [int(x) for x in temp]
    coordinates.append([temp[0],temp[1]])
for _ in range(m):
    bound = input().split()
    bound = [int(x) for x in bound]
    counter = 0
    for place in coordinates:
        if  bound[0] <= place[0] <= bound[2] and bound[1] <= place[1] <= bound[3]  :
            counter+=1
    print(counter)

    