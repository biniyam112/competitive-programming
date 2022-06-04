def strengths(powerups):
    output = ''
    n = len(powerups)
    powerups = set(powerups)
    for i in range(1,n+1):
        if i > len(powerups):
            output+= str(i)
            output+=' '
        else:
            output += str(len(powerups))
            output+=' '
    print(output)

cases = int(input())

for _ in range(cases):
    n = int(input())
    powerups = []
    powerups = list(map(int,input().split()))
    strengths(powerups)
    

