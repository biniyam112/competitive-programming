
class Solution:
    #Heapify function to maintain heap property.
    
    def upHeap(self,arr,i):
        p = (i-1)//2 
        while p >= 0 and arr[i] < arr[p]:
            arr[i],arr[p] = arr[p],arr[i]
            i = p
    
    def downHeap(self,arr,n,i):
        while True:
            l = 2 * i + 1
            r = 2 * i + 2
            minindex = i
            if l < n and arr[l] < arr[minindex]:
                minindex = l
            if r < n and arr[r] < arr[minindex]:
                minindex =  r
            if minindex == i:
                break
            arr[i],arr[minindex] = arr[minindex],arr[i]
            i = minindex
     
     
    def heapify(self,arr, n, i):
        # code here
        self.upHeap(arr,i)
        self.downHeap(arr,n,i)
        
    
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        # code here
        for i in range(n-1,-1,-1):
            self.heapify(arr,n,i)
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        #code here
        i = len(arr)-1
        self.buildHeap(arr,n)
        while i > 0:
            arr[0],arr[i] = arr[i],arr[0]
            i-=1
            self.heapify(arr,i+1,0)
            
        arr.reverse()