from typing import List


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        for i in range(1,len(nums)):
            x = i -1
            nextSmallNum = nums[i]
            while x >= 0 and nums[x] >nextSmallNum:
                nums[x+1] = nums[x]
                x-=1
            nums[x+1] = nextSmallNum
        output = []
        for i in range(len(nums)):
            if nums[i] > target:
                break
            if nums[i] == target:
                output.append(i)
        return output
