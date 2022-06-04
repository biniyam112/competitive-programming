cases =  int(input())


def maxRam(a,b,size):
    moreRam = [(x,y) for x,y in sorted(zip(a,b))]
    for i in moreRam:
        if int(i[0]) <= size:
            size += int(i[1])
        else:
            break
    print(size)


for _ in range(cases):
    size = int(input().split()[1])
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    maxRam(a,b,size)
