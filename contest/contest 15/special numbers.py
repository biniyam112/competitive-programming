cases = int(input())
for _ in range(cases):
    temp = input().split()
    n = int(temp[0])
    k = int(temp[1])
    i = 0
    j = 0
    counter = 0
    while counter < k:
        val = n ** i
        counter +=1
        if counter == k:
            break
        j = 0
        while j < i:
            counter +=1+i
            if counter == k:
                
                val += n ** j
                break
            j+=1
        i+=1
            
    print(val % ((10**9)+7))
