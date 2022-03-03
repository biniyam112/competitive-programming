def findRepeatingElement(arr, low, high):
 
    # low = 0 , high = n-1
    if low > high:
        return -1
 
    mid = (low + high) // 2
 
    # Check if the mid element is the repeating one
    if (arr[mid] != mid + 1):
     
        if (mid > 0 and arr[mid]==arr[mid-1]):
            return mid
 
        # If mid element is not at its position that means
        # the repeated element is in left
        return  findRepeatingElement(arr, low, mid-1)
 
    # If mid is at proper position then repeated one is in
    # right.
    return findRepeatingElement(arr, mid+1, high)
 
# Driver code
arr = [1, 2,3,4,5,6,7,8,9,9,10,11]
n = len(arr)
index = findRepeatingElement(arr, 0, n-1)
if (index != -1):
    print (arr[index])