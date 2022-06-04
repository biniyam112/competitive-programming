cases = int(input())

for _ in range(cases):
    size = int(input())
    unpainted = [int(x) for x in input().split()]
    unpainted.sort()
    mid = len(unpainted)//2
    red = 0
    blue = 0
    for i in range(len(unpainted)-1,-1,-1):
        if  i > mid:
            red += unpainted[i]
        elif  len(unpainted)% 2 ==0 and i == mid:
            continue
        else:
            blue += unpainted[i]
    if red > blue:
        print('YES')
    else:
        print('NO')
        
    