from typing import List
import heapq


def lastStoneWeight(self, stones: List[int]) -> int:
      heap = [-1*x for x in stones]
      heapq.heapify(heap)
      while len(heap) > 1:
        stone1 = 0-heapq.heappop(heap)
        stone2 = heapq.heappop(heap)
        heapq.heappush(heap,0-abs(stone1+stone2))
        if heap[0] == 0:
          heapq.heappop(heap)
      if heap:
        return 0-heap[0]
      else:
        return 0
        
        