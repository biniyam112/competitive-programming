from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        j = len(nums)-1
        best = 0
        while i < j:
            mid = i + (j-i)//2
            if mid >= nums[mid]:
                j = mid-1
            else:
                best = mid
                i = mid+1
        return nums[best+1]
        
        