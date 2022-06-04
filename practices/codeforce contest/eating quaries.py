cases = int(input())
for _ in range(cases):
    temp = input().split()
    temp =  [int(x) for x in temp]
    candies = input().split()
    candies = [int(x) for x in candies]
    candies.sort()
    presum = [0]
    for i in candies:
        presum.append(presum[-1]+int(i))
    for _ in range(temp[1]):
        query = int(input())
        if query <= candies[-1]:
            print(1)
        elif query > presum[-1]:
            print(-1)
        else:
            i = 0
            j = len(presum)-1
            best  = j
            while i <= j:
                mid = i + (j-i)//2
                if presum[mid] == query:
                    best = mid
                    break
                elif presum[mid] > query:
                    j = mid-1
                    best = mid
                else:
                    i = mid+1
                    best = mid
            print(best)
                
    