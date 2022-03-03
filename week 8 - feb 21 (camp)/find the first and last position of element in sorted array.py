from git import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
      
      def findlowerBound(nums:List[int],target:int)->int:
        i = 0
        j = len(nums)-1
        best  = -1
        while i <= j:
            mid = i + (j-i)//2
            if nums[mid] >= target:
                j = mid-1
                if nums[mid] ==  target:
                  best = mid
            else:
              i = mid+1
        return best
      
      def findUpperBound(nums:List[int],target:int)->int:
        i = 0
        j = len(nums)-1
        best = -1
        while i <= j:
            mid = i + (j-i)//2
            if nums[mid] <= target:
                i = mid+1
                if nums[mid] == target:
                  best = mid
            else:
                j = mid-1
        return best
      l = findlowerBound(nums,target)
      u = findUpperBound(nums,target)
      return([l,u])
          
          
          
        