class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums)-1
        if target < nums[i]:
            return i
        elif target > nums[j]:
            return j+1
        best = 0
        while i <= j:
            mid = i + (j-i)//2
            if target > nums[mid]:
                i = mid+1
            elif target < nums[mid]:
                j = mid-1
            else:
                return mid
            if nums[mid] < target:
                best = mid+1
            else:
                best = mid
        return best