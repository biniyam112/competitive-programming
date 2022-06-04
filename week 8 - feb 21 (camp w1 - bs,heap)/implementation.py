class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        # code here
        while i != 0 and arr[i] < arr[(i-1)//2]:
            arr[i],arr[(i-1)//2] = arr[(i-1)//2],arr[i]
    
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        # code here
        for i in range(len(arr)-1,-1,-1):
            self.heapify(arr,n,i)
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        #code here
        i = len(arr)-1
        while i > 0:
            arr = self.heapify(arr,n,i)
            arr[0],arr[i] = arr[i],arr[0]
            i-=1


    