size = input().split(' ')
size = [int(x) for x in size]
coveredays = {}
drange = []
counter  = 0


for i in range(size[1]):
    drange.append([int(x) for x in input().split(' ')])

drange.sort()

for i in drange:
    # if  coveredays and coveredays[-1] >= i[0]:
        # pass
        # i[0] = coveredays[-1]+1
    for j in range(i[0],i[1]+1):
        if j in coveredays:
            coveredays[j] +=1
        else:
            coveredays[j] = 1


print(counter)

    
