import math
from typing import List

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
      i = 1
      j = float('-inf')
      best = 0
      for num in nums:
        j = max(j,num)
      while i <= j:
        mid = i + (j-i)//2
        counter = 0
        for num in nums:
          counter+= math.ceil(num/mid)
        if counter > threshold:
          i = mid+1
        else:
          j = mid-1
          best = mid
      return best