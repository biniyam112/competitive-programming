from typing import List
import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)
    
    def findkthlargest(self,k:int,nums:List[int]):
      temp = nums
      for i in range(len(nums)-k):
        heapq.heappop(nums)
      value = self.nums[0]
      self.nums = temp
      return value
        

    def add(self, val: int) -> int:
      heapq.heappush(self.nums,val)
      return self.findkthlargest(self.k,self.nums)
        


# obj = KthLargest(k, nums)
# param_1 = obj.add(val)