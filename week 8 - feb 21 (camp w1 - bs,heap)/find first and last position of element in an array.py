from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = self.findElement(True,nums,target)
        end = self.findElement(False,nums,target)
        return [start,end]

    def findElement(self,start:bool,nums:List[int],target:int):
        left = 0
        right = len(nums)-1
        mid = left + (right-left)//2
        while right >= left:
          if start:
            mid = right + (right-left)//2
          else:
            mid = left - (right-left)//2
          if nums[mid] < target:
            left = mid+1
          elif nums[mid] > target:
            right = mid-1
          else:
            if start :
              right = mid-1
            else:
              left = mid+1
        return -1
      

          
          
          
        