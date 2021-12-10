def insertionSort(items):
    loopcounter = 0
    for i in range(1,len(items)):
        x = i
        while x> 0:
            if items[x] < items[x-1]:
                items[x],items[x-1] = items[x-1],items[x]
            else:
                break
            x-=1
            loopcounter+=1
    print(items,loopcounter)
    return items
            
            
insertionSort([4,7,2,7,9,5,3,1,6])