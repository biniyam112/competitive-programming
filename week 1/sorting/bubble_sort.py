
def bubbleSort(items):
    loopcount = 0
    for i in range(len(items)-1):
        for j in range(len(items)-1):
            if items[j] > items[j+1]:
                items[j],items[j+1] = items[j+1],items[j]
                loopcount+=1
    print(items,loopcount) 
    return items


bubbleSort([4,7,2,7,9,5,3,1,6])
    
    
    
def bubbleSort2(items):
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
            
            
bubbleSort2([4,7,2,7,9,5,3,1,6])
