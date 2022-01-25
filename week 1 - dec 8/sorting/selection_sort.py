from typing import List


def selectionSort(items) :
    loopCounter  = 0
    for i in range(len(items)):
        selectedIndex = i
        for j in range(i,len(items)):
            loopCounter+=1
            if items[selectedIndex] > items[j]:
                selectedIndex = j
        items[i],items[selectedIndex] =  items[selectedIndex],items[i]
    print(items,loopCounter)
    return items


selectionSort([4,7,2,7,9,5,3,1,6])



def select( arr, i):
    # code here 
    for i in range(len(arr)):
        smallestValueIndex =i
        for j in range(len(arr)):
            if arr[j] < arr[smallestValueIndex]:
                smallestValueIndex = j
        return smallestValueIndex
                

def selectionSort( arr,n):
    #code here
    for i in range(n-1):
        smallestValueIndex = i
        for j in range(i,n):
            if arr[j]<arr[smallestValueIndex]:
                smallestValueIndex = j
        arr[smallestValueIndex],arr[i]= arr[i],arr[smallestValueIndex]
    return arr