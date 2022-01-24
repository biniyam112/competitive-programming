def insertionSort(items):
    loopcounter = 0
    for i in range(1,len(items)):
        nextSmallItem = items[i]
        x = i-1
        # if loop goes till finish nextSmall items is smallest of the sorted list
        #? else if the loop breaks it's next to next smaller(equal) number to it
        while x >= 0 and items[x]> nextSmallItem:
            items[x+1] =items[x]
            x-=1
        items[x+1] = nextSmallItem
        loopcounter+=1
    print(items,loopcounter)
    return items
            
            
insertionSort([4,7,2,7,9,5,3,1,6])