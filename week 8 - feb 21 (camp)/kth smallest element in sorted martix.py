from typing import List
import heapq


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
      # heap = []
      # for i in matrix:
        # for j in i:
          # heapq.heappush(heap,j)
      # for i in range(k-1):
        # heapq.heappop(heap)
      # return heap[0]
      heap = []
      for i in range(len(matrix)):
        heapq.heappush(heap,(matrix[i][0],i,0))
        
      s = 0
      counter = 0
      while counter < k:
        s = heapq.heappop(heap)
        if s[2] < len(matrix)-1:
          heapq.heappush(heap,(matrix[s[1]][s[2]+1],s[1],s[2]+1))
        counter+=1
      return s[0]                
      
        