def countingSort(items):
    loopcount = 0
    freqlist = [0] * max(items) 
    finallist = [] 
    templist = [0] * max(items)
    for i in range(len(items)):
        freqlist[items[i]-1]  += 1
        loopcount+=1
        
    for i in range(len(freqlist)):
        for j in range(freqlist[i]):
            finallist.append(i+1)
            loopcount+=1
            
        
    print(finallist,loopcount)
    return finallist 
    
        
countingSort([4,7,2,7,9,5,3,1,6])

