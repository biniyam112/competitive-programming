size = input().split(' ')
size = [int(x) for x in size]
cansolve = input().split()
cansolve = [int(x) for x in cansolve]
difficulity = []
for i in range(size[0]):
    difficulity.append(int(input()))
cansolve.sort()


def isGood(mid,n):
    if n-mid > n/2 and n-mid < n:
        print('YES')
    else:
        print('NO')

for diff in difficulity:
    i = 0
    best = 0
    j = len(cansolve)-1
    while i <= j:
        mid = i + (j-i)//2
        if cansolve[mid] >= diff:
            best = mid
            j = mid-1
        else:
            i = mid+1
    isGood(best,len(cansolve))