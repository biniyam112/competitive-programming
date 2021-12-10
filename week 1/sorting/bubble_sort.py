
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
    
