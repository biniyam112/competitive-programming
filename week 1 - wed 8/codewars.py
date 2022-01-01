def countSwaps(a):
    # Write your code here
    swapCounter = 0
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
                swapCounter+=1
    print('Array is sorted in '+str(swapCounter)+' swaps.')
    print('First Element: '+str(a[0]))
    print('First Element: '+str(a[-1]))
    
    
# countSwaps([3,2,1])

def insertionSort1(n, arr):
    # Write your code here
    lastItem= arr[n-1]
    for i in range(n-1,0,-1):
        if lastItem < arr[i-1]:
            arr[i] = arr[i-1]
            print(*arr)
            
        else :
            arr[i] = lastItem
            print(*arr)
            break
    if arr[0] > lastItem:
        arr[0] = lastItem
        print(*arr)
        
# insertionSort1(5,[2,4,6,8,3])


def countingSort():
    # Write your code here
    strn = '63 25 73 1 98 73 56 84 86 57 16 83 8 25 81 56 9 53 98 67 99 12 83 89 80 91 39 86 76 85 74 39 25 90 59 10 94 32 44 3 89 30 27 79 46 96 27 32 18 21 92 69 81 40 40 34 68 78 24 87 42 69 23 41 78 22 6 90 99 89 50 30 20 1 43 3 70 95 33 46 44 9 69 48 33 60 65 16 82 67 61 32 21 79 75 75 13 87 70 33'
    arr = strn.split()
    print(arr)
    for i in range(len(arr)):
        arr[i] = int(arr[i])
    freqList = [0]*(max(arr)+1)
    for i in range(len(freqList)):
        freqList[arr[i]] +=1
    print(*freqList)

    

countingSort()