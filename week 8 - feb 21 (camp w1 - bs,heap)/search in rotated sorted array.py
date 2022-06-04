from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums)-1
        mid = (i+j)//2
        while i < j:
            if nums[mid] == target:
                return mid
            if nums[mid] >=nums[i]:
                if nums[i] <= target < nums[mid]:
                    j = mid-1
                else:
                    i = mid+1
            elif nums[mid] <=nums[j]:
                if nums[mid] < target <= nums[j]:
                    i = mid+1
                else:
                    j = mid-1
            mid = (i+j)//2
        if nums[mid] == target:
            return mid
        return -1
